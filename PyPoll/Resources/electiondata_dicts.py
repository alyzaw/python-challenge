# -*- coding: utf-8 -*-
import os
import csv

electionfile = os.path.join("..", "Resources", "election_data.csv")

with open(electionfile) as election_data:
    election_reader = csv.reader(election_data, delimiter=",")
    
    csvheader = next(election_reader)
 
    allvotes = []
    
    candidates = []
    votes = []
    percent = []
    
    candidatecount1 = 0
    candidatecount2 = 0
    candidatecount3 = 0
    candidatecount4 = 0
    
    for names in election_reader:
        allvotes.append(names[2])
        total_votes = len(votes)
        
        if names[2] not in candidates:
            candidates.append(names[2])
 
        if names[2] == candidates[0]:
            candidatecount1 = candidatecount1 + 1
        
        elif names[2] == candidates[1]:
            candidatecount2 = candidatecount2 + 1
            
        elif names[2] == candidates[2]:
            candidatecount3 = candidatecount3 + 1
            
        elif names[2] == candidates[3]:
            candidatecount4 = candidatecount4 + 1
            
    votes.append(candidatecount1)
    votes.append(candidatecount2)
    votes.append(candidatecount3)
    votes.append(candidatecount4)
    
    candidate1 = candidates[0]
    candidate2 = candidates[1]
    candidate3 = candidates[2]
    candidate4 = candidates[3]
    
    if min(votes) == votes[0]:
            winner = candidate1
            
    elif min(votes) == votes[1]:
            winner = candidate2
            
    elif min(votes) == votes[3]:
            winner = candidate3
            
    elif min(votes) == votes[4]:
            winner = candidate4
            
    for cand_votes in votes:
        percent.append(round((candidatecount1/total_votes)*100,3))
      

    
outputfile =  os.path.join("..", "Resources", "election_data.txt")

with open(outputfile, "w", newline="") as election_txt:
    
    election_txt.write("Election Results")
    election_txt.write("--------------------------")
    election_txt.write(f'Total Votes: {total_votes}')
    election_txt.write("--------------------------")
    election_txt.write(f'{candidate1}: {candidateperc1} ({candidatecount1})')
    election_txt.write(f'{candidate2}: {candidateperc2} ({candidatecount2})')
    election_txt.write(f'{candidate3}: {candidateperc3} ({candidatecount3})')
    election_txt.write(f'{candidate4}: {candidateperc4} ({candidatecount4})')
    election_txt.write("--------------------------")
    election_txt.write(f'Winner: {winner}')
    election_txt.write("--------------------------")
    
print("Election Results")
print("--------------------------")
print(f'Total Votes: {total_votes}')
print("--------------------------")
print(f'{candidate1}: {candidateperc1} ({candidatecount1})')
print(f'{candidate2}: {candidateperc2} ({candidatecount2})')
print(f'{candidate3}: {candidateperc3} ({candidatecount3})')
print(f'{candidate4}: {candidateperc4} ({candidatecount4})')
print("--------------------------")
print(f'Winner: {winner}')
print("--------------------------")



    
    
    

        
  
        
