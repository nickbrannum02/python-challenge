import os
import csv

CSVPATH = os.path.join("Resources", "election_data.csv")
OUTPUTPATH = os.path.join("analysis", "result.txt")
tot_votes = 0
cand1 = "Charles Casper Stockham"
cand1_count = 0
cand2 = "Diana DeGette"
cand2_count = 0
cand3 = "Raymon Anthony Doane"
cand3_count = 0


# open file
with open(CSVPATH, encoding="utf8") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)
    
    # Find values for total votes and votes for each candidate
    for row in csvreader:
        tot_votes += 1
        current_ballot = row[2]
        
        # count ballots for each candidate
        if current_ballot == cand1:
            cand1_count += 1
        elif current_ballot == cand2:
            cand2_count += 1 
        elif current_ballot == cand3:
            cand3_count += 1 
            
            
            
            
#calculate the winner of the election            
if cand1_count > cand2_count and cand3_count:
    winner = cand1   
if cand2_count > cand1_count and cand3_count:
    winner = cand2  
if cand3_count > cand2_count and cand1_count:
    winner = cand1           


# show the number of votes as a percentage            
cand1_pct = round((cand1_count / tot_votes) * 100, 3)
cand2_pct = round((cand2_count / tot_votes) * 100, 3)
cand3_pct = round((cand3_count / tot_votes) * 100, 3)

# Print Results            
result = (
    "Election Results\n"
    "-----------------------------\n"
    f"Total Votes: {tot_votes}\n"    
    "-----------------------------\n"
    f"{cand1}: {cand1_pct}% ({cand1_count})\n"
    f"{cand2}: {cand2_pct}% ({cand2_count})\n"
    f"{cand3}: {cand3_pct}% ({cand3_count})\n"
    "-----------------------------\n"
    f"Winner: {winner}\n"
    "-----------------------------\n"   
)
print(result)

# write results to a text file
with open(OUTPUTPATH, "w") as outputFile:
    outputFile.write(result)