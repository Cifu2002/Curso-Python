import time

class Student:
    def take_nap(self, seconds):
        print("Estoy muy cansado jefe TwT.")
        time.sleep(seconds)
        print("¡Dormí bien! ¡Me siento genial!")

student = Student()
student.take_nap(5)

#funcion ctime
print("")
timestamp = 1572879180
print(time.ctime(timestamp))

#Funcion localtime y gmtime
print("")
timestamp = 1572879180
print(time.gmtime(timestamp))
print(time.localtime(timestamp))
#Funcion asctime() y mktime()
print("")
timestamp = 1572879180
st = time.gmtime(timestamp)

print(time.asctime(st))
print(time.mktime((2019, 11, 4, 14, 53, 0, 0, 308, 0)))

#Fecha y hora actual
print("")
from datetime import datetime

print("hoy:", datetime.today())
print("ahora:", datetime.now())
print("utc_ahora:", datetime.utcnow())

#Marca de tiempo
print("")
dt = datetime(2020, 10, 4, 14, 55)
print("Timestamp:", dt.timestamp())

#Dar formato a fecha y hora 
print("")
dt = datetime(2025, 10, 4, 14, 55)
print("Timestamp:", dt.timestamp())

dt = datetime(2020, 11, 4, 14, 53)
print(dt.strftime("%y/%B/%d %H:%M:%S"))

#Funcion strftime()
print("")
timestamp = 1572879180
st = time.gmtime(timestamp)

print(time.strftime("%Y/%m/%d %H:%M:%S", st))
print(time.strftime("%Y/%m/%d %H:%M:%S"))

#Metodo strptime()
from datetime import datetime
print("")
print(datetime.strptime("2019/11/04 14:53:00", "%Y/%m/%d %H:%M:%S"))