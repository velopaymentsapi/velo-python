help:
	@echo ""
	@echo "\033[0;34m    Velo Payments - Python Client (\033[1;34mvelo-payments\033[0;34m) \033[0m"
	@echo ""
	@echo "    To dynamically generate the python client based on a spec issue the following command."
	@echo "    You can specify the spec by replacing the url parameter"
	@echo ""
	@echo "\033[92m    make WORKING_SPEC=https://raw.githubusercontent.com/velopaymentsapi/VeloOpenApi/master/spec/openapi.yaml client \033[0m"
	@echo ""

clean:
	rm -Rf docs
	rm -Rf velo_payments
	rm -Rf test
	rm -f README.md
	rm -f requirements.txt
	rm -f setup.py
	rm -f test-requirements.txt
	rm -f tox.ini

python-client:
	docker run --rm -v ${PWD}:/local openapitools/openapi-generator-cli generate \
		-i $$WORKING_SPEC \
		-g python \
		-o /local \
		-c /local/oa3-config.json

trim:
	rm -Rf .openapi-generator
	rm .openapi-generator-ignore
	rm .travis.yml
	rm git_push.sh

info:
	sed -i.bak '1s/# velo-python/# Python client for Velo/' README.md && rm README.md.bak
	sed -i.bak '2s/.*/This library provides a Python client that simplifies interactions with the Velo Payments API. For full details covering the API visit our docs at [Velo Payments APIs](https:\/\/apidocs.velopayments.com). Note: some of the Velo API calls which require authorization via an access token, see the full docs on how to configure./' README.md && rm README.md.bak

client: clean python-client trim info

build:
	python setup.py sdist

publish:
	## make version=2.14.90 publish
	git tag $(version)
	git push origin tag $(version)
	# pip install twine
	# twine upload dist/*
