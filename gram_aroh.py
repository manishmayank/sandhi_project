f1=open('1gram(aroh).txt','r')
f2=open('2gram(aroh).txt','r')
f3=open('3gram(aroh).txt','r')
f4=open('gram_aroh.txt','w')

count=1
for line in f1:
    f4.write(line[0:1])
    f4.write('\t')
    f4.write(str(count))
    f4.write('\n')
    count=count+1

for line in f2:
    f4.write(line[0:2])
    f4.write('\t')
    f4.write(str(count))
    f4.write('\n')
    count=count+1

for line in f3:
    f4.write(line[0:3])
    f4.write('\t')
    f4.write(str(count))
    f4.write('\n')
    count=count+1

f1.close()
f2.close()
f3.close()
f4.close()
