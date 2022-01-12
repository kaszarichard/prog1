# 1.feladat:
while True:
    try:
        x = int(input("Kérek egy számot: "))
        print(x)
        break
    except ValueError:
        print("A megadott érték nem szám!")

# 2.feladat:
try:
        in_file = open("input.txt","r")
        for line in in_file:
            print(line, end ="")
        in_file.close()

except FileNotFoundError:
    print("A fájl nem található!")

# 3.feladat:
try:
    in_file = open("input.txt","r")
    counter = 0
    word_to_find = 'Lannister'
    for line in in_file:
        words = line.split()

        for word in words:
            if word_to_find in word:
                counter += 1

    in_file.close()
    print(f"A {word_to_find} szo {counter} alkalommal talalhato meg a szovegben.")
except FileNotFoundError:
    print("A megadott fájl nem található")

# 4.feladat:
def inverse_letters(line):
    res_str = ""
    for ch in line:
        if ch.islower():
            res_str += ch.upper()
        elif ch.isupper():
            res_str += ch.lower()
        else:
            res_str += ch
    return res_str
try:
    out_file = open("output.txt","w")

    with open("input.txt","r") as in_file:
        for line in in_file:
            line = inverse_letters(line)
            print(line, file=out_file, end= "")

    out_file.close()
except FileNotFoundError:
    print("A megadott fájl nem található")

# 5.feladat:
def remove_punctuations(line):
    res_str = ""
    import string
    for ch in line:
        if ch not in string.punctuation:
            res_str += ch
    return res_str

try:
    in_file = open("input.txt","r")
    out_file = open("longestWords.txt","w")
    longest_len = 0
    longest_words = []

    for line in in_file:
        line = remove_punctuations(line)
        words = line.split()
        for word in words:
            if len(word) > longest_len:
                longest_len = len(word)

                longest_words.clear()
                longest_words.append(word)
            elif len(word) == longest_len:
                longest_words.append(word)
    print("A leghosszabb szo {} karakterbol all".format(longest_len), file=out_file)
    for word in   longest_words:
        print(word, file=out_file)

    in_file.close()
    out_file.close()

except FileNotFoundError:
    print("A megadott fájl nem található")
















