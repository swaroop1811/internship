def word_frequency(paragraph):

    paragraph = paragraph.lower()

    paragraph = paragraph.replace(".", "")

    words = paragraph.split()

    freq = {}

    for word in words:

        if word in freq:
            freq[word] += 1
        else:
            freq[word] = 1

    return freq

text = "Python is easy. Python is fun!"
print(word_frequency(text))
