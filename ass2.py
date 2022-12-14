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
    """
    
    Parameters
    ----------
    filename : csv file

    Returns
    -------
    df : dataframe with years as columns
    dftrans : dataframe with countries as columns

    """
    df = pd.read_csv(filename)
#transposing the data
    dftrans= df.set_index('Country Name').transpose()
    return df, dftrans
#creating two list of countries one for plotting the bar plot and another for the line plot
Countries1 = ['Belgium','China','Denmark','Spain','Finland','Jamaica']
Countries2 = ['Australia','Brazil','Canada', 'Germany','France','India']
#in order to plot the bar chart, creating the function to filter the data
def filter_bar_data(df):
    """
    

    Parameters
    ----------
    df : dataframe with years as columns

    Returns
    -------
    df : filtered dataframe to plot the bar chart of selected countries

    """
    df = df[['Country Name','Indicator Name','2010','2011','2012','2013','2014']]
    df = df[(df["Country Name"]=="Belgium")|
            (df["Country Name"]=="China")|
            (df["Country Name"]=="Denmark")|
            (df["Country Name"]=="Spain")|
            (df["Country Name"]=="Finland")|
            (df["Country Name"]=="Jamaica")]
    return df
#in order to plot the line chart, creating the function to filter the data
def filter_line_plot(df):
    """
    

    Parameters
    ----------
    df : dataframe with years as columns

    Returns
    -------
    df : filtered dataframe to plot the line chart of selected countries

    """
    df = df[['Country Name','Indicator Name','2010','2011','2012','2013','2014']]
    df = df[(df["Country Name"]=="Australia")|
            (df["Country Name"]=="Brazil")|
            (df["Country Name"]=="Canada")|
            (df["Country Name"]=="Germany")|
            (df["Country Name"]=="France")|
            (df["Country Name"]=="India")]
    return df
#creating the function to plot the bar chart
def barplot(df,lab1,lab2):
    """
    

    Parameters
    ----------
    df : dataframe to plot bar chart of the chosen countries
    lab1 : to label y-axis
    lab2 : to get the title of the bar graph

    Returns
    -------
    None.

    """
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
#creating the function to plot the line chart
def line_plot(df,lab1,lab2):
    """
    

    Parameters
    ----------
    df : dataframe to plot line chart of the chosen countries
    lab1 : to label y-axis
    lab2 : to get the title of the line chart

    Returns
    -------
    None.

    """
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
#bringing the csv file by displaying the path of the data with the help of function
PG_data1,PG_data2= read_file("C:/Users/CHINNU BABY/Desktop/New folder/pop growthh.csv")
PG_data1= filter_bar_data(PG_data1)
Unemployment_data1,Unemployment_data2= read_file("C:/Users/CHINNU BABY/Desktop/New folder/unemployment.csv")
Unemployment_data1= filter_bar_data(Unemployment_data1)

Energy_data1,Energy_data2= read_file("C:/Users/CHINNU BABY/Desktop/New folder/energy use.csv")
Energy_data1= filter_line_plot(Energy_data1)
CO2_data1,CO2_data2= read_file("C:/Users/CHINNU BABY/Desktop/New folder/co2 emission.csv")
CO2_data1= filter_line_plot(CO2_data1)
#giving the labels for x-axis and y-axis for the four plots
barplot(PG_data1,"Population growth (annual %)","Population Growth")
barplot(Unemployment_data1,"Unemployment, total (%) (national estimate)","Unemployment")

line_plot(Energy_data1,"Energy use (kg of oil)","Energy use")
line_plot(CO2_data1,"CO2 emissions (kt)","CO2 Emission")
#function to calculate the mean of CO2 emission
def co2_mean():
    df, dftrans = read_file("C:/Users/CHINNU BABY/Desktop/New folder/co2 emission.csv")
#filtering the dataframe
    dt = df.set_index('Country Name')
    tran = dt.transpose()
#removing unimportant columns
    tran = tran.drop(index='Country Code')
    tran = tran.drop(index='Indicator Name')
    tran = tran.drop(index='Indicator Code')
#replacing the NaN values with O
    dt_new = tran.fillna(0)
    st_mean = dt_new[["Australia","Brazil","Canada", "Germany","France","India"]].mean()
    return st_mean
st_mean = co2_mean()
#getting mean into csv file
st_mean = st_mean.to_csv("mean_co2.csv")
print(st_mean)
