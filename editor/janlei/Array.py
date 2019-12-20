#! /bin/python3

def printf2th(students):
    twice = sorted(list(set([names for name, names in students])))[1]
    for i in range(len(students) - 1, -1, -1):
        if students[i][1] == twice:
            name = students[i][0]
            print(name)


if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])
    printf2th(students)