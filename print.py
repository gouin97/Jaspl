import json
#end of line last_char
endOfLine=';'


#User input
with open ("main.jasp", "r") as myfile:
    text=myfile.read()

#reads variables
with open ("variables.json","r") as stream:
    variables=json.load(stream)

#read ordered variables
with open("ordered_variables.json") as stream:
    orderedDictionnary=json.load(stream)


#List of elements to print
elementsToPrint={}
numberOfElements=0

#makes list out of to-print elements
keyword="print"
i=0
j=0
toPrint=False
isAVariable=False
isAString=False
while i<len(text): 
    if (text[i]==keyword[j]):
        while(j<len(keyword)):
            if (text[j]==keyword[j]):
                toPrint=True
            j+=1
        j=0
        if (toPrint):
            first_char=i+1+len(keyword)
            k=i
            while(k<len(text)):
                if (text[k]==endOfLine):
                    last_char=k-1
                    break
                k+=1
            #declares the element to print 
            element=text[first_char:last_char]

            #checks if corresponds to a variable name
            for key in orderedDictionnary:
                if (element==orderedDictionnary[key][0]):
                    element=orderedDictionnary[key][1]
                    isAVariable=True
            
            #checks if its a string (doesnt work)
            if (first_char=="\""):
                if (last_char=="\""):
                    first_char+=1;
                    last_char-=1;
                    element=text[first_char:last_char]
               
            elementsToPrint[numberOfElements]=element
            numberOfElements+=1

    i+=1

    
#stores in json file
with open('toPrint.json','a') as f:
    json.dump(elementsToPrint,f)


#replaces names of variables with contents of variables
            #for key in orderedDictionnary:
             #   for m in range(0,numberOfElements):
              #      if (orderedDictionnary[key][0]==elementsToPrint[m]):
               #         elementsToPrint[m]=orderedDictionnary[key][1]



#printing
for i in range(0,numberOfElements):
    print(elementsToPrint[i])

