from people import humans

individuals = {}

for index, people in enumerate(humans):
    individuals[str(index + 1 )] = people

while True:

    print("Please select the which individual's attribute you want to see")
    for index, people in individuals.items():
        print(f"{index}: {people}")

    person = input(">> ")
    if person == '0':
        break
    elif person in individuals:
        personality = individuals[person]
        attributes = humans[personality]
        print(f"below are the attributes of {personality}")
        print(attributes)

