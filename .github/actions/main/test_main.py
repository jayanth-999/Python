import sys,os
import logging
import pytest
from unittest.mock import patch

sys.path.insert(0,'.github/actions/main')
from main import main

@pytest.mark.parametrize("range_value", [10, 20, 30])  # Add the desired values for testing
def test_main(range_value):
    with monkeypatch.context() as m:
        m.setenv("RANGE", str(range_value))
        captured_output = capsys.readouterr()
        main()
        assert captured_output.out.strip() == str(range_value)
