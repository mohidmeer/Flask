import os
import numpy as np
from string import ascii_uppercase
from PIL import Image,ImageDraw,ImageFont
from tabulate import tabulate
def GenReport(SeqA,SeqB):
    SeqFileName=os.path.basename(SeqA)
    split=os.path.splitext(SeqFileName)
    ReportFileName=split[0]+".png"
    ReportFilePath=os.path.join('C:\\Users\\mohid\\Desktop\\FLASK\\dev\\static\\DnaReports',ReportFileName)
    with open(SeqA,'r') as A ,open(SeqB,'r') as B:
        SeqAObj=A.read(300)
        SeqBObj=B.read(300)
    if len(SeqAObj)>len(SeqBObj):
        LenT=len(SeqAObj)-len(SeqBObj)
        print("A SEQUENCE  "+str(LenT)+" Times Bigger 😒😒😒😒")
        for i in range(LenT):
            SeqBObj+="-"
    elif len(SeqBObj)>len(SeqAObj):
        LenT=len(SeqBObj)-len(SeqAObj)
        print("B SEQUENCE  "+str(LenT)+" Times Bigger😒😒😒😒")
        for i in range(LenT):
            SeqAObj+="-"            
    SeqA_Counts={}
    SeqB_Counts={}
    for st in ascii_uppercase:
        SeqA_Counts[st]=SeqAObj.count(st)
        SeqB_Counts[st]=SeqBObj.count(st)
    DataList=[['Sequence A'],
            ['Sequence B']]
    HeaderList=["NAME"]
    for key,Value in SeqA_Counts.items():
        DataList[0].append(Value)
        DataList[1].append(SeqB_Counts[key])
        HeaderList.append(key)
    SeqAArrangments=[]
    SeqBArrangments=[]
    for x in  SeqAObj:
        SeqAArrangments.append(x)
    for y in SeqBObj:
        SeqBArrangments.append(y)
    list1 = np.array(SeqAArrangments)
    list2 = np.array(SeqBArrangments)
    SeqDiffInd = np.where(list1==list2)[0]
    SeqDiffList={}
    for i in SeqDiffInd:
        SeqDiffList[i]=SeqAArrangments[i]
    image=Image.open('C:\\Users\\mohid\\Desktop\\FLASK\\dev\\static\\Base\\image.png')
    d=ImageDraw.Draw(image)
    fnt=ImageFont.truetype('consola.ttf', 30)
    fntt=ImageFont.truetype('consola.ttf', 28)
    ColorRect=(127,255,212)
    FontColor=(0,0,0)
    HighligtFontColor=(0,0,255)
    MisMatchFontColor=(255,0,0)
    MisMatchBoxColor=(124,252,0)
    d.text((50,100),tabulate(DataList, HeaderList),font=fntt,fill=FontColor)
    d.text((20,500),"SEQUEN-A->",font=fnt,fill=FontColor)
    d.text((20,600),"SEQUEN-B->",font=fnt,fill=FontColor)
    YAxisFirstLine=500
    XAxisFirstLine=230
    YAxisSecondLine=530
    XAxisSecondLine=230
    YAxisThirdLine=560
    XAxisThirdLine=230
    for index,x in enumerate(SeqAObj):
        if index>200:
            d.rectangle((XAxisThirdLine,YAxisThirdLine,XAxisThirdLine+15,YAxisThirdLine+25),fill=MisMatchBoxColor)
            d.text((XAxisThirdLine,YAxisThirdLine),x,font=fnt,fill=MisMatchFontColor)
            if index in SeqDiffInd:
                d.rectangle((XAxisThirdLine,YAxisThirdLine,XAxisThirdLine+20,YAxisThirdLine+30),fill=ColorRect)
                d.text((XAxisThirdLine,YAxisThirdLine),x,font=fnt,fill=HighligtFontColor)
            XAxisThirdLine+=20
        elif index>100:
            d.rectangle((XAxisSecondLine,YAxisSecondLine,XAxisSecondLine+15,YAxisSecondLine+25),fill=MisMatchBoxColor)
            d.text((XAxisSecondLine,YAxisSecondLine),x,font=fnt,fill=MisMatchFontColor)
            if index in SeqDiffInd:
                d.rectangle((XAxisSecondLine,YAxisSecondLine,XAxisSecondLine+20,YAxisSecondLine+30),fill=ColorRect)
                d.text((XAxisSecondLine,YAxisSecondLine),x,font=fnt,fill=HighligtFontColor)
            XAxisSecondLine+=20
        else:
            d.rectangle((XAxisFirstLine,YAxisFirstLine,XAxisFirstLine+15,YAxisFirstLine+25),fill=MisMatchBoxColor)
            d.text((XAxisFirstLine,YAxisFirstLine),x,font=fnt,fill=MisMatchFontColor)
            if index in SeqDiffInd:
                d.rectangle((XAxisFirstLine,YAxisFirstLine,XAxisFirstLine+20,YAxisFirstLine+30),fill=ColorRect)
                d.text((XAxisFirstLine,YAxisFirstLine),x,font=fnt,fill=HighligtFontColor)
            XAxisFirstLine+=20      
    YAxisFirstLine=600
    XAxisFirstLine=230
    YAxisSecondLine=630
    XAxisSecondLine=230
    YAxisThirdLine=660
    XAxisThirdLine=230
    for index,x in enumerate(SeqBObj):
        if index>200:
            d.rectangle((XAxisThirdLine,YAxisThirdLine,XAxisThirdLine+15,YAxisThirdLine+25),fill=MisMatchBoxColor)
            d.text((XAxisThirdLine,YAxisThirdLine),x,font=fnt,fill=MisMatchFontColor)
            if index in SeqDiffInd:
                d.rectangle((XAxisThirdLine,YAxisThirdLine,XAxisThirdLine+20,YAxisThirdLine+30),fill=ColorRect)
                d.text((XAxisThirdLine,YAxisThirdLine),x,font=fnt,fill=HighligtFontColor)
            XAxisThirdLine+=20
        elif index>100:
            d.rectangle((XAxisSecondLine,YAxisSecondLine,XAxisSecondLine+15,YAxisSecondLine+25),fill=MisMatchBoxColor)
            d.text((XAxisSecondLine,YAxisSecondLine),x,font=fnt,fill=MisMatchFontColor)
            if index in SeqDiffInd:
                d.rectangle((XAxisSecondLine,YAxisSecondLine,XAxisSecondLine+20,YAxisSecondLine+30),fill=ColorRect)
                d.text((XAxisSecondLine,YAxisSecondLine),x,font=fnt,fill=HighligtFontColor)
            XAxisSecondLine+=20
        else:
            d.rectangle((XAxisFirstLine,YAxisFirstLine,XAxisFirstLine+15,YAxisFirstLine+25),fill=MisMatchBoxColor)
            d.text((XAxisFirstLine,YAxisFirstLine),x,font=fnt,fill=MisMatchFontColor)
            if index in SeqDiffInd:
                d.rectangle((XAxisFirstLine,YAxisFirstLine,XAxisFirstLine+20,YAxisFirstLine+30),fill=ColorRect)
                d.text((XAxisFirstLine,YAxisFirstLine),x,font=fnt,fill=HighligtFontColor)
            XAxisFirstLine+=20
    image.save(ReportFilePath)
    return ReportFilePath
    SeqFileName=os.path.basename(SeqA)
    split=os.path.splitext(SeqFileName)
    ReportFileName=split[0]+".png"
    ReportFilePath=os.path.join('C:\\Users\\mohid\\Desktop\\FLASK\\dev\\static\\DnaReports',ReportFileName)
    with open(SeqA,'r') as A ,open(SeqB,'r') as B:
        SeqAObj=A.read(300)
        SeqBObj=B.read(300)
    if len(SeqAObj)>len(SeqBObj):
        LenT=len(SeqAObj)-len(SeqBObj)
        print("A SEQUENCE  "+str(LenT)+" Times Bigger 😒😒😒😒")
        for i in range(LenT):
            SeqBObj+="-"
    elif len(SeqBObj)>len(SeqAObj):
        LenT=len(SeqBObj)-len(SeqAObj)
        print("B SEQUENCE  "+str(LenT)+" Times Bigger😒😒😒😒")
        for i in range(LenT):
            SeqAObj+="-"            
    SeqA_Counts={}
    SeqB_Counts={}
    for st in ascii_uppercase:
        SeqA_Counts[st]=SeqAObj.count(st)
        SeqB_Counts[st]=SeqBObj.count(st)
    DataList=[['Sequence A'],
            ['Sequence B']]
    HeaderList=["NAME"]
    for key,Value in SeqA_Counts.items():
        DataList[0].append(Value)
        DataList[1].append(SeqB_Counts[key])
        HeaderList.append(key)
    SeqAArrangments=[]
    SeqBArrangments=[]
    for x in  SeqAObj:
        SeqAArrangments.append(x)
    for y in SeqBObj:
        SeqBArrangments.append(y)
    list1 = np.array(SeqAArrangments)
    list2 = np.array(SeqBArrangments)
    SeqDiffInd = np.where(list1==list2)[0]
    SeqDiffList={}
    for i in SeqDiffInd:
        SeqDiffList[i]=SeqAArrangments[i]
    image=Image.open('C:\\Users\\mohid\\Desktop\\FLASK\\dev\\static\\Base\\image.png')
    d=ImageDraw.Draw(image)
    fnt=ImageFont.truetype('consola.ttf', 30)
    fntt=ImageFont.truetype('consola.ttf', 28)
    ColorRect=(127,255,212)
    FontColor=(0,0,0)
    HighligtFontColor=(0,0,255)
    MisMatchFontColor=(255,0,0)
    MisMatchBoxColor=(124,252,0)
    d.text((50,100),tabulate(DataList, HeaderList),font=fntt,fill=FontColor)
    d.text((20,500),"SEQUEN-A->",font=fnt,fill=FontColor)
    d.text((20,600),"SEQUEN-B->",font=fnt,fill=FontColor)
    YAxisFirstLine=500
    XAxisFirstLine=230
    YAxisSecondLine=530
    XAxisSecondLine=230
    YAxisThirdLine=560
    XAxisThirdLine=230
    for index,x in enumerate(SeqAObj):
        if index>200:
            d.rectangle((XAxisThirdLine,YAxisThirdLine,XAxisThirdLine+15,YAxisThirdLine+25),fill=MisMatchBoxColor)
            d.text((XAxisThirdLine,YAxisThirdLine),x,font=fnt,fill=MisMatchFontColor)
            if index in SeqDiffInd:
                d.rectangle((XAxisThirdLine,YAxisThirdLine,XAxisThirdLine+20,YAxisThirdLine+30),fill=ColorRect)
                d.text((XAxisThirdLine,YAxisThirdLine),x,font=fnt,fill=HighligtFontColor)
            XAxisThirdLine+=20
        elif index>100:
            d.rectangle((XAxisSecondLine,YAxisSecondLine,XAxisSecondLine+15,YAxisSecondLine+25),fill=MisMatchBoxColor)
            d.text((XAxisSecondLine,YAxisSecondLine),x,font=fnt,fill=MisMatchFontColor)
            if index in SeqDiffInd:
                d.rectangle((XAxisSecondLine,YAxisSecondLine,XAxisSecondLine+20,YAxisSecondLine+30),fill=ColorRect)
                d.text((XAxisSecondLine,YAxisSecondLine),x,font=fnt,fill=HighligtFontColor)
            XAxisSecondLine+=20
        else:
            d.rectangle((XAxisFirstLine,YAxisFirstLine,XAxisFirstLine+15,YAxisFirstLine+25),fill=MisMatchBoxColor)
            d.text((XAxisFirstLine,YAxisFirstLine),x,font=fnt,fill=MisMatchFontColor)
            if index in SeqDiffInd:
                d.rectangle((XAxisFirstLine,YAxisFirstLine,XAxisFirstLine+20,YAxisFirstLine+30),fill=ColorRect)
                d.text((XAxisFirstLine,YAxisFirstLine),x,font=fnt,fill=HighligtFontColor)
            XAxisFirstLine+=20      
    YAxisFirstLine=600
    XAxisFirstLine=230
    YAxisSecondLine=630
    XAxisSecondLine=230
    YAxisThirdLine=660
    XAxisThirdLine=230
    for index,x in enumerate(SeqBObj):
        if index>200:
            d.rectangle((XAxisThirdLine,YAxisThirdLine,XAxisThirdLine+15,YAxisThirdLine+25),fill=MisMatchBoxColor)
            d.text((XAxisThirdLine,YAxisThirdLine),x,font=fnt,fill=MisMatchFontColor)
            if index in SeqDiffInd:
                d.rectangle((XAxisThirdLine,YAxisThirdLine,XAxisThirdLine+20,YAxisThirdLine+30),fill=ColorRect)
                d.text((XAxisThirdLine,YAxisThirdLine),x,font=fnt,fill=HighligtFontColor)
            XAxisThirdLine+=20
        elif index>100:
            d.rectangle((XAxisSecondLine,YAxisSecondLine,XAxisSecondLine+15,YAxisSecondLine+25),fill=MisMatchBoxColor)
            d.text((XAxisSecondLine,YAxisSecondLine),x,font=fnt,fill=MisMatchFontColor)
            if index in SeqDiffInd:
                d.rectangle((XAxisSecondLine,YAxisSecondLine,XAxisSecondLine+20,YAxisSecondLine+30),fill=ColorRect)
                d.text((XAxisSecondLine,YAxisSecondLine),x,font=fnt,fill=HighligtFontColor)
            XAxisSecondLine+=20
        else:
            d.rectangle((XAxisFirstLine,YAxisFirstLine,XAxisFirstLine+15,YAxisFirstLine+25),fill=MisMatchBoxColor)
            d.text((XAxisFirstLine,YAxisFirstLine),x,font=fnt,fill=MisMatchFontColor)
            if index in SeqDiffInd:
                d.rectangle((XAxisFirstLine,YAxisFirstLine,XAxisFirstLine+20,YAxisFirstLine+30),fill=ColorRect)
                d.text((XAxisFirstLine,YAxisFirstLine),x,font=fnt,fill=HighligtFontColor)
            XAxisFirstLine+=20
    image.save(ReportFilePath)
    return ReportFilePath
    SeqFileName=os.path.basename(SeqA)
    split=os.path.splitext(SeqFileName)
    ReportFileName=split[0]+".png"
    ReportFilePath=os.path.join('C:\\Users\\mohid\\Desktop\\FLASK\\dev\\static\\DnaReports',ReportFileName)
    with open(SeqA,'r') as A ,open(SeqB,'r') as B:
        SeqAObj=A.read(300)
        SeqBObj=B.read(300)
    if len(SeqAObj)>len(SeqBObj):
        LenT=len(SeqAObj)-len(SeqBObj)
        print("A SEQUENCE  "+str(LenT)+" Times Bigger 😒😒😒😒")
        for i in range(LenT):
            SeqBObj+="-"
    elif len(SeqBObj)>len(SeqAObj):
        LenT=len(SeqBObj)-len(SeqAObj)
        print("B SEQUENCE  "+str(LenT)+" Times Bigger😒😒😒😒")
        for i in range(LenT):
            SeqAObj+="-"            
    SeqA_Counts={}
    SeqB_Counts={}
    for st in ascii_uppercase:
        SeqA_Counts[st]=SeqAObj.count(st)
        SeqB_Counts[st]=SeqBObj.count(st)
    DataList=[['Sequence A'],
            ['Sequence B']]
    HeaderList=["NAME"]
    for key,Value in SeqA_Counts.items():
        DataList[0].append(Value)
        DataList[1].append(SeqB_Counts[key])
        HeaderList.append(key)
    SeqAArrangments=[]
    SeqBArrangments=[]
    for x in  SeqAObj:
        SeqAArrangments.append(x)
    for y in SeqBObj:
        SeqBArrangments.append(y)
    list1 = np.array(SeqAArrangments)
    list2 = np.array(SeqBArrangments)
    SeqDiffInd = np.where(list1==list2)[0]
    SeqDiffList={}
    for i in SeqDiffInd:
        SeqDiffList[i]=SeqAArrangments[i]
    image=Image.open('C:\\Users\\mohid\\Desktop\\FLASK\\dev\\static\\Base\\image.png')
    d=ImageDraw.Draw(image)
    fnt=ImageFont.truetype('consola.ttf', 30)
    fntt=ImageFont.truetype('consola.ttf', 28)
    ColorRect=(127,255,212)
    FontColor=(0,0,0)
    HighligtFontColor=(0,0,255)
    MisMatchFontColor=(255,0,0)
    MisMatchBoxColor=(124,252,0)
    d.text((50,100),tabulate(DataList, HeaderList),font=fntt,fill=FontColor)
    d.text((20,500),"SEQUEN-A->",font=fnt,fill=FontColor)
    d.text((20,600),"SEQUEN-B->",font=fnt,fill=FontColor)
    YAxisFirstLine=500
    XAxisFirstLine=230
    YAxisSecondLine=530
    XAxisSecondLine=230
    YAxisThirdLine=560
    XAxisThirdLine=230
    for index,x in enumerate(SeqAObj):
        if index>200:
            d.rectangle((XAxisThirdLine,YAxisThirdLine,XAxisThirdLine+15,YAxisThirdLine+25),fill=MisMatchBoxColor)
            d.text((XAxisThirdLine,YAxisThirdLine),x,font=fnt,fill=MisMatchFontColor)
            if index in SeqDiffInd:
                d.rectangle((XAxisThirdLine,YAxisThirdLine,XAxisThirdLine+20,YAxisThirdLine+30),fill=ColorRect)
                d.text((XAxisThirdLine,YAxisThirdLine),x,font=fnt,fill=HighligtFontColor)
            XAxisThirdLine+=20
        elif index>100:
            d.rectangle((XAxisSecondLine,YAxisSecondLine,XAxisSecondLine+15,YAxisSecondLine+25),fill=MisMatchBoxColor)
            d.text((XAxisSecondLine,YAxisSecondLine),x,font=fnt,fill=MisMatchFontColor)
            if index in SeqDiffInd:
                d.rectangle((XAxisSecondLine,YAxisSecondLine,XAxisSecondLine+20,YAxisSecondLine+30),fill=ColorRect)
                d.text((XAxisSecondLine,YAxisSecondLine),x,font=fnt,fill=HighligtFontColor)
            XAxisSecondLine+=20
        else:
            d.rectangle((XAxisFirstLine,YAxisFirstLine,XAxisFirstLine+15,YAxisFirstLine+25),fill=MisMatchBoxColor)
            d.text((XAxisFirstLine,YAxisFirstLine),x,font=fnt,fill=MisMatchFontColor)
            if index in SeqDiffInd:
                d.rectangle((XAxisFirstLine,YAxisFirstLine,XAxisFirstLine+20,YAxisFirstLine+30),fill=ColorRect)
                d.text((XAxisFirstLine,YAxisFirstLine),x,font=fnt,fill=HighligtFontColor)
            XAxisFirstLine+=20      
    YAxisFirstLine=600
    XAxisFirstLine=230
    YAxisSecondLine=630
    XAxisSecondLine=230
    YAxisThirdLine=660
    XAxisThirdLine=230
    for index,x in enumerate(SeqBObj):
        if index>200:
            d.rectangle((XAxisThirdLine,YAxisThirdLine,XAxisThirdLine+15,YAxisThirdLine+25),fill=MisMatchBoxColor)
            d.text((XAxisThirdLine,YAxisThirdLine),x,font=fnt,fill=MisMatchFontColor)
            if index in SeqDiffInd:
                d.rectangle((XAxisThirdLine,YAxisThirdLine,XAxisThirdLine+20,YAxisThirdLine+30),fill=ColorRect)
                d.text((XAxisThirdLine,YAxisThirdLine),x,font=fnt,fill=HighligtFontColor)
            XAxisThirdLine+=20
        elif index>100:
            d.rectangle((XAxisSecondLine,YAxisSecondLine,XAxisSecondLine+15,YAxisSecondLine+25),fill=MisMatchBoxColor)
            d.text((XAxisSecondLine,YAxisSecondLine),x,font=fnt,fill=MisMatchFontColor)
            if index in SeqDiffInd:
                d.rectangle((XAxisSecondLine,YAxisSecondLine,XAxisSecondLine+20,YAxisSecondLine+30),fill=ColorRect)
                d.text((XAxisSecondLine,YAxisSecondLine),x,font=fnt,fill=HighligtFontColor)
            XAxisSecondLine+=20
        else:
            d.rectangle((XAxisFirstLine,YAxisFirstLine,XAxisFirstLine+15,YAxisFirstLine+25),fill=MisMatchBoxColor)
            d.text((XAxisFirstLine,YAxisFirstLine),x,font=fnt,fill=MisMatchFontColor)
            if index in SeqDiffInd:
                d.rectangle((XAxisFirstLine,YAxisFirstLine,XAxisFirstLine+20,YAxisFirstLine+30),fill=ColorRect)
                d.text((XAxisFirstLine,YAxisFirstLine),x,font=fnt,fill=HighligtFontColor)
            XAxisFirstLine+=20
    image.save(ReportFilePath)
    return ReportFilePath
    SeqFileName=os.path.basename(SeqA)
    split=os.path.splitext(SeqFileName)
    ReportFileName=split[0]+".png"
    ReportFilePath=os.path.join('C:\\Users\\mohid\\Desktop\\FLASK\\dev\\static\\DnaReports',ReportFileName)
    with open(SeqA,'r') as A ,open(SeqB,'r') as B:
        SeqAObj=A.read(300)
        SeqBObj=B.read(300)
    if len(SeqAObj)>len(SeqBObj):
        LenT=len(SeqAObj)-len(SeqBObj)
        print("A SEQUENCE  "+str(LenT)+" Times Bigger 😒😒😒😒")
        for i in range(LenT):
            SeqBObj+="-"
    elif len(SeqBObj)>len(SeqAObj):
        LenT=len(SeqBObj)-len(SeqAObj)
        print("B SEQUENCE  "+str(LenT)+" Times Bigger😒😒😒😒")
        for i in range(LenT):
            SeqAObj+="-"            
    SeqA_Counts={}
    SeqB_Counts={}
    for st in ascii_uppercase:
        SeqA_Counts[st]=SeqAObj.count(st)
        SeqB_Counts[st]=SeqBObj.count(st)
    DataList=[['Sequence A'],
            ['Sequence B']]
    HeaderList=["NAME"]
    for key,Value in SeqA_Counts.items():
        DataList[0].append(Value)
        DataList[1].append(SeqB_Counts[key])
        HeaderList.append(key)
    SeqAArrangments=[]
    SeqBArrangments=[]
    for x in  SeqAObj:
        SeqAArrangments.append(x)
    for y in SeqBObj:
        SeqBArrangments.append(y)
    list1 = np.array(SeqAArrangments)
    list2 = np.array(SeqBArrangments)
    SeqDiffInd = np.where(list1==list2)[0]
    SeqDiffList={}
    for i in SeqDiffInd:
        SeqDiffList[i]=SeqAArrangments[i]
    image=Image.open('C:\\Users\\mohid\\Desktop\\FLASK\\dev\\static\\Base\\image.png')
    d=ImageDraw.Draw(image)
    fnt=ImageFont.truetype('consola.ttf', 30)
    fntt=ImageFont.truetype('consola.ttf', 28)
    ColorRect=(127,255,212)
    FontColor=(0,0,0)
    HighligtFontColor=(0,0,255)
    MisMatchFontColor=(255,0,0)
    MisMatchBoxColor=(124,252,0)
    d.text((50,100),tabulate(DataList, HeaderList),font=fntt,fill=FontColor)
    d.text((20,500),"SEQUEN-A->",font=fnt,fill=FontColor)
    d.text((20,600),"SEQUEN-B->",font=fnt,fill=FontColor)
    YAxisFirstLine=500
    XAxisFirstLine=230
    YAxisSecondLine=530
    XAxisSecondLine=230
    YAxisThirdLine=560
    XAxisThirdLine=230
    for index,x in enumerate(SeqAObj):
        if index>200:
            d.rectangle((XAxisThirdLine,YAxisThirdLine,XAxisThirdLine+15,YAxisThirdLine+25),fill=MisMatchBoxColor)
            d.text((XAxisThirdLine,YAxisThirdLine),x,font=fnt,fill=MisMatchFontColor)
            if index in SeqDiffInd:
                d.rectangle((XAxisThirdLine,YAxisThirdLine,XAxisThirdLine+20,YAxisThirdLine+30),fill=ColorRect)
                d.text((XAxisThirdLine,YAxisThirdLine),x,font=fnt,fill=HighligtFontColor)
            XAxisThirdLine+=20
        elif index>100:
            d.rectangle((XAxisSecondLine,YAxisSecondLine,XAxisSecondLine+15,YAxisSecondLine+25),fill=MisMatchBoxColor)
            d.text((XAxisSecondLine,YAxisSecondLine),x,font=fnt,fill=MisMatchFontColor)
            if index in SeqDiffInd:
                d.rectangle((XAxisSecondLine,YAxisSecondLine,XAxisSecondLine+20,YAxisSecondLine+30),fill=ColorRect)
                d.text((XAxisSecondLine,YAxisSecondLine),x,font=fnt,fill=HighligtFontColor)
            XAxisSecondLine+=20
        else:
            d.rectangle((XAxisFirstLine,YAxisFirstLine,XAxisFirstLine+15,YAxisFirstLine+25),fill=MisMatchBoxColor)
            d.text((XAxisFirstLine,YAxisFirstLine),x,font=fnt,fill=MisMatchFontColor)
            if index in SeqDiffInd:
                d.rectangle((XAxisFirstLine,YAxisFirstLine,XAxisFirstLine+20,YAxisFirstLine+30),fill=ColorRect)
                d.text((XAxisFirstLine,YAxisFirstLine),x,font=fnt,fill=HighligtFontColor)
            XAxisFirstLine+=20      
    YAxisFirstLine=600
    XAxisFirstLine=230
    YAxisSecondLine=630
    XAxisSecondLine=230
    YAxisThirdLine=660
    XAxisThirdLine=230
    for index,x in enumerate(SeqBObj):
        if index>200:
            d.rectangle((XAxisThirdLine,YAxisThirdLine,XAxisThirdLine+15,YAxisThirdLine+25),fill=MisMatchBoxColor)
            d.text((XAxisThirdLine,YAxisThirdLine),x,font=fnt,fill=MisMatchFontColor)
            if index in SeqDiffInd:
                d.rectangle((XAxisThirdLine,YAxisThirdLine,XAxisThirdLine+20,YAxisThirdLine+30),fill=ColorRect)
                d.text((XAxisThirdLine,YAxisThirdLine),x,font=fnt,fill=HighligtFontColor)
            XAxisThirdLine+=20
        elif index>100:
            d.rectangle((XAxisSecondLine,YAxisSecondLine,XAxisSecondLine+15,YAxisSecondLine+25),fill=MisMatchBoxColor)
            d.text((XAxisSecondLine,YAxisSecondLine),x,font=fnt,fill=MisMatchFontColor)
            if index in SeqDiffInd:
                d.rectangle((XAxisSecondLine,YAxisSecondLine,XAxisSecondLine+20,YAxisSecondLine+30),fill=ColorRect)
                d.text((XAxisSecondLine,YAxisSecondLine),x,font=fnt,fill=HighligtFontColor)
            XAxisSecondLine+=20
        else:
            d.rectangle((XAxisFirstLine,YAxisFirstLine,XAxisFirstLine+15,YAxisFirstLine+25),fill=MisMatchBoxColor)
            d.text((XAxisFirstLine,YAxisFirstLine),x,font=fnt,fill=MisMatchFontColor)
            if index in SeqDiffInd:
                d.rectangle((XAxisFirstLine,YAxisFirstLine,XAxisFirstLine+20,YAxisFirstLine+30),fill=ColorRect)
                d.text((XAxisFirstLine,YAxisFirstLine),x,font=fnt,fill=HighligtFontColor)
            XAxisFirstLine+=20
    image.save(ReportFilePath)
    return ReportFilePath
    SeqFileName=os.path.basename(SeqA)
    split=os.path.splitext(SeqFileName)
    ReportFileName=split[0]+".png"
    ReportFilePath=os.path.join('C:\\Users\\mohid\\Desktop\\FLASK\\dev\\static\\DnaReports',ReportFileName)
    with open(SeqA,'r') as A ,open(SeqB,'r') as B:
        SeqAObj=A.read(300)
        SeqBObj=B.read(300)
    if len(SeqAObj)>len(SeqBObj):
        LenT=len(SeqAObj)-len(SeqBObj)
        print("A SEQUENCE  "+str(LenT)+" Times Bigger 😒😒😒😒")
        for i in range(LenT):
            SeqBObj+="-"
    elif len(SeqBObj)>len(SeqAObj):
        LenT=len(SeqBObj)-len(SeqAObj)
        print("B SEQUENCE  "+str(LenT)+" Times Bigger😒😒😒😒")
        for i in range(LenT):
            SeqAObj+="-"            
    SeqA_Counts={}
    SeqB_Counts={}
    for st in ascii_uppercase:
        SeqA_Counts[st]=SeqAObj.count(st)
        SeqB_Counts[st]=SeqBObj.count(st)
    DataList=[['Sequence A'],
            ['Sequence B']]
    HeaderList=["NAME"]
    for key,Value in SeqA_Counts.items():
        DataList[0].append(Value)
        DataList[1].append(SeqB_Counts[key])
        HeaderList.append(key)
    SeqAArrangments=[]
    SeqBArrangments=[]
    for x in  SeqAObj:
        SeqAArrangments.append(x)
    for y in SeqBObj:
        SeqBArrangments.append(y)
    list1 = np.array(SeqAArrangments)
    list2 = np.array(SeqBArrangments)
    SeqDiffInd = np.where(list1==list2)[0]
    SeqDiffList={}
    for i in SeqDiffInd:
        SeqDiffList[i]=SeqAArrangments[i]
    image=Image.open('C:\\Users\\mohid\\Desktop\\FLASK\\dev\\static\\Base\\image.png')
    d=ImageDraw.Draw(image)
    fnt=ImageFont.truetype('consola.ttf', 30)
    fntt=ImageFont.truetype('consola.ttf', 28)
    ColorRect=(127,255,212)
    FontColor=(0,0,0)
    HighligtFontColor=(0,0,255)
    MisMatchFontColor=(255,0,0)
    MisMatchBoxColor=(124,252,0)
    d.text((50,100),tabulate(DataList, HeaderList),font=fntt,fill=FontColor)
    d.text((20,500),"SEQUEN-A->",font=fnt,fill=FontColor)
    d.text((20,600),"SEQUEN-B->",font=fnt,fill=FontColor)
    YAxisFirstLine=500
    XAxisFirstLine=230
    YAxisSecondLine=530
    XAxisSecondLine=230
    YAxisThirdLine=560
    XAxisThirdLine=230
    for index,x in enumerate(SeqAObj):
        if index>200:
            d.rectangle((XAxisThirdLine,YAxisThirdLine,XAxisThirdLine+15,YAxisThirdLine+25),fill=MisMatchBoxColor)
            d.text((XAxisThirdLine,YAxisThirdLine),x,font=fnt,fill=MisMatchFontColor)
            if index in SeqDiffInd:
                d.rectangle((XAxisThirdLine,YAxisThirdLine,XAxisThirdLine+20,YAxisThirdLine+30),fill=ColorRect)
                d.text((XAxisThirdLine,YAxisThirdLine),x,font=fnt,fill=HighligtFontColor)
            XAxisThirdLine+=20
        elif index>100:
            d.rectangle((XAxisSecondLine,YAxisSecondLine,XAxisSecondLine+15,YAxisSecondLine+25),fill=MisMatchBoxColor)
            d.text((XAxisSecondLine,YAxisSecondLine),x,font=fnt,fill=MisMatchFontColor)
            if index in SeqDiffInd:
                d.rectangle((XAxisSecondLine,YAxisSecondLine,XAxisSecondLine+20,YAxisSecondLine+30),fill=ColorRect)
                d.text((XAxisSecondLine,YAxisSecondLine),x,font=fnt,fill=HighligtFontColor)
            XAxisSecondLine+=20
        else:
            d.rectangle((XAxisFirstLine,YAxisFirstLine,XAxisFirstLine+15,YAxisFirstLine+25),fill=MisMatchBoxColor)
            d.text((XAxisFirstLine,YAxisFirstLine),x,font=fnt,fill=MisMatchFontColor)
            if index in SeqDiffInd:
                d.rectangle((XAxisFirstLine,YAxisFirstLine,XAxisFirstLine+20,YAxisFirstLine+30),fill=ColorRect)
                d.text((XAxisFirstLine,YAxisFirstLine),x,font=fnt,fill=HighligtFontColor)
            XAxisFirstLine+=20      
    YAxisFirstLine=600
    XAxisFirstLine=230
    YAxisSecondLine=630
    XAxisSecondLine=230
    YAxisThirdLine=660
    XAxisThirdLine=230
    for index,x in enumerate(SeqBObj):
        if index>200:
            d.rectangle((XAxisThirdLine,YAxisThirdLine,XAxisThirdLine+15,YAxisThirdLine+25),fill=MisMatchBoxColor)
            d.text((XAxisThirdLine,YAxisThirdLine),x,font=fnt,fill=MisMatchFontColor)
            if index in SeqDiffInd:
                d.rectangle((XAxisThirdLine,YAxisThirdLine,XAxisThirdLine+20,YAxisThirdLine+30),fill=ColorRect)
                d.text((XAxisThirdLine,YAxisThirdLine),x,font=fnt,fill=HighligtFontColor)
            XAxisThirdLine+=20
        elif index>100:
            d.rectangle((XAxisSecondLine,YAxisSecondLine,XAxisSecondLine+15,YAxisSecondLine+25),fill=MisMatchBoxColor)
            d.text((XAxisSecondLine,YAxisSecondLine),x,font=fnt,fill=MisMatchFontColor)
            if index in SeqDiffInd:
                d.rectangle((XAxisSecondLine,YAxisSecondLine,XAxisSecondLine+20,YAxisSecondLine+30),fill=ColorRect)
                d.text((XAxisSecondLine,YAxisSecondLine),x,font=fnt,fill=HighligtFontColor)
            XAxisSecondLine+=20
        else:
            d.rectangle((XAxisFirstLine,YAxisFirstLine,XAxisFirstLine+15,YAxisFirstLine+25),fill=MisMatchBoxColor)
            d.text((XAxisFirstLine,YAxisFirstLine),x,font=fnt,fill=MisMatchFontColor)
            if index in SeqDiffInd:
                d.rectangle((XAxisFirstLine,YAxisFirstLine,XAxisFirstLine+20,YAxisFirstLine+30),fill=ColorRect)
                d.text((XAxisFirstLine,YAxisFirstLine),x,font=fnt,fill=HighligtFontColor)
            XAxisFirstLine+=20
    image.save(ReportFilePath)
    return ReportFilePath