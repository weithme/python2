# -*- coding: utf-8 -*-

#1. Задание на закрепление знаний по модулю CSV. Написать скрипт, осуществляющий выборку определенных данных из файлов info_1.txt, info_2.txt, info_3.txt и формирующий новый «отчетный» файл в формате CSV. Для этого:
#Создать функцию get_data(), в которой в цикле осуществляется перебор файлов с данными, их открытие и считывание данных. В этой функции из считанных данных необходимо с помощью регулярных выражений извлечь значения параметров «Изготовитель системы», «Название ОС», «Код продукта», «Тип системы». Значения каждого параметра поместить в соответствующий список. Должно получиться четыре списка — например, os_prod_list, os_name_list, os_code_list, os_type_list. В этой же функции создать главный список для хранения данных отчета — например, main_data — и поместить в него названия столбцов отчета в виде списка: «Изготовитель системы», «Название ОС», «Код продукта», «Тип системы». Значения для этих столбцов также оформить в виде списка и поместить в файл main_data (также для каждого файла);
#Создать функцию write_to_csv(), в которую передавать ссылку на CSV-файл. В этой функции реализовать получение данных через вызов функции get_data(), а также сохранение подготовленных данных в соответствующий CSV-файл;
#Проверить работу программы через вызов функции write_to_csv().

import csv
import re

def get_data(files):
    os_name_lst = []
    manufacturer_lst = []
    product_code_lst = []
    system_type_lst = []
    headers = ['Изготовитель системы', 'Название ОС', 'Код продукта', 'Тип системы']
    
    for f in files:
        with open(f, encoding='CP1251') as f_n:        
            f_n_reader = csv.reader(f_n)
            for row in f_n_reader:
                m = re.match(r"Название ОС:(.*)", row[0])
                if m:                    
                    os_name = m.group(1).strip()
                    os_name_lst.append(os_name)
                    
                m = re.match(r"Изготовитель системы:(.*)", row[0])
                if m:                    
                    manufacturer = m.group(1).strip()
                    manufacturer_lst.append(manufacturer)
                    
                m = re.match(r"Код продукта:(.*)", row[0])
                if m:                    
                    product_code = m.group(1).strip()
                    product_code_lst.append(product_code)
                    
                m = re.match(r"Тип системы:(.*)", row[0])
                if m:                    
                    system_type = m.group(1).strip()
                    system_type_lst.append(system_type)
    main_data = [headers, [os_name_lst, manufacturer_lst, product_code_lst, system_type_lst]]                
    return main_data

def write_to_csv(files):
    for f in files:
        main_data = list(get_data([f]))    
        output_name = '{}.csv'.format(f.split('.')[0])
        
        with open(output_name, 'w') as f_n:
            f_n_writer = csv.writer(f_n)
            for row in main_data:
                f_n_writer.writerow(row)
        print('Записан файл {}'.format(output_name))
    
files = ['info_1.txt', 'info_2.txt', 'info_3.txt']
write_to_csv(files)
