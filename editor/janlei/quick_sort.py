#! /bin/python3
def partition(arr,left,right):
    pivot = arr[right]
    j = left
    for i in range(left,right):
        if arr[i] < pivot:
            swap(arr,i,j)
            j += 1
    swap(arr,j,right)
    return j

def sortv(arr,left,right):
    if left < right:
        pivot_index = partition(arr,left,right)
        sortv(arr,left,pivot_index-1)
        sortv(arr,pivot_index+1,right)
def swap(arr,frm,to):
    tmp = arr[frm]
    arr[frm] = arr[to]
    arr[to] = tmp


if __name__ == '__main__':
    arr = [1,4,6,2]
    sortv(arr, 0, 3)
    print(arr)
