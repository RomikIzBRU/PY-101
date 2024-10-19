# TODO Найдите количество книг, которое можно разместить на дискете

pages_number=100
row_number=50
char_number=25
symbol_size=4
diskette_size=1.44*1024*1024 #в байтах

book_size=symbol_size*char_number*row_number*pages_number
books_number=int(diskette_size/book_size)
print("Количество книг, помещающихся на дискету:",books_number)
