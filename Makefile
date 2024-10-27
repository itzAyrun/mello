run:
	python -m mello.main

test:
	python -m mello.main --test

format:
	ruff format .

check:
	ruff check .
