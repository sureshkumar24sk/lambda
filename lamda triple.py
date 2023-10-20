l1_str = input("Enter the list:")
l = list(map(int,l1_str.split()))
triple = lambda n: n*3
result  = list(map(triple, l))
print("List of number:", l)
print("triple of list numbers:", result)