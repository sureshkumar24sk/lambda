l1_str = input("Enter the numbers:")
l = list(map(int,l1_str.split()))
square = lambda x: x * 2
result = list(map(square,l))
print("List of the numbers:", l)
print("square of the given numbers:", result)