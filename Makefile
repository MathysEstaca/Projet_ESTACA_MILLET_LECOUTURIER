.PHONY: all
all: install test sphinx coverage

install:
	@pip install -r requirements.txt

test:
	@pytest test

sphinx:
	@make -C doc/ html

coverage:
	@coverage run --source src/ -m pytest
	@coverage report