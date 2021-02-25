
import re
file = open("LGPL.txt","rt")
filetostring = file.read()
for ch in ['\\n','`','*','_','{','}','[',']','(',')','>','#','+','-','.','!','$','\'','@',str([0-9]),'(',')',',','"','\\xc0','<',";"]:
    if ch in filetostring:
        filetostring=filetostring.replace(ch," ")

# print(filetostring)
filetostring = filetostring.upper()
# print(filetostring)
filekosplit = filetostring.split("\n")
# print(filekosplit)
search_karna = input()
search_karna = search_karna.upper()
print(search_karna)


#yaha par length nikali jo ki ye bateyegi ki kitni baar occur hua hai


occurence = re.findall(search_karna, filetostring) #regx
length_occurence = len(occurence)
print(length_occurence)
file_ko_split_karene_ke_baad_doobara_split = []

for i in range(len(filekosplit)):
    file_ko_split_karene_ke_baad_doobara_split = filekosplit[i].split(" ")
    # print(file_ko_split_karene_ke_baad_doobara_split)
    for j in range(len(file_ko_split_karene_ke_baad_doobara_split)):
        if re.findall(search_karna, file_ko_split_karene_ke_baad_doobara_split[j]):
            if j == 0:
                print(file_ko_split_karene_ke_baad_doobara_split[j]+" "+file_ko_split_karene_ke_baad_doobara_split[j+1])
            elif j == len(file_ko_split_karene_ke_baad_doobara_split)-1:
                print(file_ko_split_karene_ke_baad_doobara_split[j-1]+" "+file_ko_split_karene_ke_baad_doobara_split[j])
            else:
                print(file_ko_split_karene_ke_baad_doobara_split[j-1]+" "+file_ko_split_karene_ke_baad_doobara_split[j]+" "+file_ko_split_karene_ke_baad_doobara_split[j+1])




