
#import dependencies

import os
import csv

#Import the csvpath
csvpath = os.path.join('raw_data','budget_data_2.csv')

#Open the csv file 

with open(csvpath, 'r') as csvfile:
   csvreader = csv.reader(csvfile, delimiter=',')
   header = next(csvreader)

#create empty lists 

   list1=(csvreader)
   date_list = []
   revenue_list = []
   revenue_change = []

   #loop through list1 and append rows to list 

   for row in list1:
       date_list.append(row[0])
       revenue_list.append(float(row[1]))
       total_months = len(date_list)
       total_revenue = sum(revenue_list)
   
       #Loop through revenue list  to find revenue changes 
       
   for row in range(1,len(revenue_list)):
       revenue_change.append(revenue_list[row]-revenue_list[row-1])
       avg_rev_change = sum(revenue_change)/len(revenue_change)

       max_rev_change = max(revenue_change)
       min_rev_change = min(revenue_change)

       max_rev_change_date = str(date_list[revenue_change.index(max(revenue_change))])
       min_rev_change_date = str(date_list[revenue_change.index(min(revenue_change))])
       
   #Print results to the terminal 

print("Financial Analysis")
print("----------------------------")


print(f'Total Months: {total_months}')
print(f'Total Revenue:$ {total_revenue}')
print(f'Average Revenue Change: $ {(round(avg_rev_change))}')
print("Greatest Increase in Revenue:", max_rev_change_date,"($", max_rev_change,")")
print("Greatest Decrease in Revenue:", min_rev_change_date,"($", min_rev_change,")")

   #write the text files 

text_path = os.path.join('.','budget_data_2.txt')
with open(text_path, "w") as text_file:
   text_file.write("Financial Analysis")
   text_file.write("---------------------------------")
   text_file.write("Total Months: " + str(total_months))
   text_file.write("Total Revenue: $" + str(total_revenue))
   text_file.write("Average Revenue Change: +""$" + str(round(avg_rev_change)))
   text_file.write("Greatest Increase in Revenue: " + str(max_rev_change_date)+" $" + str(max_rev_change))
   text_file.write("Greatest Decrease in Revenue: " + str(min_rev_change_date)+" $" + str(min_rev_change))