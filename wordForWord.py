import os

# do the read line by line
# google "python read text file"
# go to trusted source article / read it
# print(">>> start")
# print(os.getcwd())
# file = open("testdata/testdata1.txt", "r")
# content = file.read()
# print(type(content))
# print(content)
# file.close()

print(">>> start")

print(os.getcwd())


def kprint(filename):
    file = open(filename, "r")
    while True:
        content = file.readline()
        if not content:
            break
    print(content, end="")
    file.close()


    def kreadfile(filename):
        file = open(filename, "r")
        content = file.read()
        file.close()
        return content

    def wc(inputstring):
        chs = 0
        wds = 0
        lns = 0 #lines



        return chs, wds, lns



    if __name__ == "__main__":
        kprint("testdata/testdata1.txt")
        print(">>>>   ")
        kprint("testdata/testdata2.txt")