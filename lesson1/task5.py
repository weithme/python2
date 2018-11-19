# 5. Выполнить пинг веб-ресурсов yandex.ru, youtube.com и преобразовать результаты из байтовового в строковый тип на кириллице.

import subprocess
args = ['ping', '-c', '4', 'www.yandex.ru']
args2 = ['ping', '-c', '4','www.youtube.com']

# www.yandex.ru
subproc_ping = subprocess.Popen(args, stdout=subprocess.PIPE)
for line in subproc_ping.stdout: print(line.decode('utf-8')) # для Linux
#for line in subproc_ping.stdout: print(line.decode('cp866').encode('utf-8').decode('utf-8')) # для Windows

# www.youtube.com
subproc_ping = subprocess.Popen(args2, stdout=subprocess.PIPE)
for line in subproc_ping.stdout: print(line.decode('utf-8')) # для Linux
#for line in subproc_ping.stdout: print(line.decode('cp866').encode('utf-8').decode('utf-8')) # для Windows
