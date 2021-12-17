def capitalize(line):
    result = f'{line[0].upper()}{line[1:]}' if line else line
    return result
