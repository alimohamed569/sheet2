friends = input("Enter names separated by spaces: ").split()
presents = input("Enter names of presents separated by spaces: ").split()
present_in_mind = input("Enter the present that you love: ")


for i in range(len(friends)):
    if presents[i] == present_in_mind:
        print(f"Oh {friends[i]}, thank you, friend.")

    else:
        print("oops sorry none")
        break
