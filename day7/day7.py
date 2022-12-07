f = open('input.txt','r').readlines()


#max size of 100000
#sum of the all directory with maxsize of 100000

commands = [['$ cd /']]
directory_list = [
        ]
asd = '$ cd /'

directory_dict={
        '$ cd /': Node()
        }

if asd == directory[0]:
    print('dziala')
for i in f:
    b = ''.join(i).split('\n')
    if b[0] == directory[0]:
        directory_list.dict[b[0][:-1]]
        print(directory.index(b[0]))
    if b[0][0:3] == 'dir':
        directory_list.append([b[0][4:-1]])

print(directory_list)



head = Node('/')
dd_dir = Node('nazwa' parent='/')
