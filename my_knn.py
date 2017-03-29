from numpy import *
import operator
from os import listdir
def knn(k,testdata,traindata,labels):
    traindatasize=traindata.shape[0]
    dif=tile(testdata,(traindatasize,1))-traindata
    sqdif=dif**2
    sumsqdif=sqdif.sum(axis=1)
    distance=sumsqdif**0.5
    sortdistance=distance.argsort()
    count={}
    for i in range(0,k):
        vote=labels[sortdistance[i]]
        count[vote]=count.get(vote,0)+1
    sortcount=sorted(count.items(),key=operator.itemgetter(1),reverse=True)
    return sortcount[0][0]
def datatoarray(fname):
    arr=[]
    fh=open(fname)
    for i in range(0,32):
        thisline=fh.readline()
        for j in range(0,32):
            arr.append(int(thisline[j]))
    return arr
def seplabel(fname):
    filestr=fname.split(".")[0]
    label=int(filestr.split("_")[0])
    return label
def traindata():
    labels=[]
    trainfile=listdir("/home/yiqishe/git/knn/traindata")
    num=len(trainfile)
    trainarr=zeros((num,1024))
    for i in range(0,num):
        thisname=trainfile[i]
        thislabel=seplabel(thisname)
        labels.append(thislabel)
        trainarr[i,:]=datatoarray("/home/yiqishe/git/knn/traindata/"+thisname)
    return trainarr,labels
def testdata():
    labels=[]
    testfile=listdir("/home/yiqishe/git/knn/testdata")
    num=len(testfile)
    testarr=zeros((num,1024))
    for i in range(0,num):
        thisname=testfile[i]
        thislabel=seplabel(thisname)
        labels.append(thislabel)
        testarr[i,:]=datatoarray("/home/yiqishe/git/knn/testdata/"+thisname)
    return testarr,labels
trainarr,labels1=traindata()
testarr,labels2=testdata()
ans=0
for i in range(len(testarr)):
    rst=knn(3,testarr[i],trainarr,labels1)
    if rst==labels2[i]:
        ans+=1
ans = ans/len(testarr)
print (ans)
