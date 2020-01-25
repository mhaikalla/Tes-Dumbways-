burung = 6969
hari = 441
persen = 11.1
for i in range(1, hari+1):
    if i % 21 == 0:
        print("\n\nHari ke",i)
        jumlahmati =round(burung * (persen / 100))
        burung = round(burung-jumlahmati)
        print("Total Burung yang mati ("+ str(persen) +"%): "+ str(jumlahmati))
        print("Total Burung yang tersisa : "+ str(burung))
        burung *=2
        print("="*10)

print("Total Burung setelah "+str(hari) + " hari : " +str(round(burung))+" ekor")
