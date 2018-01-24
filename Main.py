import csv
import numpy

# get category data (non numbers data)
def getCategoryArrayNonNumber(col):
    name1 = []
    for i in range(1, colSize):
        name1.append(list1[i][col])
    return name1

# get category data (numbers data)
def getCategoryArray(col):
    name2 = []
    for i in range(1, colSize):
        name2.append(float(list1[i][col]))
    return name2

with open('pitching2018preseason.csv') as csvfile:
    readCSV = csv.reader(csvfile)
    list1 = list(readCSV)

# Get column size
colSize = 0
for i in range(1, len(list1)):
    colSize += 1

name = getCategoryArrayNonNumber(0)
teamname = getCategoryArrayNonNumber(1)
wins = getCategoryArray(2)
losses = getCategoryArray(3)
era = getCategoryArray(4)
gs = getCategoryArray(5)
g = getCategoryArray(6)
sv = getCategoryArray(7)
ip = getCategoryArray(8)
h = getCategoryArray(9)
er = getCategoryArray(10)
hr = getCategoryArray(11)
so = getCategoryArray(12)
bb = getCategoryArray(13)
whip = getCategoryArray(14)
k9 = getCategoryArray(15)
bb9 = getCategoryArray(16)
fip = getCategoryArray(17)
war = getCategoryArray(18)
ra9war = getCategoryArray(19)
adp = getCategoryArray(20)
id = getCategoryArrayNonNumber(21)
ranking = []

# so / bb
sobb = []
for i in range(0, len(so)):
    if float(bb[i]) != float(0):
        sobb.append(numpy.divide(float(so[i]), float(bb[i])))
    else:
        sobb.append(0)

# win %
winpercentage = []
for i in range(0, len(so)):
    if float(losses[i]) != float(0):
        winpercentage.append(numpy.divide(float(wins[i]), float(losses[i])))
    else:
        winpercentage.append(0)


winsRanking = numpy.argsort(wins)
winsRanking = len(list1) - winsRanking.argsort() - 2

lossesRanking = numpy.argsort(losses)

eraRanking = numpy.argsort(era)
eraRanking = eraRanking.argsort() - 2

gsRanking = numpy.argsort(gs) #
gRanking = numpy.argsort(g) #
svRanking = numpy.argsort(sv) #

ipRanking = numpy.argsort(ip)
ipRanking = len(list1) - ipRanking.argsort() - 2

hRanking = numpy.argsort(h) #
erRanking = numpy.argsort(er) #
hrRanking = numpy.argsort(hr)

soRanking = numpy.argsort(so)
soRanking = len(list1) - soRanking.argsort() - 2

bbRanking = numpy.argsort(bb)
bbRanking = bbRanking.argsort() - 2

whipRanking = numpy.argsort(whip)
whipRanking = whipRanking.argsort() - 2

k9Ranking = numpy.argsort(k9)
k9Ranking = len(list1) - k9Ranking.argsort() - 2

bb9Ranking = numpy.argsort(bb9)
bb9Ranking = bb9Ranking.argsort() - 2

fipRanking = numpy.argsort(fip)
warRanking = numpy.argsort(war) #
ra9warRanking = numpy.argsort(ra9war) #
adpRanking = numpy.argsort(adp) #

sobbRanking = numpy.argsort(sobb)
sobbRanking = len(list1) - sobbRanking.argsort() - 2

winpercentageRanking = numpy.argsort(winpercentage)
winpercentageRanking = len(list1) - winpercentageRanking.argsort() - 2


for i in range(0,len(list1) - 2):
    ranking.append((ipRanking[i] + winsRanking[i] + bbRanking[i] + soRanking[i] + eraRanking[i] + whipRanking[i] + sobbRanking[i] + k9Ranking[i] + winpercentageRanking[i] + bb9Ranking[i]) / 10)

# write data
with open('pitching2018preseason2.csv','w') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=['name','team','w', 'l', 'era', 'gs', 'g','sv', 'ip', 'h', 'er', 'hr', 'so', 'bb', 'whip', 'k/9', 'bb/9', 'fip', 'war', 'ra9-war', 'adp', 'playerid', 'so/bb','winpercentage','ranking'])
    writer.writeheader()
    for i in range(0, len(list1) - 2):
        myData = [name[i], teamname[i], wins[i], losses[i], era[i], gs[i], g[i], sv[i], ip[i], h[i], er[i], hr[i], so[i], bb[i], whip[i], k9[i], bb9[i], fip[i], war[i], ra9war[i], adp[i], id[i], sobb[i], winpercentage[i], ranking[i]]
        writer.writerow({'name':name[i],
                     'team':teamname[i],
                     'w':wins[i],
                         'l': losses[i],
                         'era': era[i],
                         'gs': gs[i],
                         'g': g[i],
                         'sv': sv[i],
                         'ip': ip[i],
                         'h': h[i],
                         'er':er[i],
                         'hr':hr[i],
                         'so':so[i],
                         'bb':bb[i],
                         'whip':whip[i],
                         'k/9':k9[i],
                         'bb/9': bb9[i],
                         'fip': fip[i],
                         'war':war[i],
                         'ra9-war':ra9war[i],
                         'adp':adp[i],
                         'playerid':id[i],
                         'so/bb': sobb[i],
                         'winpercentage':winpercentage[i],
                         'ranking':ranking[i]})

