f1 = open('aroh.txt','r')
f2 = open('4gram(aroh).txt','w')

a = set()
for line in f1:
    s = line
    for i in range(0,len(s)-4):
        t = s[i:(i+4)]
        a.add(t)
for n in a:
    print n
    f2.write(n)
    f2.write('\n')

