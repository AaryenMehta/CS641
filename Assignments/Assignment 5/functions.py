from pyfinite import ffield


dct = {'f' : [0,0,0,0], 'g' : [0,0,0,1], 'h' : [0,0,1,0], 'i' : [0,0,1,1], 'j' : [0,1,0,0], 'k' : [0,1,0,1], 'l' : [0,1,1,0], 'm' : [0,1,1,1], 'n' : [1,0,0,0], 'o' : [1,0,0,1], 'p' : [1,0,1,0], 'q' : [1,0,1,1], 'r' : [1,1,0,0], 's' : [1,1,0,1], 't' : [1,1,1,0], 'u' : [1,1,1,1]}

inv_dict = {'0000': 'f', '0001': 'g', '0010': 'h', '0011': 'i', '0100': 'j', '0101': 'k', '0110': 'l', '0111': 'm', '1000': 'n', '1001': 'o', '1010': 'p', '1011': 'q', '1100': 'r', '1101': 's', '1110': 't', '1111': 'u'}


def byte_str(b):

    '''converts byte to corresponding two character string'''

    binary = '{:0>8}'.format(format(b,"b"))
    return inv_dict[binary[0:4]] + inv_dict[binary[4:8]]


def map_to_str(st):

    '''maps the two character string to its hex value'''

    char = chr(16*(ord(st[0]) - ord('f')) + ord(st[1]) - ord('f'))
    return char


def block_to_byte(c):

    '''takes a full 16 bit block of input and returns the hex list of that'''

    plainText = ""
    for i in range(0, len(c), 2):
        plainText += map_to_str(c[i:i+2])
    return plainText

#It contains all the required functions for reuse
#Add, Multiply,Exponential, addVectors, scalarMultiplication, LinearTransformation

exp_store = [[-1]*128 for i in range(128)]

F = ffield.FField(7)

def add (n1, n2):
    return int(n1) ^ int(n2)

def mult (n1, n2):
    return F.Multiply(n1, n2)

def exp (no, pow):
    if exp_store[no][pow] != -1:
        return exp_store[no][pow]

    result = 0
    if pow == 0:
        result = 1
    elif pow == 1:
        result = no
    elif pow%2 == 0:
        sqrt_no = exp(no, pow>>1)
        result = mult(sqrt_no, sqrt_no)
    else:
        sqrt_no = exp(no, pow>>1)
        result = mult(sqrt_no, sqrt_no)
        result = mult(no, result)

    exp_store[no][pow] = result
    return result

def addVectors (v1, v2):
    result = [0]*8
    for i, (e1, e2) in enumerate(zip(v1, v2)):
        result[i] = add(e1, e2)
    return result

def scalarMultiplication (v, elem):
    result = [0]*8
    for i, e in enumerate(v):
        result[i] = mult(e, elem)
    return result

def LinearTransformation (mat, elist):
    result = [0]*8
    for row, elem in zip(mat, elist):
        result = addVectors(scalarMultiplication(row, elem), result)
    return result

def EAEAE (plaintext, lin_mat, exp_mat):

    '''mimics the EAEAE cipher'''

    plaintext = [ord(c) for c in plaintext]
    Output = [[0 for j in range (8)] for i in range(8)]
    
    for ind, elem in enumerate(plaintext):
        Output[0][ind] = exp(elem, exp_mat[ind])

    Output[1] = LinearTransformation(lin_mat, Output[0])

    for ind, elem in enumerate(Output[1]):
        Output[2][ind] = exp(elem, exp_mat[ind])

    Output[3] = LinearTransformation(lin_mat, Output[2])

    for ind, elem in enumerate(Output[3]):
        Output[4][ind] = exp(elem, exp_mat[ind])

    return Output[4]