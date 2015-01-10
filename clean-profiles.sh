#!/bin/bash
#
# Script to delete user profile directories excluding a list of known
# users to keep.  Must be run as root, and is intended to run as a launch
# daemon
#
# Written by Vaughn Miller


# define users to keep in an array 
# (use spaces between items) 
KEEPERS=( Shared ) 
AGE=0  # Number in days for age of accounts


# iterate through list of folders in /Users 
for folder in /Users/*; do 
    # remove the "/Users/" portion of the path for easier testing 
    user=$(basename ${folder}) 
    # compare folder name against KEEPER array items 
    if [[ "${KEEPERS[*]}" =~ "${user}" ]]; then 
        # skip if folder is in the skip array 
        logger -t $0 "Skipping ${user}" 
    else 
        # Check age of account and proceed with removal if appropriate 
        logger -t $0  "Checking age of ${user}..."
		if [[ -n $(find /Users/${user} -maxdepth 0 -type d -mtime +${AGE}d) ]]; then
			logger -t $0 "Deleting ${user}"
			rm -rf /Users/${user} 
		else
			logger -t $0 "Keeping ${user}"
		fi
    fi 
done