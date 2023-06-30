services = {'Air freshener': 1, 'Rain repellent': 2, 'Tire shine': 2, 'Wax': 3, 'Vacuum': 5}
base_wash = 10
total = 0

service_choice1 = input()
service_choice2 = input()

print("ZyCar Wash")
print("Base car wash - $10")

if service_choice1 == 'Air freshener':
    ex1 = 1
elif service_choice1 == 'Rain repellent':
    ex1 = 2
elif service_choice1 == 'Tire shine':
    ex1 = 2
elif service_choice1 == 'Wax':
    ex1 = 3
elif service_choice1 == 'Vacuum':
    ex1 = 5
else:
    ex1 = 0

if service_choice2 == 'Air freshener':
    ex2 = 1
elif service_choice2 == 'Rain repellent':
    ex2 = 2
elif service_choice2 == 'Tire shine':
    ex2 = 2
elif service_choice2 == 'Wax':
    ex2 = 3
elif service_choice2 == 'Vacuum':
    ex2 = 5
else:
    ex2 = 0

total = 10 + ex1 + ex2
if service_choice1 != '-':
    print(service_choice1, "- $" + str(ex1))
if service_choice2 != '-':
    print(service_choice2, "- $" + str(ex2))
print("-----")
print("Total price: $" + str(total))
