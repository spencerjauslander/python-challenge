import os
import csv

poll_csv = os.path.join('resources', 'election_data.csv')
results_csv = os.path.join( "analysis", "results.txt")

#function that checks the name against the candidateinfo dictionary:
#1.add vote to a recognized name then return back to the original for loop or 
#2.add a new name key and one vote to dictionary if there is no match
def checkname(name):
    for candidatename in Candidateinfo:
        if name == candidatename:
            Candidateinfo[name] += 1
            return      
    Candidateinfo[name] = 1

#initializing the dictionary and total votes
#the candidate name will be the key and the votes will be the content
Candidateinfo = {}
totalvotes = 0
        
#Reader that checks each name using the checkname function
#Also find the total amount of votes
with open(poll_csv, 'r', encoding='UTF-8') as election2: 
    electionreader2 = csv.reader(election2, delimiter= ",")
    storeheader = next(electionreader2)
    for vote in electionreader2:
        checkname(vote[2])
        totalvotes += 1

#finds the candidate with the most votes
winner = 0
winnername = ""
for i in Candidateinfo:
    if Candidateinfo[i] > winner:
        winner = Candidateinfo[i]
        winnername = i      

#print messages for the terminal
print('Election Results')
print('----------------------------')
print(f'Total votes: {totalvotes}')
print('----------------------------')
#for loop to print each candidate in the dictionary
for i in Candidateinfo:
        print(f'{i}: {round((Candidateinfo[i]/totalvotes)*100,3)}% ({Candidateinfo[i]})')  
print('----------------------------')
print(f'Winner: {winnername}')
print('----------------------------')

#writing the text file
with open(results_csv, 'w') as results:
    resultsvwriter = csv.writer(results, delimiter=',')
    resultsvwriter.writerow(['Election Results'])
    resultsvwriter.writerow(['----------------------------'])
    resultsvwriter.writerow([f'Total votes: {totalvotes}'])
    resultsvwriter.writerow(['----------------------------'])
    #for loop for write each candidate into the text file
    for i in Candidateinfo:
        resultsvwriter.writerow([f'{i}: {round((Candidateinfo[i]/totalvotes)*100,3)}% ({Candidateinfo[i]})'])
    resultsvwriter.writerow(['----------------------------'])
    resultsvwriter.writerow([f'Winner: {winnername}'])    
    resultsvwriter.writerow(['----------------------------'])