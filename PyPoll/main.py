import csv
import os

input_path = os.path.join("Resources", "election_data.csv")
output_path = os.path.join("analysis", "election_results.txt")

total_votes = 0
candidate_votes = {}

with open(input_path, newline="") as csvfile:
    csvreader = csv.reader(csvfile)
    header = next(csvreader)

    for row in csvreader:
        candidate = row[2]
        total_votes += 1
        if candidate not in candidate_votes:
            candidate_votes[candidate] = 0
        candidate_votes[candidate] += 1

winner = max(candidate_votes, key=candidate_votes.get)

output = [
    "Election Results",
    "-------------------------",
    f"Total Votes: {total_votes}",
    "-------------------------"
]

for candidate, votes in candidate_votes.items():
    percent = (votes / total_votes) * 100
    output.append(f"{candidate}: {percent:.3f}% ({votes})")

output += [
    "-------------------------",
    f"Winner: {winner}",
    "-------------------------"
]

final_output = "\n".join(output)
print(final_output)

with open(output_path, "w") as txtfile:
    txtfile.write(final_output)
