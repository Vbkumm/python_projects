import datetime
import time
per = ''
t1 = str(datetime.timedelta(seconds=time.time())).replace(':', '')
print(t1)
if t1.isnumeric():
    t1 = int(t1)
per = str(input('tempo de espera?'))
while per == '5':
    str(input('qual?'))
t2 = str(datetime.timedelta(seconds=666)).replace(':', '')
print(t2)
if t2.isnumeric():
    t2 = int(t2)
t3 = datetime.timedelta(microseconds=666)
tt = t2 - t1
print(f'{t2} - {t1} = {tt} {t3}')