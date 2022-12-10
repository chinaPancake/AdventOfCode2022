from re import L

f = open('input.txt', 'r').read().strip()

lines = [x for x in f.split('\n')]
hx,hy = 0,0
tx,ty = 0,0 
t_positions = set()
t_positions.add((0,0))
ans = 0
tail_list = [(0,0) for _ in range(10)]

def tail_function(hx,hy,tx,ty):
    
    if abs(hx-tx)>1 or abs(hy-ty)>1:
        ty +=(hy>ty) - (hy<ty)
        tx += (hx>tx) - (hx<tx)
    return tx, ty

for cmd in lines:
    where, amount = cmd.split()
    for amt in range(int(amount)):    
        if where == 'R':
            hx += 1 
        elif where == 'L':
            hx -= 1
        elif where == 'U':
            hy += 1
        elif where == 'D':
            hy -= 1        
        
        tail_list[0] = (hx,hy)
        for i in range(1, len(tail_list)):
            tx, ty = tail_function(hx = tail_list[i-1][0],hy = tail_list[i-1][1],tx=tail_list[i][0],ty=tail_list[i][1])
            tail_list[i] = (tx,ty)
        
        t_positions.add(tail_list[-1])


    #print(tx,ty,hx,hy)    
print(len(t_positions))


