# get the list of squares using list comprehensions
numbers = [1, 2, 3, 4]

squares = [n**2 for n in numbers]
print(squares)

# Find common numbers from two list using list comprehension:
list_a = [1, 2, 3, 4]
list_b = [2, 3, 4, 5]

common_num=[a  for a in list_a for b in list_b if a==b]
print(common_num)