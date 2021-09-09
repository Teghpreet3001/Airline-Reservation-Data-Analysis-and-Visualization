#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
df1 = pd.read_csv(r'C:\Users\Sheetel\Desktop\AirlineDetails.csv')
df2 = pd.read_csv(r'C:\Users\Sheetel\Desktop\PassengerDetails.csv')
df3 = pd.read_csv(r'C:\Users\Sheetel\Desktop\ticket.csv')
ch = input("Enter menu (AIR for AirlinDetails / PAS for PassengerDetails / TIC for Ticket)")
while(True):
    if ch == 'AIR' :
        print("AIRLINE MENU")
        print("1. To add a record")
        print("2. To delete a record")
        print("3. To add a column")
        print("4. To display records order by duration")
        print("5. To display records with number of seats greater than 100")
        ch1 = int(input("Enter choice"))
        if ch1 == 1 :
            df1[10] = pd.Series(['JJ1234','AIR INDIA','RANCHI','01-01-2021 13:00:00','GOA','02-01-2021 15:00:00', 6,300, 'ON TIME'], columns=["Airline_ID", 'Airline_Name', 'Departure_Destination' ,'Departure', 'Arrival_Destination','Arrival  Duration','Total_Seats','Status'])
            print(df1)
        elif ch1 == 2 :
            df1 = df1.drop(2)
            print(df1)
        elif ch1 ==3 :
            df1['Terminal'] = pd.Series('terminal3', index =[0,1,2,3,4,5,6,7,8,9])
            print(df1)
        elif ch1==4 :
            df1 = df1.sort_values(by='Duration', ascending=True)
            print(df1)
        elif ch1==5 :
            df1 = df1[df1['Total_Seats']>100]
            print(df1)
        else :
            print('Thank you')
            break
    if ch == 'PAS':
        print("PASSENGER DETAILS MENU")
        print("1. To display data order by age")
        print("2. To display all female records")
        print("3. To count all passengers having luggage_count>2")
        print("4. To display name, phone_number group by nationality")
        print("5. To display records of passengers with no luggage")
        print("6. To calculate maximum, minimum and average age, group by gender")
        ch2 = int(input("Enter choice"))
        if ch2 == 1 :
            df2 = df2.sort_values(by='Age', ascending=True)
            print(df2)
        elif ch2 == 2 :
            df2 = df2[df2['Gender']=="F"]
            print(df2)
        elif ch2 == 3 :
            m1 = df2[df2['Luggage_Count']>2]
            m1 = m1[['Luggage_Count']].count()
            print(m1)
        elif ch2 == 4 :
            m2 = df2.groupby(["Nationality"])
            m2 = m2['Name','Phone_Number']
            print(m2)
        elif ch2 == 5 :
            m3 = df2[df2['Luggage_Count']==0]    
            print(m3)
        elif ch2 == 6 :
            m4 = df2.groupby(["Gender"])
            m4 = m4['Age'].agg([np.max, np.min, np.mean])
            print(m4)
        else :
            print('Thank you')
            break    
    if ch == 'TIC':
        print("TICKET MENU")
        print("1. vertical Bar chart-Total seats versus Airline_ID")
        print("2. Horizontal Bar Chart- Luggage_Count versus Airline_ID")
        print("3. Pie Chart-Meal_Status versus No. of passengers")
        print("4. Pie Chart-Category versus no. of passengers")
        print("5. Histogram of no. of passengers in each age category")
        ch3 = int(input("Enter choice"))
        if ch3 == 1 :
            airline = ['INDIGO','ETIHAD AIRWAYS','SINGAPORE AIRLINES','THAI AIRWAYS','AIR INDIA','LUFTHANSIA','QATAR AIRWAYS','FLY DUBAI']
            total_seats = [180, 300, 270, 364, 256, 364, 300, 256]
            index = np.arange(len(airline))
            plt.bar(airline, total_seats, color='skyblue')
            plt.xlabel('AIRLINE ID', fontsize=10)
            plt.ylabel('TOTAL NUMBER OF SEATS', fontsize=10)
            plt.xticks(index, airline, rotation=90)
            plt.title("Bar chart-Total seats versus Airline_ID")
            plt.show()
        elif ch3 == 2 :
            airline = ['INDIGO','ETIHAD AIRWAYS','SINGAPORE AIRLINES','THAI AIRWAYS','AIR INDIA','LUFTHANSIA','QATAR AIRWAYS','FLY DUBAI']
            luggage_count = [100, 150, 320, 120, 230, 200, 100, 300]
            index = np.arange(len(airline))
            plt.barh(airline, luggage_count, color='yellow', edgecolor='k')
            plt.ylabel('AIRLINE ID', fontsize=20)
            plt.xlabel('LUGAGE COUNT', fontsize=20)
            plt.title("Horizontal Bar Chart- Luggage_Count versus Airline_ID")
            plt.show()
        elif ch3 == 3 :
            meal_status = ['YES','NO']
            y = df3[df3['Meal_Status']=='YES']
            y = y[['Meal_Status']].count()
            n = df3[df3['Meal_Status']=='NO']
            n = n[['Meal_Status']].count()
            choice =[y,n]
            e =(0.1,0.1)
            plt.pie(choice, labels= meal_status, colors=['lightcoral','lightskyblue'], shadow=True, autopct='%1.1f%%', explode=e)
            plt.title('Pie Chart representing portion of people taking meal')
            plt.axis('equal')
            plt.show()
        elif ch3 == 4 :
            category =['Economy','Premium','Business']
            e = df3[df3['Category']=='ECONOMY']
            e = e[['Category']].count()
            p = df3[df3['Category']=='PREMIUM']
            p = p[['Category']].count()
            b = df3[df3['Category']=='BUSINESS']
            b = b[['Category']].count()
            choice =[e,p,b]
            e1 = (0.1,0,0.1)
            plt.pie(choice, labels= category, colors=['lightcoral','lightskyblue','gold'],shadow=True, autopct='%1.1f%%', explode=e1)
            plt.title('Pie Chart representing Category versus no. of passengers')
            plt.axis('equal')
            plt.show()
        elif ch3 == 5 :
            plt.hist([0,10,20,30,40], bins=[0,10,20,30,40,50], weights=[5,20,40,30,10], facecolor='lightgreen', edgecolor='green')
            plt.xlabel('Age Intervals')
            plt.ylabel('Number of passengers')
            plt.title("Histogram of no. of passengers in each age category")
            plt.show()
        else :
            print('Thank you')
            break 


# In[ ]:





# In[ ]:





# In[ ]:




