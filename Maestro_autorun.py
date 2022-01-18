

import os


##for each .mol2  file  in dataset, convert them into .mae format that could be used in  Maestro
def mol2_to_mae():
    mol_order=0
    while mol_order < 14:
        with open("mol2_to_mae_"+str(mol_order)+".sh","a+") as f:
            f.write("#!/bin/bash")
            f.write("\n")
            f.write("obabel compare_"+str(mol_order)+"_.sdf -O compare_"+str(mol_order)+".mol2")
            f.write("\n")
            f.write("/shared/shared/schrodinger/2019-1/utilities/structconvert -imol2 compare_"+str(mol_order)+".mol2 -omae compare_"+str(mol_order)+".mae")
            f.write("\n")
        f.close()
        command="bash "+"mol2_to_mae_"+str(mol_order)+".sh"
        os.system(command)
        mol_order+=1


##generate .com file for each mol
## for this part, the correct and complete code is stored in torsion_angle.py script, where the script could loop through
## all the molecule list and generate corresponding CS .com file for them
def generate_com_file():
    mol_order=0
    while mol_order < 14:
        with open("compare_"+str(mol_order)+".com","a+")  as f1:
            f1.write("compare_"+str(mol_order)+".mae")
            f1.write("\n")
            f1.write("compare_"+str(mol_order)+"-out.maegz")
            f1.write("\n")
            f1.write(" MMOD       0      1      0      0     0.0000     0.0000     0.0000     0.0000 \n")
            f1.write(" DEBG      55      0      0      0     0.0000     0.0000     0.0000     0.0000 \n")
            f1.write(" DEBG    1003      0      0      0     0.0000     0.0000     0.0000     0.0000 \n")
            f1.write(" FFLD       1      1      0      0     1.0000     0.0000     0.0000     0.0000 \n")
            f1.write(" BDCO       0      0      0      0    41.5692 99999.0000     0.0000     0.0000 \n")
            f1.write(" CRMS       0      0      0      0     0.0000     0.5000     0.0000     0.0000 \n")
            f1.write(" BGIN       0      0      0      0     0.0000     0.0000     0.0000     0.0000 \n")
            f1.write(" READ       0      0      0      0     0.0000     0.0000     0.0000     0.0000 \n")
            f1.write(" CONV       2      0      0      0     0.0500     0.0000     0.0000     0.0000 \n")
            f1.write(" MINI       1      0   2500      0     0.0500     0.0000     0.0000     0.0000 \n")
            f1.write(" END        0      0      0      0     0.0000     0.0000     0.0000     0.0000 \n")
        f1.close()
        mol_order+=1


##for each mol wile  a structure file .mae  and a command file .com
##write the bash file for them
def write_CSbash_file():
    mol_order=0
    while mol_order < 15:
        with open("cs_test_"+str(mol_order)+".sh","a+") as f2:
            f2.write("#!/bin/bash")
            f2.write("\n")
            f2.write("/shared/shared/schrodinger/2019-1/bmin -WAIT compare_"+str(mol_order))
            f2.write("\n")
            f2.write("/shared/shared/schrodinger/2019-1/utilities/structconvert -imae compare_"+str(mol_order)+"-out.maegz -osd compare_"+str(mol_order)+".sdf")
        f2.close()
        mol_order+=1

##for each bash file for conformational searchinng in MacroModel, run them one by one
def run_CS_onebyone():
    mol_order=0
    while mol_order < 14:
        command="bash cs_test_"+str(mol_order)+".sh"
        os.system(command)
        mol_order+=1

##for each output .maegz file, convert them into .sdf format for further comparison with the results of Diamond_energy program
def convert2sdf_file():
    mol_order=0
    while mol_order < 14:
        with open("convert2sdf_"+str(mol_order)+".sh","a+") as f3:
            f3.write("#!/bin/bash")
            f3.write("\n")
            f3.write("/shared/shared/schrodinger/2019-1/utilities/structconvert -imae compare_"+str(mol_order)+"-out.maegz -n 1 -osd compare_"+str(mol_order)+".sdf")
        f3.close()
        command="bash convert2sdf_"+str(mol_order)+".sh"
        os.system(command)
        mol_order+=1



#mol2_to_mae()
#generate_com_file()
#write_CSbash_file()
#run_CS_onebyone()
convert2sdf_file()