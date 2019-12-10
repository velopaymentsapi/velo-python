help:
	@echo ""
	@echo "\033[0;34m    Velo Payments - Python Client (\033[1;34mvelo-payments\033[0;34m) \033[0m"
	@echo ""
	@echo "    To dynamically generate the python client based on a spec issue the following command."
	@echo "    You can specify the spec by replacing the url parameter"
	@echo ""
	@echo "\033[92m    make WORKING_SPEC=https://raw.githubusercontent.com/velopaymentsapi/VeloOpenApi/master/spec/openapi.yaml client \033[0m"
	@echo ""

version:
	@docker run -i --rm mikefarah/yq sh -c "apk -q add curl && curl -s $$WORKING_SPEC -o /tmp/oa3.yaml;  yq r /tmp/oa3.yaml info.version" 2>&1

oa3config:
	sed -i.bak 's/"packageVersion": ".*"/"packageVersion": "${VERSION}"/g' oa3-config.json && rm oa3-config.json.bak

clean:
	rm -Rf docs
	rm -Rf velo_payments
	rm -Rf test
	-rm -Rf dist
	-rm -Rf .tox
	-rm -Rf ./*.egg-info
	rm -f README.md
	rm -f requirements.txt
	rm -f setup.py
	rm -f test-requirements.txt
	rm -f tox.ini

generate:
	docker run --rm -v ${PWD}:/local openapitools/openapi-generator-cli generate \
		-i $$WORKING_SPEC \
		-g python \
		-o /local \
		-c /local/oa3-config.json

trim:
	- rm -Rf .openapi-generator
	- rm .openapi-generator-ignore
	- rm .travis.yml
	- rm git_push.sh

info:
	sed -i.bak '1s/# velo-python/# Python client for Velo/' README.md && rm README.md.bak
	sed -i.bak '2s/.*/[![License](https:\/\/img.shields.io\/badge\/License-Apache%202.0-blue.svg)](https:\/\/opensource.org\/licenses\/Apache-2.0) [![npm version](https:\/\/badge.fury.io\/py\/velo-python.svg)](https:\/\/badge.fury.io\/py\/velo-python) [![CircleCI](https:\/\/circleci.com\/gh\/velopaymentsapi\/velo-python.svg?style=svg)](https:\/\/circleci.com\/gh\/velopaymentsapi\/velo-python)/' README.md && rm README.md.bak
	sed -i.bak '3s/.*/This library provides a Python client that simplifies interactions with the Velo Payments API. For full details covering the API visit our docs at [Velo Payments APIs](https:\/\/apidocs.velopayments.com). Note: some of the Velo API calls which require authorization via an access token, see the full docs on how to configure./' README.md && rm README.md.bak

build_client:
	#

client: clean generate trim info build_client

tests:
	sed -i.bak 's/envlist = py27, py3/envlist = py3/g' tox.ini && rm tox.ini.bak
	docker build -t=client-python-tests .
	docker run -v $(PWD):/usr/src/app client-python-tests tox

commit:
	git add --all
	git commit -am 'bump version to ${VERSION}'
	git push --set-upstream origin master

build:
	sed -i.bak 's/VERSION = ".*"/VERSION = "${VERSION}"/g' setup.py && rm setup.py.bak
	docker run -v $(PWD):/usr/src/app client-python-tests python setup.py sdist

publish:
	git tag $(VERSION)
	git push origin tag $(VERSION)
	docker run -v $(PWD):/usr/src/app client-python-tests twine upload --verbose --config-file=.pypirc dist/*
