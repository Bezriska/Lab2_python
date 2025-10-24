def str_formatter(s):
    result = []
    current = ""
    in_quotes = False
    i = 0

    while i < len(s):
        char = s[i]

        if char == "'":
            in_quotes = not in_quotes
        elif char == " " and not in_quotes:
            if current:
                result.append(current)
                current = ""
        else:
            current += char

        i += 1

    if current:
        result.append(current)

    return result
