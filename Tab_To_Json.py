import sys,os,re

# Getting the File input
file_input = sys.argv[1]

# Getting the File output ready
temp = re.search('(\w+)\.(\w+)',file_input)
file_out = temp.group(1) + ".json"
FO = open(file_out,'w')

# Write some initial json strings 
FO.write("[\n\t")

# Read the whole contents to see how many entries we have
FI = open(file_input,'r')
content = FI.read()
items = content.split('\n')
items = [x for x in items if x !=''] # Get rid of empty items
data_entry = int(len(items)) - 1 

cnt = 0
for i in items:
    if cnt == 0: # if cnt = 0, split the header
        header = i.split()
    elif cnt == data_entry: # if cnt = data_entry, we have reached the end.  Print a little in different format
        temp = i.split('\t')
        temp_cnt = 0
        FO.write('{\n\t')
        temp_len = len(header)
        for j in header:
            temp2 = re.search('^\s*(.*?)\s*$',temp[temp_cnt]) #Get rid of the start & end spaces / the content is to match as little as possible so can get rid of spaces in the end
            temp2_txt = temp2.group(1) # Get only the content 
            temp3_txt = temp2_txt.replace("\"","\'") # Additional Check to Replace double quote to single quote to avoid Json format error
            if temp_cnt == temp_len - 1:
                FO.write('\"'+ j + '\"' + ':' + '\"' + temp3_txt + '\"' + '\n\t')
            else:
                FO.write('\"'+ j + '\"' + ':' + '\"' + temp3_txt + '\",' + '\n\t')
            temp_cnt = temp_cnt + 1
        FO.write('}\n')
    else: # if cnt not 0 or not data_entry, print normally
        temp = i.split('\t')
        temp_cnt = 0
        FO.write('{\n\t')
        temp_len = len(header)
        for j in header:
            temp2 = re.search('^\s*(.*?)\s*$',temp[temp_cnt]) #Get rid of the start & end spaces / the content is to match as little as possible so can get rid of spaces in the end
            temp2_txt = temp2.group(1) # Get only the content
            temp3_txt = temp2_txt.replace("\"","\'") # Additional Check to Replace double quote to single quote to avoid Json format error
            if temp_cnt == temp_len - 1: # last entry is without comma
                FO.write('\"'+ j + '\"' + ':' + '\"' + temp3_txt + '\"' + '\n\t')
            else: 
                FO.write('\"'+ j + '\"' + ':' + '\"' + temp3_txt + '\",' + '\n\t')
            temp_cnt = temp_cnt + 1
        FO.write('},\n\t')
    cnt = cnt + 1

FI.close

# write final json strings
FO.write("]\n")
FO.close
