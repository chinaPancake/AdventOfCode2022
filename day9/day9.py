from re import L


f = open('input.txt', 'r').read().strip()

lines = [x for x in f.split('\n')]
hx,hy = 0,0
tx,ty = 0,0 
t_positions = set()
t_positions.add((0,0))
ans = 0
zmiena = {(1,1),(1,0),(-1,-1),(0,-1)}

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
       
        if (hx - tx)>1 and (hy == ty): 
            tx = tx + 1

        elif (hy-ty)>1 and (hx == tx):
            ty = ty + 1

        elif (tx-hx)>1 and (hy==ty):
            tx = tx - 1 

        elif (ty-hy)>1 and (tx==hx):
            ty = ty - 1 

        elif (hx-tx)>1 and (hy-ty)>0:
            tx = tx + 1
            ty = ty + 1  

        elif (hy-ty)>1 and (hx-tx)>0:
            ty = ty + 1
            tx = tx + 1

        elif (ty-hy)>1 and (tx-hx)>0:
            ty = ty - 1
            tx = tx -1
            
        elif (tx-hx)>1 and (ty-hy)>0:
            tx = tx - 1
            ty = ty -1 
        
        elif (hx-tx)>1 and (ty-hy)>0:
            tx = tx + 1 
            ty = ty - 1
        
        elif (ty-hy)>1 and (hx-tx)>0:
            ty = ty - 1
            tx = tx + 1 
        elif (tx-hx)>1 and (hy-ty)> 0:
            tx = tx-1
            ty = ty +1
        elif (hy-ty)>1 and (tx-hx)>0:
            ty = ty+1 
            tx = tx-1 



        t_positions.add((tx,ty))

    print(tx,ty,hx,hy)    
print(len(t_positions))


