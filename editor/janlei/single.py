#! /bin/python3

def single(arr):
    sum, newsum = 0,0
    for i in arr:
        sum += i
    newarr = set(arr)
    for i in newarr:
        newsum += i
    return (newsum << 1) - sum

# xor a^b^a = b
def best(arr):
    a = arr[0]
    for i in range(1,len(arr)):
        a = (a ^ arr[i])
    return a
if __name__ == '__main__':
    arr = [1,1,5,5,7]
    print(best(arr))