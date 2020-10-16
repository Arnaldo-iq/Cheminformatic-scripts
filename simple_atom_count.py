#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""fileName
Created on Mon Jan  6 13:10:15 2020

@author: pczaf
"""
#
import numpy as np
import pandas as pd
#   
from rdkit import Chem
#
molecular_data = pd.read_csv('gsk1_new.csv')
smiles = np.array(molecular_data['Parent_SMILES'])
#
with open('dumb_input.csv', 'w') as the_file:
    the_file.write('H' +  ',' + 'C' +  ',' + 'O' +  ',' + 'N' +  ',' + 'S' +  ','\
    + 'F' +  ',' + 'Cl' +  ',' + 'Br' +  ',' + 'I' +  ',' + 'P' +  ',' + 'W' +  ',' + 'T')
    the_file.write('\n')
    l=len(smiles)      
    for i in range(l):
        m = Chem.MolFromSmiles(smiles[i])
        n = Chem.AddHs(m)
        mol = []
        for atom in n.GetAtoms():            
            mol.append(atom.GetAtomicNum())
            H = 0 
            C = 0
            O = 0
            N = 0 
            S = 0
            F = 0 
            Cl = 0 
            Br = 0
            I = 0
            P = 0
            W = 0 
            T = 0
            for i in mol:
                if i == 1:
                    H=H+1
                if i == 6:
                    C=C+1
                if i == 8:
                    O=O+1
                if i == 7:
                    N=N+1
                if i == 16:
                    S=S+1
                if i == 9:
                    F=F+1
                if i == 17:
                    Cl=Cl+1
                if i == 35:
                    Br=Br+1
                if i == 53:
                    I=I+1
                if i == 15:
                    P=P+1
        T = H+C+O+N+S+F+Cl+Br+I+P
        W = C+O+N+S+F+Cl+Br+I+P
        the_file.write(str(H) + ',' +  str(C) + "," + str(O) + "," + str(N) + "," + str(S) + "," + str(F) \
        + "," + str(Cl) + "," + str(Br) + "," + str(I) + "," + str(P) +  ',' + str(W) + ',' + str(T))
        the_file.write(' \n')
