##Virus Cure##

import sys, glob, re

#find infected files
progs = glob.glob("*.py")


for prog in progs:
    if prog == 'cure.py':
        pass
    else:
        print(prog)
        fh = open(prog,"r")
        pCode = fh.readlines()
        fh.close()
        infected = False
        i=j=z=0
        for line in pCode:
            if re.search('VIRUS BEGIN', line):
                infected = True
                break
            i+=1

        if infected:
            for line in pCode:
                if re.search('VIRUS END', line):
                    z=j
                j+=1        
            
            cureCode=pCode
            print(i)
            print(z)
            print(z-i+1)
            for k in range(0,z-i+1):       
                cureCode.remove(pCode[i])
            fh = open(prog, 'w')
            fh.writelines(cureCode)
            fh.close()

print("Cured!")

##Cure End##