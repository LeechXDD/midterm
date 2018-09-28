# -*- coding: utf8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf-8')


eachline = []
num = 0
subjectnum=0
totalgrade_list = []
meannum_subject=[]
meannum_student=[]
data =[]


f =open('report.txt','r')
for line in f.readlines():
    data.append(line)

f.close()


for each in data[1:]:
    eachline.append(each.split())

for i in range(len(eachline)):
    for index in eachline[i][1:]:
        
        num = num +int(index)

    totalgrade_list.append(num)
        
    meannum_student.append(num/9)
    num = 0
        

for j in range(9):
    for x in range(len(eachline)):
        subjectnum = subjectnum+int(eachline[x][j+1])

    meannum_subject.append(subjectnum/30)
    subjectnum =0





for totalgrade in range(len(totalgrade_list[0:])):
    
    eachline[totalgrade].insert(10,totalgrade_list[totalgrade])

for q in range(len(eachline)):
    for fail in eachline[q][1:]:
        if int(fail)<60:
            eachline[q][eachline[q].index(fail)]='不及格'

eachline = sorted(eachline,key=lambda x:x[-1],reverse=True)

eachline.insert(0,''.join(data[0]))


 
for rank in range(len(eachline[1:])):
    eachline[rank+1] = str(rank+1) +' '.join('%s'%e for e in eachline[rank+1])
    
eachline.insert(1,meannum_subject)
eachline[0]= "名次 "+''.join(eachline[0].strip())+' 总分'
eachline[1]= '0平均 '+' '.join('%s '%id for id in eachline[1])

w = open('newreport.txt','w')
w.writelines('\n'.join('%s'%m for m in eachline))
w.close()
