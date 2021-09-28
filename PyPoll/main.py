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
    print(total_vote_count)
    print(votes_by_candidates)



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