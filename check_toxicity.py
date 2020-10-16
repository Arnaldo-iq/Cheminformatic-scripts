#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
#
@author: pczaf
"""
from __future__ import print_function
from openeye import oechem
import openeye.oechem as oe
from openeye.oechem import oemolistream, oemolostream


toxic_fragment_list = ['BrCC',
                       'CCBr',
                       'ClCC',
                       'CCCl',
                       'CCF',
                       'CC=O',
                       'CC(=O)C',
                       'CN(C)N',
                       'C=CC',
                       'CC=NO',
                       'C1CN1',
                       'C1CO1',
                       'CNN',
                       'SC',
                       'O=CNC=O',
                       'O=CCC=O ',
                       'O(C=O)C=O',
                       '[S](=O)(=O)NO',
                       'C(=O)C',
                       'CN(C)N',
                       'NC(=O)O',
                       'CC=C',
                       'CNN',
                       'CCCCCCCCCC',
                       'CC(=S)N',
                       'C(CO)O',
                       'O(C(=O)C)C',
                       'C([N+]([O-])=O)',
                       'CC#C',
                       'O(CCO)C',
                       'O=C1CCC(=O)C=C1',
                       'Nc1ccccc1']



def nonallowed_toxic_fragments(mol_file):


    oe_in_file = oe.oemolistream()
    oe_in_file.open(mol_file) 
    mols = oe_in_file.GetOEMols()
    for mol in oe_in_file.GetOEMols():
        molecule = oe.OEMolToSmiles(mol)     
        for fragment in toxic_fragment_list:
            fragment_search = oe.OESubSearch(fragment)
            oe.OEPrepareSearch(molecule, fragment_search)
            if fragment_search.SingleMatch(molecule):
                return False
                break

        return True


test = nonallowed_toxic_fragments('mol.mol')
