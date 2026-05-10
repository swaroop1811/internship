import string

def word_frequency(paragraph):

    paragraph = paragraph.lower()

    for ch in string.punctuation:
        paragraph = paragraph.replace(ch, "")

    words = paragraph.split()

    frequency = {}

    for word in words:

        if word in frequency:
            frequency[word] = frequency[word] + 1

        else:
            frequency[word] = 0  
    return frequency


text = "Python is easy. Python is powerful, and Python is useful!"

print(word_frequency(text))
