#! /bin/python3

#define tree arr
# n length
# i index
def heapify(tree,n,i):
    #exit
    if i>= n:
        return
    left = i*2+1
    right = (i+1)<<1
    max = i;
    if left < n and tree[left] > tree[max]:
        max = left
    if right < n and tree[right] > tree[max]:
        max = right
    if not max == i:
        swap(tree,max,i)
        # todo
        heapify(tree,n,max)

def heapImp(tree):
    last_index = len(tree) - 1
    parent = (last_index-1)//2
    for i in range(parent,-1,-1):#[from,to)
        heapify(tree,len(tree),i)


def sort(tree):
    #buidheap
    heapImp(tree)
    #将根节点砍断 移至后尾
    for i in range(len(tree)):
        heapify(tree,len(tree)-i,0)
        #没有将其tree砍断
        swap(tree,0,len(tree)-i-1)
#define swap max
def swap(arr,to,frm):
    tmp = arr[to]
    arr[to] = arr[frm]
    arr[frm] = tmp

def prinf(arr):
    for i in range(len(arr)):
        print(arr[i])
if __name__ == '__main__':
    #arr=[4,10,3,5,1,2]
    # arr=[1,3,4,2,5,10]
    arr=[2,5,3,1,10,4]

    #heapify(arr,len(arr),0)
    heapImp(arr)
    sort(arr)
    prinf(arr)
