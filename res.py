import pandas as pd
import sqlite3
import matplotlib.pyplot as plt
import os
def fn():
    comd=sqlite3.connect("Users.db")
    print("Opened database successfully")
    cmd="SELECT * from Marks"
    cursor=comd.execute(cmd)
    df=pd.DataFrame(cursor)
    df.rename(columns={0:'ID',1:'English1',2:'Hindi1',3:"maths1"},inplace=True)
    df["total"]=( pd.to_numeric(df["English1"])+ pd.to_numeric(df["Hindi1"])+ pd.to_numeric(df["maths1"]))/150*100
    percentage=df.total
    bins = [0,10,20,30,40,50,60,70,80,90,100]
    plt.hist(percentage, bins, histtype='bar', rwidth=0.8)
    plt.xlabel('PERCENTAGE')
    plt.ylabel('NO OF STUDENTS')
    plt.title('STUDENT MARKS ANALYSIS')
    plt.savefig('testplot.png')
    os.system('testplot.png')
def fn2():
    comd=sqlite3.connect("Users.db")
    print("Opened database successfully")
    cmd="SELECT * from Marks"
    cursor=comd.execute(cmd)
    df=pd.DataFrame(cursor)
    df.rename(columns={0:'ID',1:'English1',2:'Hindi1',3:"maths1"},inplace=True)
    df["total"]=( pd.to_numeric(df["English1"])+ pd.to_numeric(df["Hindi1"])+ pd.to_numeric(df["maths1"]))/150*100
    percentage=df.total
    print(percentage)
    print("Opened database successfully")
    cmd2="SELECT * from Timer"
    cursor2=comd.execute(cmd)
    df2=pd.DataFrame(cursor2)
    df2.rename(columns={0:'ID',1:'Time'},inplace=True)
    df2["total"] = pd.to_numeric(df2["Time"])
    tt=df2.Time
    print(tt)
    plt.plot(percentage,tt)
    plt.xlabel('MARKS')
    plt.ylabel('TIME ON APP')
    plt.title('TIME V/S MARKS GRAPH')
    plt.savefig('testplot2.png')
    os.system('testplot2.png')
