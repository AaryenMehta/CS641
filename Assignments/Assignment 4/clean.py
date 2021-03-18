finput = open("/home/aaryen/Desktop/CS641/Assignments/Assignment 4/output.txt","r+")
foutput = open("/home/aaryen/Desktop/CS641/Assignments/Assignment 4/output_clean.txt","w+")
i = 0
while i < 199991:
    flag = 0
    ch = finput.readline()
    if len(ch) == 19 :
        ch = ch[2:]
        foutput.write(ch)
        i += 1