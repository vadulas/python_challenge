#import statments
import csv
import os

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Function reads the election_data.csv file and anlyzes the votes cast to find the winner 
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
def analyze_poll_data():
    #Create the source file path
    source_file_path = os.path.join("Resources", "election_data.csv")
    total_vote_count = 0 

    try:
        #A dictionary to store the candidate and the count of votes
        votes_by_candidates = {}
        #Open the file to read
        with open(source_file_path, "r") as election_data_file:
            #create a CSV Reader object
            csv_reader = csv.reader(election_data_file, delimiter=",")

            #skipt the header row
            next(csv_reader)

            #Read through the file to capture the voter information
            for row in csv_reader:
                #Get the candidate name
                candidate = row[2]

                #update the vote count for the candidate
                votes_by_candidates = update_vote_count(candidate, votes_by_candidates)

                #update the total votes cast
                total_vote_count = total_vote_count + 1


    except FileNotFoundError:
        print(f"ERROR:File {source_file_path} was not found")

    #Finally print the report
    print_report(total_vote_count, votes_by_candidates)


"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Function to print the final report
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
def print_report(total_vote_count, votes_by_candidates):

    #get the list of votes by candidates from the dictionary
    votes_list = list(votes_by_candidates.values())
    candidates_list = list(votes_by_candidates.keys())

    #determine the index of the winner in the election
    winner_index  = votes_list.index(max(votes_list))
    winner  = candidates_list[winner_index]


    #Format report output string
    seperator = "-" * 30
    new_line_character = "\n"
    output_header = f"Election Results{new_line_character}{seperator}{new_line_character} Total Votes: {total_vote_count}{new_line_character}{seperator}{new_line_character}"
    output_footer = f"{seperator}{new_line_character}Winner: {winner}{new_line_character}{seperator}"
    final_report = output_header

    for candidate in votes_by_candidates:
        vote_count = votes_by_candidates[candidate]

        #calculate percentage of vote for teh candidate
        percentage_vote_count = round((vote_count/total_vote_count) * 100, 2)

        #format candidate line
        output_candidate_line = f"{candidate}: {percentage_vote_count}% ({vote_count}){new_line_character}"
        final_report = final_report + output_candidate_line

    final_report = final_report + output_footer

    #print to the console
    print(final_report)

    #print to the output file
    output_file  = open("Analysis/analysis.txt", "w")
    output_file.write(final_report)
    output_file.close()


"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Function to update the vote count for the candidates
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
def update_vote_count(candidate, candidate_dict):

    vote_count = 1 #One vote for teh candidate

    if candidate in candidate_dict:  #If a candiate is already in the dictionaary, add one vote to his/her count
        vote_count = candidate_dict[candidate] + 1
        candidate_dict.update({candidate: vote_count})
    else: #Record the first vote for the candidate
        candidate_dict[candidate] = vote_count

    return candidate_dict


"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Main function call to analyze votes
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
analyze_poll_data()