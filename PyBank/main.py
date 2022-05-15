# Add dependencies
import csv
import os

# Create path to budget Results 
file_to_load = os.path.join(os.path.dirname(os.path.abspath(__file__)),"Resources", "budget_data.csv")


# Create variables for analyse
txt_path = "AnalyseResult.txt" 
total_months = 0
previous_revenue = 0
revenue_change = 0
total_revenue = 0
list_revenue_change = []
greatest_increase = ["",0]
greatest_decrease = ["", 1000000]
revenue_average_change = 0


# Open Election Results
with open(file_to_load, 'r') as budget_data:
    # Read budget data 
    file_reader = csv.DictReader(budget_data)
    # Print each row in the CSV file.
    for row in file_reader:
        if total_months == 0: previous_revenue = int(row["Profit/Losses"])
        
        #Calculate The net total amount of "Profit/Losses" over the entire period
        total_revenue = total_revenue + int(row["Profit/Losses"])
        #Calculate The changes in "Profit/Losses" over the entire period, and then the average of those changes

        if total_months > 0:
            revenue_change = int(row["Profit/Losses"]) - previous_revenue 
            #Append the values to the list of revenue change
            list_revenue_change.append(revenue_change)
        
        #initilize previous value
        previous_revenue = int(row["Profit/Losses"])

        if revenue_change>greatest_increase[1]:
            greatest_increase[1]= revenue_change
            greatest_increase[0] = row['Date']

        #The greatest decrease in revenue (date and amount) over the entire period
        if revenue_change<greatest_decrease[1]:
            greatest_decrease[1]= revenue_change
            greatest_decrease[0] = row['Date']

        total_months += 1


    #The average revenue of the changes
    revenue_average_change = sum(list_revenue_change)/(len(list_revenue_change))

    print("Financial Analysis")
    print("----------------------------")
    print('Total Months: ' , total_months)
    print('Total: ' , total_revenue)
    print('Average Change: ' , revenue_average_change)
    print('Greatest Increase in Profits: ' , greatest_increase)
    print('Greatest Decrease in Profits: ' , greatest_decrease)


    print("Financial Analysis", file=open(txt_path, "a"))
    print("----------------------------", file=open(txt_path, "a"))
    print(f"Total Months: {total_months}", file=open(txt_path, "a"))
    print(f"Total Revenue: ${total_revenue:,}", file=open(txt_path, "a"))
    print(f"Average Change: ${revenue_average_change:,}", file=open("PyBank.txt", "a"))
    print(f"Greatest Increase in Revenue: {greatest_increase[0]} (${greatest_increase[1]:,})", file=open(txt_path, "a"))
    print(f"Greatest Decrease in Decrease: {greatest_decrease[0]} (${greatest_decrease[1]:,})", file=open(txt_path, "a"))