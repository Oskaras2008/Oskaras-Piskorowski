# Question 16(a)
# Name and School:Oskaras Piskorowski

print("Household budget calculator. Enter the following information:")


num_adult = int(input("Number of adults in household: "))
num_child = int(input("Number of children in household: "))


cost_food_adult = 50
cost_food_child = 35
child_allowance = 140


if num_child > 3:
    extra_children = num_child - 3
    total_child_allowance = (3 * child_allowance) + (extra_children * (child_allowance + 20))
else:
    total_child_allowance = num_child * child_allowance

print("Children's allowance total: €", total_child_allowance)


total_food_cost = (num_adult * cost_food_adult) + (num_child * cost_food_child)
print("Total household food cost: €", total_food_cost)


inflation_rate = float(input("Inflation rate (e.g. 0.05 for 5% inflation): "))

food_cost_inflation = total_food_cost * (1 + inflation_rate)
print("Total household food cost with inflation: €", food_cost_inflation)


food_cost_inflation_rounded = round(food_cost_inflation, 2)
print("Total household food cost with inflation (rounded): €", food_cost_inflation_rounded)

percentage_spent = (food_cost_inflation_rounded / total_child_allowance) * 100
print("Percentage spend on food:", round(percentage_spent, 2), "%")

budget_remaining = total_child_allowance - food_cost_inflation_rounded
print("Budget remaining after food spend: €", budget_remaining)
