def read_file(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            yield line.strip()

def process_file(file_path):
    total_lines = sum(1 for line in read_file(file_path))    
    print(f"Total lines in file: {total_lines}")
    for line in read_file(file_path):
        if line:
            print(line.upper())

process_file("learning.txt")
