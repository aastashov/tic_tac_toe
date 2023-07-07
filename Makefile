back-test:
	pytest backend/tests

install-front:
	npm run install

install-back:
	poetry install

install: install-front install-back

build-js:
	cd frontend/ && npm run build

run-js-dev:
	cd frontend/ && npm run dev

run-dev:
	cd backend/src && uvicorn main:app --reload

tests:
	pytest backend/tests
