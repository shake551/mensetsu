up:
	docker-compose \
	  -f docker-compose-python.yml \
		up

upd:
	docker-compose \
	  -f docker-compose-python.yml \
		up -d

down:
	docker-compose \
	  -f docker-compose-python.yml \
		down
