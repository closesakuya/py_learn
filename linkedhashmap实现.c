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

typedef struct Node
    {
		struct Node *pPre;
		struct Node *pNxt;
		struct Node *pHNxt;		//hash map拉链下一节点
		void   *pKey;
		UINT8 pData;
    }tNode;


typedef struct Key
    {
		struct Key *pNxt;
		void  *pDown;		//
		void   *pKey;
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
	INT16 (*campkeyfunc)(void *key1, void* key2);  //key 比较方法，key1大于key2返回 1,小于返回-1,等于返回0
    tNode  *pHead;
	tNode  *pTail;
	tKey   *topkey;
    
    
} Linkedhashmap;



tKey* upgrade_skiplist_key(tKey   *topkey, UINT32 keyInterv)
{	
	tKey	*p1 = (tKey*)malloc(sizeof(tKey));
	tKey	*p2, *temp, *temp_pre;
	UINT32	skip = 1,grade = topkey->grade + 1;
	temp = topkey->pNxt;
	temp_pre = topkey;
	p1->pKey = topkey->pKey;
	p1->pDown = topkey;
	p1->pNxt = 0;
	p1->grade = grade;
	topkey = p1;
	
	while( temp )
	{
		if( skip%keyInterv == 0)
		{
			p2 = (tKey*)malloc(sizeof(tKey));
			p2->pKey = temp->pKey;
			p2->pDown = temp;
			p2->grade = grade;
			p1->pNxt = p2;
			p1 = p2;
			skip = 0;
			
		}
		
		skip++;
		temp_pre = temp;
		temp = temp->pNxt;
	}
	
	if  (temp_pre != p2->pDown)
	{
		p2 = (tKey*)malloc(sizeof(tKey));
		p2->pKey = temp_pre->pKey;
		p2->pDown = temp_pre;
		p2->grade = grade;
		p1->pNxt = p2;			
	}
	
	return topkey;
}


tNode* search_skiplist(tKey   *topkey, void *key, INT16 (*campkeyfunc)(void *, void* ))
{
	tKey	*cursor = topkey,*cursor_nxt;
	tNode	*node = 0;

	
	while(cursor)
	{
		cursor_nxt = cursor->pNxt;
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
			cursor = cursor->pNxt;
	}
	
	while(node)
	{

		if( campkeyfunc(key,node->pKey) == 1)
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

void insert_skiplist(tKey   *topkey, tNode *node, void *key, INT16 (*campkeyfunc)(void *, void* ))   //需保证key不在list中，否则直接返回
{
	tKey	*cursor = topkey,*pre_cursor = 0,*cursor_nxt, *pre_new = 0,*newkey;
	tNode	*curnode = 0, *prenode = 0;
	INT32	grade;
	

	
	//查找插入
	
	//判断是否增加跳表索引层
	
	//更新索引
	grade = random_grade(topkey->grade);
	
	while( grade > 0)
	{
		grade = cursor->grade;
		
	}

	
	return;
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