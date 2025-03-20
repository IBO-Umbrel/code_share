

def merge_dictionary(dict1, dict2):
    return {**dict1, **dict2}


def arguments_to_dictionaty(a, b, *args, **keyargs):
    pos = {key:key for key in args}
    return {"a": a, "b": b, **pos, **keyargs}


def find_longest_arg(*args):
    result = None
    score = 0

    for arg in args:
        if len(arg) > score:
            result = arg
            score = len(arg)
    return result


def get_str_dict(**keyargs):
    result = {}
    
    for key, value in keyargs.items():
        if type(value) == str:
            result[key] = value
    return result


def math(*numbers, operation: str):
    if operation == "sum":
        return sum(numbers)
    if operation == "mul":
        result = numbers[0]
        
        for num in numbers[1:]:
            result *= num
        return result
    if operation == "sub":
        result = num[0]
        
        for num in numbers[1:]:
            result -= num
        return result
    if operation == "div":
        result = numbers[0]
        
        for num in numbers[1:]:
            if 0 == num:
                return "you cannot divide by zero!"
            result /= num
        return result



print(merge_dictionary({"name": "ibo"}, {"age": 9}))
print(arguments_to_dictionaty(2, 4, "hello", "world", word="non-word", key="value"))
print(find_longest_arg("ddddd", "hello", "boffed", "arrays", "loooppppping"))
print(get_str_dict(name = "ibo", age = 9))

print(math(0, 0, 0, operation="div"))