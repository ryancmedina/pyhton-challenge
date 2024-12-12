# -*- coding: UTF-8 -*-
"""PyPoll Homework Starter File."""

# Import necessary modules
import csv
import os

# Files to load and output (update with correct file paths)

# note: files are only reading in for me while i have the root folder open in explorer, please keep that in mind if file does not read correctly
file_to_load = os.path.join("PyPoll", "Resources", "election_data.csv")  # Input file path
file_to_output = os.path.join("PyPoll", "analysis", "election_analysis.txt")  # Output file path

# Initialize variables to track the election data
total_votes = 0  # Track the total number of votes cast

# Define lists and dictionaries to track candidate names and vote counts
candidate = ""
candidates = {}

# Winning Candidate and Winning Count Tracker
winner = ["", 0]

# Open the CSV file and process it
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Skip the header row
    header = next(reader)

    # Loop through each row of the dataset and process it
    for row in reader:

        # Increment the total vote count for each row
        total_votes += 1

        # Get the candidate's name from the row
        candidate = row[2]

        # If the candidate is not already in the candidate list, add them
        if candidate not in candidates:
            candidates[candidate] = 0

        # Add a vote to the candidate's count
        candidates[candidate] += 1

# Open a text file to save the output
with open(file_to_output, "w") as txt_file:

    writer = csv.writer(txt_file)

    # Print the total vote count (to terminal)
    print("Election Results")
    print("-------------------------")
    print(f"Total Votes: {total_votes}")
    print("-------------------------")
    # Write the total vote count to the text file
    writer.writerow([f"Total Votes: {total_votes}"])

    # Loop through the candidates to determine vote percentages and identify the winner
    for i in candidates:

        # Get the vote count and calculate the percentage
        print(f"{i}: {(candidates[i] / total_votes * 100):.3f}% ({candidates[i]})")

        # Update the winning candidate if this one has more votes
        if candidates[i] > winner[1]:
            winner[0] = i
            winner[1] = candidates[i]

        # Print and save each candidate's vote count and percentage
        writer.writerow([f"{i}: {(candidates[i] / total_votes * 100):.3f}% ({candidates[i]})"])

    # Generate and print the winning candidate summary
    print("-------------------------")
    print(f"Winner: {winner[0]}")
    print("-------------------------")

    # Save the winning candidate summary to the text file
    writer.writerow([f"Winner: {winner[0]}"])