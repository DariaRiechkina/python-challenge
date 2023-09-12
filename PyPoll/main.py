import pandas as pd
import os


election = pd.read_csv("Resources/election_data.csv")
# find number of voices useing function len
votes = len(election["Ballot ID"])
print(votes)
# get list of canditades useind unique function
recieved = election["Candidate"].unique()
print(recieved)
# find number of voices which every candidate got useing value_counts
value_for_each = election["Candidate"].value_counts(ascending=False)
print(value_for_each)
# making dataframe
value_for_each1 = value_for_each.reset_index()
value_for_each1.columns = ["Candidate", "Number of voices"]
# use apply function to find the percentage
def to_percentage(number):
    return(number / value_for_each1["Number of voices"].sum()) * 100
value_for_each1["Percentage"] = round(value_for_each1["Number of voices"].apply(to_percentage), 3)
print(value_for_each1)
# find max and it's index of number of voices 
max_voice_i = value_for_each1["Number of voices"].idxmax()
# identify the name of winner
winner_candidate = value_for_each1.loc[max_voice_i, "Candidate"]
print(winner_candidate)
# results = 
# res = pd.DataFrame(results)
# write results in cvs file
path = "Analysis/Poll_Analysis.txt"
separator = "-------------------------\n"
if os.path.exists(path):
  os.remove(path)

file = open(path, 'a')
file.write('Election Results\n')
file.write(separator)
# "Hello, %s. You are %s." % (name, age)
file.write("Total Votes: %s\n" % (votes))
file.write(separator)
for ind in value_for_each1.index:
    file.write("%s: %s%% (%s)\n" % (value_for_each1['Candidate'][ind], value_for_each1['Percentage'][ind], value_for_each1['Number of voices'][ind]))
    # print(df['Name'][ind], df['Stream'][ind])
file.write(separator)
file.write("Winner: %s" % (winner_candidate))    
file.close()


# res.to_csv(path, sep='\t', index = False)
# print(res)
