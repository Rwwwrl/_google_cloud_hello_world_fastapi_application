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


gcloud_set_up:
	gcloud auth login
	gcloud config set project stately-magpie-451912-b8


gcloud_deploy_hello_world_cloud_function:
	gcloud functions deploy hello_world \
		--runtime python311 \
		--gen2 \
		--trigger-http \
		--allow-unauthenticated \
		--source=cloud_functions/hello_world \
		--entry-point=hello_world \
		--region=us-central1


gcloud_deploy_hello_world_js_cloud_function:
	gcloud functions deploy hello_world_js \
		--runtime nodejs20 \
		--no-gen2 \
		--trigger-http \
		--allow-unauthenticated \
		--source=cloud_functions/hello_world_js \
		--entry-point=hello_world_js \
		--region=us-central1

gcloud_deploy_before_create_user_cloud_function:
	gcloud functions deploy before_create_user \
		--runtime nodejs20 \
		--no-gen2 \
		--trigger-http \
		--allow-unauthenticated \
		--entry-point=beforeCreate \
		--source=cloud_functions/before_create_user \
		--region=us-central1
