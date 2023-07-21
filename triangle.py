# for i in range(1,int(input())+1): #More than 2 lines will result in 0 score. Do not leave a blank line also
#     print (i if i==1 or i==)

# def increment(i):
#     if i==1:
#         return 1
#     for j in range(1,(2*i)):
#         value=1    
#         if value==i:
#             value-=1
#         else:
#             value+=1
#         return print(value,end="")
limit=int(input("\n\tlimit(odd only!!):"))
for i in range(1,(2*limit-1)): #More than 2 lines will result in 0 score. Do not leave a blank line also
    print((pow(10,i)//9)**2)

