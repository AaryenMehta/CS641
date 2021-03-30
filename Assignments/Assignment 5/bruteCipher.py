import functions as fn


exp = [[] for i in range(8)] # will store possible exponents
diag = [[[] for i in range(8)] for j in range(8)] # will store possible diagonal values


fi = open("Assignments/Assignment 5/input.txt", 'r')
fo = open("Assignments/Assignment 5/output_clean.txt", 'r')


for ind, (iline, oline) in enumerate(zip(fi.readlines(), fo.readlines())):

    instr = []
    outstr = []
    
    # converting input to hex values

    for hexi in iline.strip().split(" "):
        instr.append(fn.block_to_byte(hexi)[ind])

    for hexo in oline.strip().split(" "):
        outstr.append(fn.block_to_byte(hexo)[ind])
        
    for i in range(1, 127):
        for j in range(1, 128):
            flag = True
            for inp, out in zip(instr, outstr):

                # iterating over possible values of e_i and a_jj and checking if input is correctly mapped to the output

                if ord(out) != fn.exp(fn.mult(fn.exp(fn.mult(fn.exp(ord(inp), i), j), i), j), i):
                    flag = False
                    break

            if flag:

                #If True, then append them to corresponding lists

                exp[ind].append(i)
                diag[ind][ind].append(j)

#print(diag)
#print(exp)

fi = open("Assignments/Assignment 5/input.txt", 'r')
fo = open("Assignments/Assignment 5/output_clean.txt", 'r')

for ind, (iline, oline) in enumerate(zip(fi.readlines(), fo.readlines())):

    if ind > 6 :

        # taking only first 6 pairs
        break

    instr = []
    outstr = []

    # converting input to hex values

    for hexi in iline.strip().split(" "):
        instr.append(fn.block_to_byte(hexi)[ind]) 

    for hexo in oline.strip().split(" "):
        outstr.append(fn.block_to_byte(hexo)[ind+1])

    for i in range(1, 128):

        # iterating over possible values of e_i and a_jj and checking if input is correctly mapped to the output

        for p1, e1 in zip(exp[ind+1], diag[ind+1][ind+1]):
            for p2, e2 in zip(exp[ind], diag[ind][ind]):

                flag = True

                for inp, outp in zip(instr, outstr):

                    # substituting the pairs ad=nd iterating over all possible values of i
                    # assume that there is a triangle (aii,aij,ajj)

                    if ord(outp) != fn.exp(fn.add(fn.mult(fn.exp(fn.mult(fn.exp(ord(inp), p2), e2), p2), i) ,fn.mult(fn.exp(fn.mult(fn.exp(ord(inp), p2), i), p1), e1)), p1):
                        flag = False
                        break

                if flag:

                    # if True, then we have found the correct values and can add them to the lists

                    exp[ind+1] = [p1]
                    diag[ind+1][ind+1] = [e1]
                    exp[ind] = [p2]
                    diag[ind][ind] = [e2]
                    diag[ind][ind+1] = [i]

#print(diag)
#print(exp)



for index in range(6):

    of = index + 2
    
    exp_E = [e[0] for e in exp]
    lin_trans_At = [[0 for i in range(8)] for j in range(8)] # filling all empty elements with 0


    for i in range(8):
        for j in range(8):

            lin_trans_At[i][j] = 0 if len(diag[i][j]) == 0 else diag[i][j][0]
            
    fi = open("Assignments/Assignment 5/input.txt", 'r')
    fo = open("Assignments/Assignment 5/output_clean.txt", 'r')

    for ind, (iline, oline) in enumerate(zip(fi.readlines(), fo.readlines())):

        if ind > (7-of):
            continue

        instr = [fn.block_to_byte(msg) for msg in iline.strip().split(" ")]
        outstr = [fn.block_to_byte(msg) for msg in oline.strip().split(" ")]

        # iterating over all possible values of a_ij to find the one that correctly maps the output of EAEAE to output

        for i in range(1, 128):

            lin_trans_At[ind][ind+of] = i
            flag = True

            for inps, outs in zip(instr, outstr):

                if fn.EAEAE(inps, lin_trans_At, exp_E)[ind+of] != ord(outs[ind+of]):
                    flag = False
                    break

            if flag:
                diag[ind][ind+of] = [i]

    fi.close()
    fo.close()

lin_trans_At = [[0 for i in range(8)] for j in range(8)] # filling all empty elements with 0

for i in range(8):
    for j in range(8):

        lin_trans_At[i][j] = 0 if len(diag[i][j]) == 0 else diag[i][j][0]

print(lin_trans_At)
print(exp_E)