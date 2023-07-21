# Enter your code here. Read input from STDIN. Print output to STDOUT

group=input("")
my_list=list(map(int,group.split(" ")))
my_sum=int(my_list[0])+int(my_list[1])
A_list=[]
B_list=[]
for i in range(1,my_sum+1):
    value=input("")
    if i<=my_list[0]:
        A_list.append(value)
    else:
        B_list.append(value)
        
for i in range(1,len(A_list)):
    for j in B_list:
        if A_list[i]==j:
            if A_list[i]=='a':
                print(i,end="")
            else:
                print(i,end="")
                
        
    

