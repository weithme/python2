# 6. Создать текстовый файл test_file.txt, заполнить его тремя строками: «сетевое программирование», «сокет», «декоратор». Проверить кодировку файла по умолчанию. Принудительно открыть файл в формате Unicode и вывести его содержимое.

# Создать текстовый файл test_file.txt
f_n = open('test_file.txt', 'w', encoding='CP866')
f_n.write('сетевое программирование\n')
f_n.write('сокет\n')
f_n.write('декоратор')
f_n.close()

# Проверить кодировку файла по умолчанию
print(f_n) # <_io.TextIOWrapper name='test_file.txt' mode='w' encoding='CP866'>

# Принудительно открыть файл в формате Unicode и вывести его содержимое
with open('test_file.txt', encoding='utf-8') as f_n:
    for line in f_n: print(line.decode('CP866'))
    
# ошибка: UnicodeDecodeError: 'utf-8' codec can't decode bytes in position 0-1: invalid continuation byte
