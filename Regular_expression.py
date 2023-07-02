# Regular expression

# re module is used for regular expression , it a built in module. 
import re

pattern = r"[A-Z]+yclone" # r is for raw string and [] is one of the meta character.
text = '''Cyclone Dumazile was a strong tropical cyclone in the South-West Indian Ocean 
that affected Madagascar and Réunion in early March 2018. Dumazile originated from a cyclone
Dyclone low-pressure area that formed near Agaléga on 27 February. It became a tropical 
disturbance on 2 March, and was named the next day after attaining tropical storm status.
Dumazile reached its peak intensity on 5 March, with 10-minute sustained winds of 165 km/h (105 mph),
1-minute sustained winds of 205 km/h (125 mph), and a central atmospheric pressure of 945 hPa (27.91 inHg).
As it tracked southeastwards, Dumazile weakened steadily over the next couple of days due to wind shear, 
and became a post-tropical cyclone on 7 March

'''
# to check if pattern exists in text
match = re.search(pattern, text)
print(match)

# to print pattern from text
matches = re.finditer(pattern, text)
for match in matches:
  print(match.span()) 
  print(text[match.span()[0]: match.span()[1]])

# for detail study of re module and meta characters:-
# 1)https://docs.python.org/3/library/re.html 
# 2)https://www.ibm.com/docs/en/rational-clearquest/9.0.1?topic=tags-meta-characters-in-regular-expressions
# https://regexr.com # for practicing meta characters
