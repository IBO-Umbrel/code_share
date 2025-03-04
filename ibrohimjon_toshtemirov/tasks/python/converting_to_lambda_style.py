

# Converting to lambda style

# 1️⃣ Square a Number
squere = lambda x: x ** 2


# 2️⃣ Add Two Numbers
add = lambda x, y: x + y


# 3️⃣ Find Maximum of Two Numbers
get_maximum = lambda x, y: x if x > y else y


# 4️⃣ Check Even or Odd
even_odd = lambda num: "Even" if num % 2 == 0 else "Odd"


# 5️⃣ Reverse a String
reverse = lambda string: string[::-1]


# 6️⃣ Find Length of a String
length = lambda string: len(string)


# 7️⃣ Check if a Number is a Palindrome
is_palindrome = lambda string: string == string[::-1]


# 8️⃣ Convert Celsius to Fahrenheit
celsius_to_fahrenheit = lambda c: (c * 1.8) + 32


# 9️⃣ Return the First Letter of a Word
get_first_letter = lambda word: word[0]


# 🔟 Multiply Each Element in a List by 2
multiply_all_by_2 = lambda nums: [i * 2 for i in nums]


# 1️⃣1️⃣
calculate_power = lambda base, exponent: base ** exponent + (base * exponent) - (base / (exponent + 1))


# print(squere(3))
# print(add(9, 10))
# print(get_maximum(20, 30))
# print(even_odd(44))
# print(reverse("popcorn"))
# print(length("popcorn"))
# print(is_palindrome("madam"))
# print(celsius_to_fahrenheit(3))
# print(get_first_letter("gop"))
# print(multiply_all_by_2([2,3,4,5]))
# print(calculate_power(2, 2))


# Comprehension Questions

# 11. Extract all vowels from a given string using list comprehension.
print( (lambda string: [c for c in string if c in "auieo"])("get ready") )


# 12. Generate a list of prime numbers from 1 to 50 using list comprehension.
print( (lambda n: [x for x in range(2, n) if all([x % y != 0 for y in range(2, x)])])(50) )


# 13. Given two lists [1, 2, 3] and [4, 5, 6], create a new list containing the sum of corresponding elements using list comprehension.
print( (lambda list1, list2: [x + y for x, y in zip(list1, list2)])([1, 2, 3], [4, 5, 6]) )


# 14. Create a list of palindromes from a given list of words using list comprehension.
print( (lambda words: [word for word in words if word == word[::-1]])(["madam", "pop", "gop", "dad", "mom", "hello"]) )


# 15. Given a list of dictionaries representing employees (e.g., {'name': 'John', 'salary': 5000}), extract only names of employees earning more than $5000 using list comprehension.
print( (lambda employees: [employee['name'] for employee in employees if employee['salary'] > 5000])([{'name': 'John', 'salary': 5000}, {'name': 'Doe', 'salary': 6000}, {'name': 'Jane', 'salary': 7000}]) )