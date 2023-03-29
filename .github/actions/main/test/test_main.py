sys.path.insert(0,'.github/actions/main')
from main import add,main

def test_main():
    assert add(2,3)==5

def test_add():
    add(2,3)
