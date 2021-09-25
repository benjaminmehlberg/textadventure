install:
	pip install --upgrade pip && pip install -r requirements.txt

format:
	black *.py

lint:
	python3 -m pylint --disable=R,C --fail-under=9 textadventure.py dungeon.py

test:
	python3 -m pytest -s -vv --cov=textadventure test_textadventure.py
