import sys,os
import logging
import pytest
from pytest import MonkeyPatch
from unittest.mock import patch

sys.path.insert(0,'.github/actions/main')
from main import main

# @pytest.mark.parametrize("range_value", [10, 20, 30])  # Add the desired values for testing
# def test_main(range_value):
#     with monkeypatch.context() as m:
#         m.setenv("RANGE", str(range_value))
#         captured_output = capsys.readouterr()
#         main()
#         assert captured_output.out.strip() == str(range_value)

@pytest.mark.parametrize("read_value", ["jayanth",'varshith'])  # Add the desired values for testing
def test_main(range_value, monkeypatch, capsys):
    monkeypatch.setenv("RANGE", str(read_value))
    main()
    captured_output = capsys.readouterr()
    # assert captured_output.out.strip() == str(range_value)
