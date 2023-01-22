import re
# 2. Quantifiers  [?, +, *]

#2.1  Use of ? . Returns match if finds 0 or 1 preceedings element occurance in string else None. \
    # In below example "u" is preceeding in colour hence, finds color and colour since 0 or 1
    # but doesnt find colouur
string1 = "color"
string2 = "colour"
string3 = "colouur"
out_ques = re.search('colou?r', string2)


#2.2 Use of + . Returns match if finds 1 or more occuring in string else None. 

qstring1 = "ac"
qstring2 = "abc"
qstring3 = "abbc"


out_q = re.search("ab+c",  qstring3)
print(out_q)
