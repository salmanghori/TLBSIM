# this script calls dineroIV for each parameter and each case

import subprocess
import os

bsize = ["32","64","128"]
l1size = ["16K","32K"]
l2size = ["512K","1M","2M"]

rootdir = "/home/rozirr/dinero/d4-7"
os.chdir(rootdir+"/Spec_Benchmark")
inputs = subprocess.check_output(['ls'])
inputs = inputs.decode('utf-8').split()
os.chdir(rootdir)

# case 1
for input in inputs:
    os.mkdir("results/case_1/"+input)
    print("started "+input)

    for i in range(3):
        for j in range(2):
            for k in range(3):
                arguments = ("./dineroIV"+" -l1-isize "+l1size[j]+" -l1-ibsize "+bsize[i]+" -l1-irepl r "+" -l1-iassoc 1 "+
                                " -l1-dsize "+l1size[j]+" -l1-dbsize "+bsize[i]+" -l1-drepl r "+" -l1-dassoc 1 "+
                                " -l2-usize "+l2size[k]+" -l2-ubsize "+bsize[i]+" -l2-urepl r "+" -l2-uassoc 1 "+
                                " -informat d "+" < Spec_Benchmark/"+input+" "+" > results/case_1/"+input+"/"+bsize[i]+"_"+l1size[j]+"_"+l2size[k]+".txt")
                os.system(arguments)

policy = ["l","r","f"]

# case 2
for input in inputs:
    os.mkdir("results/case_2/"+input)
    print("started "+input)

    for i in range(3):
        for j in range(2):
            for k in range(3):
                for l in range(3):
                    arguments = ("./dineroIV"+" -l1-isize "+l1size[j]+" -l1-ibsize "+bsize[i]+" -l1-irepl "+policy[l]+" "+" -l1-iassoc 1 "+
                                            " -l1-dsize "+l1size[j]+" -l1-dbsize "+bsize[i]+" -l1-drepl "+policy[l]+" "+" -l1-dassoc 1 "+
                                            " -l2-usize "+l2size[k]+" -l2-ubsize "+bsize[i]+" -l2-urepl "+policy[l]+" "+" -l2-uassoc 4 "+
                                            " -informat d "+" < Spec_Benchmark/"+input+" "+" > results/case_2/"+input+"/"+bsize[i]+"_"+l1size[j]+"_"+l2size[k]+"_"+policy[l]+".txt")
                    os.system(arguments)


assoc = ["1","2","4"]

# case 3
for input in inputs:
    os.mkdir("results/case_3/"+input)
    print("started "+input)

    for i in range(3):
        for j in range(2):
            for k in range(3):
                for l in range(3):
                    arguments = ("./dineroIV"+" -l1-isize "+l1size[j]+" -l1-ibsize "+bsize[i]+" -l1-irepl r "+" -l1-iassoc "+assoc[l]+" "+
                                            " -l1-dsize "+l1size[j]+" -l1-dbsize "+bsize[i]+" -l1-drepl r "+" -l1-dassoc "+assoc[l]+" "+
                                            " -l2-usize "+l2size[k]+" -l2-ubsize "+bsize[i]+" -l2-urepl r "+" -l2-uassoc "+assoc[l]+" "+
                                            " -informat d "+" < Spec_Benchmark/"+input+" "+" > results/case_3/"+input+"/"+bsize[i]+"_"+l1size[j]+"_"+l2size[k]+"_"+assoc[l]+".txt")
                    os.system(arguments)