
# Import statments
import os
import csv

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Function reads the budget_data.csv file and anlyzes the profit/loss over the years for each month
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
def analyze_budget():
    #Create the file path
    source_file_path = os.path.join("Resources", "budget_data.csv")

    #Variable declarations
    total_amount  = 0
    months_counter = 0
    greatest_increase_in_profit = 0
    greatest_decrease_in_profit = 0
    net_total_change = 0
    greatest_increase_month = ""
    greatest_decrease_month = ""

    #Open the file and create a CSV Reader Object
    with open(source_file_path, "r") as budget_data_file:

        csv_reader = csv.reader(budget_data_file, delimiter=",")
        
        #As the file contains a header, skip the first row
        next(csv_reader)

        previous_month_profit_loss_amount = 0
        
        
        #Loop through the data set for analysis
        for row in csv_reader:
            
            current_month  = row[0]
            #Get the Profit/Losses
            profit_loss_amount = int(row[1])
            
            #Calculate the net change for this current month
            net_change = profit_loss_amount - previous_month_profit_loss_amount
            
            #Add current month's net change to the total net change
            net_total_change = net_total_change + net_change

            # Determine the gretest increase and decrease in profit
            if (net_change > greatest_increase_in_profit):
                greatest_increase_in_profit = net_change
                greatest_increase_month = current_month
            elif (net_change < greatest_decrease_in_profit):
                greatest_decrease_in_profit = net_change
                greatest_decrease_month = current_month

            #Increment the month counter by 1
            months_counter = 1 + months_counter

            #Add the profit/loss to the total amount
            total_amount = total_amount + profit_loss_amount

            #FInally set the current month's profit amount to the previous month amount 
            previous_month_profit_loss_amount = profit_loss_amount
    
    #Calculate the average change
    average_change = net_total_change/months_counter

    #Print report
    printReport(months_counter, total_amount, average_change, greatest_increase_in_profit, greatest_decrease_in_profit, greatest_increase_month, greatest_decrease_month)


"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Function to print the final report
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
def printReport(months_counter, total_amount, average_change, greatest_increase_in_profit, greatest_decrease_in_profit, increase_month, decrease_month):

    #Format report output strings
    total_months = f"Total Months: {months_counter}"
    total_amount = f"Total: ${total_amount}"
    average_change = "Average Change: $ {:+.2f}".format(average_change)
    profit_increase = f"Greatest Increase in Profits: {increase_month} (${greatest_increase_in_profit})"
    profit_decrease = f"Greatest Decrease in Profits: {decrease_month} (${greatest_decrease_in_profit})"

    output_string  = "\n" + total_months + "\n" + total_amount + "\n" + average_change + "\n" + profit_increase + "\n" + profit_decrease

    #Print the final output to the console
    print(output_string)

    #Write to the output file
    output_file = open("Analysis/analysis.txt", "w")
    output_file.write(output_string)
    output_file.close()

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Main function call to analyze budget
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
analyze_budget()

