# Python library for in/out
from csv import reader, writer
# Python module
from operator import itemgetter
# system module
import sys

# Read data into a dictionary
drug_dict = {}
with open(sys.argv[1]) as csvfin:
    fin = reader(csvfin)
    iline=0
    for fields in fin:
        iline +=1
        if iline >1:
            if len(fields) == 5:
                idname = fields[1].strip().upper()+'_'+fields[2].strip().upper()
                if fields[3] not in drug_dict:
                    # adding new drug to dictionary
                    drug_dict[fields[3]] = [int(fields[4]),idname]
                else:
                    # sum the total cost and add individual name to list of individuals who prescribed the medication 
                    drug_dict[fields[3]][0] += int(fields[4])
                    drug_dict[fields[3]].append(idname)

# List of drug
drug_list = []
for key in drug_dict.keys():
    nindividuals = len(set(drug_dict[key][1:]))
    drug_list.append((key, nindividuals, drug_dict[key][0]))

# Sorting list by cost and drug name
drug_list_sorted = sorted(drug_list, key=itemgetter(2,0), reverse=True)

# Writing output data file
with open(sys.argv[2],'w') as csvfout:
    fout = writer(csvfout)
    csvfout.write('drug_name,num_prescriber,total_cost\n')
    for i in range(len(drug_list_sorted)):
        fout.writerow(drug_list_sorted[i])
