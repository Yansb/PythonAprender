metros = int(input("digite uma distancia em metros: "))
k = metros/1000
h = metros/100
d = metros/10
dm = metros*10
cm = metros*100
mm = metros*1000

print("{} metros corresponde a:\n{}km\n{}hm\n{}dam\n{}dm\n{}cm\n{}mm".format(metros, k, h, d, dm, cm, mm))