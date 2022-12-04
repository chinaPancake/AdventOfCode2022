file = open("./day4/input_file_day4.txt", "r").readlines()
wynik = 0
wyniczek = 0
for i in file:
    first, second = i.split(",")
    ffirst, sfirst = first.split("-")
    fsecond, ssecond = second.split("-")
    ffirst, sfirst, fsecond, ssecond = [
        int(x) for x in [ffirst, sfirst, fsecond, ssecond]
    ]

    if not (sfirst < fsecond or ssecond < ffirst):
        wyniczek += 1
    if (
        ffirst <= fsecond
        and ssecond <= sfirst
        or fsecond <= ffirst
        and sfirst <= ssecond
    ):
        wynik += 1
print(wynik)
print(wyniczek)
