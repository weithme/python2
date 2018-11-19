# 4. Преобразовать слова «разработка», «администрирование», «protocol», «standard» из строкового представления в байтовое и выполнить обратное преобразование (используя методы encode и decode).

s1 = 'разработка'
s2 = 'администрирование'
s3 = 'protocol'
s4 = 'standard'


# Преобразовать слова из строкового представления в байтовое
s1_b = s1.encode('utf-8')
print(s1_b) # b'\xd1\x80\xd0\xb0\xd0\xb7\xd1\x80\xd0\xb0\xd0\xb1\xd0\xbe\xd1\x82\xd0\xba\xd0\xb0'

s2_b = s2.encode('utf-8')
print(s2_b) # b'\xd0\xb0\xd0\xb4\xd0\xbc\xd0\xb8\xd0\xbd\xd0\xb8\xd1\x81\xd1\x82\xd1\x80\xd0\xb8\xd1\x80\xd0\xbe\xd0\xb2\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5'

s3_b = s3.encode('utf-8')
print(s3_b) # b'protocol'

s4_b = s4.encode('utf-8')
print(s4_b) # b'standard'


# выполнить обратное преобразование
s1_ = s1_b.decode('utf-8')
print(s1_) # разработка

s2_ = s2_b.decode('utf-8')
print(s2_) # администрирование

s3_ = s3_b.decode('utf-8')
print(s3_) # protocol

s4_ = s4_b.decode('utf-8')
print(s4_) # standard
