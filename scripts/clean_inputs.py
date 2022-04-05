import json 
import glob

files = glob.glob("data/data_*.json")

dicts = {name.split("/")[1].replace("data_","").replace(".json","") : json.load(open(name)) for name in files}

allpars = { x : map0.keys() for x,map0 in dicts.items()}
#print(allpars)

redpars = {x : [] for x in dicts.keys()}
new_map = {}
for case,pars in allpars.items():
   new_map[case] = {}
   for par in pars:
       if "Im" in par:
           par_new = par.replace("Im","")
           redpars[case].append(par)
           new_map[case][par_new] = dicts[case][par] 
       elif "Re" in par:
           par_new = par.replace("Re","")
           redpars[case].append(par)
           new_map[case][par_new] = dicts[case][par]        
       elif par == "cth" : continue
       else:
           new_map[case][par] = dicts[case][par]

for case,map0 in new_map.items():
    print("\n\n{0}".format(case))
    json.dump(map0,open("data/data_redpars_"+case+".json","w"),indent=4)
    for par in sorted(map0.keys()):
        print("<option value=\"{0}\">{0}</option>".format(par))
#for x,map0 in dicts.items():
#    new_map[x] = {}
#    for par, mapped_par in map0.items():
#        if(par == "cth"): continue
   
