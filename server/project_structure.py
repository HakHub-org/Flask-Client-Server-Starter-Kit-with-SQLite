import os

def print_tree(directory, file_output, prefix=''):
    if 'venv' in directory:
        return
    print(prefix + os.path.basename(directory), file=file_output)
    for item in os.listdir(directory):
        path = os.path.join(directory, item)
        if os.path.isdir(path):
            print_tree(path, file_output, prefix + '|-- ')
        else:
            print(prefix + '|-- ' + item, file=file_output)

with open('tree.txt', 'w') as file_output:
    print_tree('.', file_output)