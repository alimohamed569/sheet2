print("----------------------------------------------------")
print('"sheet7 lab 9"')
N = int(input("Enter a number N: "))
for i in range(1, N + 1):
    for j in range(1, i + 1):
        product = i * j
        print(product, end="\t")
    print()