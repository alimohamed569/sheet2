print("----------------------------------------------------")
print('"sheet6 lab 6"')
lengths = []
widths = []
areas = []
num_rectangles = int(input("Enter the number of rectangles: "))
for i in range(1, num_rectangles + 1):
    length = float(input(f"Enter the length of rectangle {i}: "))
    width = float(input(f"Enter the width of rectangle {i}: "))
    area = length * width
    lengths.append(length)
    widths.append(width)
    areas.append(area)

print("\nNum\tLength\tWidth\tArea (approx.)")
for i in range(num_rectangles):
    print(f"{i + 1}\t{lengths[i]}\t{widths[i]}\t{int(areas[i])}")
