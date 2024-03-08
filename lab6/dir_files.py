import os


# 1
def list_dir_files(p):
    all_items = os.listdir(p)
    dirs = [item for item in all_items if os.path.isdir(os.path.join(p, item))]
    files = [item for item in all_items if os.path.isfile(os.path.join(p, item))]

    print("Directories:", dirs)
    print("Files:", files)
    print("All Items:", all_items)


# 2

def check_access(p):
    print("Exists:", os.path.exists(p))
    print("Readable:", os.access(p, os.R_OK))
    print("Writable:", os.access(p, os.W_OK))
    print("Executable:", os.access(p, os.X_OK))


# 3
def test_path_details(p):
    if os.path.exists(p):
        print("Path exists.")
        print("Directory:", os.path.dirname(p))
        print("Filename:", os.path.basename(p))
    else:
        print("Path does not exist.")


# 4
def count_lines(file_path):
    with open(file_path, 'r') as f:
        print("Number of lines:", len(f.readlines()))


# 5
def write_list_to_file(list_items, file_path):
    with open(file_path, 'w') as f:
        for item in list_items:
            f.write(f"{item}\n")


# 6
def generate_26_files():
    for i in range(65, 91):  # ASCII codes from A to Z
        with open(f"{chr(i)}.txt", 'w') as f:
            f.write(chr(i))


# 7
def copy_file(source_p, destination_p):
    with open(source_p, 'r') as source, open(destination_p, 'w') as dest:
        dest.write(source.read())


# 8
def delete_file(p):
    if os.path.exists(p) and os.access(p, os.W_OK):
        os.remove(p)
        print("File deleted.")
    else:
        print("File does not exist or is not accessible.")