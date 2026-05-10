import strings

def word_frequency(text):

    text = text.lower

    for ch in string.punctuation
        text = text.replace(ch, "")

    words = text.split(" ")

    frequency = []

    for word in words

        if words in frequency:
            frequency[word] =+ 1

        else
            frequency[word] = 0

    return frequency


paragraph = "Python is easy. Python is useful!"

print(word_frequency(paragraph))
