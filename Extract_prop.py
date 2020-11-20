import os, fnmatch
import subprocess as sp
import os, fnmatch
import numpy as np
import pandas as pd
import itertools  
#
curr = os.getcwd()
files =[d for d in (os.listdir(curr)) if os.path.isfile(d) if fnmatch.fnmatch(d,'*.oe.score')]
#
files=sorted(files)
#print(files)
ligands=[s.strip('_receptor.oe.score' 'molecule-') for s in files]
#
for i in ligands:
   smi = os.system("/gpfs01/home/pczaf/programs/openbabel-3.0.0/bin/obabel " "-isdf molecule-" + i + ".sdf " + "-osmi " "-O molecule-" + i + ".smi")
#
num = [ ]
smiles = [ ] 
#
files_smi = [ ]
for i in ligands:
   men = "molecule-" + i + ".smi"
   files_smi.append(men)

#
for i in files_smi:
   with open(i, 'r') as inp1:
      for line in inp1:
         data = []
         data = line.split()
         string = str(data[0])
         smiles.append(string)
         num.append(i)
#
dockscore = [ ]
#
for i in files:
   with open(i, 'r') as inp2:
      data =[ ] 
      valor = 0  
      for line in inp2:
         if '.oeb_receptor.oe' in line:
            man = line.split()
            dscore = float(man[1])
            data.append(dscore)
            valor = min(data)
      dockscore.append(valor)

xlogp = [ ]
PFI = [ ] 

for i in files:
   with open(i, 'r') as inp3:
      for line in inp3:
         if 'TIME:' in line:
            data = []
            data = line.split()
            pfi_dat = str(data[7])
            logp = str(data[3])
            PFI.append(pfi_dat)
            xlogp.append(logp)

#print(xlogp)
#print(PFI)
print(len(xlogp))
print(len(PFI))
print(len(smiles))
#
#with open('gen', 'w') as inp:
#   for (a, b) in zip(smiles, num): 
#      inp.write(a + " " + b + "\n")

#
with open('gen2', 'w') as inp:
   inp.write("id," + "smiles," + "chemgauss4," + "logp," + "PFI" )
   inp.write('\n')
   for (a, b, c, d, e) in zip(num, smiles, dockscore, xlogp, PFI):
      inp.write(a + "," + str(b) + "," + str(c) + "," + str(d) + "," + str(e) + "\n")
#

#with open('gen1', 'w') as inp:
#   inp.write("ID " + "chemgauss4")
#   inp.write('\n')
#   for (c, d) in zip(num, dockscore):
#      inp.write(c + " " + str(d) + "\n")
