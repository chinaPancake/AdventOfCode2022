file = open("input_file_day1.txt", "r")
elves = []
liczba = 0
elves_sum = []
for i in file:
    if i[-1:] == "":
        continue
    elif i[-1:] == "\n":
        elves.append(i[:-1])
    else:
        elves.append(i)

for liczby in elves:
    if liczby == "":
        elves_sum.append(liczba)
        liczba = 0
    elif liczba != "":
        liczba += int(liczby)

elves_sum.sort()
elves_sum.reverse()
cc = 0
for i in range(0, 3):
    cc += elves_sum[i]
print(cc)
