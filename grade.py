# -*- coding: UTF-8 -*-

f =open('report.txt','r+')

eachline = []
num = 0
subjectnum=0
totalgrade_list = []
meannum_subject=[]
meannum_student=[]
name = []                 


for line in f.readlines()[1:]:
    eachline.append(line.split())


for i in range(len(eachline)):
    for index in eachline[i][1:]:
        num = num +int(index)
    totalgrade_list.append(num)
    meannum_student.append(num/9)
    num = 0
    name.append(eachline[i][0])

for j in range(9):
    for x in range(len(eachline)):
        subjectnum = subjectnum+int(eachline[x][j+1])
    meannum_subject.append(subjectnum/30)
    subjectnum =0

f.seek(0,0)
f.write('名次')

f.close()


totalgrade_dict = dict(zip(name,totalgrade_list))
totalgrade_dict=sorted(totalgrade_dict.items(), key=lambda x:x[1],reverse=True)






      

        
