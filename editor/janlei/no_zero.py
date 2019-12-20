#! /bin/python3
def no_zero(arr):
    index, i, lenth = 0, 0, len(arr)
    while i < lenth - index:
        if arr[i+index] == 0:
            index += 1
        else:
            arr[i] = arr[i+index]
            i += 1
    for i in range(index):
        arr[lenth-1-i] = 0
    return arr

def best(arr):
    zero_i,index = 0,0
    lenth = len(arr)
    #find zero_i
    while zero_i < lenth:
        if arr[zero_i] == 0:
            break
        else:
            zero_i += 1
    # find no_zero_i
    no_zero_index = zero_i +1
    while no_zero_index < lenth:
        if not arr[no_zero_index] == 0:
            break
        else:
            no_zero_index += 1
    #find not zero
    while no_zero_index < lenth:
        if not arr[no_zero_index] == 0:
            swap(arr,zero_i,no_zero_index)
            zero_i += 1
        no_zero_index += 1
    return arr

def swap(arr,frm,to):
    temp = arr[frm]
    arr[frm] = arr[to]
    arr[to] = temp

def move(arr):
    zero_i = 0
    for i in range(len(arr)):
        if not arr[i] == 0:
            arr[i - zero_i] = arr[i]
        else:
            zero_i += 1
    for i in range(zero_i):
        arr[len(arr)-1-i] = 0
    return arr

def bt(arr):
    j=0
    for i in range(len(arr)):
        if not arr[i] == 0:
            tmp = arr[i]
            arr[i] = arr[j]
            arr[j] = tmp
            j += 1
    return arr
if __name__ == '__main__':
    arr = [3,4,99,9,0,0,9]
    print(bt(arr))