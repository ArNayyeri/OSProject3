import copy


def fcfs(tasks):
    t = copy.deepcopy(tasks)
    s = 0
    print('First-Come, First-Served Start')
    for i in t:
        while i[2] > 0:
            i[2] -= 1
            s += 1
            print(str(s) + ': task ' + i[0] + ', remaining time -> ' + str(i[2]))
    print('First-Come, First-Served Finish\n\n')


def sjb(tasks):
    t = copy.deepcopy(tasks)
    t.sort(key=lambda x: (x[1], -x[2]), reverse=True)
    s = 0
    print('Shortest-Job-First Start')
    for i in t:
        while i[2] > 0:
            i[2] -= 1
            s += 1
            print(str(s) + ': task ' + i[0] + ', remaining time -> ' + str(i[2]))
    print('Shortest-Job-First Finish\n\n')


def rr(tasks, round_time):
    t = copy.deepcopy(tasks)
    s = 0
    print('Round-Robin Start')
    while len(t) > 0:
        is_finished = False
        for i in range(round_time):
            t[0][2] -= 1
            s += 1
            print(str(s) + ': task ' + t[0][0] + ', remaining time -> ' + str(t[0][2]))
            if t[0][2] == 0:
                is_finished = True
                break
        tt = t.pop(0)
        if not is_finished:
            t.append(tt)
    print('Round-Robin Finish\n\n')


def hrrn(tasks):
    t = copy.deepcopy(tasks)
    s = 1
    print('Highest Response Ratio Next Start')
    while len(t) > 0:
        t.sort(key=lambda x: (x[1], ((s + x[2]) / x[2]), -tasks.index(x)), reverse=True)
        while t[0][2] > 0:
            t[0][2] -= 1
            print(str(s) + ': task ' + t[0][0] + ', remaining time -> ' + str(t[0][2]))
            s += 1
        t.pop(0)
    print('Highest Response Ratio Next Finish\n\n')


if __name__ == '__main__':
    n = int(input())
    tasks = []
    for i in range(n):
        tasks.append(input().split(' '))
        tasks[i][1] = tasks[i][1].upper()
        tasks[i][2] = int(tasks[i][2])
    fcfs(tasks)
    sjb(tasks)
    rr(tasks, 1)
    hrrn(tasks)
