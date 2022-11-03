# this script extracts the results from dineroIV
# and aggregates them into csv files for each case

import subprocess
import os
import pandas as pd
import numpy as np

bsize = ["32","64","128"]
l1size = ["16K","32K"]
l2size = ["512K","1M","2M"]
policy = ["l","r","f"]
assoc = ["1","2","4"]

rootdir = "/home/rozirr/dinero/d4-7"
os.chdir(rootdir+"/Spec_Benchmark")
inputs = subprocess.check_output(['ls'])
inputs = inputs.decode('utf-8').split()
os.chdir(rootdir+"/results")

print(inputs)

case1 = []

for i in range(3):
    for j in range(2):
        for k in range(3):

            #l1i hit
            name = bsize[i]+"_"+l1size[j]+"_"+l2size[k]
            combo = name+"_l1i_h"
            case1.append([combo])
            for input in inputs: 
                file = "case_1/"+input+"/"+name+".txt"
                with open (file, 'rt') as myfile:
                    lines = myfile.readlines()
                    line = lines[44].split()
                    case1[len(case1)-1].append(line[2])

            #l1i miss
            name = bsize[i]+"_"+l1size[j]+"_"+l2size[k]
            combo = name+"_l1i_m"
            case1.append([combo])
            for input in inputs:
                file = "case_1/"+input+"/"+name+".txt"
                with open (file, 'rt') as myfile:
                    lines = myfile.readlines()
                    line = lines[47].split()
                    case1[len(case1)-1].append(line[2])
            
            #l1d hit
            name = bsize[i]+"_"+l1size[j]+"_"+l2size[k]
            combo = name+"_l1d_h"
            case1.append([combo])
            for input in inputs: 
                file = "case_1/"+input+"/"+name+".txt"
                with open (file, 'rt') as myfile:
                    lines = myfile.readlines()
                    line = lines[61].split()
                    case1[len(case1)-1].append(line[2])

            #l1d miss
            name = bsize[i]+"_"+l1size[j]+"_"+l2size[k]
            combo = name+"_l1d_m"
            case1.append([combo])
            for input in inputs:
                file = "case_1/"+input+"/"+name+".txt"
                with open (file, 'rt') as myfile:
                    lines = myfile.readlines()
                    line = lines[64].split()
                    case1[len(case1)-1].append(line[2])
            
            #l2 hit
            name = bsize[i]+"_"+l1size[j]+"_"+l2size[k]
            combo = name+"_l2_h"
            case1.append([combo])
            for input in inputs: 
                file = "case_1/"+input+"/"+name+".txt"
                with open (file, 'rt') as myfile:
                    lines = myfile.readlines()
                    line = lines[78].split()
                    case1[len(case1)-1].append(line[2])

            #l2 miss
            name = bsize[i]+"_"+l1size[j]+"_"+l2size[k]
            combo = name+"_l2_m"
            case1.append([combo])
            for input in inputs:
                file = "case_1/"+input+"/"+name+".txt"
                with open (file, 'rt') as myfile:
                    lines = myfile.readlines()
                    line = lines[81].split()
                    case1[len(case1)-1].append(line[2])

                    
arr = np.asarray(case1).transpose()
#pd.DataFrame(arr).to_csv('case1.csv') 

case2 = []

