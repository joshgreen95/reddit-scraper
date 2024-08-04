import os
import json

#Opens and reads template credentials JSON. 
with open('modules/credentials_harvester/credentialstemplate.json') as file:
    credentialsTemplateJson = json.load(file)
    file.close()

def FindCredentialsFile():
    scriptDir = os.path.abspath(__file__)
    scriptDir = scriptDir.split('/')
    
    #Removes /modules/credentials_harvester/credentialsharvester.py from file path to find root directory
    for i in range(3):
        scriptDir.pop()

    #Joins file path string back together
    joinedScriptDir = ''
    
    for i in range(len(scriptDir)):
        joinedScriptDir += scriptDir[i]
        joinedScriptDir += '/'

    #Appends credentials file in the root directory
    credentialsFilePath = os.path.join(joinedScriptDir, 'credentials.json')
    #If root credentials file does not exist create one from template 
    pathExists = os.path.exists(credentialsFilePath)
    
    if(not pathExists):
       with open(credentialsFilePath, 'w') as file:
           json.dump(credentialsTemplateJson, file)

    return credentialsFilePath

def RuntimeHarvest():
    #Harvests credentials at runtime through a series of prompts. 
    #TODO Clean up names in credentials file for easier prompting
    credentialsFile = open(FindCredentialsFile(), 'r')
    credentialsJson = json.load(credentialsFile)

    #If credentials have been entered already gives chance to skip
    print('Skip Credential Entry: Y/N')
    choice = input().lower()

    if(choice != 'y'):
        for category in credentialsJson:
            for subCategory in credentialsJson[category]:
                print(f'Please enter your {category} : {subCategory}')
                print(f'Current value: {credentialsJson[category][subCategory]}  * to skip')
                choice = input()
                if(choice != '*'):
                    credentialsJson[category][subCategory] = choice
        
    credentialsFile = open(FindCredentialsFile(), 'w')
    json.dump(credentialsJson, credentialsFile)
    credentialsFile.close()

def GetCredential(category, value):
    credentialsFile = open(FindCredentialsFile(), 'r')
    credentialsJson = json.load(credentialsFile)
    credentialsFile.close()
    
    value = credentialsJson[category][value]
    return(value)