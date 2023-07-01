# dictionaries
dic={83:'jaadu',84:"nishchay",87:"vanisha",92:"chandan"}
print(dic)
print(dic[92])
print(dic.get(97)) # both 4th and 5th line are same but in get() we don't get an error if the key is not present in the dictionary
print(dic.keys()) # To get all the keys 
# to get values corresponding to keys we can use for:
for keys in dic.keys():
    print(dic[keys])
# to get values with keys    
for keys in dic.keys():   #this can be used for using fstrings also like
    print(f"the corresponding values to the {keys} is {dic[keys]}")

print(dic.values())  #to get all values
print(dic.items())   #to get keys and values in pair
# to get keys and values seperately in pairs
for keys,values in dic.items():
    print(keys,':',values)
