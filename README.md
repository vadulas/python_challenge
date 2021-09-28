# python_homework

Script to analyze the budget data. 

The script has 2 main functions:
    1. analyse_budget() - This is the heart of the script that opens the source file and reads all the vaues before calcualting the required statistics for reporting purposes
    2. printReport() - This function is responsible for printing the output to the console and also to the output file, following are the parameters required for this function:
        months_counter, 
        total_amount, 
        average_change, 
        greatest_increase_in_profit, 
        greatest_decrease_in_profit, 
        increase_month, 
        decrease_month


analyse_budget() is invoked once a the bottom of the script


Following is the sample output from the script:

Total Months: 86
Total: $38382578
Average Change: $ +7803.48
Greatest Increase in Profits: Feb-2012 ($1926159)
Greatest Decrease in Profits: Sep-2013 ($-2196167)



Script to analyze the poll data. 

The script has 2 main functions:
    1. analyse_poll_data() - This is the heart of the script that opens the source file and reads all the vaues before calcualting the required statistics for reporting purposes
    2. print_report() - This function is responsible for printing the output to the console and also to the output file, following are the parameters required for this function:
        total number ov votes
        a dictionary containing the total votes by candidates


analyse_poll_data() is invoked once a the bottom of the script


Following is the sample output from the script:

Election Results
------------------------------
 Total Votes: 3521001
------------------------------
Khan: 63.0% (2218231)
Correy: 20.0% (704200)
Li: 14.0% (492940)
O'Tooley: 3.0% (105630)
------------------------------
Winner: Khan
------------------------------
