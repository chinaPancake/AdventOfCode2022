f = open('input.txt', 'r').read().strip()
lines = [x for x in f.split('\n')]

ans = 0
x = 1 
processing = -1 
display = [['?' for i in range(40)] for i in range(6)]

def change(pro:int, y:int, display):
    display[pro//40][pro%40] = ('#' if abs(y-(processing%40))<=1 else '.')
    return display 
   


for line in lines:
    cmd = line.split()
    if cmd[0] == 'noop':
        processing +=1
        change(pro=processing, y = x, display=display)
        if processing in [20,60,100,140,180,220]:
            ans += x*processing
    elif cmd[0] == 'addx':
        processing += 1
        change(pro=processing, y = x, display = display)
        if processing in [20,60,100,140,180,220]:
            ans += x*processing 
        processing +=1
        change(pro = processing, y = x, display = display)
        if processing in [20,60,100,140,180,220]:
            ans += x* processing
        x += int(cmd[1])

change(processing,x, display=display )

for i in display:
    print(' ')
    for x in i:
        print(x, end="")
