from collections import defaultdict


f = open('input.txt','r').readlines()


#max size of 100000
#sum of the all directory with maxsize of 100000

# pomysły na rozwiązanie, 
# 1. Zrobienie dicta który reaguje na komendy // problemy: jak rozwiązać sprawę z przejściem do stworzonego folderu, 
# po komendzie cd folder tworzymy nową liste do której później appendujemy podfoldery, i wage plików jako int.
# jak poruszamy sie po listach list? 
# tworzenie nowego dicta jako folder? 

#2. Stworzenie klasy folder, która wywołuje się po komendzie cd

directory = [['$ cd /']]
directory_list = []
file_size_dict = defaultdict(int)
file_size = 0
make_dir = []

#part two
needed_disc_space = 70000000 - 30000000

for commands in f:
    cmd = commands.strip().split()
    if cmd[1] == 'cd':
        if cmd[2] == '..':
            make_dir.pop()
        else:
            make_dir.append(cmd[2])
    else:
        try:
            file_size = int(cmd[0])
            for i in range(len(make_dir)+1):
                file_size_dict['/'.join(make_dir[:i])] += file_size
        except:
            pass

total_used_space = file_size_dict['/']
to_delete = total_used_space - needed_disc_space
print(total_used_space)


ans = 99999999999999999
for key,value in file_size_dict.items():
    if value >=to_delete:
        ans = min(ans,value)
print(ans)
#    if value <= 100000:
#        ans += value
