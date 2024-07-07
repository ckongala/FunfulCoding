def string_transformer(s: str) -> str:
    transformed_chars = []
    for i in s:
        if i == " ":
            transformed_chars.append('-')
        elif i.isupper():
            transformed_chars.append(i.lower())
        else:
            transformed_chars.append(i.upper())
    return "".join(transformed_chars[::-1])



input_1 = input("Enter a string:")
print(string_transformer(input_1))


