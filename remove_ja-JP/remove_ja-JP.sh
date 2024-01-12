#!/bin/bash

# Directory containing the folders to be deleted
DIR=~/Desktop/Integration

# Check if the directory exists
if [[ ! -d $DIR ]]; then
    echo "Directory $DIR not found!"
    exit 1
fi

# Find and remove directories named "ja-JP"
find $DIR -type d -name "ja-JP" -exec rm -rf {} + 

echo "All 'ja-JP' directories have been removed."
