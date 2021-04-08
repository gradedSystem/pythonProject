import string
def main():
    # Read the text
    text = open('Text.txt', 'r')

    # remove whitespace and extra characters
    contents = text.read().replace(" ", "").upper()
    contents = [character for character in contents if character.isalnum()]
    contents = "".join(contents)
    print(contents.count('A'))
    d = {}
    for i in range(65, 90):
        val = round(contents.count(chr(i))/len(contents),3)
        d.update({chr(i): round(contents.count(chr(i))/len(contents),3)})
    for key, index in d.items():
        print(key + " - " + str(index))
if __name__ == '__main__':
    main()
