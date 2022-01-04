import csv
import statistics as st

with open("data.csv",newline="") as f:
    reader=csv.reader(f)
    filedata=list(reader)

filedata.pop(0)

newdata=[]
for i in range(len(filedata)):
    n_num=filedata[i][2]
    newdata.append(float(n_num))

total=0
n=len(newdata)

for i in newdata:
    total=total+i 

mean=total/n 
print(mean)

median=st.median(newdata)
print(median)

mode=st.mode(newdata)
print(mode)


