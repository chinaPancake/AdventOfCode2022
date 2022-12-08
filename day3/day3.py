file = open("./day3/input_file_day3.txt", "r")
wynik = 0
a = 0
for i in file:
    secik = set()
    i_first = i[: len(i) // 2]
    i_second = i[len(i) // 2 :]
    for letters in i_first:
        if letters in i_second:
            if letters in secik:
                pass
            else:
                if letters.isupper() == True:
                    print(ord(letters) - 38, letters)
                    wynik += ord(letters) - 38
                else:
                    print(ord(letters) - 96, letters)
                    wynik += ord(letters) - 96

                secik.add(letters)
# --------- second part


X = [line for line in open("./day3/input_file_day3.txt")]
x = 0
wyniczek = 0
while x < len(X):
    for y in X[x]:
        secik = set()
        if y in X[x + 1] and y in X[x + 2]:
            if "a" <= y <= "z":
                wyniczek += ord(y) - ord("a") + 1
            else:
                wyniczek += ord(y) - ord("A") + 1 + 26
            break
    x += 3
print(wyniczek)


X = [line for line in open("./day3/input_file_day3.txt")]
x = 0
wyniczek = 0
while x < len(X):
    for y in X[x]:
        secik = set()
        if y in X[x + 1] and y in X[x + 2]:
            if "a" <= y <= "z":
                wyniczek += ord(y) - ord("a") + 1
            else:
                wyniczek += ord(y) - ord("A") + 1 + 26
            break
    x += 3
print(wyniczek)


# print(wynik)

"abc dea"
"a  aa baa"
