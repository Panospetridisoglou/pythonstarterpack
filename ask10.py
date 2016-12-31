import datetime,calendar,urllib2,time
print "DATE-MONTH-YEAR"
date_text = raw_input()
date = int(time.mktime(time.strptime(date_text, "%d-%m-%Y")))
date2 = int(time.mktime(time.strptime("01-01-1970", "%d-%m-%Y")))
date=date-date2
print date
response=urllib2.urlopen("https://www.cryptocompare.com/api/data/pricehistorical?fsym=BTC&tsyms=USD,CNY,EUR,GBP&ts=%s"%date)
html=response.read()
html= html.split("{")

stuff=[]
for i in range (2,6):
    stuff.append(html[i].split("}")[0])
#sybmol :print stuff[i].split(":")[1].split('"')[1]
#price :print stuff[i].split('"')[6].split(":")[1].split(",")[0]
for i in range (0,4):
    for j in range (1,4):
        a =stuff[i].split('"')[6].split(":")[1].split(",")[0]
        b =stuff[j].split('"')[6].split(":")[1].split(",")[0]
        if (a>b):
            tmp=stuff[i]
            stuff[i]=stuff[j]
            stuff[j]=tmp
for i in range (0,4):
    print stuff[i].split('"')[6].split(":")[1].split(",")[0] + " " + stuff[i].split(":")[1].split('"')[1]
