import re
def minion_game(string):
    # your code goes here
    j=0
    count_vow=0
    count_cons=0
    for i in range(0,len(string)):
        if string[i]=="A" or string[i]=="E" or string[i]=="I" or string[i]=="O" or string[i]=="U":
            j=j+i+1
            substr1=string[i:j]
            if re.search(substr1,string):
                count_vow+=1
                # print(count_vow)
                
        else:
            j=j+i+1
            substr2=string[i:j]
            if re.search(substr2,string):
                count_cons+=1
                # print(count_cons)
    
    if count_cons>count_vow:
        print(f"Stuart {count_cons}")
    else:
        print(f"Kevin {count_vow}")
        
             

if __name__ == '__main__':
    s = input()
    minion_game(s)