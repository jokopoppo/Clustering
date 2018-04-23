import random
import numpy as np
import operator

def readExel(exelname):
    import xlrd

    ExcelFileName= exelname
    workbook = xlrd.open_workbook(ExcelFileName)
    worksheet = workbook.sheet_by_name("Data")

    num_rows = worksheet.nrows  #Number of Rows
    num_cols = worksheet.ncols  #Number of Columns

    result_data =[]
    for curr_row in range(2,num_rows): # read except header
        row_data = []

        for curr_col in range(1, num_cols): # read except ID
            data = worksheet.cell_value(curr_row, curr_col) # Read the data in the current cell
            # print(data)
            row_data.append(data)

        result_data.append(row_data)
    print("read done")
    # print(result_data[0].__len__())
    return result_data
def mean(c):

    mc=[]
    for j in range(c[0].__len__()):
        tmp=0
        for i in range(c.__len__()):
            tmp+=c[i][j]

        mc.append(tmp/c.__len__())
    return mc
def error(c,m):
    c=np.array(c)
    m=np.array(m)

    err=[]
    for i in range(c.__len__()):
        err.append(c[i]-m)
        err[i]=(err[i]**2)

    return sum(sum(err))
def distance(dat,mean,ans):

    group=[]
    a=[]
    for i in range(k):
        group.append([])
        a.append([])
    for c in range(dat.__len__()):
        for j in range(dat[c].__len__()):
            d=[]
            for i in range(mean.__len__()) :
                d.append(np.array(dat[c][j])-np.array(mean[i]))
                d[i]=(sum(d[i]**2))**(1/2)
            index, value = min(enumerate(d), key=operator.itemgetter(1))
            group[index].append(dat[c][j])
            a[index].append(ans[c][j])
    return group,a

data = readExel('Data.xls')
random.shuffle(data)

ans=[]
for i in data:
    ans.append(int(i.pop(i.__len__()-1)))

datatest = data[0:int(data.__len__()*(10/100))]
data=data[int(data.__len__()*(10/100)):]

anstest= ans[0:int(ans.__len__()*(10/100))]
ans=ans[int(ans.__len__()*(10/100)):]

k=2
percent=int(data.__len__()*1/k)

dat = []
answer=[]
for i in range(k):
    dat.append(data[i*percent:percent*(i+1)])
    answer.append(ans[i*percent:percent*(i+1)])
n=0
while(True):
    n+=1
    meanC=[]
    errC=[]

    for i in range(k):
        print("Number of C",i,"=",dat[i].__len__())
        meanC.append(mean(dat[i]))
        errC.append(error(dat[i],meanC[i]))

    Err=sum(errC)
    print("ERROR =",Err)
    datc,answer=distance(dat,meanC,answer)
    if(datc == dat):
        break
    dat=datc

print(n)

c=0
for i in range(k):

    if(answer[i].__len__() > 20000):
        c+=answer[i].count(0)
    else:
        c+=answer[i].count(1)
print()
print(c,"%")



