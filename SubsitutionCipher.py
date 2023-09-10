
from collections import Counter

q1 = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
q2 = ['e','t','a','o','i','n','s','h','r','d','i','c','u']

string = "slaz tlla avupnoa ha aol whyr"
keys = []
string1 = string
string1 = string1.replace(" ","")

# Find the highest Alphabet
result = Counter(string1)
result = max(result, key=result.get)
print("Most frequent character: ", result)

# Find the Index Of the largest occurring alphabet in q2 list
index1 = q1.index(str(result))
print("Index of most frequent", index1)

# Finding the keys difference between the character and 
for j in range(0, len(q2)):
    index2 = q1.index(q2[j])	
    key = index2 - index1
    keys.append(key)


l3 = []

# Convert String to list
string2 = list(string)


z=0
for i in range(0,len(keys)):
    l3=[]
    for j in range(0,len(string2)):
        if string[j] != " ":
            k = int(q1.index(str(string2[j]))) + int(keys[i])
            f= k%26
            l3.append(q1[f])
        else:
            l3.append(" ")
    print("For ",q2[i],":-",end=" ")
    result_string = " ".join(l3)
    print(result_string)
    z=input("Is the Sentence MeaningFull(y or n):-")
    if(z=="y"):
        break
    else:
        continue
        