#ver fecha y hora
from datetime import date

hoy = date.today()

print("Hoy:", hoy)
print("Año:", hoy.year)
print("Mes:", hoy.month)
print("Día:", hoy.day)

#crear 
print("")
mi_fecha = date(2019, 11, 4)
print(mi_fecha)

#crear fecha desde una marca de tiempo
print("")
from datetime import date
import time

timestamp = time.time()
print("Marca de tiempo:", timestamp)

d = date.fromtimestamp(timestamp)
print("Fecha:", d)

#metodo replace
print("")
d = date(1991, 2, 5)
print(d)

d = d.replace(year=1992, month=1, day=16)
print(d)
    
#Identificar dia de la semana
print("")
d = date(2019, 11, 4)
print(d.weekday())

#crear objeto datetime
print("")
from datetime import time

t = time(14, 53, 20, 1)

print("Tiempo:", t)
print("Hora:", t.hour)
print("Minutos:", t.minute)
print("Segundos:", t.second)
print("Microsegundo:", t.microsecond)