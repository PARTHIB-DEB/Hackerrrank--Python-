# if __name__ == '__main__':
#     big_list=[]
#     for _ in range(int(input("\n\tHow many:"))):
#         name = input("\n\tEnter name:")
#         score = float(input("\n\tEnter Score:"))
#         big_list.append([name,score])
#         big_dict=dict(big_list)
#         big_dict1={key: val for key, val in sorted(big_dict.items(), key = lambda ele: ele[0])}
#         min_value=min(big_dict1.values())
        
#         big_dict1.pop()
#     print(big_dict1)

# if __name__ == '__main__':
#     n = int(input())
#     arr = list(map(int, input().split()))
#     for i in range(0,len(arr)):
#         max_value=max(arr)
#         if arr[i]<max_value:
#             for j in range (0,len(arr)):
#                 if arr[i]>=arr[j] and arr[i]<max(arr):
#                     print(arr[i])
#                     break
    
# n=int(input())
# my_tuple=(input().split())
# print(hash(my_tuple))

def solve(s):
    my_list=list(s.split(" "))
    for i in range(0,len(my_list)):
        my_str=str(my_list[i])
        my_str.capitalize()

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()

    