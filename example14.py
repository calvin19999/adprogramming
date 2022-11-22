import csv

file=open("TitanicSurvival.csv","r")
data = list (csv.reader(file,delimiter=","))
file.close()
#for i in range(1,(len(data))):
# data[i][-1]='1st'

data[-1][4]="1st"
data[-1].append("GOOD PERSON")
print(data)


