


# Recrusion


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
        return replacement + replace(search, replacement, text[1:]) if text[0] == search else text[0] + replace(search, replacement, text[1:])
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
print(replace("A", "B", "ABACADA"))
# print(is_sorted([1, 2, 4, 3, 3, 5]))