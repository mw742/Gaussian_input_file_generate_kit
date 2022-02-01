#############################################################################################################
##
## This is a script to run some functions of Macrromodel(Maestro interface) using command line automatically
## to run the task including minimation/conformational searchin etc.
## we need a structure file end with .mae format and a command file end with .com format
##
##
## script was written by the illustraction of macromodel_reference_manual
##
#############################################################################################################

import os


##for each .mol2  file  in dataset, convert them into .mae format that could be used in  Maestro
def mol2_to_mae():
    mol_order=0
    while mol_order < 10:
        with open("mol2_to_mae_"+str(mol_order)+".sh","a+") as f:
            f.write("#!/bin/bash")
            f.write("\n")
            ## using openbabel files format convert functions
            f.write("obabel compare_"+str(mol_order)+".mol -O mini_"+str(mol_order)+".mol2")
            f.write("\n")
            ## using structureconvert function in university work station system,
            ## more explaination can be found with tying structconvert -h
            f.write("/shared/shared/schrodinger/2019-1/utilities/structconvert -imol2 mini_"+str(mol_order)+".mol2 -omae mini_"+str(mol_order)+".mae")
            f.write("\n")
        f.close()
        command="bash "+"mol2_to_mae_"+str(mol_order)+".sh"
        os.system(command)
        mol_order+=1


##for each mol wile  a structure file .mae  and a command file .com
##write the bash file for them
def write_CSbash_file():
    mol_order=0
    while mol_order < 10:
        with open("mini_"+str(mol_order)+".sh","a+") as f2:
            f2.write("#!/bin/bash")
            f2.write("\n")
            f2.write("/shared/shared/schrodinger/2019-1/bmin -WAIT mini_"+str(mol_order))
            f2.write("\n")
            #f2.write("/shared/shared/schrodinger/2019-1/utilities/structconvert -imae mini_"+str(mol_order)+"-out.maegz -osd mini_"+str(mol_order)+"_result.sdf")
        f2.close()
        mol_order+=1

##for each bash file for conformational searchinng in MacroModel, run them one by one
def run_CS_onebyone():
    mol_order=0
    while mol_order < 10:
        command="bash mini_"+str(mol_order)+".sh"
        os.system(command)
        mol_order+=1

##for each output .maegz file, convert them into .sdf format for further comparison with the results of Diamond_energy program
def convert2sdf_file():
    mol_order=0
    while mol_order < 10:
        with open("convert2sdf_"+str(mol_order)+".sh","a+") as f3:
            f3.write("#!/bin/bash")
            f3.write("\n")
            f3.write("/shared/shared/schrodinger/2019-1/utilities/structconvert -imae mini_"+str(mol_order)+"-out.maegz -n 1 -osd mini_"+str(mol_order)+".sdf")
        f3.close()
        command="bash convert2sdf_"+str(mol_order)+".sh"
        os.system(command)
        mol_order+=1


## .com file fpr minimation task
def mini_file_write():
    mol_order=0
    while mol_order < 10:
        with open("mini_"+str(mol_order)+".com", "a+") as f4:
            f4.write("mini_"+str(mol_order)+".mae")
            f4.write("\n")
            f4.write("mini_"+str(mol_order)+"-out.maegz")
            f4.write("\n")
            f4.write(" MMOD       0      1      0      0     0.0000     0.0000     0.0000     0.0000\n")
            f4.write(" DEBG      55      0      0      0     0.0000     0.0000     0.0000     0.0000\n")
            f4.write(" DEBG    1003      0      0      0     0.0000     0.0000     0.0000     0.0000\n")
            f4.write(" FFLD       1      1      0      0     1.0000     0.0000     0.0000     0.0000\n")
            f4.write(" BDCO       0      0      0      0    41.5692 99999.0000     0.0000     0.0000\n")
            f4.write(" CRMS       0      0      0      0     0.0000     0.5000     0.0000     0.0000\n")
            f4.write(" BGIN       0      0      0      0     0.0000     0.0000     0.0000     0.0000\n")
            f4.write(" READ       0      0      0      0     0.0000     0.0000     0.0000     0.0000\n")
            f4.write(" CONV       2      0      0      0     0.0500     0.0000     0.0000     0.0000\n")
            f4.write(" MINI       1      0   2500      0     0.0000     0.0000     0.0000     0.0000\n")
            f4.write(" END        0      0      0      0     0.0000     0.0000     0.0000     0.0000\n")
        f4.close()
        mol_order+=1



#####################################################
##
## run the funtion needed below by remove the
## "#" to call each funtion
##
#####################################################

#mol2_to_mae()
#generate_com_file()
#write_CSbash_file()
#run_CS_onebyone()
convert2sdf_file()
#mini_file_write()
