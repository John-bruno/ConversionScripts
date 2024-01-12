import os

def count_words_in_markdown_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        contents = file.read()
        words = contents.split()
        return len(words)

def main(root_dir):
    total_files = 0
    total_words = 0

    for root, dirs, files in os.walk(root_dir):
        for file in files:
            if file.endswith('.md'):
                total_files += 1
                file_path = os.path.join(root, file)
                total_words += count_words_in_markdown_file(file_path)

    print(f"Total Markdown Pages: {total_files}")
    print(f"Total Word Count: {total_words}")

if __name__ == "__main__":
    home_directory = os.path.expanduser('~')  # This will find your home directory
    root_directory = os.path.join(home_directory, 'Documents', 'Boomi_docs', 'Docs', 'Atomsphere')
    main(root_directory)
