#!/bin/python3

# 将n个hanoi从A移动到C借助B
def hanoi(n, A, B, C):
    if n == 1:  # 只有一个的时候
        mv(A, C)  # 将最后的一个从A移到C
    else:
        hanoi(n - 1, A, C, B)  # 将n-1从A-》B借助C
        mv(A, C)  # 最下面的从A移动到C
        hanoi(n - 1, B, A, C)  # 将剩余的n-1放到从B放到C


def mv(a, c):
    print(a, c, sep="->", end="\n")


# define n个hannoi从A移动到C借助B
def newHanoi(n, A, C, B):
    if n == 1:
        # 最后一个从A到C
        mv(A, C)
    else:  # 否则将n看做1 与 n-1来进行拆分
        newHanoi(n - 1, A, B, C)  # step1,将n-1（顶部）从A移动到B
        mv(A, C);  # 将最大的从A移动到C
        newHanoi(n - 1, B, C, A)  # 由于step1，所有需要将n-1从B移动到C


if __name__ == '__main__':
    newHanoi(3, "A", "C", "B")
