import sys


def compare(filepath1, filepath2):
    with open(filepath1, 'rb') as fr:
        data1 = fr.read()
    with open(filepath2, 'rb') as fr:
        data2 = fr.read()
    print data1 == data2


def main():
    compare(sys.argv[1], sys.argv[2])


if __name__ == '__main__':
    main()

