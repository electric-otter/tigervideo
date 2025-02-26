import os

def add_object_to_file(filename, object_data):
    with open(filename, 'a') as file:
        file.write(object_data + '\n')

def open_file(filename):
    if os.name == 'nt':  # For Windows
        os.startfile(filename)
    elif os.name == 'posix':  # For macOS and Linux
        os.system(f'open {filename}')
    else:
        print(f'Unsupported OS: {os.name}')

if __name__ == '__main__':
    print('This script will save default data to object.tvid')
    filename = 'object.tvid'
    object_data = 'data.tvidata'  # Default object data
    add_object_to_file(filename, object_data)
    open_file(filename)
