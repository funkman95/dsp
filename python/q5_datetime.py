from datetime import datetime

start = []
stop = []

date_start_a = '01-02-2013'
date_stop_a = '07-28-2015'
start.append(datetime.strptime(date_start_a, '%m-%d-%Y'))
stop.append(datetime.strptime(date_stop_a, '%m-%d-%Y'))

date_start_b = '12312013'
date_stop_b = '05282015'
start.append(datetime.fromtimestamp(int(date_start_b)))
stop.append(datetime.fromtimestamp(int(date_stop_b)))

date_start_c = '15-Jan-1994'
date_stop_c = '14-Jul-2015'
start.append(datetime.strptime(date_start_c, '%d-%b-%Y'))
stop.append(datetime.strptime(date_stop_c, '%d-%b-%Y'))

for i in range(3):
    print('Duration for part %s: %s days' % (chr(ord('a')+i), abs((start[i]-stop[i]).days)))
