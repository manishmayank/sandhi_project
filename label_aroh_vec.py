f1=open('gram_aroh.txt','r')
f2=open('aroh_vec.txt','r')
f3=open('label_aroh.txt','w')
dic={}
str='raad  ---  gfh  ---  hdsa  ---  '
str1=str[0:len(str)-7].split('  ---  ')
print str1
for line in f1:
    l=line.split('\t')
    dic.update({l[0]:l[1][0:len(l[1])-1]})
#print dic
#print dic['DN']
count=0
for line in f2:
    if(count%5==0):
        count1=0    
        for l in line[0:len(line)-7].split('  ---  '):
            #print str(count)+' '+str(count1)
            count1=count1+1
            temp=l.split(':')
            print temp[0]
            print temp[1]
            f3.write(dic[temp[0]])
            f3.write(':')
            f3.write(temp[1])
            f3.write('  ---  ')           
    if(count%5==0):
        f3.write('\n\n\n')
    count=count+1

f1.close()
f2.close()
f3.close()
