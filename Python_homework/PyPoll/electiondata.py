#import dependencies

import os                               

import csv                              



# generate and return a separater line

def sep_line_gen(char, count):

    seperator_line = str(char) * count

    return seperator_line



# Function receives dictionary and displays results to stdout

def displayoutput(candidates):

 # Prints out the separator line and repeats
    print(sep_line_gen('-', 25))          


    # Find  total votes by adding values in dictionary

    totalvotes = sum(candidates.values())



    #  total votes output

    print(f"Total Votes: {totalvotes}")



    print(sep_line_gen('-', 25))



    # loop through key-value pairs in dictionary

    for candidate, votes in candidates.items():



     # Calculates percentage of votes for each candidate

        candidate_percent = round(((votes / totalvotes) * 100), 1)



     # Displays summary line for each candidate

        print(candidate + ": " + str(candidate_percent) + '% (' + str(votes) + ')')



    print(sep_line_gen('-', 25))



    # Finds winner by finding max value in dictionary

    winner = max(candidates, key=lambda key: candidates[key])


#Displaying the winner
    print(f"Winner: {winner}")      



    print(sep_line_gen('-', 25))


  # Displays newline to separate results
    print('\n')                      



# Function receives dictionary and writes results to output file

def writeoutput(cadidates):


#outputting into a text file
    outfile = 'output.txt'          


    # Opens output file for write in append mode

    with open(outfile, 'a') as file_object:


        # Writes separator line, repeats

        file_object.write(sep_line_gen('-', 25) + '\n')



        # Calculating total votes by summing values in dictionary

        totalvotes = sum(candidates.values())



        # Writing total votes to output file

        file_object.write("Total Votes: " + str(totalvotes) + '\n')



        file_object.write(sep_line_gen('-', 25) + '\n')



        # Iterates through key-value pairs in dictionary

        for candidate, votes in candidates.items():



            # Calculates percentage of votes for each candidate

            candidate_percent = round(((votes / totalvotes) * 100), 1)



            # Writes a summary line for each candidate to output file

            file_object.write(candidate + ": " + str(candidate_percent) + '% (' + str(votes) + ')' + '\n')



        file_object.write(sep_line_gen('-', 25) + '\n')



        # Finds winner by finding max value in dictionary

        winner = max(candidates, key=lambda key: candidates[key])



        # Writes winner to output file

        file_object.write("Winner: " + winner + '\n')



        file_object.write(sep_line_gen('-', 25) + '\n')


#displays newline to separate results
        file_object.write('\n')         



# Defines import file list

files = ['election_data_2.csv','election_data_1.csv']

#loop through candidates

for filename in files:                  



    candidates = {}                     # Initializes empty dictionary



    # Specifies import path and file

    csv_in = os.path.join(".", "raw_data", filename)



    # Opens and reads csv

    with open(csv_in, newline="") as csvfile:

        csvreader = csv.reader(csvfile, delimiter=",")



        next(csvreader)                 # skips header row



        # Iterates through each row in csv

        for row in csvreader:



            # if candidate not in dict, adds key and initializes value

            if row[2] not in candidates:

                candidates[row[2]] = 0



            candidates[row[2]] += 1     # increments dictionary value



    displayoutput(candidates)           # Calls function, passes dictionary



    writeoutput(candidates)             # Calls function, passes dictionary