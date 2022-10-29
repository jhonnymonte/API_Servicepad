def freq(text):
    text = text.lower()
    text = text.split()

    str2 = []
    for i in text:
        if i not in str2:
            str2.append(i)

    for i in range(0, len(str2)):

        print('Frequency of', str2[i], 'is :', text.count(str2[i]))

if __name__ == '__main__':

    text = "Hi how are things? How are you? Are you a developer? I am also a developer"
    freq(text)


