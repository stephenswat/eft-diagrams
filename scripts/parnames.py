import json
import glob

files = glob.glob("data/data_redpars_*.json")
json.dump({x.replace("data/data_redpars_","").replace(".json","") : json.load(open(x)).keys()   for x in files},open("out.json","w"),indent=1)
