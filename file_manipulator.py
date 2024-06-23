import os
import sys

def get_input_path_and_filename(filename):
    path = os.getcwd()
    return path + '/' + filename

def readfile(filename):
    with open(get_input_path_and_filename(filename)) as f:
        contents = f.read()
        return contents

def writefile(filename, contents):
    with open(get_input_path_and_filename(filename), 'w') as f:
        f.write(contents)

def reverse_contents(filename):
    contents = readfile(filename)
    reversed_contents =  ''.join(list(reversed(contents)))
    writefile(filename, reversed_contents)
        
def copy_contents(filename, output_pathname):
    contents = ''
    with open(get_input_path_and_filename(filename)) as f:
        contents = f.read()
        
    with open(output_pathname, 'w') as f:
        f.write(contents)

def main():
    
    processing_input = sys.argv[1]
    args2 = sys.argv[2]
    args3 = sys.argv[3]
    
    if (processing_input == 'reverse'):
        reverse_contents(args2)
    elif (processing_input == 'copy'):
        copy_contents(args2, args3)
        
    return 0

if __name__ == '__main__':
    sys.exit(main())
    