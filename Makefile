.PHONY: tests

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
	@docker run -i --rm mikefarah/yq:3 sh -c "apk -q add curl && curl -s $$WORKING_SPEC -o /tmp/oa3.yaml;  yq r /tmp/oa3.yaml info.version" 2>&1

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
	docker run --rm -v ${PWD}:/local openapitools/openapi-generator-cli:v4.1.3 generate \
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
	# wget https://raw.githubusercontent.com/velopaymentsapi/changelog/main/README.md -O CHANGELOG.md
	sed -i.bak '1s/# velo-python/# Python client for Velo/' README.md && rm README.md.bak
	sed -i.bak '2s/.*/[![License](https:\/\/img.shields.io\/badge\/License-Apache%202.0-blue.svg)](https:\/\/opensource.org\/licenses\/Apache-2.0) [![npm version](https:\/\/badge.fury.io\/py\/velo-python.svg)](https:\/\/badge.fury.io\/py\/velo-python) [![CircleCI](https:\/\/circleci.com\/gh\/velopaymentsapi\/velo-python.svg?style=svg)](https:\/\/circleci.com\/gh\/velopaymentsapi\/velo-python)/' README.md && rm README.md.bak
	sed -i.bak '3s/.*/This library provides a Python client that simplifies interactions with the Velo Payments API. For full details covering the API visit our docs at [Velo Payments APIs](https:\/\/apidocs.velopayments.com). Note: some of the Velo API calls which require authorization via an access token, see the full docs on how to configure./' README.md && rm README.md.bak
	# single quote syntax issue
	sed -i.bak "s/'Payment cannot be processed because of the Payee's OFAC or Compliance Status'/'Payment cannot be processed because of the Payee OFAC or Compliance Status'/" test/test_rejected_payment_v3.py && rm test/test_rejected_payment_v3.py.bak
	# fix generated code : bools
	- sed -i.bak "s/:true/:True/g" test/test_paged_user_response.py && rm test/test_paged_user_response.py.bak
	- sed -i.bak "s/:true/:True/g" test/test_paged_payee_response.py && rm test/test_paged_payee_response.py.bak
	- sed -i.bak "s/:true/:True/g" test/test_paged_payee_response2.py && rm test/test_paged_payee_response2.py.bak
	- sed -i.bak "s/:true/:True/g" test/test_query_batch_response.py && rm test/test_query_batch_response.py.bak
	- sed -i.bak "s/:true/:True/g" test/test_payment.py && rm test/test_payment.py.bak
	- sed -i.bak "s/:true/:True/g" test/test_access_token_response.py && rm test/test_access_token_response.py.bak
	- sed -i.bak "s/:true/:True/g" test/test_failed_submission.py && rm test/test_failed_submission.py.bak
	- sed -i.bak "s/:true/:True/g" test/test_list_payments_response_v4.py && rm test/test_list_payments_response_v4.py.bak
	- sed -i.bak "s/:true/:True/g" test/test_payment_channel_country.py && rm test/test_payment_channel_country.py.bak
	- sed -i.bak "s/:true/:True/g" test/test_list_source_account_response_v3.py && rm test/test_list_source_account_response_v3.py.bak
	- sed -i.bak "s/:true/:True/g" test/test_payment_channel_rules_response.py && rm test/test_payment_channel_rules_response.py.bak
	- sed -i.bak "s/:true/:True/g" test/test_source_account_response_v2.py && rm test/test_source_account_response_v2.py.bak
	- sed -i.bak "s/:true/:True/g" test/test_source_account_response_v3.py && rm test/test_source_account_response_v3.py.bak
	- sed -i.bak "s/:true/:True/g" test/test_get_payments_for_payout_response_v4.py && rm test/test_get_payments_for_payout_response_v4.py.bak
	- sed -i.bak "s/:true/:True/g" test/test_payee.py && rm test/test_payee.py.bak
	- sed -i.bak "s/:true/:True/g" test/test_query_batch_response2.py && rm test/test_query_batch_response2.py.bak
	- sed -i.bak "s/:true/:True/g" test/test_payee_response.py && rm test/test_payee_response.py.bak
	- sed -i.bak "s/:true/:True/g" test/test_user_info.py && rm test/test_user_info.py.bak
	- sed -i.bak "s/:true/:True/g" test/test_failed_submission2.py && rm test/test_failed_submission2.py.bak
	- sed -i.bak "s/:true/:True/g" test/test_payee_response2.py && rm test/test_payee_response2.py.bak
	- sed -i.bak "s/:true/:True/g" test/test_paged_payments_response.py && rm test/test_paged_payments_response.py.bak
	- sed -i.bak "s/:true/:True/g" test/test_list_source_account_response.py && rm test/test_list_source_account_response.py.bak
	- sed -i.bak "s/:false/:False/g" test/test_paged_payments_response.py && rm test/test_paged_payments_response.py.bak
	- sed -i.bak "s/:true/:True/g" test/test_list_source_account_response_v2.py && rm test/test_list_source_account_response_v2.py.bak
	- sed -i.bak "s/:true/:True/g" test/test_payee2.py && rm test/test_payee2.py.bak
	- sed -i.bak "s/:true/:True/g" test/test_payor_v1.py && rm test/test_payor_v1.py.bak
	- sed -i.bak "s/:true/:True/g" test/test_payor_v2.py && rm test/test_payor_v2.py.bak
	- sed -i.bak "s/:false/:False/g" test/test_paged_payments_response_v3.py && rm test/test_paged_payments_response_v3.py.bak
	- sed -i.bak "s/:true/:True/g" test/test_create_payee2.py && rm test/test_create_payee2.py.bak
	- sed -i.bak "s/:true/:True/g" test/test_create_payees_request2.py && rm test/test_create_payees_request2.py.bak
	- sed -i.bak "s/:true/:True/g" test/test_payee_detail_response.py && rm test/test_payee_detail_response.py.bak
	- sed -i.bak "s/:true/:True/g" test/test_get_payee_list_response2.py && rm test/test_get_payee_list_response2.py.bak
	- sed -i.bak "s/:true/:True/g" test/test_payee_detail_response2.py && rm test/test_payee_detail_response2.py.bak
	- sed -i.bak "s/:true/:True/g" test/test_get_payee_list_response.py && rm test/test_get_payee_list_response.py.bak
	- sed -i.bak "s/:true/:True/g" test/test_create_payee.py && rm test/test_create_payee.py.bak
	
	# fix generated code : suffixes
	- sed -i.bak "s/create_payee_address_2/create_payee_address2/g" test/test_create_payee2.py && rm test/test_create_payee2.py.bak
	- sed -i.bak "s/CreatePayeeAddress_2/CreatePayeeAddress2/g" test/test_create_payee2.py && rm test/test_create_payee2.py.bak
	- sed -i.bak "s/create_payment_channel_2/create_payment_channel2/g" test/test_create_payee2.py && rm test/test_create_payee2.py.bak
	- sed -i.bak "s/CreatePaymentChannel_2/CreatePaymentChannel2/g" test/test_create_payee2.py && rm test/test_create_payee2.py.bak
	- sed -i.bak "s/create_individual_2/create_individual2/g" test/test_create_payee2.py && rm test/test_create_payee2.py.bak
	- sed -i.bak "s/CreateIndividual_2/CreateIndividual2/g" test/test_create_payee2.py && rm test/test_create_payee2.py.bak
	- sed -i.bak "s/CreateIndividual2_name/CreateIndividual2Name/g" test/test_create_payee2.py && rm test/test_create_payee2.py.bak
	- sed -i.bak "s/inline_response_401_errors/inline_response401_errors/g" test/test_create_payee2.py && rm test/test_create_payee2.py.bak
	- sed -i.bak "s/models.inline_response_401_errors.inline_response_401_errors/models.inline_response401_errors.InlineResponse401Errors/g" test/test_inline_response401.py && rm test/test_inline_response401.py.bak
	- sed -i.bak "s/PagedResponse_page/PagedResponsePage/g" test/test_get_fundings_response.py && rm test/test_get_fundings_response.py.bak
	- sed -i.bak "s/inline_response_400_errors/inline_response400_errors/g" test/test_inline_response400.py && rm test/test_inline_response400.py.bak
	- sed -i.bak "s/models.inline_response400_errors.inline_response400_errors/models.inline_response400_errors.InlineResponse400Errors/g" test/test_inline_response400.py && rm test/test_inline_response400.py.bak
	- sed -i.bak "s/PagedResponse_page/PagedResponsePage/g" test/test_paged_response.py && rm test/test_paged_response.py.bak
	- sed -i.bak "s/create_individual_2_name/create_individual2_name/g" test/test_create_individual2.py && rm test/test_create_individual2.py.bak
	- sed -i.bak "s/CreateIndividual_2_name/CreateIndividual2Name/g" test/test_create_individual2.py && rm test/test_create_individual2.py.bak
	- sed -i.bak "s/inline_response_409_errors/inline_response409_errors/g" test/test_inline_response409.py && rm test/test_inline_response409.py.bak
	- sed -i.bak "s/models.inline_response409_errors.inline_response409_errors/models.inline_response409_errors.InlineResponse409Errors/g" test/test_inline_response409.py && rm test/test_inline_response409.py.bak
	- sed -i.bak "s/models.inline_response_403_errors.inline_response_403_errors/models.inline_response403_errors.InlineResponse403Errors/g" test/test_inline_response403.py && rm test/test_inline_response403.py.bak
	- sed -i.bak "s/create_individual_2/create_individual2/g" test/test_create_payees_request2.py && rm test/test_create_payees_request2.py.bak
	- sed -i.bak "s/CreateIndividual_2/CreateIndividual2/g" test/test_create_payees_request2.py && rm test/test_create_payees_request2.py.bak
	- sed -i.bak "s/create_payee_2/create_payee2/g" test/test_create_payees_request2.py && rm test/test_create_payees_request2.py.bak
	- sed -i.bak "s/CreatePayee_2/CreatePayee2/g" test/test_create_payees_request2.py && rm test/test_create_payees_request2.py.bak
	- sed -i.bak "s/create_payee_address_2/create_payee_address2/g" test/test_create_payees_request2.py && rm test/test_create_payees_request2.py.bak
	- sed -i.bak "s/CreatePayeeAddress_2/CreatePayeeAddress2/g" test/test_create_payees_request2.py && rm test/test_create_payees_request2.py.bak
	- sed -i.bak "s/create_payment_channel_2/create_payment_channel2/g" test/test_create_payees_request2.py && rm test/test_create_payees_request2.py.bak
	- sed -i.bak "s/CreatePaymentChannel_2/CreatePaymentChannel2/g" test/test_create_payees_request2.py && rm test/test_create_payees_request2.py.bak
	- sed -i.bak "s/CreateIndividual2_name/CreateIndividual2Name/g" test/test_create_payees_request2.py && rm test/test_create_payees_request2.py.bak
	- sed -i.bak "s/inline_response_412_errors.inline_response_412_errors/inline_response412_errors.InlineResponse412Errors/g" test/test_inline_response412.py && rm test/test_inline_response412.py.bak
	- sed -i.bak "s/inline_response_404_errors.inline_response_404_errors/inline_response404_errors.InlineResponse404Errors/g" test/test_inline_response404.py && rm test/test_inline_response404.py.bak
	
	# adjust tox file
	sed -i.bak 's/envlist = py27, py3/envlist = py3/g' tox.ini && rm tox.ini.bak
	sed -i.bak 's/\[\]/-w .\/tests -s/' tox.ini && rm tox.ini.bak
	echo "passenv = *" >> tox.ini

build_client:
	#

client: clean generate trim info build_client

tests:
	# overwrite the generated test stubs _api.py tests only
	rm -Rf test/test_*.py
	cp -Rf tests/ test/
	docker build -t=client-python-tests .
	docker run -t -v $(PWD):/usr/src/app -e KEY=${KEY} -e SECRET=${SECRET} -e PAYOR=${PAYOR} -e APIURL=${APIURL} -e APITOKEN="" client-python-tests tox

commit:
	git add --all
	git commit -am 'bump version to ${VERSION}'
	git push --set-upstream origin master

build:
	docker build -t=client-python-tests .
	sed -i.bak 's/VERSION = ".*"/VERSION = "${VERSION}"/g' setup.py && rm setup.py.bak
	docker run -v $(PWD):/usr/src/app client-python-tests python setup.py sdist

publish:
	git tag $(VERSION)
	git push origin tag $(VERSION)
	docker run -v $(PWD):/usr/src/app client-python-tests twine upload --verbose --config-file=.pypirc dist/*
