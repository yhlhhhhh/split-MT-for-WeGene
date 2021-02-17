import re
def split_mt():
    haplogroup = inputs['haplogroup']
    mtdic = haplogroup['mt']
    MT = mtdic['haplogroup']
    letter_group = re.split("\d",MT)
    number_group = re.split('\D',MT)
    Simple_MT1 = letter_group[0]     
    number1 = number_group[1]
    letter1 = letter_group[1]
    Simple_MT2 = Simple_MT1 + number1   
    Simple_MT3 = Simple_MT2 + letter1  
    Simple_MT = [Simple_MT1,Simple_MT2,Simple_MT3]
    return Simple_MT