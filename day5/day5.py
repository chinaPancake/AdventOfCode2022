f = open("./day5/input.txt").read().strip()
cmd = [x.strip() for x in f.split("\n")]
start = [
    [],
    ["W", "R", "T", "G"],
    ["W", "V", "S", "M", "P", "H", "C", "G"],
    ["M", "G", "S", "T", "L", "C"],
    ["F", "R", "W", "M", "D", "H", "J"],
    ["J", "F", "W", "S", "H", "L", "Q", "P"],
    ["S", "M", "F", "N", "D", "J", "P"],
    ["J", "S", "C", "G", "F", "D", "B", "Z"],
    ["B", "T", "R"],
    ["C", "L", "W", "N", "H"],
]
for command in cmd:
    command_moves = command.split()
    # from command_moves[3]
    from_ = int(command_moves[3])
    # move command_moves[1]
    number_ = int(command_moves[1])
    # to command_moves[5]
    to_ = int(command_moves[5])
    Move_ = start[from_][:number_]
    start[from_] = start[from_][number_:]
    start[to_] = Move_ + start[to_]

for s in start:
    if len(s) > 0:
        print(s[0])
