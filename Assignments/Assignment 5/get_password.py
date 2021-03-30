import functions as fn

# these matrices were found after running bruteCipher

LINEAR_MATRIX = [[84, 125, 19, 104, 100, 19, 10, 66], [0, 70, 28, 20, 42, 51, 118, 8], [0, 0, 43, 2, 13, 18, 9, 94], [0, 0, 0, 12, 115, 32, 101, 23], [0, 0, 0, 0, 112, 101, 23, 17], [0, 0, 0, 0, 0, 11, 92, 72], [0, 0, 0, 0, 0, 0, 27, 31], [0, 0, 0, 0, 0, 0, 0, 38]]
EXPONENT_MATRIX = [17, 113, 40, 67, 88, 42, 25, 14]

#Two halves of password immhmnlqhmltismgmsjhgmhqhflfjjif

password_1 = "immhmnlqhmltismg"
password_2 = "msjhgmhqhflfjjif"


#We iterate over all possible 128 byte values and perform EAEAE to check for which input the password (half) matches

def DecryptPassword(password):
    passw = fn.block_to_byte(password)
    op = ""
    for ind in range(8):
        for ans in range(128):
            inp = op + fn.byte_str(ans)+(16-len(op)-2)*'f'
            if ord(passw[ind]) == fn.EAEAE(fn.block_to_byte(inp), LINEAR_MATRIX, EXPONENT_MATRIX)[ind]:
                op += fn.byte_str(ans)
                break
    return op

print(fn.block_to_byte(DecryptPassword(password_1))+fn.block_to_byte(DecryptPassword(password_2)))