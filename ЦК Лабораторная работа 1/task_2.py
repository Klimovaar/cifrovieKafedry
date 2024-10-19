# TODO Найдите количество книг, которое можно разместить на дискете
disk_size = 1.44
str = 100
strok_na_str = 50
synvol_na_stroky = 25

symvol_in_book = str * strok_na_str * synvol_na_stroky

obyem = symvol_in_book * 4
disk_size *= 1024**2

number = int (disk_size // obyem)


print("Количество книг, помещающихся на дискету:",number)
