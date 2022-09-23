# ***************************************************
# Delaware State University
# Division of Physics, Engineering, Mathematics, and
# Computer Science
# CSCI-121 Elements of Computer Programming II
# Recitation 2 - Input/Output and Crypto
# ***************************************************

def crypto(filename, cypher):
        with open(filename, 'r') as fh:
            for line in fh:
                eLine = ''
                for ch in line:
                    eLine += cypher(ch)
        with open(filename, 'w') as fhenc:
                fhenc.write(eLine)

# DO NOT touch the lines below


if __name__ == "__main__":
    crypto('hello.txt', lambda x: chr((ord(x) + 5) % 256))