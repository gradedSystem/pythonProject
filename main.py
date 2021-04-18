def main():
    # Read the text
    text = open('Text.txt', 'r')

    contents = text.read()
    d = {}
    for i in range(0, 127):
        if contents.count(chr(i)) != 0:
            val = round(contents.count(chr(i))/len(contents), 3)
            d.update({chr(i): val})
    for key, index in sorted(d.items(), key=lambda item: item[1],reverse=True):
        print(key + " - " + str(index))
    print(contents)

if __name__ == '__main__':
    main()
