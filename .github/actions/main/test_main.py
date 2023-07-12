import sys
import logging
sys.path.insert(0,'.github/actions/main')
from main import main

ef test_main(monkeypatch, capsys):
    monkeypatch.setenv('range', '10')
    sys.argv = ['sample.py', 'argument1']
    main()
    captured = capsys.readouterr()
