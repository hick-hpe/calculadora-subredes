.PHONY: tests

build:
	docker compose up --build

up:
	docker compose up

down:
	docker compose down

ps:
	docker compose ps

logs:
	docker compose logs -f

tests:
	docker exec -it app_rede python -m pytest -v --disable-warnings --maxfail=1