#####################################################################################333
## BATTING ##

with open('batting2018preseason.csv') as csvfile:
    readCSV = csv.reader(csvfile)
    list1 = list(readCSV)

colSize = 0

for i in range(1, len(list1)):
    colSize += 1

name = getCategoryArrayNonNumber(0)
teamname = getCategoryArrayNonNumber(1)
g = getCategoryArray(2)
pa = getCategoryArray(3)
ab = getCategoryArray(4)
h = getCategoryArray(5)
b2 = getCategoryArray(6)
b3 = getCategoryArray(7)
hr = getCategoryArray(8)
r = getCategoryArray(9)
rbi = getCategoryArray(10)
bb = getCategoryArray(11)
so = getCategoryArray(12)
hbp = getCategoryArray(13)
sb = getCategoryArray(14)
cs = getCategoryArray(15)
eeh = getCategoryArrayNonNumber(16)
avg = getCategoryArray(17)
obp = getCategoryArray(18)
slg = getCategoryArray(19)
ops = getCategoryArray(20)
woba = getCategoryArray(21)
eeh2 = getCategoryArrayNonNumber(22)
wrc = getCategoryArray(23)
bsr = getCategoryArray(24)
fld = getCategoryArray(25)
eeh3 = getCategoryArrayNonNumber(26)
off = getCategoryArray(27)
def1 = getCategoryArray(28)
war = getCategoryArray(29)
eeh4 = getCategoryArrayNonNumber(30)
adp = getCategoryArray(31)
id = getCategoryArrayNonNumber(32)

tb = []
for i in range(0, len(so)):
    tb.append(float(h[i]) + 2 * float(b2[i]) + 3 * float(b3[i]) + 4 * float(hr[i]))


xbh = []
for i in range(0, len(so)):
    xbh.append(float(b2[i]) + float(b3[i]) + float(hr[i]))

ranking = []

gRanking = numpy.argsort(g)
gRanking = len(list1) - gRanking.argsort() - 2

paRanking = numpy.argsort(pa)
paRanking = len(list1) - paRanking.argsort() - 2

abRanking = numpy.argsort(ab)
abRanking = len(list1) - abRanking.argsort() - 2

hRanking = numpy.argsort(h)
hRanking = len(list1) - hRanking.argsort() - 2

b2Ranking = numpy.argsort(b2)
b2Ranking = len(list1) - b2Ranking.argsort() - 2

b3Ranking = numpy.argsort(b3)
b3Ranking = len(list1) - b3Ranking.argsort() - 2

hrRanking = numpy.argsort(hr)
hrRanking = len(list1) - hrRanking.argsort() - 2

rRanking = numpy.argsort(r)
rRanking = len(list1) - rRanking.argsort() - 2

rbiRanking = numpy.argsort(rbi)
rbiRanking = len(list1) - rbiRanking.argsort() - 2

bbRanking = numpy.argsort(bb)
bbRanking = len(list1) - bbRanking.argsort() - 2

soRanking = numpy.argsort(so)
soRanking = soRanking.argsort() - 2

sbRanking = numpy.argsort(sb)
sbRanking = len(list1) - sbRanking.argsort() - 2

tbRanking = numpy.argsort(tb)
tbRanking = len(list1) - tbRanking.argsort() - 2

avgRanking = numpy.argsort(avg)
avgRanking = len(list1) - avgRanking.argsort() - 2

obpRanking = numpy.argsort(obp)
obpRanking = len(list1) - obpRanking.argsort() - 2

slgRanking = numpy.argsort(slg)
slgRanking = len(list1) - slgRanking.argsort() - 2

xbhRanking = numpy.argsort(xbh)
xbhRanking = len(list1) - xbhRanking.argsort() - 2

for i in range(0,len(list1) - 2):
    ranking.append((rRanking[i] + hRanking[i] + b2Ranking[i] + hrRanking[i] + rbiRanking[i] + bbRanking[i] + tbRanking[i] + avgRanking[i] + obpRanking[i] + slgRanking[i] + xbhRanking[i] + paRanking[i]) / 12)

# write data
with open('batting2018preseason2.csv','w') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=['name','r','h','2b', 'hr', 'rbi', 'sb', 'bb','tb', 'avg', 'obp', 'slg', 'xbh', 'pa', 'ranking'])
    writer.writeheader()
    for i in range(0, len(list1) - 2):
        myData = [name[i], r[i], h[i], b2[i], hr[i], rbi[i], sb[i], bb[i], tb[i], fld[i], avg[i], obp[i], slg[i], xbh[i], pa[i], ranking[i]]
        writer.writerow({
                    'name':name[i],
                    'r':r[i],
                     'h':h[i],
                     '2b':b2[i],
                         'hr': hr[i],
                         'rbi': rbi[i],
                         'sb': sb[i],
                         'bb': bb[i],
                         'tb':tb[i],
                         'avg': avg[i],
                         'obp': obp[i],
                         'slg':slg[i],
                         'xbh':xbh[i],
                         'pa':pa[i],
            'ranking':ranking[i]
                         })

