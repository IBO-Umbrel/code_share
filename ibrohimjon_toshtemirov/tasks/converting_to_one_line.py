# functions to make coding easier, and less

# checks divisibility
def div(x: int, y: int, z: int = None):
    if z:
        return x % y == z
    return x % y == 0



# Tasks
L = ["red", "green", "blue"]
D = {}
for x, y in enumerate(L):
    D[x] = y
print(D)


D = {}
for x in range(6):
    if div(x, 2):
        D[x] = x**2
print(D)


D = {}
for x in range(2):
    for y in range(2):
        D[(x, y)] = x + y
print(D)


# vowels = "aeiou"
# word = "Hello!"
restricted_number = 4
safe_numbers = []
for x in range(6):
    if (div(x, 2) or div(x, 3)) and x is not restricted_number:
        safe_numbers.append(x)
print(safe_numbers)


matrix = [[1, 2], [3, 4], [5, 6]]
values = []
for row in matrix:
    for column in row:
        if div(x, 2, 1):
            values.append(column)
print(values)