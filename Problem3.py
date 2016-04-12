import pdb

lines = [line.rstrip('/n') for line in open('elelib.std')]
data = []
for line in lines: 
    data.append(line.split())

    

Eledict = {}
Elenames = []
EleMM = []
EleZ = []
Elerho = []
Elenumisos = []
Elemassnums= []
EleAbund = []



Number_of_lines = len(data)
#Number of lines
line_number = 0
element_number = -1
while line_number < Number_of_lines:
#    if len(data[line_number]) == 5:
        element_number = element_number + 1
        Elenames.append(data[line_number][0])
        EleMM.append(data[line_number][1])
        EleZ.append(data[line_number][2])
        Elerho.append(data[line_number][3])
        Elenumisos.append(data[line_number][4])

	pdb.set_trace()
        for num in range(int(Elenumisos[line_number])):
            abundances = [] 
            massnums = [] 
            for isotope in range(int(Elenumisos[element_number])):
                massnums.append(data[element_number + isotope+1][0])
                abundances.append(data[line_number + isotope+1][1]) 
                Elemassnums.append(massnums) 
                EleAbund.append(abundances)
        
        line_number = line_number + int(data[line_number][4]) + 1
