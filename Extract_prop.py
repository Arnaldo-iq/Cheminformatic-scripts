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

aro = [ ]
PSA = [ ]
MolW = [ ]
NAc = [ ]
NDon = [ ]
ratio = [ ] 
sp3Frac = [ ]
LLE = [ ] 
LE = [ ] 

xlogp = [ ]
PFI = [ ] 
ScScore = [ ]
SAR  = [ ]

for i in files:
   with open(i, 'r') as inp3:
      for line in inp3:
         if 'TIME:' in line:
            data = []
            data = line.split()
            scs_dat = str(data[25])
            sar_dat = str(data[13])
            pfi_dat = str(data[7])
            logp_dat = str(data[3])
            aro_dat = str(data[5])
            PSA_dat = str(data[9]) 
            MolW_dat = str(data[11])  
            NAc_dat = str(data[16])
            NDon_dat = str(data[19])
            ratio_dat = str(data[28])
            sp3_dat = str(data[32])
            LLE_dat = str(data[35])
            LE_dat = str(data[38])

            ScScore.append(scs_dat)
            SAR.append(sar_dat)
            PFI.append(pfi_dat)
            xlogp.append(logp_dat)
            aro.append(aro_dat)
            PSA.append(PSA_dat)
            MolW.append(MolW_dat)
            NAc.append(NAc_dat)
            NDon.append(NDon_dat)
            ratio.append(ratio_dat)
            sp3Frac.append(sp3_dat)
            LLE.append(LLE_dat)
            LE.append(LE_dat)


with open('gen2.csv', 'w') as inp:
   inp.write("id," + "smiles," + "MPO_SCORE," + "pIC50," + "PFI," + "logp," + "Ar_rings," + "PSA," +  "MolW," + "NAc," + "NDon," + "(C)/(O)(N)_Ratio," + "sp3_frac," + "LLE," + "LE," + "ScScore" )
   inp.write('\n')
   for (a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p) in zip(num, smiles, dockscore, SAR, PFI, xlogp, aro, PSA, MolW, NAc, NDon, ratio, sp3Frac, LLE, LE, ScScore):
      inp.write(str(a) + "," + str(b) + "," + str(c) + "," + str(d) + "," + str(e) + "," + str(f) + "," + str(g) + "," + str(h) + "," + str(i) + "," + str(j) + "," + str(k) + "," + str(l) + "," + str(m) + "," + str(n) + "," + str(o) + "," + str(p) + "\n")
#
print( 'number of candidates is', len(smiles))
print(len(dockscore))
print(len(PFI))
print(len(SAR))
print(len(xlogp))
print(len(ScScore))
