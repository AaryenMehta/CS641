#include <bits/stdc++.h>
using namespace std;
int main()
{
  char ch[100],temp[100];
  FILE *fi,*fo;
  fi = fopen("/home/aaryen/Desktop/Assignment5_new/Programs/output.txt","r+");
  fo = fopen("/home/aaryen/Desktop/Assignment5_new/Programs/output_clean.txt","w+");
  long int i = 0;
  int count = 0;
  int count2 = 0;
  while(i < 17573)
  {
    int flag = 0;
    strcpy(ch,temp);
    fscanf(fi,"%s",ch);
    if(strlen(ch) == 16 && ch != "transformations:")
    {
      //cout << ch << "\n";
      printf("%s",ch);
        fprintf(fo, "%s ",ch);
        //cout << "yo" ;
        i++;
        count++;
        count2++;
        if (count == 128){
          count = 0;
          fprintf(fo, "\n");
        }
        if (count2 == 1024) {
          break;
        }
    }
  }
}
