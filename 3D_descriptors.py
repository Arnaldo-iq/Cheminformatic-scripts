#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 11 25:34:12 2020
#
@author: pczaf
"""
from rdkit import Chem
from rdkit.Chem.Draw import IPythonConsole
from rdkit.Chem import rdMolDescriptors
from rdkit.Chem import AllChem
from rdkit.Chem import Descriptors3D
from rdkit.Chem import PandasTools

import numpy as np
import pandas as pd


molecular_data = pd.read_csv('liter.csv')

smiles = np.array(molecular_data['smiles'])

print(smiles)

for mol in smiles:

   m = Chem.AddHs(Chem.MolFromSmiles(mol))

   ps = AllChem.ETKDGv2()
   ps.randomSeed = 0xf00d
   AllChem.EmbedMolecule(m,ps)

   descrs = ('PBF','PMI1','PMI2','PMI3','NPR1','NPR2','RadiusOfGyration','InertialShapeFactor', 'Eccentricity','Asphericity','SpherocityIndex')
   for descr in descrs:
       calc_fn = getattr(rdMolDescriptors,'Calc%s'%descr)
       print(f"{descr} {calc_fn(m):.4f}")
