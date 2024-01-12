import os
import re

def remove_extra_head_blocks(content):
    return re.sub(r"<head>.*?</head>", "", content, flags=re.DOTALL)

# Set the path to your directory containing the Markdown files
path = "/Users/johnbruno/Desktop/Release Notes"

# Traverse the directory tree
for dirpath, dirnames, filenames in os.walk(path):
    for filename in filenames:
        if filename.endswith(".md"):
            guid_search = re.search(r"([a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12})", filename)

            if guid_search:
                guid = guid_search.group(1)

                full_path = os.path.join(dirpath, filename)
                with open(full_path, "r+") as file:
                    content = file.read()

                    # Remove existing <head> blocks
                    content = remove_extra_head_blocks(content)

                    # Locate the first header and insert the <head> block below it
                    header_index = content.find("# ")
                    if header_index != -1:
                        insert_index = content.find("\n", header_index) + 1  # +1 to insert right after the newline
                        new_content = content[:insert_index] + f"<head>\n  <meta name=\"guidename\" content=\"Release Notes\"/>\n  <meta name=\"context\" content=\"GUID-{guid}\"/>\n</head>\n" + content[insert_index:]

                        file.seek(0)
                        file.write(new_content)
                        file.truncate()

                    else:
                        print(f"Could not find the first header in the file: {filename}")
            else:
                print(f"Could not find a GUID in the file name: {filename}")
        else:
            print(f"Skipping non-Markdown file: {filename}")
