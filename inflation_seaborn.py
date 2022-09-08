# -*- coding: utf-8 -*-
"""
Created on Sat Aug  6 14:28:10 2022

@author: Mehmet Akif
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import dataframe_image as dfi

inflation = pd.DataFrame(pd.read_csv("C:/Users/Mehmet Akif/OneDrive/Masaüstü/Excel Files/inflation.csv"))

def get_data():
    data2 = inflation.iloc[:,0:8]
    smp = data2.sample(n=20)
    smp_t = smp.style.background_gradient() #adding a gradient based on values in cell
    dfi.export(smp_t,"mytable.png")

c_inf = inflation.groupby("SUBJECT").get_group("TOT")
f_inf = inflation.groupby("SUBJECT").get_group("FOOD")

def turk_oecd():
    turk,oecde = c_inf[c_inf["LOCATION"] == "TUR"], c_inf[c_inf["LOCATION"] == "OECDE"]
    sns.set_theme(style="darkgrid")
    sns.lineplot(x="TIME",y="Value",data=turk,err_style="bars")
    sns.lineplot(x="TIME",y="Value",data=oecde,err_style="bars")
    locs, labels = plt.xticks()
    plt.setp(labels, rotation=45)
    plt.xlabel("Months")
    plt.ylabel("Inflation (%)")
    plt.legend(["Turkey","OECD Countries"])
    plt.savefig("ConsumerInflation(TURK - OECD).pdf", format="pdf", bbox_inches="tight")
    plt.show()

def similar_turk():
    turk,bra = c_inf[c_inf["LOCATION"] == "TUR"], c_inf[c_inf["LOCATION"] == "OECDE"]
    sns.set_theme(style="darkgrid")
    sns.lineplot(x="TIME",y="Value",data=turk,err_style="bars")
    sns.lineplot(x="TIME",y="Value",data=bra,err_style="bars")
    locs, labels = plt.xticks()
    plt.setp(labels, rotation=45)
    plt.xlabel("Months")
    plt.ylabel("Inflation (%)")
    plt.legend(["Turkey","Brazil"])
    plt.savefig("ConsumerInflation(TURK - Brazil).pdf", format="pdf", bbox_inches="tight")
    plt.show()

def turk_oecd_food():
    turk,oecde = f_inf[f_inf["LOCATION"] == "TUR"], f_inf[f_inf["LOCATION"] == "OECDE"]
    sns.set_theme(style="darkgrid")
    sns.set_theme(style="darkgrid")
    sns.lineplot(x="TIME",y="Value",data=turk,err_style="bars")
    sns.lineplot(x="TIME",y="Value",data=oecde,err_style="bars")
    locs, labels = plt.xticks()
    plt.setp(labels, rotation=45)
    plt.xlabel("Months")
    plt.ylabel("Food Inflation (%)")
    plt.legend(["Turkey","OECD Countries"])
    plt.savefig("FoodInflation(TURK - OECD).pdf", format="pdf", bbox_inches="tight")
    plt.show()


def turk_eu():
    turk,eu = c_inf[c_inf["LOCATION"] == "TUR"], c_inf[c_inf["LOCATION"] == "EU27_2020"]
    sns.set_theme(style="darkgrid")
    sns.set_theme(style="darkgrid")
    sns.lineplot(x="TIME",y="Value",data=turk,err_style="bars")
    sns.lineplot(x="TIME",y="Value",data=eu,err_style="bars")
    locs, labels = plt.xticks()
    plt.setp(labels, rotation=45)
    plt.xlabel("Months")
    plt.ylabel("Consumer Inflation (%)")
    plt.legend(["Turkey","EU Countries"])
    plt.savefig("ConsumerInflation(TURK - EU).pdf", format="pdf", bbox_inches="tight")
    plt.show()

def scatter():
    a = c_inf.groupby("LOCATION")["Value"].median()
    t = pd.DataFrame(a)
    k = t.sample(n=20)
    sns.set(font_scale = 0.7)
    sns.scatterplot(x="LOCATION",y="Value",data=k,hue = "LOCATION")
    locs, labels = plt.xticks()
    plt.setp(labels, rotation=90)
    legend = plt.legend(loc ="upper left", fontsize = 'small', fancybox = True)
    frame = legend.get_frame() #sets up for color, edge, and transparency
    frame.set_facecolor('#b4aeae') #color of legend
    frame.set_edgecolor('black') #edge color of legend
    frame.set_alpha(0.1) #deals with transparency
    plt.legend(bbox_to_anchor=(1,0.7))
    plt.ylabel("Median Inflation (%)")
    plt.xlabel("Location")
    plt.savefig("MedianInflation.pdf", format="pdf", bbox_inches="tight")
    plt.show()
    
get_data()
turk_oecd()
similar_turk()
turk_oecd_food()
turk_eu()
scatter()
