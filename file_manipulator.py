import os
import sys

def get_input_path_and_filename(filename):
    path = os.getcwd()
    return path + '/' + filename

def get_output_path_and_filename(filename):
    path = os.getcwd()
    return path + '/' + filename

def readfile(filename):
    with open(get_input_path_and_filename(filename)) as f:
        contents = f.read()
        return contents

def writefile(filename, contents):
    with open(get_output_path_and_filename(filename), 'w') as f:
        f.write(contents)

def reverse_contents(filename):
    contents = readfile(filename)
    reversed_contents =  ''.join(list(reversed(contents)))
    writefile(filename, reversed_contents)
        
def copy_contents(filename, copy_filename):
    contents = readfile(filename)
    writefile(copy_filename, contents)   
        
def duplicate_contents(filename, n):
    # output_pathname = get_input_path_and_filename(filename)
    output_dirname = os.getcwd()
    output_filename = 'sample'
    
    for i in range(1, int(n) + 1):
        contents = readfile(filename)
        with open(f'{output_dirname}/{output_filename} copy({str(i)}).txt', 'w') as f:
            f.write(contents)

def replace_string(filename, needle, newstring):
    contents = readfile(filename)
    contents = contents.replace(needle, newstring)
    print(contents)
    writefile(filename, contents)

def main():
    
    processing_input = sys.argv[1]
    
    if (processing_input == 'reverse'):
        filename = sys.argv[2]
        reverse_contents(filename)
    elif (processing_input == 'copy'):
        filename = sys.argv[2]
        outputpath = sys.argv[3]
        copy_contents(filename, outputpath)
    elif (processing_input == 'duplicate'):
        filename = sys.argv[2]
        n = sys.argv[3]
        duplicate_contents(filename, n)
    elif (processing_input == 'replace-string'):
        filename = sys.argv[2]
        needle = sys.argv[3]
        newstring = sys.argv[4]
        replace_string(filename, needle, newstring)
    return 0

if __name__ == '__main__':
    sys.exit(main())
    