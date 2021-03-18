finput = open("/home/aaryen/Desktop/CS641/Assignments/Assignment 4/random.txt","r+")
foutput = open("/home/aaryen/Desktop/CS641/Assignments/Assignment 4/random_input.txt","w+")
temp1 = [0]*64
temp2 = [0]*64
s1 = [0]*16
s2 = [0]*16
s = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0]
i = 0

while i < 100000 :
    temp1 = finput.readline()
    for j in range(64):
        t1 = ord(temp1[j]) - 48
        t2 = s[j]
        temp2[j] = t1 ^ t2
    for k in range(16):
        h1 = (ord(temp1[k*4])-48)*8+(ord(temp1[k*4+1])-48)*4+(ord(temp1[k*4+2])-48)*2+(ord(temp1[k*4+3])-48)
        h2 = temp2[k*4]*8+temp2[k*4+1]*4+temp2[k*4+2]*2+temp2[k*4+3]
        h1 += 102
        h2 += 102
        s1[k] = h1
        s2[k] = h2
    i += 1
    for _ in range(len(s1)):
        s1[_] = chr(s1[_])
        s2[_] = chr(s2[_])
    s1str = ''.join(s1)
    s2str = ''.join(s2)
    foutput.write(s1str+"\n")
    foutput.write(s2str+"\n")
# #include <bits/stdc++.h>
# using namespace std;


# int main()
# {
#   FILE *fi,*fo;
#   fi = fopen("random.txt","r+");
#   fo = fopen("input_random.txt","w+");
#   long long int i = 0;
#   long long int k;
#   char temp1[64];
#   long long int temp2[64];
#   long long int t1,t2;
#   char  s1[17],s2[17];
#   int  s[64] = {0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0};
#   //cout << ">>>>>>>>>>" << s << "\n" ;

#   while(i < 100000)
#   {
#     //for(int j = 0 ; j < 64 ; j++)
#     fscanf(fi,"%s",temp1);
#     for(int j = 0 ; j < 64 ; j++)
#     {
#       t1 = temp1[j]-48;
#       t2 = s[j];
#       //cout << "t2 = =" << t2  << " " << s[j] << " " << temp1[j]<< "\n";
#       temp2[j] =(t1^t2);

#     }
#     //cout << temp1 << "\n" ;
#     int l;
#     for(l = 0 ; l < 16 ; l++)
#     {
#       int h1,h2;
#       h1 = (temp1[l*4]-48)*8+(temp1[l*4+1]-48)*4+(temp1[l*4+2]-48)*2+(temp1[l*4+3]-48);
#       h2 = temp2[l*4]*8+temp2[l*4+1]*4+temp2[l*4+2]*2+temp2[l*4+3];
#       h1 += 102;
#       h2 += 102;
#       s1[l] = h1;
#       s2[l] = h2;
#     }
#     s1[l] = '\0';
#     s2[l] = '\0';
#     i++;
#     fprintf(fo, "%s\n",s1);
#     fprintf(fo, "%s\n",s2);
#     //k temp
#   }
# }
