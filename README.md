# ConversionScripts

Overview
This repository, ConversionScripts, contains a collection of scripts designed to facilitate various file conversion and processing tasks. Each script serves a specific purpose, ranging from format conversion to file renaming and content modification.

Scripts
1. convert_files
Location: convert_files/convert_files.sh
Description: This script is designed to convert files while maintaining the folder structure. It is particularly useful for converting .dita, .xml, and .ditamap files to Markdown format.

2. file_count
Location: file_count/File-count.py
Description: A Python script that counts the number of files within a specified directory. It's useful for inventory management and data analysis purposes.

3. insert_guid
Location: insert_guid/insert_guid_frontmatter.py
Description: This Python script inserts a GUID (Globally Unique Identifier) in the front matter of files. It's typically used for ensuring unique identification of documents.

4. recursive_rename
Location: recursive_rename/recursive_rename.sh
Description: A Bash script for recursively renaming files in a directory. This script is helpful for batch renaming files according to specific patterns or criteria.

5. remove_ja-JP
Location: remove_ja-JP/remove_ja-JP.sh
Description: This script is designed to remove files with the ja-JP locale. It is particularly useful in scenarios where project files need to be filtered based on language criteria.

Getting Started
To use these scripts, clone the repository to your local machine:

bash
Copy code
git clone https://github.com/your-username/ConversionScripts.git
Navigate to the script's directory and follow the individual instructions provided in each script's comments for usage.

Contributions
Contributions to ConversionScripts are welcome. If you have a fix or an improvement, please fork the repository and submit a pull request.

License
This project is licensed under the MIT License - see the LICENSE file for details.
