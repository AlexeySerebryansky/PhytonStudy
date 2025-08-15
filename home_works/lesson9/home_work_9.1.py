def popular_words (text: str, words: list) -> dict:

    new_text = text.lower().split()
    count_word = list(map(lambda x: new_text.count(x), words))
    result_dict  = dict(zip(words, count_word))

    return result_dict


assert popular_words('''When I was One I had just begun When I was Two I was nearly new ''', ['i', 'was', 'three', 'near']) == { 'i': 4, 'was': 3, 'three': 0, 'near': 0 }, 'Test1'
print('OK')