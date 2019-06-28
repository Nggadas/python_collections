travel_expenses = [
    [5.00, 2.75, 22.00, 0.00, 0.00],
    [24.75, 5.50, 15.00, 22.00, 8.00],
    [2.75, 5.50, 0.00, 29.00, 5.00],
]


# Efficient Solution
print("Travel Expenses(efficient solution):")
week_number = 1

for week in travel_expenses:
    print("* Week #{}: £{}".format(week_number, sum(week)))
    week_number += 1


# Long solution
print()
print("Travel Expenses(long solution):")
week_number = 1
travel_cost = 0

for week in travel_expenses:
    for day in week:
        travel_cost += day

    print("* Week #{}: £{}".format(week_number, travel_cost))
    week_number += 1
    travel_cost = 0






















