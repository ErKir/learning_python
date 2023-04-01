def capitalize(string):
    if (string == ''):
        return ''
    first_char, *chars = string
    rest_chars = ''.join(chars)
    return f'{first_char.upper()}{rest_chars}'
