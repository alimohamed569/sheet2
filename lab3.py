attempts = 5

while attempts > 0:
    weight = float(input("Enter weight: "))
    if weight < 0:
        print("Invalid weight")
    else:
        unit = int(input("Enter weight unit (1 for mg, 2 for kg, 3 for ton): "))
        if unit in [1, 2, 3]:
            if unit == 1:
                weight_grams = weight / 1000
                print(weight)
            elif unit == 2:
                weight_grams = weight * 1000
                print(weight)
            else:
                weight_grams = weight * 1000000
                print(weight)
            print(weight_grams)
        else:
            print("Invalid unit")

    response = input("Do you want to make another conversion? (Yes/No): ")
    if response == "y":
        break

    attempts -= 1

print("Program execution")
