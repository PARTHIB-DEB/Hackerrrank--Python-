if __name__ == '__main__':
    result = []
    scores  = []
    for _ in range(int( input())):
        name = input()
        score= float( input())
        result.append([name,score])
        scores.append( score)
    minimum = min(scores)
    while(minimum in scores):
       scores.remove(minimum)
    
    result.sort()
    b = min(scores)
    for i in range(len(result)):
         if(result[i][1]==b):
               print(result[i][0])
            