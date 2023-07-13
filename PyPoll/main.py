import os
import csv

poll_csv = os.path.join('resources', 'election_data.csv')
results_csv = os.path.join( "analysis", "results.txt")
name1 = 'Charles Casper Stockham'
name2 = "Diana DeGette"
name3 = 'Raymon Anthony Doane'
vote1 = 0
vote2 = 0
vote3 = 0
totalvotes = 0
winner = ""

print('Election Results')
print('----------------------------')

with open(poll_csv, 'r', encoding='UTF-8') as election1: 
    electionreader1 = csv.reader(election1, delimiter= ",")
    next(electionreader1)
    for row in electionreader1:
        totalvotes += 1
print(f'Total votes: {totalvotes}')
print('----------------------------')
with open(poll_csv, 'r', encoding='UTF-8') as election2: 
    electionreader2 = csv.reader(election2, delimiter= ",")
    # https://stackoverflow.com/questions/3392397/python-how-do-i-always-start-from-the-second-row-in-csv code credit
    # skips the header of csv file
    next(electionreader2)
    for vote in electionreader2:
        if vote[2] == name1:
                vote1 += 1
        elif vote[2] == name2:
                vote2 += 1
        elif vote[2] == name3:
            vote3 += 1
print (f'{name1}: {round((vote1/totalvotes)*100,3)}% ({vote1})')
print (f'{name2}: {round((vote2/totalvotes)*100,3)}% ({vote2})')
print (f'{name3}: {round((vote3/totalvotes)*100,3)}% ({vote3})')
if (vote1 > vote2):
    if (vote1 > vote3):
        winner = name1
    else:
         winner = name3
elif (vote2 > vote3):
        winner = name2
else:
     winner = name3       
print('----------------------------')
print(f'Winner: {winner}')    
print('----------------------------')

with open(results_csv, 'w') as results:
    resultsvwriter = csv.writer(results, delimiter=',')
    resultsvwriter.writerow(['Election Results'])
    resultsvwriter.writerow(['----------------------------'])
    resultsvwriter.writerow([f'Total votes: {totalvotes}'])
    resultsvwriter.writerow(['----------------------------'])
    resultsvwriter.writerow([f'{name1}: {round((vote1/totalvotes)*100,3)}% ({vote1})'])
    resultsvwriter.writerow([f'{name2}: {round((vote2/totalvotes)*100,3)}% ({vote2})'])
    resultsvwriter.writerow([f'{name3}: {round((vote3/totalvotes)*100,3)}% ({vote3})'])
    resultsvwriter.writerow(['----------------------------'])
    resultsvwriter.writerow([f'Winner: {winner}'])    
    resultsvwriter.writerow(['----------------------------'])