import csv

data = {
    "2019" : {
        "treatment" : [],
        "buffer" : []
},
    "2020" : {
        "treatment" : [],
        "buffer" : []
    },
    "2021" : {
        "treatment" : [],
        "buffer" : []
    },
    "2022" : {
        "treatment" : [],
        "buffer" : []
    }
}


with open('data_table.csv','r') as data_table:
    reader = csv.reader(data_table)
    skipFirst = False
    for read_row in reader:
        if skipFirst == False:
            first_row = read_row
            skipFirst = True
            #print(first_row)
        else:
            year = read_row[0]
            oid = read_row[1]
            buffer = read_row[2]
            data[year][buffer].append(oid)
            #print(f"{year}, {buffer}, {oid}")

for year in data:
    for buffer in data[year]:
        print(f"{year}, {buffer} : {len(data[year][buffer])}")