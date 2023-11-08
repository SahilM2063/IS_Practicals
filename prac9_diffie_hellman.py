def power(a, b, p):
    if b == 1:
        return a
    else:
        return (a ** b) % p

def main():
    P = int(input("Enter the prime number P: "))
    print("The value of P:", P)

    G = int(input("Enter the primitive root G: "))
    print("The value of G:", G)

    a = int(input("Enter the private key for Alice (a): "))
    print("The private key a for Alice:", a)

    x = power(G, a, P)

    b = int(input("Enter the private key for Bob (b): "))
    print("The private key b for Bob:", b)

    y = power(G, b, P)

    ka = power(y, a, P)
    kb = power(x, b, P)

    print("Secret key for Alice is:", ka)
    print("Secret key for Bob is:", kb)

if __name__ == "__main__":
    main()
