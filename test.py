import pytest
import os
import shutil
from file_manipulator import *

# テスト用のファイルを作成
TEST_FILENAME = "testfile.txt"
TEST_CONTENTS = "Hello, World!"
REVERSED_CONTENTS = "!dlroW ,olleH"
COPY_FILENAME = "copy_of_testfile.txt"
TEST_DIR = 'test_files'
DUPLICATE_FILENAME = "sample"

@pytest.fixture
def setup_and_teardown():
    with open(TEST_FILENAME, 'w') as f:
        f.write(TEST_CONTENTS)
    os.makedirs(TEST_DIR, exist_ok=True)
    yield
    os.remove(TEST_FILENAME)
    if os.path.exists(COPY_FILENAME):
        os.remove(COPY_FILENAME)
    elif os.path.exists(TEST_DIR):
        files = os.listdir(TEST_DIR)
        for file in files:
            os.remove(os.path.join(TEST_DIR, file))
        os.rmdir(TEST_DIR)
        
def test_reverse_contents(setup_and_teardown):
    reverse_contents(TEST_FILENAME)
    
    with open(TEST_FILENAME, 'r') as f:
        contents = f.read()
    assert contents == REVERSED_CONTENTS

def test_copy_contents(setup_and_teardown):
    copy_contents(TEST_FILENAME, COPY_FILENAME)
    assert os.path.exists(COPY_FILENAME), f"Error: The file {COPY_FILENAME} was not created."
    with open(COPY_FILENAME, 'r') as f:
        contents = f.read()
    assert contents == TEST_CONTENTS, f"Error: The contents of {COPY_FILENAME} do not match the original file."

def test_duplicate_contents(setup_and_teardown):
    n = 3
    duplicate_contents(TEST_FILENAME, n)
    for i in range(1, n + 1):
        shutil.move(f'{DUPLICATE_FILENAME} copy({str(i)}).txt', f'{TEST_DIR}/')
        copy_path = f'{TEST_DIR}/{DUPLICATE_FILENAME} copy({str(i)}).txt'
        assert os.path.exists(copy_path)
        with open(copy_path, 'r') as f:
            contents = f.read()
            assert contents == TEST_CONTENTS, f"Error: The contents of {copy_path} do not match the original file."