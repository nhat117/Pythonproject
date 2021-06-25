import sys
def read_input(file):
    for line in file:
        yield line.split()

def main(seperator = '\t'):
    #input comes from STDIN
    data = read_input(sys.stdin)
    for words in data:
        for word in words:
            print("%s%s%d" %(word,seperator,1))

if __name__ == "__main__":
    main()
