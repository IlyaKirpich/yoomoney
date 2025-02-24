.PHONY: all build run down ps logs config

PREFIX=docker-compose --env-file .env

all: build run

build:
	${PREFIX} build

run:
	${PREFIX} up -d

down:
	${PREFIX} down -v

ps:
	${PREFIX} ps -a

logs:
	${PREFIX} logs ${AT}

config:
	cp .env.example .env