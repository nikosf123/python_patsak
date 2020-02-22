from datetime import datetime, time

def date_diff_in_seconds(dt2, dt1):
  timedelta = abs(dt1-dt2)
  return timedelta.days * 24 * 3600 + timedelta.seconds

def dhms_from_seconds(seconds):
	minutes, seconds = divmod(seconds, 60)
	hours, minutes = divmod(minutes, 60)
	days, hours = divmod(hours, 24)
	return (days, hours, seconds)

#Eisagwgh hmeromhnias - 1os tropos   

#user_date = input('Εισαγετε ημερομηνία στη μορφή ΗΗ-MM-ΕΕΕΕ: ')
#day, month, year = map(int, user_date.split('-'))
#date1 = datetime(year, month, day)

#Eisagwgh hmeromhnias - 2os tropos

hmera = int(input('dwse hmera '))
while hmera>31 or hmera<1:
  print("edwses lathos arithmo meras janadwse")
  hmera = int(input('dwse hmera '))
mhnas = int(input('dwse mhna '))
while mhnas>12 or mhnas<1:
  print("edwses lathos mhna janadwse ")
  mhnas = int(input('dwse mhna '))
if mhnas == 2:
  while hmera>29:
    print("den ginetai se ayton ton mhna na dwseis panw apo 29 meres janadwse")
    hmera = int(input('dwse hmera '))
if mhnas==4 or mhnas==6 or mhnas==9 or mhnas==11:
  while hmera>30:
    print("o mhnas poy edwses den ginetai na exei panw apo 30 meres")
    hmera = int(input('dwse hmera '))
    
xronia = int(input('dwse xronia '))

while xronia<1 or xronia>9999:
  print ("lathos xronologia janadwse ")
  xronia = int(input('dwse xronia '))
  a=str(xronia)
  n=len(a)
if mhnas == 2 and(xronia % 4) !=0:
  while hmera>28:
    print("den ginetai na dwseis arithmo meras panw apo 28 se ayton ton mhna dioti ton etos poy exeis dwsei den einai disekto")
    hmera = int(input('dwse hmera '))


elif xronia % 100 !=0:
  print("")

elif xronia % 400 !=0:
  print("")

else:
  while hmera>28:
    print("den ginetai na dwseis arithmo meras 29 se ayton ton mhna dioti ton etos poy exeis dwsei den einai disekto")
    hmera = int(input('dwse hmera '))


date1 = datetime(xronia, mhnas, hmera)


#Current date
date2 = datetime.now()


print("\n%d days, %d hours, %d seconds" % dhms_from_seconds(date_diff_in_seconds(date2, date1)))
import calendar
print ("oi meres aytoy toy mhna einai",calendar.monthrange(xronia,mhnas)[1])
