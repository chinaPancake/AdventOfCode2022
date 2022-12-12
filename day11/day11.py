f = open('input.txt','r').read().strip()
lines = [x for x in f.split('\n')]

monke_list = []
operation_list = []
new = 0 
for cmd in f.split('\n\n'):
    m_id, items, operation, test, istrue, isfalse = cmd.split('\n')
    monke_list.append([int(i) for i in items.split(':')[1].split(',')])
    operation_list.append([i for i in operation.split()[3:6]])
    for op in operation_list:
        i = len(monke_list) - 1
        old = sum(monke_list[i])
        print(old)
        if op[0] == 'old' and op[2] == 'old' and op[1] == '*':
            new = old * old
        elif op[0] == 'old' and op[1] == '+':
            new = old + int(op[2]) 
        elif op[0] == 'old' and op[1] == '*':
            new = old * int(op[2])
        print(op)
    print(new)
        

