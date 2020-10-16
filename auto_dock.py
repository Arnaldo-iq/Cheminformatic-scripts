#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
@author: pczaf-Arnaldo-Filho
"""
# Module that converts data from the .csv file from gsk. It used obabel to convert smiles to .xyz. Make sure to load anaconda and Openbabel modules
# Note 1- This can take a while, depending on the number an lines in that spreadsheet 
#
import os, fnmatch, shutil
# Creat our arrays with the group, Molecule name and smiles code
import numpy as np
# Pandas is used for data manipulation
import pandas as pd
#
curr = os.getcwd()
#
# Adquire all data from gsk sheet
molecule_data = pd.read_csv('Test.csv')
#
#get our  smiles codes. Will be used by Openbabel
#
smiles = np.array(molecule_data['Parent_SMILES'])
smiles = list(smiles)

pic50 = np.array(molecule_data['Value'])
pic50 = list(pic50)

# Molecule's name, apparently
parent_compound = np.array(molecule_data['ID'])
parent_compound = list(parent_compound)
#Group that the ligand belongs to:
#
#  ####02###### ##04## ###05####  #######17###### #####01##### ##03## ########07##########
#  7-aryl_ATAQ   THQ   Quinoline  Fuzed triazoles 5-aryl_ATAQ   BZD   Phenyl_sulphonamides
#  ############ ###### #########  ############### ############ ###### #####################
#
group = np.array(molecule_data['Template_Name']) 
# Remove the first three charchters from each element of the array for aesthetics
group = [e[3:] for e in group]
#
#-----------------------Define class object atom_________________
class lig(object):
    def __init__(self, nbr, sml, grp, act):
        self.nbr = nbr
        self.sml = sml
        self.grp = grp
        self.act = act
#_________________________________________________________________
#
my_lig = []
#
# append the charcteristcs of each given ligand
#
for i in range(len(group)):    
    my_lig.append(lig(str(parent_compound[i]), str(smiles[i]), str(group[i]), str(pic50[i])))
#    
#call openbabel and write x,y,z coordinates:
for i in range(len(smiles)):    
    os.system("obabel -:" + "'" + my_lig[i].sml + "' " "-opdb -h --gen3D > " + my_lig[i].nbr + "_" + my_lig[i].grp + "_" + my_lig[i].act + ".pdb")
#ssay_Result_Type_Name
# Save each unique ligand name and group in a list, removing themy_bond.append(bon(lba[i], ra_dat[i], ka_dat[i])) xyz part 
#
ligands=[d for d in os.listdir(curr) if os.path.isfile(d) if fnmatch.fnmatch(d,'*pdb')]
ligands = map(lambda each:each.strip(".pdb"), ligands)
#
#___________ __________Generate the conformers for each ligand_________________
#
for  line in ligands:
    dirName = line
    os.mkdir(dirName)
    os.system("mv " +  dirName + ".pdb " + dirName)
    shutil.copy(curr + '/receptor.oeb.gz', os.path.join(dirName) + '/receptor.oeb.gz')
    os.chdir(os.path.join(dirName))
    os.system("oeomega  classic -in " +  dirName + ".pdb" + " -buildff mmff94s  -rms 0.15 -out ligand.oeb.gz -maxconfs 3000")
    os.system ("sleep 5")
#____________________Dock the ligands___________________________________________
    os.system("fred -dock_resolution High -receptor receptor.oeb.gz -dbase ligand.oeb.gz -docked_molecule_file mol.sdf")
    os.system ("sleep 5")
    os.chdir(os.path.join(curr))
