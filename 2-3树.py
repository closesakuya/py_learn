#默认不含重复key

class Node(object):
    def __init__(self,value,data,value_2 = None,data2 = None,l = None,r = None,m = None):
        self.value = value
        self.value_2 = value_2
        self.f = None
        self.l = l
        self.r = r
        self.m = m

    def __str__(self):
        return str(self.value)+','+str(self.value_2)

class Search2_3Tree(object):
    def __init__(self):
        self.root = None



    def __str__( self ):  #beautiful print
        ret = ''
        for i in range(1,self.layernum + 1):
            lt = self.getNodesByLayer(i)
            s = '\n\n'
            for item in lt:
                s = s.split('\n')
                item = str(item).split('\n')
                for i in range(len(s)):
                    s[i] += item[i]
                s = '\n'.join(s)
            ret += s + '\n'

        return ret
        
    @property
    def layernum( self ): #获取层数
        def _getlayernum(root, curlayer, maxlayer):
            if root:
                curlayer += 1
                _getlayernum(root.l,curlayer,maxlayer)
                _getlayernum(root.m,curlayer,maxlayer)
                _getlayernum(root.r,curlayer,maxlayer)
            else:
                if curlayer > maxlayer[0]:
                    maxlayer[0] = curlayer
            return

        max1 = [1]
        _getlayernum(self.root,1,max1)
        return max1[0]

    def getNodesByLayer(self, layer = 1): #按层获取元素
        lt = []
        if self.root:
            self._getNodeByLayer([(self.root,1)], lt, layer)

        return lt[::]

    def _getNodeByLayer( self, blk = [], res = [],destlayer = 1):
        if not blk:
            return
        root = blk.pop(0)
        if root[1] == destlayer:
            res.append(root[0])
        if root[0].r:
            blk.insert(0,(root[0].r,root[1]+1))
        if root[0].m:
            blk.insert(0,(root[0].m,root[1]+1))
        if root[0].l:
            blk.insert(0,(root[0].l,root[1]+1))

        self._getNodeByLayer(blk[::],res,destlayer)        



    def split_4(self, node):  #四节点分裂
        if not hasattr(node,'value_3'):
            return
        if not node.value_3:
            return
        father = node.f
        if not father:  #根结点，需要增加一层
            father = Node(node.value_2,node.data_2)
            self.root = father
            node_r = Node(node.value_3,node.data_3)
            node_r.l = node.m_2
            node_r.r = node.r

            node.l = node.l
            node.r = node.m
            node.value2 = None
            node.data2 = None
            node.m = None
            delattr(node,'value_3')
            delattr(node,'data_3')
            delattr(node,'m_2')

            father.l = node_l
            father.r = node_r
            return

        newfather = False
        if not father:  #根结点，需要增加一层
            newfather = True
            father = Node(node.value_2,node.data_2)
            self.root = father
        #非根结点
        if not father.value2: #父节点为2节点
            father.value2 = node.value3
            father.data2 = node.data3
            father.m = node
            node_r = Node(node.value_3,node.data_3)
            node_r.l = node.m_2
            node_r.r = node.r

            node.l = node.l
            node.r = node.m
            node.value2 = None
            node.data2 = None
            node.m = None
            delattr(node,'value_3')
            delattr(node,'data_3')
            delattr(node,'m_2')

            father.l = node_l
            father.r = node_r            
            
            
            
            
            

    def insert(self, node):
        if not self.root:
            self.root = node
            return

        cur = self.root
        while( True):   #查找插入到的叶子节点

        return


    def search(self, value):
        cur = self.root
        while(cur):
            if value == cur.value or value == cur.value_2:
                return cur
            if value < cur.value:
                cur = cur.l
            else if cur.value_2:
                if value > cur.value_2:
                    cur = cur.l
                else:
                    cur = cur.m
            else:
                cur = cur.r
             
        return res

    #遍历，参数，遍历方法(默认中序遍历，输出有序)
    def traverse(self, pfunc = print,method = 'mid'):
        if r'wid' in method or r'WID' in method:
            return self._traverse_Width([self.root],pfunc)
        else:
            return self._traverse_mid(self.root,pfunc)
            

    
    def _traverse_mid(self, root, pfunc = print):
        if not root:
            return
        self._traverse_mid(root.l,pfunc = pfunc)
        pfunc(root.value)
        self._traverse_mid(root.m,pfunc = pfunc)
        if root.value_2:
            pfunc(root.value_2)
        self._traverse_mid(root.r,pfunc = pfunc)
        

    #广度优先遍历
    def _traverse_Width(self,blk = [], pfunc = print):
        if not blk:
            return
        root = blk.pop(0)
        pfunc(root.value)
        if root.value_2:
            pfunc(root.value_2)
        if root.l:
            blk.append(root.l)
        if root.m:
            blk.append(root.m)
        if root.r:
            blk.append(root.r)

        self._traverse_Width(blk[::],pfunc = pfunc)
            

    def delete(self, value):

        cur = self.root
        father = None
        while(cur):
            if cur.value < value:
                father = cur
                drt = 1
                cur = cur.r
            elif cur.value > value:
                father = cur
                drt = -1
                cur = cur.l
            else:
                #右子树为空，同值结点都在右结点，可直接删除
                if not cur.r:
                    if father:
                        if 1 == drt:
                            father.r = cur.l
                        else:
                            father.l = cur.l
                    else:   #无父节点，删除根结点,左子节点上移，右子节点为空不操作
                        self.root = cur.l
                            
                    del cur
                    break
                        
                
                #与右子树最小值替换，后删除cur
                #查找右子树值最小结点,该最小结点其左子节点必为none
                swap = cur.r
                swap_father = cur
                while(True):
                    if swap.l:
                        swap_father = swap
                        swap = swap.l
                    else:
                        break

                if swap_father is not cur:   #防止自引用
                    swap_father.l = swap.r #swap的右子树放在其父节点的左结点
                    swap.l = cur.l
                    swap.r = cur.r

                else:   #只差一层，直接上移
                    swap.l = cur.l
                    
                if father:
                    if 1 == drt:
                        father.r = swap
                    else:
                        father.l = swap
                else:   #无父节点，删除根结点,右子节点上移，左子节点重新插入
                    self.root = cur.r
                    if cur.l:
                        self.insert(cur.l)
                del cur

                #继续右子树搜索同值结点
                if swap.value != value:
                    cur = swap.r
                else:   #交换后结点正好值为value  继续删除该结点
                    cur = swap

                        


aa = SearchBTree()
aa.insert(Node(1111))
aa.insert(Node(2222))
aa.insert(Node(7777))
aa.insert(Node(9999))
aa.insert(Node(5555))
aa.insert(Node(3333))
aa.insert(Node(7777))
aa.insert(Node(2222))
aa.traverse(method = 'mid',pfunc = lambda x: print(x.value))
print('---------')
print(aa)
print('---------')
aa.delete(7777)
print(aa)
print('---------')
aa.insert(Node(1111))
print(aa)
print('---------')
aa.delete(1111)
print(aa)
print('---------')
                    
              
                
                
