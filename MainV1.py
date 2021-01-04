import csv
from matplotlib import pyplot as plt

with open('rainfall.csv', newline='') as f:
    reader0 = csv.reader(f)
    rainfall_ls = list(reader0)

with open('potableusage.csv', newline='') as g:
    reader1 = csv.reader(f)
    potusage_ls = list(reader1)

with open('stpusage.csv', newline='') as i:
    reader3 = csv.reader(f)
    treatusage_ls = list(reader3)

with open('stpinput.csv', newline='') as j:
    reader4 = csv.reader(f)
    treatinput_ls = list(reader4)

rainwater_harv = []
day_log = []
usablerain = []

hardscape = int(input("Hardscape area : "))
landscape = int(input("Landscape area : "))
roof = int(input("Roof area : "))
y = []

for k in range(len(rainfall_ls)):
    x = (0.01*(rainfall_ls[k])*(100*hardscape+10*landscape+90*roof))
    rainwater_harv.append(x)
    day_log.append(k+1)
    y.append(0.01*rainfall_ls[k]*90*landscape*10*roof)

treatneeded = []

for l in range(len(day_log)):
    if treatinput_ls[l] < treatusage_ls[l]:
        treatneeded.append(treatusage_ls[l]-treatinput_ls[l])
    else:
        treatneeded.append(0)

potneeded = []

for m in range(len(day_log)):
    if rainwater_harv[m] >= potusage_ls[m]:
        potneeded.append(0)
        usablerain.append(rainwater_harv[m]-potusage_ls[m])
    else:
        potneeded.append(potusage_ls[m]-rainwater_harv[m])
        usablerain.append(0)

landneeded = []

tank = []

for n in range(len(day_log)):
    if y[n] >= landscape:
        landneeded.append(0)
    elif (landscape-y[n]) <= usablerain[n]:
        tank.append(usablerain[n] - (landscape-y[n]))
        landneeded.append(0)
    else:
        tank.append(0)
        landneeded.append((landscape-y[n]) - usablerain[n])

plt.plot(treatneeded,day_log,'bo')
plt.plot(potneeded,day_log,'ro')
plt.plot(landneeded,day_log,'go')
plt.plot(tank,day_log,'yx')
plt.legend()
plt.show()
