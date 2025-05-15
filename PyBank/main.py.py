import csv
import os

input_path = os.path.join("Resources", "budget_data.csv")
output_path = os.path.join("analysis", "financial_analysis.txt")

total_months = 0
total_profit = 0
changes = []
months = []

with open(input_path, newline="") as csvfile:
    csvreader = csv.reader(csvfile)
    header = next(csvreader)

    first_row = next(csvreader)
    total_months += 1
    total_profit += int(first_row[1])
    prev_value = int(first_row[1])

    for row in csvreader:
        month = row[0]
        profit = int(row[1])

        total_months += 1
        total_profit += profit

        change = profit - prev_value
        changes.append(change)
        months.append(month)

        prev_value = profit

average_change = sum(changes) / len(changes)
greatest_increase = max(changes)
greatest_decrease = min(changes)
greatest_month = months[changes.index(greatest_increase)]
worst_month = months[changes.index(greatest_decrease)]

output = (
    "Financial Analysis\n"
    "----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${total_profit}\n"
    f"Average Change: ${average_change:.2f}\n"
    f"Greatest Increase in Profits: {greatest_month} (${greatest_increase})\n"
    f"Greatest Decrease in Profits: {worst_month} (${greatest_decrease})\n"
)

print(output)

with open(output_path, "w") as txtfile:
    txtfile.write(output)
