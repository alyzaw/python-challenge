# -*- coding: utf-8 -*-
import os
import csv

electionfile = os.path.join("..", "Resources", "election_data.csv")

with open(electionfile) as election_data:
    election_reader = csv.reader(election_data, delimiter=",")
    
    csvheader = next(election_reader)
 
    candidates = []
   
    candidatecount1 = 0
    candidatecount2 = 0
    candidatecount3 = 0
    candidatecount4 = 0
    
    votes = []
    
    for names in election_reader:
        votes.append(names[2])
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
  
    candidate1 = candidates[0]
    candidate2 = candidates[1]
    candidate3 = candidates[2]
    candidate4 = candidates[3]
    
    all_votes = [candidatecount1,candidatecount2,candidatecount3,candidatecount4]
    if max(all_votes) == candidatecount1:
            winner = candidate1
    elif max(all_votes) == candidatecount2:
            winner = candidate2
            
    elif max(all_votes) == candidatecount3:
            winner = candidate3
            
    elif max(all_votes) == candidatecount4:
            winner = candidate4
      
    candidateperc1 = round((candidatecount1/total_votes)*100,3)
    candidateperc2 = round((candidatecount2/total_votes)*100,3)
    candidateperc3 = round((candidatecount3/total_votes)*100,3)
    candidateperc4 = round((candidatecount4/total_votes)*100,3)
    
outputfile =  os.path.join("..", "Resources", "election_data.txt")

with open(outputfile, "w", newline="") as election_txt:
    
    election_txt.write("Election Results\n")
    election_txt.write("--------------------------\n")
    election_txt.write(f'Total Votes: {total_votes}\n')
    election_txt.write("--------------------------\n")
    election_txt.write(f'{candidate1}: {candidateperc1} ({candidatecount1})\n')
    election_txt.write(f'{candidate2}: {candidateperc2} ({candidatecount2})\n')
    election_txt.write(f'{candidate3}: {candidateperc3} ({candidatecount3})\n')
    election_txt.write(f'{candidate4}: {candidateperc4} ({candidatecount4})\n')
    election_txt.write("--------------------------\n")
    election_txt.write(f'Winner: {winner}\n')
    election_txt.write("--------------------------\n")
    
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



    
    
    

        
  
        
