

def find_word_locations(search_word: str, file_name: str):
    with open(file_name) as file:
        lines = file.readlines()
        locations = []
        for index, line in enumerate(lines):
            if search_word in line:
                locations.append(index + 1)
        return locations


def merge_files(file_names: list, output_filename: str):
    new_content = ""
    for file_name in file_names:
        with open(file_name) as file:
            content = file.read()
            new_content += content
    with open(output_filename, "w") as file:
        file.write(new_content)


def replace_word(word: str, new_word: str, file_name: str, output_filename: str):
    with open(file_name) as file:
        content = file.read()
        new_content = content.replace(word, new_word)
        with open(output_filename, "w") as output_file:
            output_file.write(new_content)


# Runing the functions here:
print(find_word_locations("else", "Functions.ts"))
merge_files(["main.py", "multipication_table.py"], "merged_output.py")
replace_word("private", "public", "PrivateFunctions.ts", "PublicFunctions.ts")