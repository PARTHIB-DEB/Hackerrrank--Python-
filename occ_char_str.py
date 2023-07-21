def occ_char(item,num_str,length):
    count=1
    k=item+1
    for j in range(k,length):
        if num_str[item]==num_str[j]:
            count+=1
        else:
            break
    index_tup=(count,int(num_str[item]))
    my_list.insert(item,str(index_tup))
    return count

str_inp=input("\n\t NUM-STRING:")
progress=1
i=0
my_list=[]
while (i<len(str_inp)):    # selecting each item
    progress=occ_char(i,str_inp,len(str_inp))
    i+=progress
# print(my_list)
my_str=" ".join(my_list)
print(my_str)