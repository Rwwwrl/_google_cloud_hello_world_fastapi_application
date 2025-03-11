# Docker
up_mongo:
	docker compose -p fastapi-hello-world -f docker-compose.mongo.yml up -d

down_mongo:
	docker compose -p fastapi-hello-world -f docker-compose.mongo.yml down

restart_mongo:
	$(MAKE) down_mongo
	$(MAKE) up_mongo


# Tests
run_pytest:
	pytest -c pytest.ini fastapi_hello_world/tests -s --disable-warnings


# Google cloud
deploy:
	gcloud app deploy --quiet
