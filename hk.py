if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    for i,j in enumerate(arr):
        if j==(max(arr)-1):
            print(j)