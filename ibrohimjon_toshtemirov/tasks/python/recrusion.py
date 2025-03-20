


# Recrusion

# 1. Print numbers from N to 1 (Countdown)
def countdown(n: int):
    if n == 0:
        return
    print(n)
    countdown(n - 1)


# 2. Print "Hello" N times
def hello(n: int):
    if n == 0:
        return
    print("Hello")
    hello(n - 1)


# 3. Find the sum of even numbers from 1 to N
def sum_even(n: int):
    if n <= 1:
        return n
    if n % 2 == 0:
        return n + sum_even(n - 2)
    return sum_even(n - 1)

# odd ver
def sum_odd(n: int):
    if n <= 1:
        return n
    if n % 3 == 0:
        return n + sum_even(n - 2)
    return sum_even(n - 1)


# 4. Count occurrences of a given character in a string
def count_char(word: str, char: str, index: int = 0):
    if not word:
        return 0
    if index < 0:
        if word[index] == char:
            return 1 + count_char(word, char, index - 1)
        else:
            return count_char(word, char, index - 1)
    if word[len(word) - 1] == char:
        return 1 + count_char(word, char, len(word) - 2)
    return count_char(word, char, len(word) - 2)


# 5. Find the minimum number in a list
def min_num(arg):
    if len(arg) == 1:
        return arg[0]
    return min(arg[0], min_num(arg[1:]))


# 6. Check if a number is even or odd
def is_even(n: int):
    if n == 0:
        return True
    if n == 1:
        return False
    return is_even(n - 2)


# 7. Find the sum of elements in a list
def sum_list(arg):
    if not arg:
        return 0
    return arg[0] + sum_list(arg[1:])


# 8. Find the product of digits of a number
def product_digits(n: int):
    if n == 0:
        return 1
    return (n % 10) * product_digits(n // 10)


# countdown(5)
# hello(3)
# print(sum_even(10))
# print(sum_odd(10))
# print(count_char("hello", "l"))
# print(min_num([3, 5, 1, 7, 2]))
# print(is_even(5))
# print(sum_list([1, 2, 3, 4, 5]))
# print(product_digits(12345))\


# more recrusion


# 1. Find the Length of a String Using Recursion
def length(text: str):
    if text:
        return 1 + length(text[1:])
    return 0


# 2. Remove Duplicates from a String Using Recursion
def unduplicate(text: str):
    if text:
        return text[0] + unduplicate(text[1:]) if text[0] not in text[1:] else unduplicate(text[1:])
    return text


# 3. Find the Maximum Element in a List Using Recursion
def get_largest_element(elements: list[int]):
    # print(elements)
    if length(elements) > 1:
        if elements[0] > elements[1]:
            temp = elements.copy()
            temp.pop(1)
            return get_largest_element(temp)
        else:
            return get_largest_element(elements[1:])
    elif length(elements) == 1:
        return elements[0]
    return None


# 4. Count Occurrences of a Character in a String Using Recursion
def count_occurrence(text: str, char: str):
    if text:
        return 1 + count_occurrence(text[1:], char) if text[0] == char else count_occurrence(text[1:], char)
    return 0


# 5. Replace All ‘A’ with ‘B’ in a String
def replace(search: str, replacement: str, text: str):
    if text:
        return replacement + replace(search, replacement, text[1:]) if text[0] == search else replace(search, replacement, text[1:])
    return text


# 6. Check if an Array is Sorted
def is_sorted(array: list):
    if length(array) > 1:
        if array[0] <= array[1]:
            return is_sorted(array[1:])
        else:
            return False
    elif length(array) == 1:
        return True
    return False




# print(length("popcorn"))
# print(unduplicate("hello"))
# print(get_largest_element([4, 9023, 109, 3004]))
# print(count_occurrence("hello word", "l"))
print(is_sorted([1, 2, 3, 3, 5]))