

is_palindrome = lambda word: word == word[::-1]
print(is_palindrome("madad"))


# def find_greatest_common_divisor(num1: int, num2: int):
#     num1_divisors = []
#     num2_divisors = []

#     for divisor in range(1, num1+1):



find_greatest_common_divisor = lambda num1, num2: [divisor for divisor in [[divisor for divisor in range(2, (num1 if num1 > num2 else num2)+1)], [divisor for divisor in range(2, ((num2 if num2 < num1 else num1))+1)]][1] if num1 % divisor == 0 and num2 % divisor == 0].pop()

print(find_greatest_common_divisor(150, 400))


def get_fibonacci(num):
    fibonacci = [0, 1]
    for i in range(2, num + 1):
        fibonacci.append(fibonacci[i-1] + fibonacci[i-2])
    return fibonacci[num]


# get_fibonacci = lambda num: 0 if num == 0 else 1 if num == 1 else get_fibonacci(num - 1) + get_fibonacci(num - 2)

print(get_fibonacci(15))


# find_greatest_common_divisor = lambda num1, num2: (num1, num2) if [] else find_greatest_common_divisor(num1, num2)