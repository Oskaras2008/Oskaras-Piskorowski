# Question 16 (a)
# Name and School:Oskaras Piskorowski

# Question 16 (a)
# Name and School:

flight_num = input("Enter your flight number: ")
destination = input("Enter your destination: ")
num_ppl = int(input("Enter the number of people in the travel group: "))

print("Your flight number is", flight_num)
print("You are travelling to", destination)
print("There are", num_ppl, "people in the travel group")


cost_per_person = 0


if flight_num.upper() == "EI121":
    cost_per_person = 520
elif flight_num.upper() == "EI125":
    cost_per_person = 400

total_cost = cost_per_person * num_ppl

print("The total cost of your flights is €" + str(total_cost))

children = int(input("Enter the number of children in the travel group: "))

adult_cost = cost_per_person
child_cost = cost_per_person * 0.75

num_adults = num_ppl - children

total_cost = (num_adults * adult_cost) + (children * child_cost)

print("The total cost of your flights is €" + str(int(total_cost)))