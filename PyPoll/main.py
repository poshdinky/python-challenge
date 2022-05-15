# Add dependencies
import csv
import os

# Create path to Election Results 
file_to_load = os.path.join(os.path.dirname(os.path.abspath(__file__)),"Resources", "election_data.csv")

# Create a filename variable to a direct path to a file
file_to_save = os.path.join("AnalyseResultPyPoll.txt")

# Create variables for voting 
total_votes = 0
candidate_options = []
candidate_votes = {}
county_options = []
county_votes = {}

# Create variables for winning candidate
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Create variables for winning county
winning_county = ""
winning_county_count = 0

# Open Election Results
with open(file_to_load, 'r') as election_data:

    # Read Election Results 
    file_reader = csv.reader(election_data)

    # Print the header row.
    headers = next(file_reader)

    # Print each row in the CSV file.
    for row in file_reader:
        total_votes += 1
        
        # Print candidate name from each row
        candidate_name = row[2]
       
        if candidate_name not in candidate_options:
            
            # Add unique candidate name to candidate list
            candidate_options.append(candidate_name)
            
            # Track votes for each candidate
            candidate_votes[candidate_name] = 0
        candidate_votes[candidate_name] += 1

        # Print county name from each row
        county_name = row[1]

        if county_name not in county_options:

            # Add unique county name to county list
            county_options.append(county_name) 

            # Track votes for each county
            county_votes[county_name] = 0
        county_votes[county_name] += 1

# Save results to text file
with open(file_to_save, 'w') as analyse_results_file:

    election_results = (
        f"Election Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n\n"
        f"County Votes:\n")

    print(election_results, end="")   
    
    # Save the final vote count to the text file.
    analyse_results_file.write(election_results)

    
    #Determine the percentage of votes for each county
    #Iterate through the county list
    for county_name in county_votes:
        
        # Retrieve vote count of a candidate
        votes_1 = county_votes[county_name]

        # Calculate percentage of votes
        vote_percentage_1 = float(votes_1) / float(total_votes) * 100

        # Write the county name and percentage of votes
        county_results = (f"{county_name}: {vote_percentage_1:.1f}% ({votes_1:,})\n")
        print(county_results)
        analyse_results_file.write(county_results)

    # Determine the percentage of votes for each candidate by looping through the counts.
    # Iterate through the candidate list.
    for candidate_name in candidate_votes:
        
        # Retrieve vote count of a candidate.
        votes_2 = candidate_votes[candidate_name]
        
        # Calculate the percentage of votes.
        vote_percentage_2 = float(votes_2) / float(total_votes) * 100

        # Write the candidate name and percentage of votes.
        candidate_results = (f"{candidate_name}: {vote_percentage_2:.1f}% ({votes_2:,})\n")
        print(candidate_results)
        analyse_results_file.write(candidate_results)

        # Determine winning candidate
        # Determine if votes is greater than winning count
        if (votes_2 > winning_count) and (vote_percentage_2 > winning_percentage):
            
            # If True, set winning count = votes, winning percentage = vote percentage,
            # and set winning candidate = candidate name
            winning_count = votes_2
            winning_percentage = vote_percentage_2
            winning_candidate = candidate_name

    # Write winning candidate 
    winning_candidate_summary = ( 
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"-------------------------\n")
    print(winning_candidate_summary)
    analyse_results_file.write(winning_candidate_summary)