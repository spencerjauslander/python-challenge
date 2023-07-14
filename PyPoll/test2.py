import os
import csv

poll_csv = os.path.join('resources', 'election_data.csv')
results_csv = os.path.join( "analysis", "testresults2.txt")
Candidateinfo = {}
totalvotes = 0

def checkname(name):
    for candidatename in Candidateinfo:
        if name == candidatename:
            Candidateinfo[name] += 1
            return      
    Candidateinfo[name] = 1

def printcandidates():
    for i in Candidateinfo:
        print(f'{i}: {round((Candidateinfo[i]/totalvotes)*100,3)}% ({Candidateinfo[i]})')

def findwinner():
    global winner
    global winnername
    winner = 0
    winnername = ""
    for i in Candidateinfo:
        if Candidateinfo[i] > winner:
            winner = Candidateinfo[i]
            winnername = i
    return(winnername)      

def writecandidate():
    for i in Candidateinfo:
        resultsvwriter.writerow([f'{i}: {round((Candidateinfo[i]/totalvotes)*100,3)}% ({Candidateinfo[i]})'])

print('Election Results')
print('----------------------------')


with open(poll_csv, 'r', encoding='UTF-8') as election1: 
    electionreader1 = csv.reader(election1, delimiter= ",")
    next(electionreader1)
    for row in electionreader1:
        totalvotes += 1
with open(poll_csv, 'r', encoding='UTF-8') as election2: 
    electionreader2 = csv.reader(election2, delimiter= ",")
    # https://stackoverflow.com/questions/3392397/python-how-do-i-always-start-from-the-second-row-in-csv code credit
    # skips the header of csv file
    next(electionreader2)
    for vote in electionreader2:
        checkname(str(vote[2]))

print(f'Total votes: {totalvotes}')
print('----------------------------')
printcandidates()
print('----------------------------')
print(f'Winner: {findwinner()}')
print('----------------------------')    

with open(results_csv, 'w') as results:
    resultsvwriter = csv.writer(results, delimiter=',')
    resultsvwriter.writerow(['Election Results'])
    resultsvwriter.writerow(['----------------------------'])
    resultsvwriter.writerow([f'Total votes: {totalvotes}'])
    resultsvwriter.writerow(['----------------------------'])
    writecandidate()
    resultsvwriter.writerow(['----------------------------'])
    resultsvwriter.writerow([f'Winner: {winnername}'])    
    resultsvwriter.writerow(['----------------------------'])