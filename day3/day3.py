file = open("./day3/input_file_day3.txt", "r")
wynik = 0
a = 0
secik = set()
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

print(wynik)

"abc dea"
"a  aa baa"
