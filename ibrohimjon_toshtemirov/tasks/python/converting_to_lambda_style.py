

# Converting to lambda style

# 1️⃣ Square a Number
squere = lambda x: x ** 2


# 2️⃣ Add Two Numbers
add = lambda x, y: x + y


# 3️⃣ Find Maximum of Two Numbers
maximum = lambda x, y: x if x > y else y


# 4️⃣ Check Even or Odd
even_odd = lambda num: "Even" if num % 2 == 0 else "Odd"


# 5️⃣ Reverse a String
reverse = lambda string: string[::-1]


# 6️⃣ Find Length of a String
length = lambda string: len(string)


# 7️⃣ Check if a Number is a Palindrome
palindrome = lambda string: string == string[::-1]


# 8️⃣ Convert Celsius to Fahrenheit
celsius_to_fahrenheit = lambda c: (c * 1.8) + 32


# 9️⃣ Return the First Letter of a Word
first_letter = lambda word: word[0]


# 🔟 Multiply Each Element in a List by 2
multiply_by_2 = lambda nums: [i * 2 for i in nums]


# 1️⃣1️⃣
calculate_power = lambda base, exponent: base ** exponent + (base * exponent) - (base / (exponent + 1))


