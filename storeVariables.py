import json

class Variable:
    name="non initialized"
    contents="0"
    def __init__(self, name, contents):
        self.name_ = name
        self.contents_ = contents
    def getName(self):
        return name_
    def getContents(self):
        return contents_

#Sets characters
with open('characters.json') as stream:
    characters = json.load(stream)


#User input
with open ("main.jasp", "r") as myfile:
    text=myfile.read()


#Makes a dictionnary out of all the variables in the code
text=str(text)
dictionnary={}
orderedDictionnary={}
numberOfVariables=0
i=0
while i < len(text):
    if (text[i]=='{'):
        name_first_char=i+1
    if (text[i]=='='):
        name_last_char=i
        contents_first_char=i+1
    if (text[i]=='}'):
        contents_last_char=i
        name=text[name_first_char:name_last_char]
        contents=text[contents_first_char:contents_last_char]
        variable=Variable(name,contents)
        dictionnary[name]=contents
        orderedDictionnary[numberOfVariables]=(name,contents)
        numberOfVariables+=1
    i += 1

#Stores the dictionnary in variables.json file
with open('variables.json','a') as f:
    json.dump(dictionnary,f)

with open('ordered_variables.json','a') as f:
    json.dump(orderedDictionnary,f)
