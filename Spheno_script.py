#! /usr/bin/python3

import os

######################
### 0. SET FOLDERS ###
######################

current_dir = os.getcwd() + "/"
#os.chdir(current_dir)

spheno_folder = "/home/juri/Documents/Munster/SPheno/SPheno-4.0.3/"
input_folder = current_dir
output_folder = input_folder

template_slha_file_name = "SPheno_input_wino.in"

#os.chdir(input_folder)

###################
### 1. GAUGINOS ###
###################

mu = 3000

tanb = 5

M3 = 5000 ### decouple gluinos
A0 = -500

#### Mostly bino scenario
#M1 = 100
#M2 = 2000

### Mostly wino scenario
M1 = 2000
M2 = 100




# Initialize

template_slha_file = open(template_slha_file_name, "r")
slha_text = template_slha_file.read()
template_slha_file.close()

### M1
old_M1_line = " 1   1.000000E+02       # M1 (Bino mass)"
new_M1_line = " 1   " + str("{:.6E}".format(M1)) + "       # M1 (Bino mass)"
slha_text = slha_text.replace(old_M1_line, new_M1_line)

### M2
old_M2_line = " 2   1.000000E+02       # M2 (Wino mass)"
new_M2_line = " 2   " + str("{:.6E}".format(M2)) + "       # M2 (Wino mass)"
slha_text = slha_text.replace(old_M2_line, new_M2_line)

### M3
old_M3_line = " 3   5.800000E+02       # M3 (gluino mass)"
new_M3_line = " 3   " + str("{:.6E}".format(M3)) + "       # M3 (gluino mass)"
slha_text = slha_text.replace(old_M3_line, new_M3_line)

### mA0
old_mA0_line = "26   4.000000E+02       # mA0"
new_mA0_line = "26   " + str("{:.6E}".format(M3)) + "       # mA0"
slha_text = slha_text.replace(old_mA0_line, new_mA0_line)

### squark diagonal
old_squark1_line = "41   5.000000E+02       # M~Q1_L"
new_squark1_line = "41   " + str("{:.6E}".format(M3)) + "       # M~Q1_L"
slha_text = slha_text.replace(old_squark1_line, new_squark1_line)

old_squark2_line = "42   5.000000E+02       # M~Q2_L"
new_squark2_line = "42   " + str("{:.6E}".format(M3)) + "       # M~Q2_L"
slha_text = slha_text.replace(old_squark2_line, new_squark2_line)

old_squark3_line = "43   4.000000E+02       # M~Q3_L"
new_squark3_line = "43   " + str("{:.6E}".format(M3)) + "       # M~Q3_L"
slha_text = slha_text.replace(old_squark3_line, new_squark3_line)

old_uR_line = "44   5.000000E+02       # M~u_R"
new_uR_line = "44   " + str("{:.6E}".format(M3)) + "       # M~u_R"
slha_text = slha_text.replace(old_uR_line, new_uR_line)

old_cR_line = "45   5.000000E+02       # M~c_R"
new_cR_line = "45   " + str("{:.6E}".format(M3)) + "       # M~c_R"
slha_text = slha_text.replace(old_cR_line, new_cR_line)

old_tR_line = "46   5.000000E+02       # M~t_R"
new_tR_line = "46   " + str("{:.6E}".format(M3)) + "       # M~t_R"
slha_text = slha_text.replace(old_tR_line, new_tR_line)

old_dR_line = "47   5.000000E+02       # M~d_R"
new_dR_line = "47   " + str("{:.6E}".format(M3)) + "       # M~d_R"
slha_text = slha_text.replace(old_dR_line, new_dR_line)

old_sR_line = "48   5.000000E+02       # M~s_R"
new_sR_line = "48   " + str("{:.6E}".format(M3)) + "       # M~s_R"
slha_text = slha_text.replace(old_sR_line, new_sR_line)

old_bR_line = "49   5.000000E+02       # M~b_R"
new_bR_line = "49   " + str("{:.6E}".format(M3)) + "       # M~b_R"
slha_text = slha_text.replace(old_bR_line, new_bR_line)

### squark mixing
old_At_line = "11  -5.000000E+02       # At"
new_At_line = "11  " + str("{:.6E}".format(A0)) + "       # At"
slha_text = slha_text.replace(old_At_line, new_At_line)

old_Ab_line = "12  -8.000000E+02       # Ab"
new_Ab_line = "12  " + str("{:.6E}".format(A0)) + "       # Ab"
slha_text = slha_text.replace(old_Ab_line, new_Ab_line)

### slepton diagonal
old_eL_line = "31   2.000000E+02       # M~e_L"
new_eL_line = "31   " + str("{:.6E}".format(M3)) + "       # M~e_L"
slha_text = slha_text.replace(old_eL_line, new_eL_line)

old_muL_line = "32   2.000000E+02       # M~mu_L"
new_muL_line = "32   " + str("{:.6E}".format(M3)) + "       # M~mu_L"
slha_text = slha_text.replace(old_muL_line, new_muL_line)

old_tauL_line = "33   2.000000E+02       # M~tau_L"
new_tauL_line = "33   " + str("{:.6E}".format(M3)) + "       # M~tau_L"
slha_text = slha_text.replace(old_tauL_line, new_tauL_line)

old_eR_line = "34   1.500000E+02       # M~e_R"
new_eR_line = "34   " + str("{:.6E}".format(M3)) + "       # M~e_R"
slha_text = slha_text.replace(old_eR_line, new_eR_line)

old_muR_line = "35   1.500000E+02       # M~mu_R"
new_muR_line = "35   " + str("{:.6E}".format(M3)) + "       # M~mu_R"
slha_text = slha_text.replace(old_muR_line, new_muR_line)

old_tauR_line = "36   1.500000E+02       # M~tau_R"
new_tauR_line = "36   " + str("{:.6E}".format(M3)) + "       # M~tau_R"
slha_text = slha_text.replace(old_tauR_line, new_tauR_line)

### slepton mixing
old_Atau_line = "13  -2.500000E+02       # Atau"
new_Atau_line = "13  " + str("{:.6E}".format(A0)) + "       # Atau"
slha_text = slha_text.replace(old_Atau_line, new_Atau_line)

### mu
old_mu_line = "23   1.000000E+02       # mu"
new_mu_line = "23   " + str("{:.6E}".format(mu)) + "       # mu"
slha_text = slha_text.replace(old_mu_line, new_mu_line)

### tanbeta
old_tanb_line = "25   1.000000E+01       # tan(beta)"
new_tanb_line = "25   " + str("{:.6E}".format(tanb)) + "       # tan(beta)"
slha_text = slha_text.replace(old_tanb_line, new_tanb_line)

### Save slha file
slha_file_name = "mu_"+str(mu)+"_tanb_"+str(tanb)+"_M1_"+str(M1)+"_M2_"+str(M2)+".in"
slha_file = open(slha_file_name, "w")
slha_file.write(slha_text)
slha_file.close()

### RUN SPHENO
print("Running SPheno for M1 = " + str(M1) + ", M2 = " + str(M2) + ", mu = " + str(mu) + ", tanb = " + str(tanb))
slha_output_file_name = "mu_"+str(mu)+"_tanb_"+str(tanb)+"_M1_"+str(M1)+"_M2_"+str(M2)+".out"
command = spheno_folder + "bin/SPheno " + input_folder + slha_file_name + " " + output_folder + slha_output_file_name
os.system(command)
