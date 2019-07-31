#使用(0,1,2,3) 序号表示行号，例表示四颗棋子:(0,0)(1,1)(2,2)(3,3) 


#核心，利用形参trace传递时 递归调用返回时自动回溯
#若递归传参使用trace += [i] 而非 trace+[i] 则会修改初始传入list
#trace + [i] 实际会新建对象传递给新的递归函数
def queen( num, trace = []):
    for i in range(num):
        flag = False
        if [] == trace and i != 0:
            flag = True
        else:
            for idx,item in enumerate(trace):
                if i != item and (len(trace) - idx) != abs(item - i):
                    flag = True
                else:
                    flag = False
                    break;
        if flag:
            if len(trace) == (num - 1):
                print(trace+[i])
            else:
                #newtrace = trace + [i] 等价
                #queen(num,newtrace) 等价
                #trace+= [i]    不等价
                queen(num,trace + [i])
                


queen(8)


#使用递归加生成器
def arrange_queen(num, queen_tup=list()):
    """
    :param num:棋盘的的行数，当然数值也等于棋盘的列数
    :param queen_tup: 设置一个空队列，用于保存符合规则的棋子的信息
    """
 
    for new_queen in range(num):    # 遍历一行棋子的每一列
 
        if is_rule(queen_tup, new_queen):   # 判断是否冲突
 
            if len(queen_tup) == num-1:     # 判断是否是最后一行
                yield [new_queen]   # yield关键字
 
            else:
                # 若果不是最后一行，递归函数接着放置棋子
                for result in arrange_queen(num, queen_tup+[new_queen]):
                    yield [new_queen] + result
 
 
for i in arrange_queen(4):
    print(i)
--------------------- 
作者：NicolasLinJieChuang 
来源：CSDN 
原文：https://blog.csdn.net/weixin_41865447/article/details/80034433 
版权声明：本文为博主原创文章，转载请附上博文链接！
