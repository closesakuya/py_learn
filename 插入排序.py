
def insert_sort( lst ):
    for i in range(1,len(lst)):
        insert_val = lst[i]

        for j in range(i)[::-1]:
            if lst[j] > insert_val:
                lst[j+1] = lst[j]
            else:
                break
        else:   #!!!!循环正常执行完，未break则进入
            j -= 1
            
        lst[j+1] = insert_val
                

a = [777,555,1,3,5,1,8,3,5,1,9,121]
insert_sort(a)
print(a)
              