for i in range(3):
    for j in range(2):
        for k in range(3):
            for l in range(3):
                #l1i hit 
                name = bsize[i]+"_"+l1size[j]+"_"+l2size[k]+"_"+policy[l]
                combo = name+"_l1i_h"
                case2.append([combo])
                for input in inputs: 
                    file = "case_2/"+input+"/"+name+".txt"
                    with open (file, 'rt') as myfile:
                        lines = myfile.readlines()
                        line = lines[44].split()
                        case2[len(case2)-1].append(line[2])

                #l1i miss
                name = bsize[i]+"_"+l1size[j]+"_"+l2size[k]+"_"+policy[l]
                combo = name+"_l1i_m"
                case2.append([combo])
                for input in inputs:
                    file = "case_2/"+input+"/"+name+".txt"
                    with open (file, 'rt') as myfile:
                        lines = myfile.readlines()
                        line = lines[47].split()
                        case2[len(case2)-1].append(line[2])
                
                #l1d hit
                name = bsize[i]+"_"+l1size[j]+"_"+l2size[k]+"_"+policy[l]
                combo = name+"_l1d_h"
                case2.append([combo])
                for input in inputs: 
                    file = "case_2/"+input+"/"+name+".txt"
                    with open (file, 'rt') as myfile:
                        lines = myfile.readlines()
                        line = lines[61].split()
                        case2[len(case2)-1].append(line[2])

                #l1d miss
                name = bsize[i]+"_"+l1size[j]+"_"+l2size[k]+"_"+policy[l]
                combo = name+"_l1d_m"
                case2.append([combo])
                for input in inputs:
                    file = "case_2/"+input+"/"+name+".txt"
                    with open (file, 'rt') as myfile:
                        lines = myfile.readlines()
                        line = lines[64].split()
                        case2[len(case2)-1].append(line[2])
                
                #l2 hit
                name = bsize[i]+"_"+l1size[j]+"_"+l2size[k]+"_"+policy[l]
                combo = name+"_l2_h"
                case2.append([combo])
                for input in inputs: 
                    file = "case_2/"+input+"/"+name+".txt"
                    with open (file, 'rt') as myfile:
                        lines = myfile.readlines()
                        line = lines[78].split()
                        case2[len(case2)-1].append(line[2])

                #l2 miss
                name = bsize[i]+"_"+l1size[j]+"_"+l2size[k]+"_"+policy[l]
                combo = name+"_l2_m"
                case2.append([combo])
                for input in inputs:
                    file = "case_2/"+input+"/"+name+".txt"
                    with open (file, 'rt') as myfile:
                        lines = myfile.readlines()
                        line = lines[81].split()
                        case2[len(case2)-1].append(line[2])

                    
arr = np.asarray(case2).transpose()
#pd.DataFrame(arr).to_csv('case2.csv') 

case3 = []

for i in range(3):
    for j in range(2):
        for k in range(3):
            for l in range(3):
                #l1i hit 
                name = bsize[i]+"_"+l1size[j]+"_"+l2size[k]+"_"+assoc[l]
                combo = name+"_l1i_h"
                case3.append([combo])
                for input in inputs: 
                    file = "case_3/"+input+"/"+name+".txt"
                    with open (file, 'rt') as myfile:
                        lines = myfile.readlines()
                        line = lines[44].split()
                        case3[len(case3)-1].append(line[2])

                #l1i miss
                name = bsize[i]+"_"+l1size[j]+"_"+l2size[k]+"_"+assoc[l]
                combo = name+"_l1i_m"
                case3.append([combo])
                for input in inputs:
                    file = "case_3/"+input+"/"+name+".txt"
                    with open (file, 'rt') as myfile:
                        lines = myfile.readlines()
                        line = lines[47].split()
                        case3[len(case3)-1].append(line[2])
                
                #l1d hit
                name = bsize[i]+"_"+l1size[j]+"_"+l2size[k]+"_"+assoc[l]
                combo = name+"_l1d_h"
                case3.append([combo])
                for input in inputs: 
                    file = "case_3/"+input+"/"+name+".txt"
                    with open (file, 'rt') as myfile:
                        lines = myfile.readlines()
                        line = lines[61].split()
                        case3[len(case3)-1].append(line[2])

                #l1d miss
                name = bsize[i]+"_"+l1size[j]+"_"+l2size[k]+"_"+assoc[l]
                combo = name+"_l1d_m"
                case3.append([combo])
                for input in inputs:
                    file = "case_3/"+input+"/"+name+".txt"
                    with open (file, 'rt') as myfile:
                        lines = myfile.readlines()
                        line = lines[64].split()
                        case3[len(case3)-1].append(line[2])
                
                #l2 hit
                name = bsize[i]+"_"+l1size[j]+"_"+l2size[k]+"_"+assoc[l]
                combo = name+"_l2_h"
                case3.append([combo])
                for input in inputs: 
                    file = "case_3/"+input+"/"+name+".txt"
                    with open (file, 'rt') as myfile:
                        lines = myfile.readlines()
                        line = lines[78].split()
                        case3[len(case3)-1].append(line[2])

                #l2 miss
                name = bsize[i]+"_"+l1size[j]+"_"+l2size[k]+"_"+assoc[l]
                combo = name+"_l2_m"
                case3.append([combo])
                for input in inputs:
                    file = "case_3/"+input+"/"+name+".txt"
                    with open (file, 'rt') as myfile:
                        lines = myfile.readlines()
                        line = lines[81].split()
                        case3[len(case3)-1].append(line[2])

                    
arr = np.asarray(case3).transpose()
#pd.DataFrame(arr).to_csv('case3.csv') 