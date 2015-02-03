#!/usr/bin/python
#
# Script to modify the exception.sites for Oracle Java
#
# Written by Vaughn Miller with inspiration from Rich Trouton's information here :
# https://derflounder.wordpress.com/2014/01/16/managing-oracles-java-exception-site-list/
# 
# This script modifies the exception.sites for Oracle Java to allow unsigned applets to 
# run.  This a peruser setting, and thus this script is intended be run as a 
# LaunchAgent.  Script does not overwrite existing user exceptions, rather merges in
# our desired exceptions.  Script can also remove exceptions from the list.

import os

# Modify these two lists.  Lists are allowed to be empty.
#======================================================================
EXCEPTION_LIST=[]

REMOVE_LIST=[]
#=======================================================================

# Build the path to the users exception list
exceptionFile=os.path.expanduser(
    '~/Library/Application Support/Oracle/Java/Deployment/security/exception.sites')


if os.path.exists(exceptionFile):
    # File exists : read the contents into a list
    with open(exceptionFile) as f:
        newExceptions = f.readlines()
        
    # Compare and add in our exceptions if missing    
    for site in EXCEPTION_LIST:
        if str(site + '\n') not in newExceptions:
            newExceptions.append(str(site + '\n'))
    # Compare and remove sites if needed
    for site in REMOVE_LIST:
        if str(site + '\n') in newExceptions:
            newExceptions.remove(str(site + '\n'))
else:
    # If the list does not exist, just make it the same as our exception list
    newExceptions = EXCEPTION_LIST

# Write out the modified list    
outFile = open(exceptionFile, "w")
for site in newExceptions:
    outFile.write(str(site) + '\n')

    