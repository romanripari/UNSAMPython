# %%

from pprint import pprint
import datetime
fecha_hora = datetime.datetime.now()
print(fecha_hora)
fecha = datetime.date.today()
print(fecha)
pprint(dir(datetime))
pprint(dir(datetime.time.hour))
# %%
import datetime
d = datetime.date(2019, 4, 13)
print(d)

# %%
from datetime import date
d = date(2019, 4, 13)
print(d)
timestamp = date.fromtimestamp(1326244364)
print('Fecha =', timestamp)


# %%
from datetime import time
a = time()  
b = time(11, 34, 56)
c = time(hour = 11, minute = 34, second = 56)
d = time(11, 34, 56, 234566) 
print('a =', a)
print('b =', b)
print('c =', c)
print('d =', d)

# %%
# import datetime
from datetime import time

# a = datetime.time(datetime.datetime.now())
a = time(11, 34, 56)
print('hour =', a.hour)
print('minute =', a.minute)
print('second =', a.second)
print('microsecond =', a.microsecond)
# %%
from datetime import datetime
a = datetime(2020, 4, 21)
b = datetime(2021, 4, 21, 6, 53, 31, 342260)
print(a)
print(b)

# %%
from datetime import datetime

a = datetime(2021, 4, 21, 6, 53, 31, 342260)
#a = datetime.now()
print('año =', a.year)
print('mes =', a.month)
print('día =', a.day)
print('hora =', a.hour)
print('minuto =', a.minute)
print('timestamp =', a.timestamp())

# %%
from datetime import datetime, date
ahora = datetime.now()
t1 = date(year = 2021, month = 4, day = 21)
t1 = date(year = ahora.year, month = ahora.month, day = ahora.day)
t2 = date(year = 2021, month = 10, day = 1)
t3 = t1 - t2


t4 = datetime(year = 2020, month = 7, day = 12, hour = 7, minute = 9, second = 33)
t5 = datetime(year = 2021, month = 6, day = 10, hour = 5, minute = 55, second = 13)
t6 = t4 - t5
# -333 days, 1:14:20
print("resta entre date")
print(t3)
print('tipo de t3 =', type(t3))
# tipo de t3 = <class 'datetime.timedelta'>
print("resta entre datetime")
print(t6)
print('tipo de t6 =', type(t6))
# tipo de t6 = <class 'datetime.timedelta'>
from datetime import timedelta
t1 = timedelta(weeks = 1, days = 2, hours = 1, seconds = 33)
t2 = timedelta(days = 6, hours = 11, minutes = 4, seconds = 54)
t3 = t1 - t2
print("resta entre timedelta")
print('t3 =', t3)
print('tipo de t3 =', type(t3))



# %%
from datetime import timedelta

t1 = timedelta(seconds = 21)
t2 = timedelta(seconds = 55)
t3 = t1 - t2

print(t3)
print(abs(t3))

# %%
from datetime import timedelta

t = timedelta(days = 1, hours = 2, seconds = 30, microseconds = 100000)
print('segundos totales =', t.total_seconds())

# %%

from datetime import datetime
now = datetime.now()
t = now.strftime('%H:%M:%S')
print('hora:', t)
s1 = now.strftime('%m/%d/%Y, %H:%M:%S')
# en formato mm/dd/YY H:M:S
print('s1:', s1)
s2 = now.strftime('%d/%m/%Y, %H:%M:%S')
# en formato dd/mm/YY H:M:S
print('s2:', s2)

# %%
from datetime import datetime

cadena_con_fecha= '21 September, 2021'
print('date_string =', cadena_con_fecha)

date_object = datetime.strptime(cadena_con_fecha, '%d %B, %Y')
print('date_object =', date_object)
