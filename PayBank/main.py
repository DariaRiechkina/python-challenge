import pandas as pd


budget = pd.read_csv("Resourses/budget_data.csv")
# to find amount of months use function len
months = len(budget["Date"])
print(months)
# to find total of profit/losses use function sum
total = budget["Profit/Losses"].sum()
print(total)
# create new column which contains differences between previos rows in profit/losses
budget["Profit/Losses Change"] = budget["Profit/Losses"].diff()
# find average changes in profit/losses
average = round(budget["Profit/Losses Change"].mean(), 2)
print(average)
# find max value in profit/losses and index of this value
max_profit_i = budget["Profit/Losses"].idxmax()
# use index and loc to indentify date and amount of max value
date_max_p = budget.loc[max_profit_i, "Date"]
max_profit_a = budget.loc[max_profit_i, "Profit/Losses"]
print(date_max_p, max_profit_a)
# find min value and index of min value
min_profit_i = budget["Profit/Losses"].idxmin()
# use index and loc to find date and amount of min value
date_min_p = budget.loc[min_profit_i, "Date"]
min_profit_a = budget.loc[min_profit_i, "Profit/Losses"]
print(date_min_p, min_profit_a)
# create dictionary to present results in table format
results = {"Total months" : months, 
            "Total" : ["$ " + str(total)], 
            "Average change" : ["$ " + str(average)],
            "Greatest increase in profit" : [str(date_max_p) + ' ' + '$' + str(max_profit_a)],
            "Greatest decrease in profit" : [str(date_min_p) + ' ' + '$' + str(min_profit_a)]

    }
res = pd.DataFrame(results)
# write results in cvs file
path = ("Analysis/Financial_Analysis.csv")
res.to_csv(path, sep='\t', index = False)
print(res)