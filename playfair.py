message = input("Enter the text you want to encrypt:-")

def my_function(message):
    # Adding a x between two consecutive alphabets
    message = list(message)
    print("Encryption:-")
    l1=[]

    print("Your Key is:- ")
    print("   |0  |  1 |  2 |  3 | 4 ")
    print("-----------------------")
    print("0 | a  | b  | c  | d  | e")
    print("-----------------------")
    print("1 | f  | g  | h  | i  | k")
    print("-----------------------")
    print("2 | l  | m  | n  | o  | p")
    print("-----------------------")
    print("3 | q  | r  | s  | t  | u")
    print("-----------------------")
    print("4 | v  | w  | x  | y  | z")
    print("-----------------------")

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
        "a": "00",
        "b": "01",
        "c": "02",
        "d": "03",
        "e": "04",
        "f": "10",
        "g": "11",
        "h": "12",
        "i": "13",
        "j": "13",
        "k": "14",
        "l": "20",
        "m": "21",
        "n": "22",
        "o": "23",
        "p": "24",
        "q": "30",
        "r": "31",
        "s": "32",
        "t": "33",
        "u": "34",
        "v": "40",
        "w": "41",
        "x": "42",
        "y": "43",
        "z": "44",

        "00": "a",
        "01": "b",
        "02": "c",
        "03": "d",
        "04": "e",
        "10": "f",
        "11": "g",
        "12": "h",
        "13": "i",
        "14": "k",
        "20": "l",
        "21": "m",
        "22": "n",
        "23": "o",
        "24": "p",
        "30": "q",
        "31": "r",
        "32": "s",
        "33": "t",
        "34": "u",
        "40": "v",
        "41": "w",
        "42": "x",
        "43": "y",
        "44": "z"
    }


    
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
        if l4[i+1] != l4[i+3] and l4[i] != l4[i+2]:
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


Encrypted_message = my_function(message)
print(Encrypted_message)

def decryption(message) :
    print("Decryption:-")
    # Creating Key Matrix by dictionary

    key = {
        "a": "00",
        "b": "01",
        "c": "02",
        "d": "03",
        "e": "04",
        "f": "10",
        "g": "11",
        "h": "12",
        "i": "13",
        "j": "13",
        "k": "14",
        "l": "20",
        "m": "21",
        "n": "22",
        "o": "23",
        "p": "24",
        "q": "30",
        "r": "31",
        "s": "32",
        "t": "33",
        "u": "34",
        "v": "40",
        "w": "41",
        "x": "42",
        "y": "43",
        "z": "44",

        "00": "a",
        "01": "b",
        "02": "c",
        "03": "d",
        "04": "e",
        "10": "f",
        "11": "g",
        "12": "h",
        "13": "i",
        "14": "k",
        "20": "l",
        "21": "m",
        "22": "n",
        "23": "o",
        "24": "p",
        "30": "q",
        "31": "r",
        "32": "s",
        "33": "t",
        "34": "u",
        "40": "v",
        "41": "w",
        "42": "x",
        "43": "y",
        "44": "z"
    }    
    print("Your Key is:- ")
    print("   |0  |  1 |  2 |  3 | 4 ")
    print("-----------------------")
    print("0 | a  | b  | c  | d  | e")
    print("-----------------------")
    print("1 | f  | g  | h  | i  | k")
    print("-----------------------")
    print("2 | l  | m  | n  | o  | p")
    print("-----------------------")
    print("3 | q  | r  | s  | t  | u")
    print("-----------------------")
    print("4 | v  | w  | x  | y  | z")
    print("-----------------------")
    message = list(message)
    print(message)

    l1=[]
    #  convert each item to lowercase
    for item in message:
        l1.append(item.lower())
    print("Step 1 :-",l1)


    message.clear()
    for i in range(0,len(l1)):
        message.append(key[l1[i]])
    print("Step 2 :-",message)

    l1.clear()
    for element in message:
        for char in element:
            l1.append(char)
    print("Step 3:-",l1)
    l4=l1


    for i in range(0, len(l4) - 1, 4):
        if l4[i+1] != l4[i+3] and l4[i] != l4[i+2]:
            temp = l4[i + 1]
            l4[i + 1] = l4[i + 3]
            l4[i + 3] = temp
        
        if l4[i+1] == l4[i+3]:
            l4[i]= str((int(l4[i]) + 2)%5)
            l4[i+2]= str((int(l4[i+2]) + 2)%5)

        if l4[i] == l4[i+2]:
            l4[i+1]= str((int(l4[i+1]) + 2)%5)
            l4[i+3]= str((int(l4[i+3]) + 2)%5)
       

    print("Step 4 :-",l4)
    l3=[]

    for i in range(0,len(l4)):
        if(i%2==0):
            l3.append(l4[i]+l4[i+1])

    print("Step 5 :-",l3)

#  Reverse Mapping
    l4.clear()
    for i in range(0,len(l3)):
        l4.append(key[l3[i]])

    print("Step 6 :-",l4)


    # # Making the list to an string

    Decrypted_message = ''.join(l4)
    print(Decrypted_message)

decryption(Encrypted_message)





