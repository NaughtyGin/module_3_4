def single_root_words(root_word, *other_words):
    same_words = []
    root_word_up = root_word.upper()
    other_words_up = [i.upper() for i in other_words]
    for j in range(len(other_words)):
        if str(root_word_up) in str(other_words_up[j]) or str(other_words_up[j]) in root_word_up:
            same_words.append(other_words[j])
    return same_words


result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)
