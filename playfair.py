message = input("Enter the text you want to encrypt:-")

def my_function(message):
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
        "a": "01",
        "b": "02",
        "c": "03",
        "d": "04",
        "e": "05",
        "f": "11",
        "g": "12",
        "h": "13",
        "i": "14",
        "j": "14",
        "k": "15",
        "l": "21",
        "m": "22",
        "n": "23",
        "o": "24",
        "p": "25",
        "q": "31",
        "r": "32",
        "s": "33",
        "t": "34",
        "u": "35",
        "v": "41",
        "w": "42",
        "x": "43",
        "y": "44",
        "z": "45",

        "01": "a",
        "02": "b",
        "03": "c",
        "04": "d",
        "05": "e",
        "11": "f",
        "12": "g",
        "13": "h",
        "14": "i",
        "15": "k",
        "21": "l",
        "22": "m",
        "23": "n",
        "24": "o",
        "25": "p",
        "31": "q",
        "32": "r",
        "33": "s",
        "34": "t",
        "35": "u",
        "41": "v",
        "42": "w",
        "43": "x",
        "44": "y",
        "45": "z"
    }

    print("Your Key is:- ")
    print("  |  1 |  2 |  3 | 4  |  5")
    print("-----------------------")
    print("1 | a  | b  | c  | d  | e")
    print("-----------------------")
    print("2 | f  | g  | h  | i  | k")
    print("-----------------------")
    print("3 | l  | m  | n  | o  | p")
    print("-----------------------")
    print("4 | q  | r  | s  | t  | u")
    print("-----------------------")
    print("5 | v  | w  | x  | y  | z")
    print("-----------------------")
    
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
        
        if l4[i+1] == l4[i+3]:
            l4[i]= str((int(l4[i]) + 2)%5)
            l4[i+2]= str((int(l4[i+2]) + 2)%5)

        if l4[i] == l4[i+2]:
            l4[i+1]= str((int(l4[i+1]) + 2)%5)
            l4[i+3]= str((int(l4[i+3]) + 2)%5)
       

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


    # Making the list to an string

    Encrypted_message = ''.join(l4)
    return Encrypted_message 

print(my_function(message))



