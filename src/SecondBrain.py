'''
Created on Dec 2, 2016

@author: Brady
'''
from __builtin__ import file, exit

def readTissueFile(fileName):
    tempSkull = {}  #stores all our brain tissue dynamically
    openBracket = False
    openBrace = False
    foundCategory = False
    foundValue = False
    numOpenBraces = 0
    numOpenQuotes = 0
    #lineCorrect = False #?
    word = "" 
    parent = ""
    
    tissue = open(fileLocation, 'r')
                
    firstLine =tissue.readline().strip()
        
    if firstLine != "[BrainTissue]{":
        print "Not a Brain Tissue file."
        print "Read" + firstLine
        exit
    else:
        for line in tissue: #iterate over each line in the file. 
            line = line.strip()
            word = ""
            for char in line: #iterate over each character in the line
                if char == '[': #marks the beginning of a category
                    openBracket = True
                    foundCategory = True
                elif char == ']' and openBracket == True: #marks the end of a category
                    openBracket = False
                elif char == '{' and openBracket == False:
                    #lineCorrect = True
                    openBrace = True
                    numOpenBraces += 1
                elif char == '}' and numOpenBraces > 0:
                    numOpenBraces -= 1
                elif char == "\"":
                    if numOpenQuotes == 0:
                        numOpenQuotes += 1
                        foundValue = True
                    else:
                        numOpenQuotes -= 1
                else:
                    word += char
            print word   
            
            if openBracket == False and numOpenQuotes == 0: #line formatted correctly
                print "Line read successfully"
                if foundCategory == True:
                    key = word
                    value = {} #empty dictionary to store further subcategories
                    #print "Key = " + key
                    #print " Value = ", value
                    #tempSkull[key] = value
                    tempSkull[key] = value
                    if len(parent) != 0:
                        tempSkull[key]["Parent Dir"] = parent #create parent key with parent directory as value
                    if openBrace == True: #has children
                        parent = key #save key as parent for following

                elif foundValue == True:
                    valuePieces = word.split(",") #split the two pieces of the value string
                    key = valuePieces[0]
                    value = valuePieces[1]
                    tempSkull[key] = value
                    if len(parent) != 0:
                        tempSkull[key]["Parent Dir"] = parent #create parent key with parent directory as value
                else:
                    print "Something went wrong. Line was neither a category nor value"
                    exit
                
                foundCategory = False
                foundValue = False
            else:
                print "Error reading in brain file. Last read word: " + word
                exit


inUse = True
skull = {}


print "Welcome to Brady's Second Brain. This is where he keeps everything that will eventually leak out of his primary brain."
print "Feel free to use it in a similar way."

while inUse == True:
    print "Options:"
    print "1. Create a Brain Tissue file"
    print "2. Read a Brain Tissue file"
    print "3. Edit a Brain Tissue file"
    print "4. Help (AKA What the hell is this?)"
    print "5. Exit"
    
    response = int(raw_input("Please enter a command: "))
    if response == 1 or response == 2 or response == 3 or response == 4:
        if response == 1:
            print "Okay I'll get to this. Gotta logic through how the file's will built up."
        elif response == 2:
                fileLocation = raw_input("Please enter absolute file path: ")
                readTissueFile(fileLocation)
        elif response == 3:
            print "time to edit a file"
        elif response == 4:
            print "Explain shit here"
        elif response == 5:
            exit
    else:
            print "Invalid response. Please try again."

