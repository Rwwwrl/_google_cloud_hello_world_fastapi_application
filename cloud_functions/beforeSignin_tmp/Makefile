deploy:
	gcloud functions deploy before-signin \
		--runtime nodejs20 \
		--no-gen2 \
	    --trigger-http \
		--allow-unauthenticated \
		--entry-point=beforeSignIn \
		--source=. \
		--region europe-central2 \
		--project=fast-academy-458612-a4
