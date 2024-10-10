def is_valid(s):
    # Continuously check for and remove adjacent matching pairs of brackets
    while '()' in s or '{}' in s or '[]' in s:
        # Replace the found pairs with an empty string
        s = s.replace('()', '').replace('{}', '').replace('[]', '')
    
    # After all pairs are removed, check if the string is empty
    return s == ''  #all brackets were matched correctly
print(is_valid("[{}()]")) 
