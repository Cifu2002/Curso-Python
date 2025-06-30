import calendar
print(calendar.calendar(2025))

calendar.prcal(2020)

#Calendario mes especifico
print("")
print(calendar.month(2025, 6))

#funcion setfirstweekday()
print("")
calendar.setfirstweekday(calendar.SUNDAY)
calendar.prmonth(2025, 6)

#Funcion weekday() devuelve el dia de la semana
print("")
print(calendar.weekday(2025, 6, 22))

#Funcion weekheader()
print("")
print(calendar.weekheader(2))

#Año bisiesto
print("")
print(calendar.isleap(2020))
print(calendar.leapdays(2010, 2025))

#Crear un objeto calendario
print("")
c = calendar.Calendar(calendar.SUNDAY)

for weekday in c.iterweekdays():
    print(weekday, end=" ")

#Metodo itermonthdates()
print("")
c = calendar.Calendar()

for date in c.itermonthdates(2025, 11):
    print(date, end=" ")

#Metodo monthdays2calendar()
print("")
c = calendar.Calendar()

for data in c.monthdays2calendar(2025, 12):
    print(data)
    