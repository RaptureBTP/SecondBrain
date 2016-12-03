'''
Created on Dec 2, 2016

@author: Brady
'''
from __builtin__ import file, exit

inUse = True

print "Welcome to Brady's Second Brain. This is where he keeps everything that will eventually leak out of his primary brain."
print "Feel free to use it in a similar way."

while inUse == True:
    print "Options:"
    print "1. Create a Brain Tissue file"
    print "2. Read a Brain Tissue file"
    print "3. Edit a Brain Tissue file"
    print "4. Help (AKA What the hell is this?"
    print "5. Exit"
    
    response = raw_input("Please enter a command: ")
    if response == 1 or response == 2 or response == 3 or response == 4:
        if response == 1:
            print "Okay I'll get to this. Gotta logic through how the file's will built up."
        elif response == 2:
                fileLocation = raw_input("Please enter absolute file path: ")
                tissue = open(fileLocation, 'r')
        
                if tissue.readline() != "[BrainTissue]":
                    print "Not a Brain Tissue file."
                    for line in tissue:
                        print line #temp
        elif response == 3:
            print "time to edit a file"
        elif response == 4:
            print "Explain shit here"
        elif response == 5:
            exit
        else:
            print "Invalid response. Please try again."