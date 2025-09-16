import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import csv
import statistics
import io
######################################
#Function to display Main menu
######################################
#matplotlib inline
def menuset():
    
    opt=""
    print()
    print("*************** SALARY SURVEY *****************")
    print("1.Data Visualization\n")
    print("2.Analysis\n")
    print("3.Read or Duplicate CSV\n")
    print("4.Manipulation\n")
    print("5.Exit\n")
    opt=int(input('Enter ur choice : '))
    if opt==1:
        visuals()
    elif opt==2:
        analysis()
    elif opt==3:
        read_csv_excel()
    elif opt==4:
        manipulation()
    elif opt==5:
        print('Thanks for Visit')
        exit()
def visuals():
    
    opt=""
    print()
    print("***************Data Visualization Menu*****************")
    print("1.Line Chart-Salary\n")
    print("2.Bar Chart-Working hours per week\n")
    print("3.Exit\n")
    opt=int(input('Enter ur choice : '))
    if opt==1:
        line_chart()
    elif opt==2:
        bar_chart()
    elif opt==3:
        ch=input('Press m/M for main menu\nPress e/E for exit : ')
        if ch=='m' or ch=='M':
            menuset()
        elif ch=='e' or ch=='E':
            print('Thanks for Visit')
            exit()

def analysis():
    
    opt=""
    print()
    print("***************DataFrame Analysis Menu*****************")
    print("1.Top Records\n")
    print("2.Bottom Records\n")
    print("3.To Print Particular Column\n")
    print("4.To Print Multiple Columns\n")
    print("5.To Display Complete Statistics of DataFrame\n")
    print("6.To Display Complete Information about DataFrame\n")
    print("7.To Display Unique Values of the column\n")
    print("8.To applying aggregate functions\n")
    print("9.Exit\n")
    opt=int(input('Enter ur choice : '))
    if opt==1:
        top()
    elif opt==2:
        bottom()
    elif opt==3:
        single_column()
    elif opt==4:
        multiple_columns()
    elif opt==5:
        statistics()
    elif opt==6:
        comp_dataframe()
    elif opt==7:
        unique()
    elif opt==8:
        aggregate()
    elif opt==9:
        ch=input('Press m/M for main menu\nPress e/E for exit : ')
        if ch=='m' or ch=='M':
            menuset()
        elif ch=='e' or ch=='E':
            print('Thanks for Visit')
            exit()

def read_csv_excel():
    cs=pd.read_csv('ss.csv')
    df=pd.DataFrame(cs)
    opt=""
    print()
    print("***************Read CSV/Excel File Menu*****************")
    print("1.Read CSV file to create and display dataframe\n")
    print("2.Read Excel file and display dataframe\n")
    print("3.To Go Back\n")
    opt=int(input('Enter ur choice : '))
    if opt==1:
        cs=pd.read_csv('ss.csv')
        df=pd.DataFrame(cs)
        print(df.to_string(index=False))
        menuset()
    elif opt==2:
        
        f=input('Enter File Name in Excel : ')
        d=pd.read_excel(f)
        print(d)
        print('File retrieved Successfully')
        menuset()
   
    elif opt==3:
        ch=input('Press m/M for main menu\nPress e/E for exit : ')
        if ch=='m' or ch=='M':
            menuset()
        elif ch=='e' or ch=='E':
            print('Thanks for Visit')
            exit()

def manipulation():
    
    opt=""
    print()
    print("***************Data Manipulation Menu*****************")
    print("1.Insert a Row\n")
    print("2.Delete a Row\n")
    print("3.Exit\n")
    opt=int(input('Enter ur choice : '))
    if opt==1:
        cs=pd.read_csv('ss.csv')
        df=pd.DataFrame(cs)
        print(df.columns)
        nw=eval(input('Plz enter values for above columns as list in square bracket[] : '))
        df.loc[len(df.index)] = nw 
        print(df)
        df.to_csv('ss.csv')
        menuset()
    elif opt==2:
        cs=pd.read_csv('ss.csv')
        df=pd.DataFrame(cs)
        print(df)
        ind=int(input('Enter Row Index To Delete : '))
        df = df.drop(df.index [ind])
        df.to_csv('ss.csv')
        print(df)
        menuset()
    elif opt==3:
        ch=input('Press m/M for main menu\nPress e/E for exit : ')
        if ch=='m' or ch=='M':
            menuset()
        elif ch=='e' or ch=='E':
            print('Thanks for Visit')
            exit()

def top():
    cs=pd.read_csv('ss.csv')
    df=pd.DataFrame(cs)
    print(df.head())
    menuset()
    
def bottom():
    cs=pd.read_csv('ss.csv')
    df=pd.DataFrame(cs)
    print(df.tail())
    menuset() 
    
def single_column():
    cs=pd.read_csv('ss.csv')
    df=pd.DataFrame(cs)
    cl=input('Plz enter column name : ')
    print(df[cl])
    menuset()
    
def multiple_columns():
    cs=pd.read_csv('ss.csv')
    df=pd.DataFrame(cs)
    cl=eval(input('Plz enter column names as list in square bracket[] : '))
    print(df[cl])
    menuset()
    
def statistics():
    cs=pd.read_csv('ss.csv')
    df=pd.DataFrame(cs)
    print('1.Max Function')
    print('2.Min Function')
    print('3.Mean Function')
    print('4.Count Function')
    ch=int(input('Enter ur Choice : '))
    if ch==1:
        c=input('Enter Column Name For Max Value : ')
        print('Maximum Value of',c,' = ', df[c].max())
    elif ch==2:
        c=input('Enter Column Name For Min Value : ')
        print('Minimum Value of',c,' = ', df[c].min())
    elif ch==3:
        c=input('Enter Column Name For Mean Value :')
        print('Mean Value of',c,' = ', df[c].mean())
    elif ch==4:
        print('Total number of records = ')
        print(df.count(axis=0))
    menuset()
    
def comp_dataframe():
    cs=pd.read_csv('ss.csv')
    df=pd.DataFrame(cs)
    print(df.to_string(index=False))
    menuset()
    
def unique():
    cs=pd.read_csv('ss.csv')
    df=pd.DataFrame(cs)
    print(df.columns)
    cl=input('Plz enter column name : ')
    print(df[cl].unique())
    menuset()
    
def aggregate():
    cs=pd.read_csv('ss.csv')
    df=pd.DataFrame(cs)
    print(df.columns)
    print(df.aggregate(['sum','min','max']))
    menuset()
    
def line_chart():
    l=[]
    cs=pd.read_csv('ss.csv')
    df=pd.DataFrame(cs)
    x1=df['Country_Name']
    y1=df['Salary']
    plt.xlabel('Country Name' , fontsize= 12 , color='red')
    plt.ylabel('Salary' , fontsize= 12 , color='red')
    plt.plot(x1,y1, color='blue' , linewidth= 5)
    plt.show()
    menuset()
    
def bar_chart():
    cs=pd.read_csv('ss.csv')
    df=pd.DataFrame(cs)
    x1=df['Country_Name']
    y1=df['Working_hours_per_week']
    plt.xlabel('Country Name' , fontsize= 12 , color='r')
    plt.ylabel('Working hours per week' , fontsize= 12 , color='r')
    plt.bar(x1,y1, facecolor='green' , edgecolor='purple')
    plt.show()
    menuset()

menuset()
