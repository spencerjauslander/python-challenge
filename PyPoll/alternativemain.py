import os
import csv

#alternative solution to the pypoll using lists instead of dictionary
poll_csv = os.path.join('resources', 'election_data.csv')
results_csv = os.path.join( "analysis", "altresults.txt")

#function that checks the name against the candidateinfo list:
#1.add vote to a recognized name then return back to the original for loop or 
#2.add a new name and one vote to list if there is no match
def checkname(name):
    for i in range(0,len(Candidateinfo)):
        if name == Candidateinfo[i]:
            Candidateinfo[i+1] += 1
            return      
    Candidateinfo.append(name)
    Candidateinfo.append(1)

#candidate name goes first then their respective vote
#candidate names are in the odds indexes and the votes are in the evens indexes
#to find an unique candidate's votes, it's +1 index from the candidate's name
#to find just names or just votes, the for loops take 2 steps
Candidateinfo =[]
totalvotes = 0

#Reader that checks each name using the checkname function
#Also find the total amount of votes
with open(poll_csv, 'r', encoding='UTF-8') as election2: 
    electionreader2 = csv.reader(election2, delimiter= ",")
    next(electionreader2)
    for vote in electionreader2:
        checkname(vote[2])
        totalvotes += 1

#finds the candidate with the most votes
winner = 0
winnername = ""
for i in range(1,len(Candidateinfo),2):
    if Candidateinfo[i] > winner:
        winner = Candidateinfo[i]
        winnername = Candidateinfo[i-1]

#print messages for the terminal    
print('Election Results')
print('----------------------------')
print(f'Total votes: {totalvotes}')
print('----------------------------')
#for loop to print each candidate in the list
for i in range(0,len(Candidateinfo),2):
        print(f'{Candidateinfo[i]}: {round((Candidateinfo[i+1]/totalvotes)*100,3)}% ({Candidateinfo[i+1]})') 
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
    for i in range(0,len(Candidateinfo),2):
        resultsvwriter.writerow([f'{Candidateinfo[i]}: {round((Candidateinfo[i+1]/totalvotes)*100,3)}% ({Candidateinfo[i+1]})'])
    resultsvwriter.writerow(['----------------------------'])
    resultsvwriter.writerow([f'Winner: {winnername}'])    
    resultsvwriter.writerow(['----------------------------'])