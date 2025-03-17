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



# Test stand
test_stand_deploy_to_app_engine:
	mv env.toml env.back.toml
	gcloud storage cp gs://test-eu-configuration/env.toml ./
	gcloud app deploy --project fastapi-hello-world-test-eu --quiet
	rm env.toml
	mv env.back.toml env.toml

test_stand_deploy_before_create_user_cloud_function:
	gcloud functions deploy before_create_user \
		--runtime nodejs20 \
		--no-gen2 \
		--trigger-http \
		--allow-unauthenticated \
		--entry-point=beforeCreate \
		--source=cloud_functions/before_create_user \
		--region=europe-central2 \
		--project=fastapi-hello-world-test-eu

test_stand_deploy_before_hello_world_js_cloud_function:
	gcloud functions deploy hello_world_js \
		--runtime nodejs20 \
		--no-gen2 \
		--trigger-http \
		--allow-unauthenticated \
		--entry-point=hello_world_js \
		--source=cloud_functions/for_tests/hello_world_js \
		--region=europe-central2 \
		--project=fastapi-hello-world-test-eu \
		--set-env-vars ENV_VARIABLE1=ENV_VARIABLE1_VALUE
