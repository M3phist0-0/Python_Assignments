import os
import re



def retrieve_files(filetype: str):
    """
    processes the files in sibling directories searching for files with a specific
    extension and returns a list of their paths
    Args:
        filetype(str): file extension to search for
    Returns:
        list: list of file path that match the extension
    """
    retrieved_files = []
    working_directory = os.path.abspath('.')
    parent_directory = os.path.dirname(working_directory)

    # Traversing sibling directories
    for sib_dir in os.listdir(parent_directory):
        sib_path = os.path.join(parent_directory, sib_dir)
        if not os.path.isdir(sib_path):
            continue

        for root, dirs, files in os.walk(sib_path):
            for file in files:
                if file.endswith(filetype):
                    file_path = os.path.join(root, file)
                    file_path = file_path.replace('\\', '/')
                    retrieved_files.append(file_path)
    return retrieved_files


def record_loader_gen(files: list):
    """
    processes each file in the provided list, extracting the name, gender, births
    and year from each line.
    Args:
        files(list): list of file paths to process
    Returns:
        tuple: (name, gender, births, year)
    """

    year_pattern = re.compile(r'yob(\d{4})\.txt$')

    for file_path in files:
        year_match = year_pattern.search(file_path)
        if year_match:
            year = int(year_match.group(1))
            with open(file_path, 'r') as file:
                for line in file:
                    parts = line.strip().split(',')
                    if len(parts) >= 3:
                        name = parts[0].lower()
                        gender = parts[1]
                        births = int(parts[2])
                        yield name, gender, births, year



def main():

    directory = retrieve_files(".txt")

    print(f"Number of .txt files found: {len(directory)}")

    if directory:
        for i, record in enumerate(record_loader_gen(directory)):
            print(f"Record {i + 1}: {record}")
            if i >= 4:
                print("...")
                break
    else:
        print("(=✖ᆽ✖=)No .txt files found.")


if __name__ == '__main__':
    main()

# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡀⠀⠀⠀⠀
# ⠀⠀⠀⠀⢀⡴⣆⠀⠀⠀⠀⠀⣠⡀⠀⠀⠀⠀⠀⠀⣼⣿⡗⠀⠀⠀⠀
# ⠀⠀⠀⣠⠟⠀⠘⠷⠶⠶⠶⠾⠉⢳⡄⠀⠀⠀⠀⠀⣧⣿⠀⠀⠀⠀⠀
# ⠀⠀⣰⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣤⣤⣤⣤⣤⣿⢿⣄⠀⠀⠀⠀
# ⠀⠀⡇⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣧⠀⠀⠀⠀⠀⠀⠙⣷⡴⠶⣦
# ⠀⠀⢱⡀⠀⠉⠉⠀⠀⠀⠀⠛⠃⠀⢠⡟⠂⠀⠀⢀⣀⣠⣤⠿⠞⠛⠋
# ⣠⠾⠋⠙⣶⣤⣤⣤⣤⣤⣀⣠⣤⣾⣿⠴⠶⠚⠋⠉⠁⠀⠀⠀⠀⠀⠀
# ⠛⠒⠛⠉⠉⠀⠀⠀⣴⠟⣣⡴⠛⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⠛⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