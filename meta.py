
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


out2 = re.findall('[^a-z]', "Hi I am manoj")


# Special Sequences \d[0-9] , \w[0-9a-Z]

# Search( ) returns matches while findall returns list

out3 = re.findall('\d', "Hi 9834 is my number")
print(out3)






