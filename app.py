from threading import *

class Encrypt:    
    def getReverseLetter(self,letter):
            alpha = "abcdefghijklmnopqrstuvwxyz"
            rev_alpha = "zyxwvutsrqponmlkjihgfedcba"
            for i in range(0,len(alpha)):
                if letter.islower() and letter==alpha[i]:
                    return rev_alpha[i]
                if letter.isupper() and letter==alpha[i].upper():
                    return rev_alpha[i].upper()
            return -1
           
    def cipher(self):
        with open('inputfile.txt') as f:
            inputString = f.read()

        outputString=""
        for s in inputString:
            rev_Letter=self.getReverseLetter(s)
            if(rev_Letter!=-1):
                outputString+=str(rev_Letter)
            else:
                outputString+=s
        print(outputString)
        with open('outputfile.txt','w') as f:
            f.write(outputString)
        return outputString
       
a = Encrypt()
t1 = Thread(target=a.cipher)
t1.start()
t1.join()
print("done")
    