import string


def is_palindrome(text: str) -> bool:
    text =''.join([char for char in text if char not in string.punctuation]).lower()
    new_text = text.replace(" ", "")

    return True if new_text == new_text[::-1] else False



assert is_palindrome('A man, a plan, a canal: Panama') == True, 'Test1'
assert is_palindrome('0P') == False, 'Test2'
assert is_palindrome('a.') == True, 'Test3'
assert is_palindrome('aurora') == False, 'Test4'
print("ОК")