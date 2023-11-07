soup=input("enter the order of soup").split()
meal=input("enter the order of meal").split()
if 'vegetables' in soup:
    print("she loves vegetables")
elif 'vegetables' not in soup:
    print("she hates vegetables")
else:
    print("she would neither hate nor love it.")