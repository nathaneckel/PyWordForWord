#Pasted yesterday's class code;
#Found percentage distribution code online
#Still need to use that code within this code's context.

import os

# do the read line by line.
import string

print(">>> start")

print(os.getcwd())

def kprint(filename):
    file = open(filename, "r")
    while True:
        content=file.readline()
        if not content:
            break
        print(content, end="")
    file.close()

def kreadfile(filename):
    file = open(filename, "r")
    content = file.read()
    file.close()
    return content

def kprintwc(filename):
    txt = kreadfile(filename)
    testtuple = wc(txt)
    print(testtuple, filename)


def wc(inputstring):
    chs = 0 # characters
    wds = 0 # words
    lns = 0 # lines

    chs = len(inputstring)

    for ch in inputstring:
        if ch == '\n':
            lns += 1

    wds = len([word.strip(string.punctuation) for word in inputstring.split()])

    return lns, wds, chs


def wordFrequency(inputstring):
    d = {}
    wdlist = [word.strip(string.punctuation).lower() for word in inputstring.split()]

    # d = {'kris': 1, 'chris': 1, 'lydia': 2} if the 'kris chris lydia lydia'
    for word in wdlist:
        if word in d:
            d[word] += 1
        else:
            d[word] = 1
    return {k: v for k, v in sorted(d.items(), key=lambda item: item[1], reverse=True)}

def letterFrequency(inputstring):
    d = {}
    wdlist = [word.strip(string.punctuation).lower() for word in inputstring.split()]
    # print(wdlist)

    # d = {'kris': 1, 'chris': 1, 'lydia': 2} if the 'kris chris lydia lydia'
    for word in wdlist:
        chword = list(word) # 'kris' -> ['k'....
        for ch in chword:
            if ch in 'abcdefghijklmnopqrstuvwxyz':
                if ch in d:
                    d[ch] += 1
                else:
                    d[ch] = 1

    return {k: v for k, v in sorted(d.items(), key=lambda item: item[1], reverse=True)}

if __name__ == "__main__":

    for n in range(8):
        # there is a weird file name in the input datasets.
        t = '5a' if n == 5 else str(n)
        fname = "testdata/testdata" + t + ".txt"
        kprintwc(fname)

    # print(wordFrequency('kris chris lydia lydia'))
    # print(wordFrequency(kreadfile("testdata/testdata0.txt")))
    # print(wordFrequency(kreadfile("testdata/testdata1.txt")))
    # print(wordFrequency(kreadfile("testdata/testdata2.txt")))
    # print(wordFrequency(kreadfile("testdata/testdata3.txt")))
    #
    # randj = wordFrequency(kreadfile("testdata/testdata3.txt"))
    # for w in sorted(randj, key=randj.get, reverse=True):
    #     print(w, randj[w])

    for n in range(8):
        # there is a weird file name in the input datasets.
        t = '5a' if n == 5 else str(n)
        fname = "testdata/testdata" + t + ".txt"
        print(wordFrequency(kreadfile("testdata/testdata3.txt")))

    print(letterFrequency('kris chris lydia lydia'))

    for n in range(8):
        # there is a weird file name in the input datasets.
        t = '5a' if n == 5 else str(n)
        fname = "testdata/testdata" + t + ".txt"
        print(fname, letterFrequency(kreadfile(fname)))