# -*- coding: utf-8 -*-
import os
import csv

budgetfile = os.path.join("..", "Resources", "budget_data.csv")

with open(budgetfile) as budget_data:
    budget_reader = csv.reader(budget_data, delimiter=",")
    
    csvheader = next(budget_reader)
 
    monthlist = []
    profitlist = []
    profit_change = []
    
    for rows in budget_reader:
        monthlist.append(rows[0])
        total_months = len(monthlist)
        
        profitlist.append(int(rows[1]))
        total_profit = sum(profitlist)
      
    for profits in profitlist[1:]:
        profit_change.append(profits - profitlist[profitlist.index(profits)-1])
    
    avg_change = round(sum(profit_change)/len(profit_change),2)
    max_change = max(profit_change)
    min_change = min(profit_change)
    max_chg_mth = (profit_change.index(max_change)+1)
    min_chg_mth = (profit_change.index(min_change)+1)
    max_month = monthlist[max_chg_mth]
    min_month = monthlist[min_chg_mth]
        
outputfile =  os.path.join("..", "Resources", "budget_data.txt")

with open(outputfile, "w", newline="") as budget_txt:
    
    budget_txt.write("Financial Analysis\n")
    budget_txt.write("--------------------------\n")
    budget_txt.write(f'Total: {total_profit}\n')
    budget_txt.write(f'Total months: {total_months}\n')
    budget_txt.write(f'Average Change: ${avg_change}\n')
    budget_txt.write(f'"Greatest Increase in Profits: {max_month} (${max_change}\n')
    budget_txt.write(f'Greatest Decrease in Profits: {min_month} (${min_change})\n')
    budget_txt.write("--------------------------\n")
    
print("Financial Analysis")
print("--------------------------")
print(f'Total months: {total_months}') 
print(f'Total: ${total_profit}')
print(f'Average Change: ${avg_change}')
print(f'Greatest Increase in Profits: {max_month} (${max_change})')
print(f'Greatest Decrease in Profits: {min_month} (${min_change})')
print("--------------------------")



    
    
    

        
  
        
