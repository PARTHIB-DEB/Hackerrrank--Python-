# def merge_the_tools(string, k):
#     # your code goes here
#     length=len(string)
#     sub_len=(length//k)
#     i=0
#     for i in range(0,length,sub_len):
#         new_substr=string[i:i+sub_len]
#         print(f"SUBSTR[%d]:{new_substr}" %(i))
#         word=list()
#         for j in range(0,len(new_substr)):
#             word.insert(j,new_substr[j])
#         print(word)
#         word[i]=None
#         print(word)
def merge_the_tools(string, k):
    # your code goes here
    c=0
    s=''
    for i in string:
        if i not in s:
            s=s+i
            print(f"{i} OF INDEX {c} OF STRING ADDED :{s}")
        c+=1
        if(c==k):
            print(s)
            c=0
            s=''
    

        
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)