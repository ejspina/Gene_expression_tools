#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      Eli
#
# Created:     03/03/2014
# Copyright:   (c) Eli 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()

import sys

mirbase = open("C:/rnaseq/ref/Cs_mirbase_mature.txt", "r")
#collation = open("collated_Ci.txt", "w")

pairs = []

for line in mirbase:
    if line.startswith(">"):
        name = line.lstrip(">") #line.replace(line, line[5:-14])
        #print new
    else:
        seq = line
        pairs.append([name, seq])
        #print sys.stdout.write(str(name)+str(seq))
        #print "name", name, "seq", seq

for pair in pairs:
    sys.stdout.write(str(pair).strip("['']").replace("\\n","") + "\n")
    #sys.stdout(str(pair))
    #collation.write(str(pair))

#print len(pairs)

#collation.close
