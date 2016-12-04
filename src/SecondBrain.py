'''
Created on Dec 2, 2016

@author: Brady
'''
from __builtin__ import file, exit

def readTissueFile(fileName):
    tempSkull = {}  #stores all our brain tissue dynamically
    openBracket = False
    openBrace = False
    lineCorrect = False #?
    word = "" #?
    parentCategory = []
    directory = {}
    bottomLevel = False
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
                elif char == ']' and openBracket == True: #marks the end of a category
                    openBracket = False
                elif char == '{' and openBracket == False:
                    lineCorrect = True
                    openBrace = True
                else:
                    word += char
            print word   
            
            if openBracket == False and lineCorrect == True: #line formatted correctly
                print "Line read successfully"
                key = word
                value = {} #empty dictionary to store further subcategories
                print "Key = " + key
                print " Value = ", value
                '''if len(parentCategory) == 0: #top level category
                    tempSkull[key] = value
                else:
                    i = 0
                    directory = tempSkull #create association to the current 'directory' in the dictionary
                    while bottomLevel == False:
                        for key in directory: #iterate down keys in current directory
                                if key == parentCategory[i]: #find that parent categories subcategory
                                    directory = directory[key] #save that directory as the next directory to traverse
                                    i += 1
                                    break
                        bottomLevel = True #if key not found, must be bottom level
                if openBrace == True: #contains subcategories, so make value a dictionary
                    parentCategory.append(word)
                
                else:
                    print "done with subcategories?"
                '''
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

