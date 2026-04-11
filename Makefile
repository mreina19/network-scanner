.PHONY: run install clean

install:
	pip install -r requirements.txt

run:
	python network_scanner.py

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -name "*.pyc" -delete
