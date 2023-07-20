"""
before: "hi my name is john and i am learning python"
after: "Hi mY NaMe iS JoHn aNd i aM LeArNiNg pYtHoN"
"""

# 1st solution
def converter(str):
    result = ""
    for i, char in enumerate(str):
        if i % 2 == 0:
            result += char.upper()
        else:
            result += char.lower()
    return result


str = "hi my name is john and i am learning python"
print(converter(str))


# 2nd solution:
def converter2(str):
    result2 = ""
    for index in range(len(str)):
        if index % 2 == 0:
            result2 += str[index].upper()
        else:
            result2 += str[index].lower()

    return result2


print(converter2(str))
