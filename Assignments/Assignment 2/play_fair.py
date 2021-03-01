# Key for Play Fair Cipher #

# S E C U R
# I T Y A B
# D F G H K
# L M N O P
# Q V W X Z

# J is omitted similar to a standard Playfair Cipher. And I is used in place of it.



import numpy as np # makes array related computations easy



def Decrypt(arr):

    '''Decrypting Play Fair Cipher'''

    key = np.array([["S","E","C","U","R"],["I","T","Y","A","B"],["D","F","G","H","K"],["L","M","N","O","P"],["Q","V","W","X","Z"]]) # creating playfair square
    decrypted = "" # stores decrypted string
    n = len(arr)

    i = 0 # loop variable

    while i < n-1 :

        # breaking the input string into smaller string of length 2
        char1 = arr[i]
        char2 = arr[i+1]

        flag = 0

        if char1 == char2: # if both characters are same then second character is replaced by X
            char2 = "X"
            flag = 1

        # capture the location of char1 and char2 in the Playfair square
        x = np.where(key == char1)
        y = np.where(key == char2)

        if x[1] == y[1]: # if the characters are in same column
            # take the character above them. ie, same column, row above.
            decrypted += key[(x[0]-1)%5,x[1]][0]
            decrypted += key[(y[0]-1)%5,y[1]][0]

        elif x[0] == y[0]: # if the characters are in same row
            # take the character on left of them. ie, same row, previous column.
            decrypted += key[x[0],(x[1]-1)%5][0]
            decrypted += key[y[0],(y[1]-1)%5][0]

        else : # otherwise
            # build a rectangle and take the elements on the opposite diagonal. 
            # if (a,b) and (c,d) are on diagonal of rectangle then the opposite diagonal has (a,d) and (c,b).
            decrypted += key[x[0],y[1]][0]
            decrypted += key[y[0],x[1]][0]

        i += (2 - flag) # updating loop variable

    return decrypted
        


def preProcess(arr):

    '''Remove all punctuations from the array before parsing it to Decrypt function'''

    punc = '''!()-[]{};:'"\, <>./?@#$%^&*_~'''

    for i in arr:

        if i in punc:
            arr = arr.replace(i,"") # if there is a punctuation mark then replace it by empty space

    return arr



if __name__ == "__main__":

    arr = input() # input array in a single line

    arr = preProcess(arr) # removing punctuations 

    decrypted = Decrypt(arr) # decrypting playfair cipher with SECURITY key

    print(decrypted)
    #print(len(arr))
    #print(len(decrypted))

# second cipher text #
# B MH AFC MUVY EOHPTCS, AFCSS TE QCSI NTYIMS TNA AFCSC. EMRBH XAA VAFR MIUCQPUH "LMRL_CCETOT" FN HM AKUXAHK. OTA WANA OTXT FFU EISCWNAF HME BFU MCVA UGTOTRE. BM HYLF IFU UVTY ANE HBSEI QYOQM OUVSF AM EAFTE PYHYS XNSKE IFUSC.