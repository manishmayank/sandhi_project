list = []
f1 = open('avroh.txt','r')
f3 = open('avroh_vec.txt','w')

for line in f1:
    s = line[0:len(line)-1]
    dict = {}
    f2 = open('1gram(avroh).txt','r')
    for line1 in f2:
        t = line1[0:len(line1)-1]
        if(s.find(t) == -1):
            dict.update({t : 0})
        else:
            dict.update({t : 1})
    f2.close()
    
    f2 = open('2gram(avroh).txt','r')
    for line1 in f2:
        t = line1[0:len(line1)-1]
        if(s.find(t) == -1):
            dict.update({t : 0})
        else:
            dict.update({t : 1})
    f2.close()

    f2 = open('3gram(avroh).txt','r')
    for line1 in f2:
        t = line1[0:len(line1)-1]
        if(s.find(t) == -1):
            dict.update({t : 0})
        else:
            dict.update({t : 1})
    f2.close()

    f2 = open('4gram(avroh).txt','r')
    for line1 in f2:
        t = line1[0:len(line1)-1]
        if(s.find(t) == -1):
            dict.update({t : 0})
        else:
            dict.update({t : 1})
    f2.close()
    list.append(dict)
f1.close()

print list[0]

for i in range(0,len(list)):
    for (key , value) in list[i].iteritems():
        print value
        f3.write(key)
        f3.write(':')
        f3.write(str(value))
        f3.write('  ---  ')
    f3.write('\n\n\n\n\n')
f3.close()
