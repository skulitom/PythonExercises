def exponent(base, power):
    result = 1
    while power:
        if power & 1:
            result *= base
        power >>= 1
        base *= base
    return result


def main():
    print exponent(6, 50)


if __name__ == "__main__":
    main()
