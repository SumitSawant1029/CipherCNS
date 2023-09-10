message = 'Lerr'

# Adding a x between two consecutive alphabets

message = list(message)
l1=[]
for i in range(0,(len(message)-1)):
    l1.append(message[i])
    if message[i] == message[i+1]:
        l1.append('x')
l1.append(message[-1]) 
print("Step 1 :-",l1)

# Removing the spaces
l2=[]
for i in range(0,len(l1)):
    if l1[i]!=' ':
        l2.append(l1[i])
print("Step 2:-",l2)

# Separating the message in combination of two
l1.clear()
if(len(l2)%2!=0):
    l2.append('x')
print("Step 3 :-",l2)

# convert each item to lowercase
for item in l2:
    l1.append(item.lower())
print("Step 4 :-",l1)


# Creating Key Matrix by dictionary

key = {
    "a": "11",
    "b": "12",
    "c": "13",
    "d": "14",
    "e": "15",
    "f": "21",
    "g": "22",
    "h": "23",
    "i": "24",
    "k": "25",
    "l": "31",
    "m": "32",
    "n": "33",
    "o": "34",
    "p": "35",
    "q": "41",
    "r": "42",
    "s": "43",
    "t": "44",
    "u": "45",
    "v": "51",
    "w": "52",
    "x": "53",
    "y": "54",
    "z": "55",

    "11": "a",
    "12": "b",
    "13": "c",
    "14": "d",
    "15":"e",
    "21": "f",
    "22": "g",
    "23": "h",
    "24":"i",
    "25":"k",
    "31": "l",
    "32": "m",
    "33": "n",
    "34":"o",
    "35":"p",
    "41": "q",
    "42": "r",
    "43": "s",
    "44":"t",
    "45":"u",
    "51": "v",
    "52": "w",
    "53": "x",
    "54":"y",
    "55":"z",
}
# |  1 |  2 |  3 | 4  |  5
# -----------------------
#1 | a  | b  | c  | d  | e
# -----------------------
#2 | f  | g  | h  | i  | k
# -------------------------
#3 | l  | m  | n  | o  | p
# -------------------------
#4 | q  | r  | s  | t  | u
# -------------------------
#5 | v  | w  | x  | y  | z
# Encrypting the message
l3=[]
for i in range(0,len(l1)):
    l3.append(key[l1[i]])
print("Step 5 :-",l3)

l4=[]
for element in l3:
    for char in element:
        l4.append(char)
print("Step 6 :-",l4)




# Encrypting
for i in range(0, len(l4) - 1, 4):
    if i + 3 < len(l4):
        temp = l4[i + 1]
        l4[i + 1] = l4[i + 3]
        l4[i + 3] = temp
print("Step 7 :-",l4)

l3.clear()

for i in range(0,len(l4)):
    if(i%2==0):
        l3.append(l4[i]+l4[i+1])

print("Step 8 :-",l3)

# Reverse Mapping
l4.clear()
for i in range(0,len(l3)):
    l4.append(key[l3[i]])

print("Step 9 :-",l4)

