


# 1. Create a function that accepts any number of numbers as positional arguments and prints the sum of those numbers.
def sum_of_numbers(*args):
    return sum(args)


# 2. Create a function that accepts any number of positional and keyword arguments, and that prints them back to the user. Your output should indicate which values were provided as positional arguments, and which were provided as keyword arguments.
def print_args(*args, **kwargs):
    print(f"Positional arguments: {args}")
    print(f"Keyword arguments: {kwargs}")


# 3. Print the following dictionary using the format method and ** unpacking
country = { 
"name": "Germany",
"population": "83 million",
"capital": "Berlin",
"currency": "Euro"
}
print("name: {name} \npopulation: {population} \ncapital: {capital} \ncurrency: {currency}".format(**country))


# 4. Using * unpacking and range, print the numbers 1 to 20, separated by commas.
print(*range(1, 21), sep=",")


# 5. Modify your code from exercise 4 so that each number prints on a different line. You can only use a single print call.
print(*range(1, 21), sep="\n")


# 6. Write a Python function called `calculate_total_cost` that calculates the total cost of items purchased.
def calculate_total_cost(*args, **kwargs):
    total_cost = sum(args)
    for item, discount in kwargs.items():
        total_cost -= discount
    return total_cost
print(calculate_total_cost(100, 50, 75, apple=10, banana=5))


# 7. Write a Python function called `create_shopping_list` 
def create_shopping_list(*args, **kwargs):
    shopping_list = {}
    for item in args:
        shopping_list[item] = kwargs[item]
    return shopping_list

lst1 = []
lst2 = {}
while True:
    input1 = input("Input Product Name: ")
    if input1 == "q":
        break;
    input2 = input("Input Product quntity: ")
    if input2 == "q":
        break;
    lst1.append(input1)
    lst2[input1] = input2

print(create_shopping_list(*lst1, **lst2))