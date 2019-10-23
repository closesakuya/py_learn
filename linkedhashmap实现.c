/*
插入删除 查找 O(1)
依据初始化参数可选择：
1.链表按照LRU顺序存储
2.链表按照key值存储，并用跳表实现O(logn查找)

实现动态扩容，装载因子大于阈值后每次插入分散迁移
hash表使用链表法解决冲突，并使用跳表存储索引, 索引



*/

#include <stdio.h>
#include <malloc.h>

#define INT16	signed short
#define INT32	signed int
#define INT64	signed long
#define UINT8	unsigned char
#define UINT16	unsigned short
#define UINT32	unsigned int
#define UINT64	unsigned long
#define FLT32	float
#define FLT64	double


static INT16 (*campkeyfunc)(void *, void* )[20];


typedef struct Node
    {
		struct Node *pPre;
		struct Node *pNxt;
		struct Node *pHNxt;		//hash map拉链下一节点
		void   *pKey;
		void   *pScore;
		void   *pData;
    }tNode;


typedef struct Key
    {
		struct Key *pHNxt;
		void  *pDown;		//
		void   *pScore;
		UINT32	grade;
    }tKey;

typedef struct {
    UINT64 capacity;
	UINT64 datasize;
	UINT64 keysize;
	UINT64 offset_of_keyindata;
	UINT64 keyInterv;
	enum {
		key_int16 = 0,
		key_int32,
		key_int64,
		key_uint16,
		key_uint32,
		key_uint64,
		key_flt32,
		key_flt64,
		key_str,
	}keytype;
	INT16 (*campkeyfunc)(void *score1, void* score2);  //key 比较方法，key1大于key2返回 1,小于返回-1,等于返回0
	tNode  *phash;
    tNode  *pHead;
	tNode  *pTail;
	tKey   *topkey;
	UINT32 *nodenums;
	UINT64 TTnodenums;
    
    
} Linkedhashmap;



tNode* search_skiplist(tKey   *topkey, void *key, INT16 (*campkeyfunc)(void *, void* ))
{
	tKey	*cursor = topkey,*cursor_nxt;
	tNode	*node = 0;

	
	while(cursor)
	{
		cursor_nxt = cursor->pHNxt;
		if( 0 == cursor_nxt || campkeyfunc(key,cursor_nxt->pKey) == -1)
		{
			if( cursor->grade <= 1)
			{
				node = (tNode*)(cursor->pDown);
				break;
			}
			else 
			{
				cursor = (tKey*)(cursor->pDown);
			}
			
		}
		else
			cursor = cursor->pHNxt;
	}
	
	while(node)
	{
		
		if( 0 == node->pKey || campkeyfunc(key,node->pKey) == 1)
			{node = node->pHNxt;continue;}
		else if( campkeyfunc(key,node->pKey) == 0)
			return node;
		else
			break;
	}
	
	return 0;
}


INT32 random_grade(INT32 K)
{
	
	
	return K/2;
}

INT16  insert_skiplist(tKey   **ptopkey, tNode *node, void *key, INT16 (*campkeyfunc)(void *, void* ))   //需保证key不在list中，否则直接返回
{
	tKey	*topkey = *ptopkey,*cursor,*cursor_nxt, *pre_new = 0, *cur_new = 0;
	tNode	*curnode = 0;
	INT32	grade;
	

	cursor = topkey;
	//查找插入
	
	//判断是否增加跳表索引层
	
	//更新索引
	grade = random_grade(topkey->grade + 1);
	if(grade > topkey->grade)	//升级一层索引
	{
		cursor = (tKey*)malloc(sizeof(tKey));
		cursor->grade = grade;
		cursor->pHNxt = 0;
		cursor->pKey = key;
		cursor->pDown = topkey;
		topkey = cursor;
	}
	
	*ptopkey = topkey;
	
	while( cursor)
	{
		cursor_nxt = cursor->pHNxt;
		if(cursor_nxt == 0 || campkeyfunc(key,cursor_nxt->pKey) == -1) //判断是否到下一层索引
		{
			if(cursor->grade <= grade)			//判断是否要加索引
			{
				cur_new = (tKey*)malloc(sizeof(tKey));
				cursor->pKey = key;
				cursor->pHNxt = cur_new;
				cur_new->pHNxt = cursor_nxt;
				if( pre_new)
				{
					pre_new->pDown = cur_new;	
				}
				pre_new = cur_new;
			}

			if( 1 == cursor->grade)	 //首层，开始查询数据
			{
				curnode = (tNode*)(cursor->pDown);
				break;
			}
			else
			{
				cursor = (tKey*)(cursor->pDown);
			}	
		}
		else
		{
			cursor = cursor->pHNxt;
		}	
	}
	
	while( curnode) //查询数据
	{
		if(curnode->pHNxt == 0 || campkeyfunc(key,curnode->pHNxt->pKey) == -1) 
		{
			curnode->pHNxt = node;
			node->pHNxt = curnode->pHNxt;
			if( pre_new )
				pre_new->pDown = node;
			return 1;
		}
		
		curnode = curnode->pHNxt;
	}

	
	return 0;
}



