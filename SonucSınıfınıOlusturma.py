import pandas as pd
import numpy as np

data = pd.read_csv('dataSet.csv')
df=pd.DataFrame(data)
df=df.fillna(df.mean())

def calculatingSO2(so2):
    soi2=0
    if (so2>=0 and so2<=100):
     soi2= ((50.0-0.0)/(100.0-0.0))*(so2-0.0) + 0.0
    if (so2>=101 and so2<=250):
     soi2= ((100.0-51.0)/(250.0-101.0))*(so2-101.0) + 51.0
    if (so2>=251 and so2<=500):
     soi2= ((150-101)/(500-251))*(so2-251) + 101
    if (so2>=501 and so2<=850):
     soi2= ((200-151)/(850-501))*(so2-501) + 151
    if (so2>=851 and so2<=1100):
     soi2= ((300-201)/(1100-851))*(so2-851) + 201
    if (so2>=1101 and so2<= 1500):
     soi2= ((500-301)/(1500-1101))*(so2-1101) + 301

    return soi2

def calculatingNO2(no2):
    noi2=0
    if (no2>=0 and no2<=100):
     noi2= ((50.0-0.0)/(100.0-0.0))*(no2-0.0) + 0.0
    if (no2>=101 and no2<=200):
     noi2= ((100-51)/(200-101))*(no2-101) + 51
    if (no2>=201 and no2<=500):
     noi2= ((150-101)/(500-201))*(no2-201) + 101
    if (no2>=501 and no2<=1000):
     noi2= ((200-151)/(1000-501))*(no2-501) + 151
    if (no2>=1001 and no2<=2000):
     noi2= ((300-201)/(2000-1001))*(no2-1001) + 201
    if (no2>=2001 and no2<= 3000):
     noi2= ((500-301)/(3000-2001))*(no2-2001) + 301
    return noi2

def calculatingPM10(pm10):
    pm10i2=0
    if (pm10>=0 and pm10<=50):
     pm10i2= ((50.0-0.0)/(50.0-0.0))*(pm10-0.0) + 0.0
    if (pm10>=51 and pm10<=100):
     pm10i2= ((100.0-51.0)/(100.0-51.0))*(pm10-51.0) + 51.0
    if (pm10>=101 and pm10<=260):
     pm10i2= ((150.0-101.0)/(260.0-101.0))*(pm10-101.0) + 101.0
    if (pm10>=261 and pm10<=400):
     pm10i2= ((200-151)/(400-261))*(pm10-261) + 151
    if (pm10>=401 and pm10<=520):
     pm10i2= ((300-201)/(520-401))*(pm10-401) + 201
    if (pm10>=521 and pm10<= 620):
     pm10i2= ((500-301)/(620-521))*(pm10-521) + 301

    return pm10i2

def calculatingCO(CO):
    coi2=0
    if (CO>=0 and CO<=5500):
     coi2= ((50.0-0.0)/(5500.0-0.0))*(CO-0.0) + 0.0
    if (CO>=5501 and CO<=10000):
     coi2= ((100-51)/(10000-5501))*(CO-5501) + 51
    if (CO>=10001 and CO<=16000):
     coi2= ((150-101)/(16000-10001))*(CO-10001) + 101
    if (CO>=16001 and CO<=24000):
     coi2= ((200-151)/(24000-16001))*(CO-16001) + 151
    if (CO>=24001 and CO<=32000):
     coi2= ((300-201)/(32000-24001))*(CO-24001) + 201
    if (CO>=32001 and CO<=40000):
     coi2= ((500-301)/(40000-32001))*(CO-32001) + 301
    return coi2


def calculateHKI():
    listPM10 = list(df.filter(like='PM10').columns)
    listSO2 = list(df.filter(like='SO2').columns)
    listNO2 = list(df.filter(like='NO2').columns)
    listCO = list(df.filter(like='CO').columns)
    for pm10 in listPM10:
        df["HKI"+pm10] = df[pm10].apply(calculatingPM10)
    for so2 in listSO2:
        df["HKI"+so2] = df[so2].apply(calculatingSO2)
    for no2 in listNO2:
        df["HKI"+no2] = df[no2].apply(calculatingNO2)
    for co in listCO:
        df["HKI"+co] = df[co].apply(calculatingCO)

def calculatingStoves(s):
    rs = 0
    if s >= 0 and s <= 50:
        rs = 0
    elif s >= 51 and s <= 100:
        rs = 1
    elif s >= 101 and s <= 150:
        rs = 2
    elif s >= 151 and s <= 200:
        rs = 3
    elif s >= 201 and s <= 300:
        rs = 4
    elif s >= 301 and s <= 500:
        rs = 5
    return rs
calculateHKI()
listPM10 = list(df.filter(like='HKIPM10').columns)
listSO2 = list(df.filter(like='HKISO2').columns)
listNO2 = list(df.filter(like='HKINO2').columns)
listCO = list(df.filter(like='HKICO').columns)

df['sonuc'] = df['HKIPM10'] + df['HKISO2'] + df['HKINO2'] + df['HKICO']
listsonuc = list(df.filter(like='sonuc').columns)
for sonuc in listsonuc:
    df["HKI"+sonuc] = df[sonuc].apply(calculatingStoves)

del df['HKISO2']
del df['HKIPM10']
del df['HKINO2']
del df['HKICO']
del df['sonuc']
del df['Tarih']

df.to_csv('result.csv')

print df
