#! /bin/python3

def merge(frm,to):
    result=[]
    i,j=0,0
    while i<len(frm) and j<len(to):
        if frm[i] < to[j]:
            result.append(frm[i])
            i += 1
        else:
            result.append(to[j])
            j += 1
    while i < len(frm):
        result.append(frm[i])
        i += 1
    while j < len(to):
        result.append(to[j])
        j += 1
    # put result into frm
    for n in range(len(result)):
        if n < i:
            frm[n] = result[n]
        else:
            frm.append(result[n])
    return frm
if __name__ == '__main__':
    frm=[8,4,5,6,7]
    to = [2,5,3,8,9,15]
    result = merge(sorted(frm),sorted(to))
    print(result)
    print(set(result))
    # 1, 2, 4, 5, 5, 6, 6, 7, 8, 9, 15
    # 1, 2, 4, 5, 5, 6, 6, 7, 8, 9, 15
    #[1, 2, 4, 5, 5, 6, 6, 7, 8]