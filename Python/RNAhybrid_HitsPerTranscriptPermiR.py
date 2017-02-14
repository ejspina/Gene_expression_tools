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

# THIS FILE REQUIRES TSV format RNAhybrid OUTPUT SORTED BY GENE ID then miRNA ID


targets = open("C:/RNAseq/mir_targets/rnahybrid/targets_6bp_e20p01_k2-4.srt.txt", "r")

first = targets.readline()
mRNA = str(first.split()[1])
mir = str(first.split()[3])
cluster = 0
count = 0
unique = 1

for line in targets:
    if mRNA == str(line.split()[1]): #check if mRNA is same as previous
        cluster += 1 # increment cluster size for each target in an mRNA
        if mir == str(line.split()[3]): #check if miR is same as previous
            count += 1  # increment hit count if miR already in cluster
        else: #if new miR
            print mRNA, mir, count # Hits per mRNA for previous miRNA
            count = 1 # reset hit count
            unique += 1 #increment unique miRs for current mRNA
            mir = str(line.split()[3]) # reset current miR
    else:
        #New Gene: print previous line and restart comparison
        print mRNA, mir, cluster, unique # total miR targets/transcript & unique miRs/transcript
        mRNA = str(line.split()[1]) # reset current mRNA for new cluster
        mir = str(line.split()[3]) # reset current miR for new cluster
        cluster = 1 # reset cluster size
        unique = 1 # reset miR count for new transcript
print mRNA, mir, cluster, unique # Last miR in list hits/cluster & unique targets/cluster
