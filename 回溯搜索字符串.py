#单词搜索
#例
# b a d
# p p e
# e c f
#dict{apple,pin}
#return: apple [(0,1)(1,1)(1,0)(2,0)]  不允许路径交叉


def get_xy_valid(xy, maxsizex,maxsizey):
    if xy[0] >= maxsizex or xy[1] >= maxsizey or \
        xy[0] < 0 or xy[1] < 0:
        return False
    else:
        return True
    

def find_nxt(cur_word, cur_xy, path, mat):
    if path:
        drt = [(0,1),(1,0),(0,-1),(-1,0)]
    else:
        drt = [(0,0)]
    for i,j in drt:
        newxy = (cur_xy[0]+i,cur_xy[1]+j)
        if get_xy_valid(newxy,len(mat),len(mat[0])):
            if cur_word[0] == mat[newxy[0]][newxy[1]]:
                if newxy not in path:
                    if len(cur_word) == 1:
                        print(path+[newxy])
                    else:
                        find_nxt(cur_word[1:],newxy,path+[newxy],mat)
    return None
                    
    


def findword(word,mat):
    print('find-->'+word)
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            find_nxt(word,(i,j),[],mat)


def finddict(dct,mat):
    for item in dct:
        findword(item,mat)

mat =[
    'badcda',
    'ppeape',
    'leappl'

    ]

findword('a',mat)

finddict(['apple','bad'],mat)
        
