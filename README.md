# Simple CSV comparsion tool

A simple Python script to compare two CSV files and identify differences between them. The comparison is case insensitive and focuses on the first column of each CSV. Differences are printed to the terminal and saved to a new CSV file.  

## Features

- Load two CSV files  
- Compare the first column of each file  
- Case-insensitive comparison (`Apple` = `apple`)  
- Show items only in A or only in B  
- Export differences to `differences.csv`  

## Requirements

- Python 3.x  

## Usage

1. Place your CSV files in the same folder as the script
2. Modify the file names in the code at file_a and file_b 
3. Run the script
4. Check the terminal output for differences
5. Differences are also saved in differences.csv

You are free to use this script and modify it to your liking. 

```bash
python kompr.py


