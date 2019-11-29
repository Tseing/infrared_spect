import csv

from matplotlib import pyplot as plt

#Read IR csv
print("Please enter a filename of IR data CSV :")
filename = input()
with open(filename+'.CSV') as f:
    reader = csv.reader(f)

    wavenums = []
    trans = []
    for row in reader:
        wavenum = float(row[0])
        tran = float(row[1])
        wavenums.append(wavenum)
        trans.append(tran)

    wavenums=wavenums[1:len(wavenums)-1]
    trans=trans[1:len(trans)-1]

#Options of figure
fig = plt.figure(dpi=256, figsize=(10,7))
plt.plot(wavenums, trans, linewidth=1, c='red')
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)
plt.xlabel(r'Wavenumber / $cm^{-1}$', fontsize=12)
plt.ylabel(r'Transmittance / %', fontsize=12)
plt.xlim(400, 4000)
plt.ylim(0, 100)
ax=plt.gca()
ax.invert_xaxis()

plt.savefig(filename+".pdf", dpi =600, format="pdf")
