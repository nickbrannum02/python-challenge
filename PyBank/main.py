import os
import csv

#set constant values
CSVPATH = os.path.join("Resources", "budget_data.csv")
OUTPUTPATH = os.path.join("analysis", "Results.txt")
PROFIT_IDX = 1
MONTH_IDX = 0

# initialize variables
month_count = 0
Total = 0
avgChange = 0
totChange = 0
current_change = 0
previous_profit = None
GrIncrease = 0
GrDecrease = 0
GrMonthInc = ""
GrMonthDec = ""


#open CSV file
with open(CSVPATH, encoding="utf8") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    # skip header row
    next(csvreader)
    
       
    for row in csvreader:
        # count number of months, store current profit, and add to the total
        month_count += 1
        current_profit = int(row[PROFIT_IDX])
        Total += current_profit
        
        # calculate the total change in profit
        if previous_profit is not None:
            current_change = current_profit - previous_profit
        previous_profit = current_profit    # prepare for the next month 
        totChange += current_change
        
        #calculate the greatest change increase and decrease 
        if current_change > GrIncrease:
            GrIncrease = current_change
            GrMonthInc = row[MONTH_IDX]
        elif current_change < GrDecrease:
            GrDecrease = current_change
            GrMonthDec = row[MONTH_IDX]
        
# calculate average change      
avgChange = round(totChange / (month_count - 1), 2)

#print results
result = (
    "Financial Analysys\n"
    "----------------------------------\n"
    f"Number of months: {month_count}\n"
    f'Total: ${Total}\n'
    f'Average Change: ${avgChange}\n'
    f'Greatest Increase in Profits: {GrMonthInc} (${GrIncrease}\n'
    f'Greatest Decrease in Profits: {GrMonthDec} (${GrDecrease})'
)
print(result)


# write to text file
with open(OUTPUTPATH, "w") as outputFile:
    outputFile.write(result)
    