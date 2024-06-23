import pytest
import os
from file_manipulator import *

# テスト用のファイルを作成
TEST_FILENAME = "testfile.txt"
COPY_FILENAME = "copy_of_testfile.txt"
TEST_CONTENTS = "Hello, World!"
REVERSED_CONTENTS = "!dlroW ,olleH"

@pytest.fixture
def setup_and_teardown():
    with open(TEST_FILENAME, 'w') as f:
        f.write(TEST_CONTENTS)
    yield
    os.remove(TEST_FILENAME)
    if os.path.exists(COPY_FILENAME):
        os.remove(COPY_FILENAME)

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
