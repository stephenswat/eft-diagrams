import json

names = json.load(open("tex_names.json","r"))
parnames = json.load(open("parnames.json","r"))
#print(names)
print(names.keys())
print(parnames.keys())

for case,pars in parnames.items():
    dict0 = {}
    print("case : {0} with number of parameters {1}".format(case,str(len(pars))))
    print("\n"+case)
    for par in pars:
        found = False
        for texpar in names.keys():
           if texpar in par:
               par = par.replace("Re","").replace("Im","")
               dict0[par] = names[texpar].replace("\\e","\\epsilon")
               found = True
        if found == False: print(par)
    
    with open("out_"+case+".json","w") as f:
         json.dump(dict0,f,indent=2)
