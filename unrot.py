import sys

lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def unrot(encoded, index):
        if encoded[index].islower():
            return lower[lower.index(encoded[index]) - 13]
        elif encoded[index].isupper():
            return upper[upper.index(encoded[index]) - 13]
        else:
            return encoded[index]

def main():
    encoded = sys.argv[1]
    decoded = ""

    for i in range(0, len(encoded)):
        backed = unrot(encoded, i)
        decoded += backed

    print(decoded)

main()
