
# sublist1=(1,2,3)
# sublist2=(4,5,6)
# sublist3=(8,9,10)
# main_lits=sublist1+sublist2+sublist3
# print(main_lits)

new_list=[]
rc_list=input("").split(" ")
# print(rc_list)
for i in range(int(rc_list[1])):
    # print(f"{i+1}th value of both:",end="")
    sub_list=[]
    sub_list.append(input("").split(" "))
    new_list+=sub_list
    new_list1=list(zip(*new_list))
    

# print (new_list1)
for i in range(len(new_list1)):
    sub=new_list1[i]
    sum=0
    for j in range(0,len(sub)):
        sum+=float(sub[j])
    result=sum/len(sub)
    # print(f"\n\tSTUDENT {i} GOT {result} IN AVERAGE")
    print(result)