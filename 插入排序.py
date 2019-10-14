
def insert_sort( lst ):
    for i in range(1,len(lst)):
        insert_val = lst[i]
        for j in range(i)[::-1]:
            if lst[j] > insert_val:
                lst[j+1] = lst[j]
            else:
                lst[j+1] = insert_val
                break
                

a = [1,3,5,1,8,3,5,1,9,121]
insert_sort(a)
print(a)
              
