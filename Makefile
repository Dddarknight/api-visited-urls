lint:
	poetry run flake8 .

install:
	poetry install

run:
	poetry run uvicorn api_visited_urls.server:app --reload

test-coverage:
	poetry run pytest --cov=. --cov-report xml

test:
	poetry run pytest