import json
import glob
from get_indicateurs import *
import multiprocessing as mp

res = {}


items = ["taux_incidence","hospitalisations","soins_critiques","deces","vaccins","cas_positifs","taux_positivite"]

res['taux_incidence'] = getTauxIncidence()
res['hospitalisations'] = getHospitalisations()
res['hospitalisations_moyenne_quotidien'] = getMeanHospitalisations()
res['soins_critiques'] = getReas()
res['soins_critiques_moyenne_quotidien'] = getMeanReas()
res['deces'] = getDeces()
res['deces_moyenne_quotidien'] = getMeanDeces()
res['vaccins_premiere_dose'] = getFirstDoseVaccins()
res['vaccins_vaccines'] = getFullVaccins()
res['cas_positifs'] = getCasPositifs()
res['taux_positivite'] = getTauxPositivite()

for item in res:
    with open('data/'+item+'.json','w') as fp:
        json.dump(res[item], fp)

resglobal = {}
files = glob.glob("data/*.json")

for file in files:
    with open(file) as json_file:
        print(file.replace('data/','').replace('.json',''))
        resglobal[file.replace('data/','').replace('.json','')] = json.load(json_file)

with open('global_new.json','w') as fp:
    json.dump(resglobal, fp)
 