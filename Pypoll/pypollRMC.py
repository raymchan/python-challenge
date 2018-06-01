# """ In this challenge, you are tasked with helping a small, rural town modernize its vote-counting process. (Up until now, Uncle Cleetus had been trustfully tallying them one-by-one, but unfortunately, his concentration isn't what it used to be.)

# You will be given two sets of poll data (`election_data_1.csv` and `election_data_2.csv`). Each dataset is composed of three columns: `Voter ID`, `County`, and `Candidate`. Your task is to create a Python script that analyzes the votes and calculates each of the following:

# * The total number of votes cast

# * A complete list of candidates who received votes

# * The percentage of votes each candidate won

# * The total number of votes each candidate won

# * The winner of the election based on popular vote.

# As an example, your analysis should look similar to the one below:

# ```
# Election Results
# -------------------------
# Total Votes: 620100
# -------------------------
# Rogers: 36.0% (223236)
# Gomez: 54.0% (334854)
# Brentwood: 4.0% (24804)
# Higgins: 6.0% (37206)
# -------------------------
# Winner: Gomez
# -------------------------
# ```

# Your final script must be able to handle any such similarly-structured dataset in the future (i.e you have zero intentions of living in this hillbilly town -- 
#so your script needs to work without massive re-writes). In addition, your final script should both print the analysis to the terminal and export a text file with the results. """



#PyPoll Code by Raymond M. Chan

import csv

#get an input of the csv file
text = input("After placing CSV file in the raw_data folder, please input name of file (including .csv for example election_data_1.csv):  ")
csvpath = "raw_data/" + text

#declare variables
vid = []
county = []
candidate = []

#iterate through the csv file
with open(csvpath, newline='') as vdata:
    read = csv.reader(vdata, delimiter=',')
    next(read)
    for column in read:
        vid.append(column[0])
        county.append(column[1])
        candidate.append(column[2])

#get total votes, unique candidates, calculate winner    
totvotes = len(vid)
totcandidates = list(set(candidate))
win = max(set(candidate),key=candidate.count)

#Printing to terminal
print("```")
print("Election Results")
print("-------------------------")
print(f"Total Votes: {totvotes}")
print("-------------------------")
for x in range(len(totcandidates)):
    name = totcandidates[x]
    pvotes = (candidate.count(totcandidates[x]) * 100) / totvotes
    VE = candidate.count(totcandidates[x])
    print(f"{name}: {pvotes}% ({VE})")
print("-------------------------")
print(f"Winner: {win}")
print("-------------------------")
print("```")


#Creating Txt file output
with open("output.txt", 'w') as textfile:
    print("```", file=textfile)
    print("Election Results", file=textfile)
    print("-------------------------",file=textfile)
    print(f"Total Votes: {totvotes}",file=textfile)
    print("-------------------------",file=textfile)
    for x in range(len(totcandidates)):
        name = totcandidates[x]
        pvotes = (candidate.count(totcandidates[x]) * 100) / totvotes
        VE = (candidate.count(totcandidates[x]))
        print(f"{name}: {pvotes}% ({VE})", file=textfile)
    print("-------------------------",file=textfile)
    print(f"Winner: {win}",file=textfile)
    print("-------------------------",file=textfile)
    print("```",file=textfile)