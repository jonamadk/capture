from ast import pattern
import re

#1. Metacharacters [^,$] 

strings = "dogs are adorable"
start_pattern = '^dogs'
end_pattern = '$dogs'

#1.1  Use of ^. Returns match if finds starts with ^pattern in sentence else None
out = re.search(pattern=start_pattern, string=strings)


#1.2 Use of $. Returns match if finds ends with ^pattern in sentence else None
out1 =re.search(pattern=end_pattern, string=strings) 











