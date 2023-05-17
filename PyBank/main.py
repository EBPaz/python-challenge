# make the import run on any system and use the csv reading module
import os
import csv

# read the CSV file and convert it
csvpath = os.path.join('C:\\Users\\evapa\\OneDrive\\Desktop\\Data Class Incoming Folder\\UofW-VIRT-DATA-PT-04-2023-U-LOLC\\03-Python\\Homework\\Starter_Code\\PyBank\\Resources\\budget_data.csv')
textfile = os.path.join('C:\Users\evapa\OneDrive\Desktop\Python\python-challenge\PyBank\analysis\\budget_analysis.txt')

#set values for the varaibles in the dataset
total_months = 1
profit_loss = 0
daily_change_list = []
greatest_increase = ['',0]
greatest_decrease = ['',0]

# Read the csv and convert it into a list of dictionaries
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile)

    # Read the header row
    header = next(csvreader)

    # set up to read the first row in the right variables   
    yesterdays_row = next(csvreader)
    net_profit_loss = float(yesterdays_row[1])
    
    #set up a loop to run through the dataset
    for row in csvreader:
        date = (row[0])
        profit_loss = float(row[1])

    # find the total months the dataset holds
        total_months += 1
       
    # find the net total profit/loss of the dataset
        net_profit_loss += profit_loss
       
    # find the daily change in profit/loss of the dataset by doing math with the variables
        yesterdays_price = int(yesterdays_row[1])
        daily_change = (profit_loss - yesterdays_price)
    # create a new dataset for daily-change
        daily_change_list.append(daily_change)
   
    # find the greatest increase and decrease by running an if statement and holding the value with the date 
        if daily_change > greatest_increase[1]:
            greatest_increase[1] = daily_change
            greatest_increase[0] = date

        if daily_change< greatest_decrease[1]:
            greatest_decrease[1] = daily_change
            greatest_decrease[0] = date    

        yesterdays_row = row 
   
    # find the average of the daily change in profit/loss, outside of the loop (once all of the data is calculated)
    average_daily_change = sum(daily_change_list) / len(daily_change_list)
    print(max(daily_change_list))

    # print all final statements to the terminal   
    print(f'Total Months: {total_months}')
    print(f'Total: ${net_profit_loss:.0f}')
    print(f'Average Change: ${average_daily_change:.2f})')
    print(f'Greatest Increase in Profits: {greatest_increase[0]}, {greatest_increase[1]}')
    print(f'Greatest Decrease in Profits: {greatest_decrease[0]}, {greatest_decrease[1]}')

# export all final statements as a text file

with open(textfile, 'w') as summary:
    summary.write(f'Total Months: {total_months}\n'
                 f'Total: ${net_profit_loss:.0f}\n'
                 f'Average Change: ${average_daily_change:.2f}\n'
                 f'Greatest Increase in Profits: {greatest_increase[0]}, {greatest_increase[1]}\n'
                 f'Greatest Decrease in Profits: {greatest_decrease[0]}, {greatest_decrease[1]}\n')
    

