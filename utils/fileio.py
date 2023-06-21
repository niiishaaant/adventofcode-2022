def read_file(file_path: str) -> str:
    try:
        with open(file_path, 'r') as f:
            return f.read().strip()
    except FileNotFoundError:
        print('File not found')
        exit(1)
