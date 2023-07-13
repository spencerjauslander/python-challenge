import os
import csv

poll_csv = os.path.join('resources', 'election_data.csv')
results_csv = os.path.join( "analysis", "testresults.txt")
Candidateinfo =[]
totalvotes = 0

def newname(newname):
    Candidateinfo.append(newname)
    Candidateinfo.append(1)

def addvote(index):
    Candidateinfo[index+1] += 1

def checkname(name):
    for i in range(0,len(Candidateinfo)):
        if name == Candidateinfo[i]:
            addvote(i)
            return      
    newname(name)

def printcandidates():
    for i in range(0,len(Candidateinfo),2):
        print(f'{Candidateinfo[i]}: {round((Candidateinfo[i+1]/totalvotes)*100,3)}% {Candidateinfo[i+1]}')

def findwinner():
    global winner
    global winnername
    winner = 0
    winnername = ""
    for i in range(1,len(Candidateinfo),2):
        if Candidateinfo[i] > winner:
            winner = Candidateinfo[i]
            winnername = Candidateinfo[i-1]
    return(winnername)      

def writecandidate():
    for i in range(0,len(Candidateinfo),2):
        resultsvwriter.writerow([f'{Candidateinfo[i]}: {round((Candidateinfo[i+1]/totalvotes)*100,3)}% ({Candidateinfo[i+1]})'])

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