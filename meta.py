
import re

#1. Metacharacters [^,$, .] 

strings = "dogs are adorable"
start_pattern = '^dogs'
end_pattern = '$dogs'

#1.1  Use of ^. Returns match if finds starts with ^pattern in string/sentence else None
out = re.search(pattern=start_pattern, string=strings)


#1.2 Use of $. Returns match if finds ends with ^pattern in string/sentence else None
out1 =re.search(pattern=end_pattern, string=strings) 

#1.3  "." Matches any characters except new line

#1.4  "set" --> "[]" Matches any element that is in [] from string, say ["man"] matches m or a or n from "manoj"
    #"[a-z]" matches range from a to z, 
    # [^a-z]  matches not starting with but ^[a-z] matches starting with,
    # [a-Z] matches a-z and A-Z all    











