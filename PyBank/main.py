import os
import csv

budget_csv = os.path.join('resources', 'budget_data.csv')
results_csv = os.path.join( "analysis", "results.txt")
Total_Months = 0
Total = 0
Sum_Change = 0
Greatest_IN = 0
Greatest_DE = 0
IN_row = 0
DE_row = 0
prerow = 0

with open(budget_csv, 'r', encoding='UTF-8') as budget:
    budgetreader = csv.reader(budget, delimiter= ",")
    next(budgetreader)
    for row in budgetreader:
        #counting each month
        Total_Months += 1
        #running total of the profit/losses
        Total += int(row[1])
        #check to see if this is the first month or entry. if so, just store the row value for the change calculation
        if Total_Months == 1:
            prerow = int(row[1])
        #calculate the change by taking the current profit/loss and subtracting it from last month's profit/loss
        #add that change to a running total
        else:
            Current_Change = int(row[1]) - prerow
            Sum_Change += Current_Change
            #If change variable is the greatest increase so far, retrieve the date and set change as the max
            #Same logic applies to greatest decrease so far
            if Current_Change > Greatest_IN:
                IN_row = row[0]
                Greatest_IN = Current_Change
            elif Current_Change < Greatest_DE:
                DE_row = row[0]
                Greatest_DE = Current_Change
        #set the current row as the previous row for the next loop calculation
        prerow = int(row[1])
    #aftering exiting the loop, calcuate the average change with the final totals
    Average_Change = round(Sum_Change / (Total_Months-1), 2)
with open(results_csv, 'w') as results:
    #printing results in terminal
    print('Financial Analysis')
    print('----------------------------')
    print('Total Months: ' +  str(Total_Months))
    print('Total: $' + str(Total))
    print('Average Change: $' + str(Average_Change))
    print('Greatest Increase in Profits: ' + str(IN_row) + ' $(' + str(Greatest_IN) + ')')
    print('Greatest Decrease in Profits: ' + str(DE_row) + ' $(' + str(Greatest_DE) + ')')
    #writing results in text file
    resultsvwriter = csv.writer(results, delimiter=',')
    resultsvwriter.writerow(['Financial Analysis'])
    resultsvwriter.writerow(['----------------------------'])
    resultsvwriter.writerow(['Total Months: ' +  str(Total_Months)])
    resultsvwriter.writerow(['Total: $' + str(Total)])
    resultsvwriter.writerow(['Average Change: $' + str(Average_Change)])
    resultsvwriter.writerow(['Greatest Increase in Profits: ' + str(IN_row) + ' $(' + str(Greatest_IN) + ')'])
    resultsvwriter.writerow(['Greatest Decrease in Profits: ' + str(DE_row) + ' $(' + str(Greatest_DE) + ')'])
