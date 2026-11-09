build:
	docker compose up -d --build

up:
	docker compose up -d

down:
	docker compose down

ps:
	docker compose ps

logs:
	docker compose logs -f

t1:
	export VALUE=1
	python client/requisicao.py