import pytest
import os
from file_manipulator import *

# テスト用のファイルを作成
TEST_FILENAME = "testfile.txt"
TEST_CONTENTS = "Hello, World!"
REVERSED_CONTENTS = "!dlroW ,olleH"

@pytest.fixture
def setup_and_teardown():
    with open(TEST_FILENAME, 'w') as f:
        f.write(TEST_CONTENTS)
    yield
    os.remove(TEST_FILENAME)

def test_reverse_contents(setup_and_teardown):
    reverse_contents(TEST_FILENAME)
    
    with open(TEST_FILENAME, 'r') as f:
        contents = f.read()
    assert contents == REVERSED_CONTENTS

