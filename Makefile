build:
	docker build -t platform-microservice-template .

test:
	pytest --cov

linter:
	black -l 120 --check .