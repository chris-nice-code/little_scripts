# -*- coding: utf-8 -*-
"""
Created on Fri Feb 17 12:04:08 2023

@author: josh.roberts
"""
# Output batch directory
output_batch = "S:\\02_Projects\\gs261_Otter_NBS\\08_MF\\in"

# Loop over the number of copies to create new nam files
with open(output_batch + "\\batch_file.bat", "w") as file:    
    for i in range(21, 49): #number of mf96 runs, needs tinkering depending on numbering system used
        instr1 = 'cd S:\\02_Projects\\gs261_Otter_NBS\\08_MF\\in\\otrmf{}'.format(i+385)
        instr2 = 'mfintel009i.exe<otrmf{}.txt'.format(i+385)
        file.write(instr1 + "\n")
        file.write(instr2 + "\n")
        file.write("\n")
 