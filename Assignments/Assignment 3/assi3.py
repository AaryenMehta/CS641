a,b,c = 324, 2345, 9513 # number a b and c as given in the ciphertext
p = 19807040628566084398385987581 # prime number p for multiplicative group Z^*_p
A1,A2,A3 = 11226815350263531814963336315, 9190548667900274300830391220, 4138652629655613570819000497 # 2nd half of the tuple


def inverse(a, p):

    '''Finds inverse of a number a in the multiplicative group Z'''

    return pow(a,p-2,p) # by Fermat's little theorem, a * a^(p-2) = 1 mod p.


if __name__ == "__main__":

    g1 = (A2 * inverse(A1,p)) % p # g^2345 * g^(-324) = g^2021
    g2 = (A3 * inverse(A1,p)) % p # g^9513 * g^(-324) = g^9189

    x,y = 2021,9189


    while x != 1 : # when x == 1, we will find 'g'

        # basically this is a form of Euclidean algorithm

        z = y//x # to what power should g1 be raised
        g1 = pow(g1,z,p) # g1 ^ z mod p
        g1 = (g2 * inverse(g1,p)) % p # g2 * g1^(-1)
        x = y-z*x # updating power for next loop


    print(g1) # value of 'g' is stored in g1 at the end of the loop
    g_324 = pow(g1,324,p) # g^324
    g_324_inv = inverse(g_324,p) # g^(-324)
    password = (A1 * g_324_inv) % p # multiplying g^(-324) on both sides to get password
    print(password)