def word_processor()
    text = input("Enter sentence: ")

    vowels = "aeiou"
    count = 0

    for ch in text.lower
        if ch in vowels
            count = count + 1

    print("Vowel count:" count)


    words = text.split

    print("Words with more than 3 letters")

    for w in words:
        if len(w) > 3
            print w

word_processor
