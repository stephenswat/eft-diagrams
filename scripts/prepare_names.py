import json

names = json.load(open("data/tex_names.json","r"))
parnames = json.load(open("data/parnames.json","r"))
#print(names)
print(names.keys())
print(parnames.keys())

pair = [str(i)+str(j) for i in range(1,4) for j in range(1,4)]
quad = [str(i)+str(j)+str(k)+str(l) for i in range(1,4) for j in range(1,4) for k in range(1,4) for l in range(1,4)]

for case,pars in parnames.items():
    if case == "topU3l":
        dict0 = {}
        print("case : {0} with number of parameters {1}".format(case,str(len(pars))))
        print("\n"+case)
        for par in list(set(pars)):
            #print("searching for {0}\n".format(par))
            found = False
            for texpar in names.keys():
               if texpar == par:
                   par = par.replace("Re","").replace("Im","")
                   dict0[par] = names[texpar].replace("\\e","\\epsilon").replace("\\s_","\\sigma_").replace("\\s^","\\sigma^")
                   found = True
                   print("{0} ----> {1}".format(par, dict0[par]))
               elif par[len(par)-4:] in quad:

#                   print("inside 4")
                   if texpar == par[0:len(par)-4].replace("Re","").replace("Im",""):
                      par = par.replace("Re","").replace("Im","")#.replace("dag","dagger").replace("\\s_","\\sigma_").replace("\\s^","\\sigma^")
                      dict0[par] = "\\big("+ names[texpar].replace("\\e","\\epsilon").replace("=","\\big)_{"+par[len(par)-4:]+"} = \\Big(")+"\\Big)_{"+par[len(par)-4:]+"}".replace("dag","dagger").replace("\\s_","\\sigma_").replace("\\s^","\\sigma^")
                      found = True
                      print("{0} ----> {1}".format(par, dict0[par]))

               elif par[len(par)-2:] in pair:
                   #print("pair"+par[0:len(par)-2])
                   if texpar == par[0:len(par)-2].replace("Re","").replace("Im",""):
                      par = par.replace("Re","").replace("Im","")#.replace("dag","dagger").replace("\\s_","\\sigma_").replace("\\s^","\\sigma^")
                      dict0[par] = "\\big("+ names[texpar].replace("\\e","\\epsilon").replace("=","\\big)_{"+par[len(par)-2:]+"} = \\Big(")+"\\Big)_{"+par[len(par)-2:]+"}".replace("dag","dagger").replace("\\s_","\\sigma_").replace("\\s^","\\sigma^")
                      found = True
                      print("{0} ----> {1}".format(par, dict0[par]))
               elif texpar == par.replace("Re","").replace("Im",""):
                   par = par.replace("Re","").replace("Im","")
                   dict0[par] = names[texpar].replace("\\e","\\epsilon")
                   found = True
                   print("{0} ----> {1}".format(par, dict0[par]))

            if found == False: print("Not found "+par)
        
        with open("out_"+case+".json","w") as f:
             json.dump(dict0,f,indent=4)
