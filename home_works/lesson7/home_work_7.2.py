def correct_sentence(text: str) -> str:

    sentence = text[0].upper()+text[1:]

    if sentence[-1] != ".":
        return sentence.rstrip("") + "."
    else:
        return sentence


assert correct_sentence("greetings, friends") == "Greetings, friends.", 'Test1'
assert correct_sentence("hello") == "Hello.", 'Test2'
assert correct_sentence("Greetings. Friends") == "Greetings. Friends.", 'Test3'
assert correct_sentence("Greetings, friends.") == "Greetings, friends.", 'Test4'
assert correct_sentence("greetings, friends.") == "Greetings, friends.", 'Test5'
print('ОК')