install:
	pip install -r requirements.txt

gui:
	python3 reconciliation_gui/reconciliation_gui.py
cli:
	python3 reconciliation-cli/reconciliation_cli.py -s reconciliation-cli/source.csv -t reconciliation-cli/target.csv -o reconciliation-cli/reconciliation_report.csv

black:
	python3 -m black .
isort:
	python3 -m isort .


