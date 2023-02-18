import os
import time
time.sleep(0.2)
os.system("cls")

def listToString(s):
 
    # initialize an empty string
    str1 = ""
 
    # traverse in the string
    for ele in s:
        str1 += ele
 
    # return string
    return str1

def loadinTextAnimation():
    a=str(input())
    a=list(a)
    for t in range(0,len(a)):
        a[t]=a[t].lower()
    for j in range(0,len(a)):
        for i in range(0,len(a)):
            if a[i]!=' ':
                a[j]=a[j].upper()
        a=listToString(a)
        print(a)
        a=list(a)
        for t in range(0,len(a)):
            a[t]=a[t].lower()
        time.sleep(0.2)
        os.system("cls")

print("Finished!")