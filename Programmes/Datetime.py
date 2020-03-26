import datetime

t = datetime.time(5,25,1)

print ('Time was set at:', t)
print (t.hour,'heure(s)')
print (t.minute,'minute(s)')
print (t.second,'seconde(s)')

print ('Quel est le temps mini possible? :', datetime.time.min)
print ('Quel est le temps maxi possible? :', datetime.time.max)
print ('Quel est la resolution possible? :', datetime.time.resolution)

print ('la date d\'aujourd\'hui est : ', datetime.date.today(),'\n')
today = datetime.date.today()
print ('les attributs du module datetime sont :', today.timetuple())

print('on peut egalement voir le nombre de année, jous, minutes, etc... entre deux dates')
d1 = datetime.date(2020, 10, 13)
d2 = d1.replace(year=2019, month=4) #on reprends la date D1 et on change juste année et mois

print(d1-d2)