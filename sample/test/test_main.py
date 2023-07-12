import sys,os
sys.path.insert(0,'runner/_work/Python/Python/shared_repo/.github/action/sample')
from main import main

# def test_main():
#     sys.argv[0]="hi"
#     range=10
#     main()
# def test_main():
#     os.environ['range'] = '10'
#     sys.argv = ['sample.py', 'argument1']
#     main()
    # assert range == 10
    # assert sample == 'sample.py'

def test_main(monkeypatch, capsys):
    monkeypatch.setenv('range', '10')
    sys.argv = ['sample.py', 'argument1']
    main()
    captured = capsys.readouterr()
