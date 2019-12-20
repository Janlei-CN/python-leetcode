#! /bin/python3

#0,1,2,4,8,16
#转换为2进制
def isPower(num):
    if num < 1:
        return False
    #change from 10 to 2
    result = bin(num).replace('0b', '')
    # 统计1出现的次数
    count = result.count('1')
    if count > 1:
        return False
    else:
        return True

def best(num):
    if num < 1:
        return False
    return num&(num-1)==0 if True else False
if __name__ == '__main__':
    print(best(4))