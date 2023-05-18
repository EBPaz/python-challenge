# make the import run on any system and use the csv reading module
import os
import csv

# read the CSV file and convert it
csvpath = os.path.join('C:\\Users\\evapa\\OneDrive\\Desktop\\Python\\python-challenge\\PyPoll\\Resources\election_data.csv')
textfile = os.path.join('C:\\Users\\evapa\\OneDrive\\Desktop\\Python\\python-challenge\\PyPoll\Analysis\\election_summary.txt')

#set values for the varaibles in the dataset
total_votes = 0
votes ={}
winning_count = 0
winning_candidate = ""

# Read the csv and convert it into a list of dictionaries
with open(csvpath) as vote_file:
    csvreader = csv.reader(vote_file)

    # Read the header row
    header = next(csvreader)

    # set up a loop to read each row and define it
    for row in csvreader:
        voter_id = int(row[0])
        county = str(row[1])
        candidate_name = str(row[2])

        # count the total number of votes
        total_votes += 1
    print(total_votes)
      
    if candidate_name in votes:
      votes[candidate_name] = votes[candidate_name]+1
    else:
      votes[candidate_name]=0

    print(votes)

       
    for row in votes:
        cand_votes = votes.get(row)
        cand_percentage = cand_votes / total_votes
        print(cand_percentage)

        if cand_votes > winning_count:
            winning_count = cand_votes
            winning_candidate = row
    print(winning_candidate, winning_count)

    
    
with open(textfile, 'w') as summary:
  summary.write(f'Election Results)\n'
               f'-------------------------\n'
                 f'Total Votes: {total_votes}\n'
                 f'-------------------------\n'
                 f'{candidate_name[0]}: {cand_percentage[0]:.3f} {cand_votes[0]}\n'
                f'{candidate_name[1]}: {cand_percentage[1]:.3f} {cand_votes[1]}\n'
                f'{candidate_name[2]}: {cand_percentage[2]:.3f} {cand_votes[2]}\n'
                 f'-------------------------\n'
                 f' Winner: {winning_candidate}\n'
                 f'-------------------------\n')
      