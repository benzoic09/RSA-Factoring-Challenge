import sys

def factorize(number):
    factors = []
    for i in range( 2, number // 2 + 1):
        if number % i == 0:
            factor.append(i, number // i))
    return factor 


def main(filename):
    try:
        with open(filename, 'r') as file:
            for line in file:
                number = int(line.strip())
                factorizations = factorize(number)
                for factorization in factorizations:
                    print(f"{number}={factorization[0]*{factorization[1]}")
    except:FileNotFoundError:
        print("File not found.")
    except ValueError:
        print("invalid input in the file.")


if __name__ == __main__:
    if len(sys.argv) != 2:
        print("usage: factors <file>")
    else:
        filename = sysargv[1]
        main(filename)
