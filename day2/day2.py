file = open("./day2/input_file_day2.txt", "r")
score = 0
for i in file:
    oponent, player = i.split()
    print(player, oponent)
    score += {"X": 0, "Y": 3, "Z": 6}[player]
    score += {
        ("A", "X"): 3,
        ("A", "Y"): 1,
        ("A", "Z"): 2,
        ("B", "X"): 1,
        ("B", "Y"): 2,
        ("B", "Z"): 3,
        ("C", "X"): 2,
        ("C", "Y"): 3,
        ("C", "Z"): 1,
    }[(oponent, player)]

print(score)

# A for rock
# B for paper
# C for scisors

# X for rock 1
# Y for paper 2
# Z for Scissors 3

# lose 0
# draw 3
# win 6
X = 1
Y = 2
Z = 3