INT16 load_linkedhashmap( Linkedhashmap	*map)
{
	tKey   *topkey ,*curkey = 0;
	tNode  *HeadNode = 0,*TailNode = 0, *curnode = 0;
	UINT64	i;
	
	
	HeadNode = (tNode*)malloc(sizeof(tNode));
	TailNode = (tNode*)malloc(sizeof(tNode));
	HeadNode->pPre = 0;
	HeadNode->pNxt = TailNode;
	HeadNode->pHNxt = 0;		//hash map拉链下一节点
	HeadNode->pKey = 0;
	HeadNode->pScore = 0;
	HeadNode->pData = 0;
	map->pHead = HeadNode;
	
	TailNode->pPre = HeadNode;
	TailNode->pNxt = 0;
	TailNode->pHNxt = 0;		//hash map拉链下一节点
	TailNode->pKey = 0;
	TailNode->pScore = 0;
	TailNode->pData = 0;
	map->pTail = TailNode;	
	

	
	
	map->phash = (tNode*)malloc(sizeof(tNode)*map->capacity);
	map->topkey = (tKey*)malloc(sizeof(tKey)*map->capacity);
	map->nodenums = (UINT32*)malloc(sizeof(UINT32)*map->capacity);
	
	for(i = 0; i < map->capacity; i++)
	{
		//hash表中头结点初始化
		curnode = &(map->phash[i]);
		curnode->pPre = 0;
		curnode->pNxt = 0;
		curnode->pHNxt = 0;		//hash map拉链下一节点
		curnode->pKey = 0;
		curnode->pScore = 0;
		curnode->pData = 0;
		
		curkey = &(map->topkey[i]);
		curkey->pHNxt = 0;
		curkey->pDown = &(map->phash[i]);		//
		curkey->pScore = 0;
		curkey->grade = 1;
		
		map->nodenums[i] = 0;
	
		
	}
	
}

tNode* search_hashmap(void *key,UINT32 keylen,  Linkedhashmap	*map)
{
	tNode  *HeadNode = 0, *node = 0;
	tKey   *topkey = 0;
	UINT64 hashval;
	
	hashval = hash( key, keylen, map->capacity);
	HeadNode = &(map->phash[hashval]);
	if(0 == HeadNode->pHNxt)
		return 0;
	
	//通过跳表搜素
	topkey = &(map->topkey[hashval]);
	
	node = search_skiplist(topkey, key, INT16 (*campkeyfunc)(void *, void* ))
	
}


UINT64	hash(void *key, UINT32 keylen, UINT64  capacity)
{
	
	return 0;
}


INT16 campkey_int16(void *score1, void *score2 )
{
	if( (*(INT16*)score1) == (*(INT16*)score2)) return 0;
	else if ( (*(INT16*)score1) > (*(INT16*)score2)) return 1;
	else return -1;
}


#define SWAP_LK(A,B) do{                    \
		tNode *temp;		                \
		temp = A->pNxt;                     \
		A->pNxt = B->pNxt;                  \
		B->pNxt = temp;                     \
		temp = A->pPre;                     \
		A->pPre = B->pPre;                  \
		B->pPre; = temp;                    \
		temp = A->pHNxt;                    \
		A->pHNxt = B->pHNxt;                \
		B->pHNxt = temp;                    \
}while(0)
	
#define INSERT_LK(A,IST) do{                \
		tNode *temp;		                \
		temp = A->pNxt;                     \
		IST->pPre = A;                      \
		IST->pNxt = A->pNxt;                \
		A->pNxt = IST;                      \
		if(temp)                            \
			temp->pPre = IST;	            \
}while(0)
	
#define DELETE_LK(A) do{                     \
		if(A->pPre)                          \
			A->pPre->pNxt = A->pNxt;         \
		if(A->pNxt)                          \
			A->pNxt->pPre = a->pPre;		 \
}while(0)

int main( void)
{
	short a = 1, b = 2;
	short c = 5;
	printf("%d",c);
	
	
}