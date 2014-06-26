# code to create labels from time.txt file which are to be used in multi-label classification

f1 = open('label_time.txt','w')
f2 = open('time.txt','r')

for line in f2:
    if(line[0:1] == 'n'):
        f1.write('1')
    elif(line[0:1] == 'd'):
        f1.write('2')
    elif(line[0:1] == 'm'):
        f1.write('3')
    elif(line[0:1] == 's'):
        f1.write('4')
    elif(line[0:1] == 'e'):
        f1.write('5')
    elif(line[0:1] == 'a'):
        f1.write('6')
    else:
        f1.write('7')
    f1.write('\n')

    
    
