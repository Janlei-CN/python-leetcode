#! /bin/python3
def lastPre(arr):
    newarr = set(list(arr))
    newarr.remove(max(newarr))
    print(max(newarr))

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    lastPre(arr)