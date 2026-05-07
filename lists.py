print("\n")

print("\n")

print("WElcome to the list app,we will tell the words with the same starting an ending letter ")

print("\n")

def match_words(words):

    ctr = 0

    lst = []

    for word in words:

        if len(word) > 1 and word[0] == word[-1]:

            ctr += 1

            lst.append(word)

    print("List of words with first and last character same", lst)

    print("\n")

    return ctr

count = match_words(['abc', 'cfc', 'xyz', 'aba', '1221'])

print("Number of words having first and last character same:", count)

print("\n")

print("\n")