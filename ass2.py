# -*- coding: utf-8 -*-
"""
Created on Thu Dec  8 12:34:14 2022

@author: CHINNU BABY
"""
#importing libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#
def read_file(filename):
    df = pd.read_csv(filename)
#transposing the data
    dftrans= df.set_index('Country Name').transpose()
    return df, dftrans
Countries1 = ['Belgium','China','Denmark','Spain','Finland','Jamaica']
Countries2 = ['Australia','Brazil','Canada', 'Germany','France','India']

def filter_bar_data(df):
    df = df[['Country Name','Indicator Name','2010','2011','2012','2013','2014']]
    df = df[(df["Country Name"]=="Belgium")|
            (df["Country Name"]=="China")|
            (df["Country Name"]=="Denmark")|
            (df["Country Name"]=="Spain")|
            (df["Country Name"]=="Finland")|
            (df["Country Name"]=="Jamaica")]
    return df

def filter_line_plot(df):
    df = df[['Country Name','Indicator Name','2010','2011','2012','2013','2014']]
    df = df[(df["Country Name"]=="Australia")|
            (df["Country Name"]=="Brazil")|
            (df["Country Name"]=="Canada")|
            (df["Country Name"]=="Germany")|
            (df["Country Name"]=="France")|
            (df["Country Name"]=="India")]
    return df

def barplot(df,lab1,lab2):
    plt.figure(figsize=(25,18))
    dx= plt.subplot(1,1,1)
    x = np.arange(6)
    width= 0.2
    
    bar1= dx.bar(x, df["2010"],width,label=2010)
    bar2= dx.bar(x+width, df["2011"],width,label=2011)
    bar3= dx.bar(x+width*2, df["2012"],width,label=2012)
    
    dx.set_xlabel("Countries", fontsize=40)
    dx.set_ylabel(lab1, fontsize=40)
    dx.set_title(lab2, fontsize=40)
    dx.set_xticks(x,Countries1,fontsize=30,rotation=90)
    dx.legend(fontsize=30)
    dx.bar_label(bar1,padding=2,rotation=90,fontsize=18)
    dx.bar_label(bar2,padding=2,rotation=90,fontsize=18)
    dx.bar_label(bar3,padding=2,rotation=90,fontsize=18)
    plt.savefig("barplot.png")
    plt.show()

def line_plot(df,lab1,lab2):
    plt.figure(figsize=(25,15))
    ss=df.set_index('Country Name')
    trans=ss.transpose()
    trans=trans.drop(index=['Indicator Name'])
    
    for i in range(len(Countries2)):
        plt.plot(trans.index,trans[Countries2[i]],label=Countries2[i])
        
    plt.title(lab2,size=40)
    plt.xlabel("Years",size=40)
    plt.ylabel(lab1,size=40)
    plt.xticks(rotation=90)
    plt.legend(fontsize=30)
    plt.savefig("lineplot.png")
    plt.show()

PG_data1,PG_data2= read_file("pop growthh.csv")
PG_data1= filter_bar_data(PG_data1)
Unemployment_data1,Unemployment_data2= read_file("unemployment.csv")
Unemployment_data1= filter_bar_data(Unemployment_data1)

Energy_data1,Energy_data2= read_file("energy use.csv")
Energy_data1= filter_line_plot(Energy_data1)
CO2_data1,CO2_data2= read_file("co2 emission.csv")
CO2_data1= filter_line_plot(CO2_data1)

barplot(PG_data1,"Population growth (annual %)","Population Growth")
barplot(Unemployment_data1,"Unemployment, total (%) (national estimate)","Unemployment")

line_plot(Energy_data1,"Energy use (kg of oil)","Energy use")
line_plot(CO2_data1,"CO2 emissions (kt)","CO2 Emission")
