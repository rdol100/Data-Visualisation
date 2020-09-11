from tkinter import *
from tkinter.ttk import *
import pandas as pd

# Let's create the Tkinter window
window = Tk()

# Then, you will define the size of the window in width(312) and height(324) using the 'geometry' method
window.geometry("1000x1000")

# In order to prevent the window from getting resized you will call 'resizable' method on the window
#window.resizable(0, 0)

#Finally, define the title of the window
window.title("Search")

total_df = []

#define what to do when Load is clicked

def clicked():
        
    if div_combo.get()=="Premier League":
        division = "E0"
    elif div_combo.get()=="Championship":
        division = "E1"
    elif div_combo.get()=="League One":
        division = "E2"
    elif div_combo.get()=="League Two":
        division = "E3"
    elif div_combo.get()=="Conference":
        division = "EC"
    
    if (season_check_1920.get()==False and season_check_1819.get()==False and season_check_1718.get()==False):
        
        print("No season(s) selected")
    
    else:
    
        
        if season_check_1920.get() == True:
            
            season = "1920"
            url = "https://www.football-data.co.uk/mmz4281/{}/{}.csv".format(season,division)
            df1920 = pd.read_csv(url)
            df1920_small = df1920[['Date','HomeTeam','AwayTeam','FTHG','FTAG','Avg>2.5','Max>2.5']]
            
        if season_check_1819.get() == True:
                
            season = "1819"
            url = "https://www.football-data.co.uk/mmz4281/{}/{}.csv".format(season,division)
            df1819 = pd.read_csv(url)
            df1819['Avg>2.5']= df1819['BbAv>2.5']
            df1819['Max>2.5']= df1819['BbMx>2.5']
            df1819_small = df1819[['Date','HomeTeam','AwayTeam','FTHG','FTAG','Avg>2.5','Max>2.5']]
                
        if season_check_1718.get() == True:
                    
            season = "1718"
            url = "https://www.football-data.co.uk/mmz4281/{}/{}.csv".format(season,division)
            df1718 = pd.read_csv(url)
            df1718['Avg>2.5']= df1718['BbAv>2.5']
            df1718['Max>2.5']= df1718['BbMx>2.5']
            df1718_small = df1718[['Date','HomeTeam','AwayTeam','FTHG','FTAG','Avg>2.5', 'Max>2.5']]
         
            
            
        if (season_check_1718.get() == True):
            
            if (season_check_1819.get() == True):
                
               if (season_check_1920.get() == True):
                   
                   total_df = df1718_small.append([df1819_small, df1920_small], ignore_index=True)
               
               else:
             
                   total_df = df1718_small.append(df1819_small, ignore_index=True) 
               
            elif (season_check_1920.get() == True):
                
                total_df = df1718_small.append(df1920_small, ignore_index=True)
                
            else:
                
                total_df = df1718_small
    
            
        elif (season_check_1819.get() == True):
            
            if (season_check_1920.get() == True):
                   
                total_df = df1819_small.append(df1920_small, ignore_index=True)
                   
            else:
            
                total_df = df1819_small
                
        elif (season_check_1920.get() == True):
            
            total_df = df1920_small


        #make additional columns for imported data
        bet_size_units = int(bet_size.get())
        loss = bet_size_units
    
        
        total_df['TG']= total_df['FTHG'] + total_df['FTAG']
        total_df['AvProfit'] = total_df['Avg>2.5']* bet_size_units
        total_df['MaxProfit'] = total_df['Max>2.5']* bet_size_units
        total_df['AvROI'] = (total_df['Avg>2.5']-1)*100
        total_df['MaxROI'] = (total_df['Max>2.5']-1)*100
        
        print(total_df)
        
        
        #Start applying filters to data
        
        total_goals_condition = float(total_goals.get())
      
        
        home_team = home_team_txt.get()
        away_team = away_team_txt.get()
        
        team_filtered_df = total_df[(total_df['HomeTeam']==home_team) & (total_df['AwayTeam']==away_team)]
        #filtered_df = total_df[(total_df['FTHG']>total_goals_condition) & (total_df['HomeTeam']==home_team)]
        goals_team_filtered_df = team_filtered_df[team_filtered_df['TG'] > total_goals_condition]
    
        #print(team_filtered_df)
       # print(team_filtered_df[team_filtered_df['TG']>2.5].count())
       # print("Games with greater than 2.5 goals: ").format(games_G25)
       # print(goals_team_filtered_df)



###############################################################################################
    
#create 'Load' button

btn = Button(window, text="Load", command=clicked)
 
btn.grid(column=15, row=15)


#Total goals filter

total_goals_lbl = Label(window, text="Total Goals >")
 
total_goals_lbl.grid(column=13, row=0)

total_goals = Spinbox(values=(0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5), width=5)

total_goals.set(0.5)

total_goals.grid(column=14, row=0)




test_lbl = Label(window, text="Bet Size")
 
test_lbl.grid(column=13, row=2)


#Division drop down menu
div_combo = Combobox(window) 

div_combo['values']= ("Premier League", "Championship", "League One", "League Two", "Conference") 

div_combo.current(0) #set the selected item 

div_combo.grid(column=1, row=0)

div_lbl = Label(window, text="Division")

div_lbl.grid(column=0, row=0)



#Season choice tick boxes

season_lbl = Label(window, text="Season(s)")

season_lbl.grid(column=0, row=2)


season_check_1718 = BooleanVar()
 
season_check_1718.set(False) #set check state
 
season_checkbox_1718 = Checkbutton(window, text='2017-18', var=season_check_1718)

season_checkbox_1718.grid(column=1,row=2)


season_check_1819 = BooleanVar()
 
season_check_1819.set(False) #set check state
 
season_checkbox_1819 = Checkbutton(window, text='2018-19          ', var=season_check_1819)

season_checkbox_1819.grid(column=2,row=2)


season_check_1920 = BooleanVar()
 
season_check_1920.set(False) #set check state
 
season_checkbox_1920 = Checkbutton(window, text='2019-20', var=season_check_1920)

season_checkbox_1920.grid(column=3,row=2)



#Window for home team choice
home_team_txt = Entry(window,width=20)
 
home_team_txt.grid(column=1, row=6)

home_team_lbl = Label(window, text="Home Team")

home_team_lbl.grid(column=0, row=6)


#Window for away team choice
away_team_txt = Entry(window,width=20)
 
away_team_txt.grid(column=1, row=8)

away_team_lbl = Label(window, text="Away Team")

away_team_lbl.grid(column=0, row=8)



#More than goals choice box
bet_size = Spinbox(values=(1,2,3,4,5,6,7,8,9,10), width=5)

bet_size.set(1)

bet_size.config(textvariable="test")

bet_size.grid(column=14, row=2)



window.mainloop()
