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
        
def duplicate_contents(filename, copy_filename, n):
    output_pathname = get_input_path_and_filename(filename)
    output_filepath = os.path.dirname(output_pathname)
    output_filename = copy_filename
    
    for i in range(1, int(n) + 1):
        contents = ''
        with open(get_input_path_and_filename(filename)) as f:
            contents = f.read()
        
        with open(output_filepath + '/' + f'{output_filename} copy({str(i)}).txt', 'w') as f:
            f.write(contents)

def main():
    
    copy_filename = 'sample'
    processing_input = sys.argv[1]
    args2 = sys.argv[2]
    args3 = sys.argv[3]
    
    if (processing_input == 'reverse'):
        reverse_contents(args2)
    elif (processing_input == 'copy'):
        copy_contents(args2, args3)
    elif (processing_input == 'duplicate'):
        duplicate_contents(args2, copy_filename, args3)
        
    return 0

if __name__ == '__main__':
    sys.exit(main())
    