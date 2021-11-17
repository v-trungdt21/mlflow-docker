.PHONY: up down logs build

build:
	docker-compose build
up:
	docker-compose up -d
up-test:
	docker-compose up
down:
	docker-compose down
logs:
	docker-compose logs -f