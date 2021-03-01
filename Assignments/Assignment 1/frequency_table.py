import collections # makes the frequency analysis easier


def Print(a):

    '''Pretty Printing a list of lists'''

    print()
    for i in a:
        print(i[0],"|",i[1])
    print()


if __name__ == "__main__":

    master = '' # stores input string
    for _ in range(4):
        s = input() # python only takes a single line as input
        master = master + s # adding each single line to master

    master = master.replace(" ","") # removing all whitespaces from the input string
    master = master.replace(".","")
    master = master.replace(",","")
    master = master.replace("!","")
    master = master.replace("\"","")
    #print(master)

    freq = collections.Counter(master) # creates a freuqency dictionary from master
    freq_per = [[i, freq[i] / len(master) * 100.0] for i,count in freq.most_common()] # conversion of frequency to percentage in a sorted order

    Print(freq_per)
    print(len(master))

# Second Cipher Text #
# B MH AFC MUVY EOHPTCS, AFCSS TE QCSI NTYIMS TNA AFCSC. 
# EMRBH XAA VAFR MIUCQPUH "LMRL_CCETOT" FN HM AKUXAHK. OTA WANA
# OTXT FFU EISCWNAF HME BFU MCVA UGTOTRE. BM HYLF IFU UVTY ANE 
# HBSEI QYOQM OUVSF AM EAFTE PYHYS XNSKE IFUSC.