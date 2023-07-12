import sys
import logging
import pytest
from unittest.mock import patch

sys.path.insert(0,'.github/actions/main')
from main import main

def test_main(monkeypatch, capsys):
    monkeypatch.setenv('range', '10')
    sys.argv = ['sample.py', 'argument1']
    main()
    captured = capsys.readouterr()

@pytest.fixture
def mock_os_getenv():
    with patch.object(os, 'getenv', return_value='10'):
        yield

def test_range_mocked(mock_os_getenv):
    range = os.getenv('range')
    assert range == '10'
