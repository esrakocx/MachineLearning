# Create a dictionary, numbers let be keys and the square of the numbers let be values. Add only the even numbers. Use dict comprehensions.

numbers = range(10)
new_dict = {}

# Classical solution
for i in numbers:
    if i % 2 == 0:
        new_dict[i] = i ** 2

print(new_dict)

# With dict comprehensions
{i: i ** 2 for i in numbers if i % 2 == 0}

