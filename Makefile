install:
	pip install --upgrade pip && pip install -r requirements.txt

format:
	black *.py

lint:
	pylint --disable=R,C --fail-under=8 textadventure.py dungeon.py

test:
	python -m pytest -vv --cov=dungeon test_textadventure.py
