f = open('input.txt').read().strip()
data = [x for x in f.split('\n')]
width = []
height = []

for i in data:
    row = i
    width.append(row)

width_len = len(width)
height_len = len(width[0])
print(width_len, height_len)
ans = 0
#(2*width_len + 2*height_len)-4) 

check= [(-1,0), (1,0), (0,1), (0,-1)]
for r in range(width_len):
    for c in range(height_len):
        #        print(width[r], width[c])
#        print(width[r][r], width[r][c])
        is_visable= False
        for check_r, check_c in check: 
            rr = r
            cc = c
            check_f = True
            while True:
                rr += check_r
                cc += check_c
                if not (0<=rr<width_len and 0<=cc<height_len):
                    break
                if width[rr][cc] >= width[r][c]:
                    check_f = False
            if check_f:
                is_visable = True
        if is_visable:
            ans+=1

highest_tree = 0
for rows in range(width_len):
    for column in range(height_len):
        score = 1
        for check_r, check_c in check:
            distance = 1 
            rr = rows + check_r
            cc = column +check_c
            check_f = True
            while True:
                if not (0<= rr < width_len and 0<=cc<height_len):
                    distance -= 1
                    break
                if width[rr][cc] >= width[rows][column]:
                    break
                distance += 1
                rr += check_r
                cc += check_c
            score *= distance
        highest_tree = max(highest_tree, score) 
print(highest_tree)







