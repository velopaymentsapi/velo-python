# Python client for Velo
This library provides a Python client that simplifies interactions with the Velo Payments API. For full details covering the API visit our docs at [Velo Payments APIs](https://apidocs.velopayments.com). Note: some of the Velo API calls which require authorization via an access token, see the full docs on how to configure.

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 2.15.95
- Package version: 2.15.95
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import velo_payments 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import velo_payments
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import velo_payments
from velo_payments.rest import ApiException
from pprint import pprint

configuration = velo_payments.Configuration()
# Configure HTTP basic authorization: basicAuth
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# Defining host is optional and default to https://api.sandbox.velopayments.com
configuration.host = "https://api.sandbox.velopayments.com"
# Create an instance of the API class
api_instance = velo_payments.AuthApi(velo_payments.ApiClient(configuration))
grant_type = 'client_credentials' # str | OAuth grant type. Should use 'client_credentials' (optional) (default to 'client_credentials')

try:
    # Authentication endpoint
    api_response = api_instance.velo_auth(grant_type=grant_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthApi->velo_auth: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://api.sandbox.velopayments.com*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AuthApi* | [**velo_auth**](docs/AuthApi.md#velo_auth) | **POST** /v1/authenticate | Authentication endpoint
*CountriesApi* | [**list_supported_countries**](docs/CountriesApi.md#list_supported_countries) | **GET** /v1/supportedCountries | List Supported Countries
*CountriesApi* | [**v1_payment_channel_rules_get**](docs/CountriesApi.md#v1_payment_channel_rules_get) | **GET** /v1/paymentChannelRules | List Payment Channel Country Rules
*CurrenciesApi* | [**list_supported_currencies**](docs/CurrenciesApi.md#list_supported_currencies) | **GET** /v2/currencies | List Supported Currencies
*FundingManagerApi* | [**create_ach_funding_request**](docs/FundingManagerApi.md#create_ach_funding_request) | **POST** /v1/sourceAccounts/{sourceAccountId}/achFundingRequest | Create Funding Request
*FundingManagerApi* | [**create_funding_request**](docs/FundingManagerApi.md#create_funding_request) | **POST** /v2/sourceAccounts/{sourceAccountId}/fundingRequest | Create Funding Request
*FundingManagerApi* | [**get_fundings**](docs/FundingManagerApi.md#get_fundings) | **GET** /v1/paymentaudit/fundings | Get Fundings for Payor
*FundingManagerApi* | [**get_source_account**](docs/FundingManagerApi.md#get_source_account) | **GET** /v1/sourceAccounts/{sourceAccountId} | Get details about given source account.
*FundingManagerApi* | [**get_source_account_v2**](docs/FundingManagerApi.md#get_source_account_v2) | **GET** /v2/sourceAccounts/{sourceAccountId} | Get details about given source account.
*FundingManagerApi* | [**get_source_accounts**](docs/FundingManagerApi.md#get_source_accounts) | **GET** /v1/sourceAccounts | Get list of source accounts
*FundingManagerApi* | [**get_source_accounts_v2**](docs/FundingManagerApi.md#get_source_accounts_v2) | **GET** /v2/sourceAccounts | Get list of source accounts
*FundingManagerApi* | [**set_notifications_request**](docs/FundingManagerApi.md#set_notifications_request) | **POST** /v1/sourceAccounts/{sourceAccountId}/notifications | Set notifications
*GetPayoutApi* | [**v3_payouts_payout_id_get**](docs/GetPayoutApi.md#v3_payouts_payout_id_get) | **GET** /v3/payouts/{payoutId} | Get Payout Summary
*InstructPayoutApi* | [**v3_payouts_payout_id_post**](docs/InstructPayoutApi.md#v3_payouts_payout_id_post) | **POST** /v3/payouts/{payoutId} | Instruct Payout
*PayeeInvitationApi* | [**get_payees_invitation_status**](docs/PayeeInvitationApi.md#get_payees_invitation_status) | **GET** /v1/payees/payors/{payorId}/invitationStatus | Get Payee Invitation Status
*PayeeInvitationApi* | [**get_payees_invitation_status_v2**](docs/PayeeInvitationApi.md#get_payees_invitation_status_v2) | **GET** /v2/payees/payors/{payorId}/invitationStatus | Get Payee Invitation Status
*PayeeInvitationApi* | [**resend_payee_invite**](docs/PayeeInvitationApi.md#resend_payee_invite) | **POST** /v1/payees/{payeeId}/invite | Resend Payee Invite
*PayeeInvitationApi* | [**v2_create_payee**](docs/PayeeInvitationApi.md#v2_create_payee) | **POST** /v2/payees | Intiate Payee Creation
*PayeeInvitationApi* | [**v2_query_batch_status**](docs/PayeeInvitationApi.md#v2_query_batch_status) | **GET** /v2/payees/batch/{batchId} | Query Batch Status
*PayeesApi* | [**delete_payee_by_id**](docs/PayeesApi.md#delete_payee_by_id) | **DELETE** /v1/payees/{payeeId} | Delete Payee by Id
*PayeesApi* | [**get_payee_by_id**](docs/PayeesApi.md#get_payee_by_id) | **GET** /v1/payees/{payeeId} | Get Payee by Id
*PayeesApi* | [**list_payee_changes**](docs/PayeesApi.md#list_payee_changes) | **GET** /v1/deltas/payees | List Payee Changes
*PayeesApi* | [**list_payees**](docs/PayeesApi.md#list_payees) | **GET** /v1/payees | List Payees
*PaymentAuditServiceApi* | [**export_transactions_csv**](docs/PaymentAuditServiceApi.md#export_transactions_csv) | **GET** /v4/paymentaudit/transactions | Export Transactions
*PaymentAuditServiceApi* | [**get_fundings**](docs/PaymentAuditServiceApi.md#get_fundings) | **GET** /v1/paymentaudit/fundings | Get Fundings for Payor
*PaymentAuditServiceApi* | [**get_payment_details**](docs/PaymentAuditServiceApi.md#get_payment_details) | **GET** /v3/paymentaudit/payments/{paymentId} | Get Payment
*PaymentAuditServiceApi* | [**get_payment_details_v4**](docs/PaymentAuditServiceApi.md#get_payment_details_v4) | **GET** /v4/paymentaudit/payments/{paymentId} | Get Payment
*PaymentAuditServiceApi* | [**get_payments_for_payout**](docs/PaymentAuditServiceApi.md#get_payments_for_payout) | **GET** /v3/paymentaudit/payouts/{payoutId} | Get Payments for Payout
*PaymentAuditServiceApi* | [**get_payments_for_payout_v4**](docs/PaymentAuditServiceApi.md#get_payments_for_payout_v4) | **GET** /v4/paymentaudit/payouts/{payoutId} | Get Payments for Payout
*PaymentAuditServiceApi* | [**get_payouts_for_payor**](docs/PaymentAuditServiceApi.md#get_payouts_for_payor) | **GET** /v3/paymentaudit/payouts | Get Payouts for Payor
*PaymentAuditServiceApi* | [**get_payouts_for_payor_v4**](docs/PaymentAuditServiceApi.md#get_payouts_for_payor_v4) | **GET** /v4/paymentaudit/payouts | Get Payouts for Payor
*PaymentAuditServiceApi* | [**list_payment_changes**](docs/PaymentAuditServiceApi.md#list_payment_changes) | **GET** /v1/deltas/payments | List Payment Changes
*PaymentAuditServiceApi* | [**list_payments_audit**](docs/PaymentAuditServiceApi.md#list_payments_audit) | **GET** /v3/paymentaudit/payments | Get List of Payments
*PaymentAuditServiceApi* | [**list_payments_audit_v4**](docs/PaymentAuditServiceApi.md#list_payments_audit_v4) | **GET** /v4/paymentaudit/payments | Get List of Payments
*PayorApplicationsApi* | [**payor_create_api_key_request**](docs/PayorApplicationsApi.md#payor_create_api_key_request) | **POST** /v1/payors/{payorId}/applications/{applicationId}/keys | Create API Key
*PayorApplicationsApi* | [**payor_create_application_request**](docs/PayorApplicationsApi.md#payor_create_application_request) | **POST** /v1/payors/{payorId}/applications | Create Application
*PayorsApi* | [**get_payor_by_id**](docs/PayorsApi.md#get_payor_by_id) | **GET** /v1/payors/{payorId} | Get Payor
*PayorsApi* | [**get_payor_by_id_v2**](docs/PayorsApi.md#get_payor_by_id_v2) | **GET** /v2/payors/{payorId} | Get Payor
*PayorsApi* | [**payor_add_payor_logo**](docs/PayorsApi.md#payor_add_payor_logo) | **POST** /v1/payors/{payorId}/branding/logos | Add Logo
*PayorsApi* | [**payor_email_opt_out**](docs/PayorsApi.md#payor_email_opt_out) | **POST** /v1/payors/{payorId}/reminderEmailsUpdate | Reminder Email Opt-Out
*PayorsApi* | [**payor_get_branding**](docs/PayorsApi.md#payor_get_branding) | **GET** /v1/payors/{payorId}/branding | Get Branding
*PayorsApi* | [**payor_links**](docs/PayorsApi.md#payor_links) | **GET** /v1/payorLinks | List Payor Links
*PayoutHistoryApi* | [**get_payments_for_payout**](docs/PayoutHistoryApi.md#get_payments_for_payout) | **GET** /v3/paymentaudit/payouts/{payoutId} | Get Payments for Payout
*PayoutHistoryApi* | [**get_payments_for_payout_v4**](docs/PayoutHistoryApi.md#get_payments_for_payout_v4) | **GET** /v4/paymentaudit/payouts/{payoutId} | Get Payments for Payout
*PayoutHistoryApi* | [**get_payout_stats**](docs/PayoutHistoryApi.md#get_payout_stats) | **GET** /v1/paymentaudit/payoutStatistics | Get Payout Statistics
*QuotePayoutApi* | [**v3_payouts_payout_id_quote_post**](docs/QuotePayoutApi.md#v3_payouts_payout_id_quote_post) | **POST** /v3/payouts/{payoutId}/quote | Create a quote for the payout
*SubmitPayoutApi* | [**submit_payout**](docs/SubmitPayoutApi.md#submit_payout) | **POST** /v3/payouts | Submit Payout
*WithdrawPayoutApi* | [**v3_payouts_payout_id_delete**](docs/WithdrawPayoutApi.md#v3_payouts_payout_id_delete) | **DELETE** /v3/payouts/{payoutId} | Withdraw Payout


## Documentation For Models

 - [Address](docs/Address.md)
 - [AuthResponse](docs/AuthResponse.md)
 - [AutoTopUpConfig](docs/AutoTopUpConfig.md)
 - [Challenge](docs/Challenge.md)
 - [Company](docs/Company.md)
 - [CreateIndividual](docs/CreateIndividual.md)
 - [CreatePayee](docs/CreatePayee.md)
 - [CreatePayeeAddress](docs/CreatePayeeAddress.md)
 - [CreatePayeesCSVRequest](docs/CreatePayeesCSVRequest.md)
 - [CreatePayeesCSVResponse](docs/CreatePayeesCSVResponse.md)
 - [CreatePayeesRequest](docs/CreatePayeesRequest.md)
 - [CreatePaymentChannel](docs/CreatePaymentChannel.md)
 - [CreatePayoutRequest](docs/CreatePayoutRequest.md)
 - [FailedSubmission](docs/FailedSubmission.md)
 - [FundingAudit](docs/FundingAudit.md)
 - [FundingEvent](docs/FundingEvent.md)
 - [FundingEventType](docs/FundingEventType.md)
 - [FundingRequestV1](docs/FundingRequestV1.md)
 - [FundingRequestV2](docs/FundingRequestV2.md)
 - [FxSummaryV3](docs/FxSummaryV3.md)
 - [FxSummaryV4](docs/FxSummaryV4.md)
 - [GetFundingsResponse](docs/GetFundingsResponse.md)
 - [GetFundingsResponseAllOf](docs/GetFundingsResponseAllOf.md)
 - [GetPaymentsForPayoutResponseV3](docs/GetPaymentsForPayoutResponseV3.md)
 - [GetPaymentsForPayoutResponseV3Page](docs/GetPaymentsForPayoutResponseV3Page.md)
 - [GetPaymentsForPayoutResponseV3Summary](docs/GetPaymentsForPayoutResponseV3Summary.md)
 - [GetPaymentsForPayoutResponseV4](docs/GetPaymentsForPayoutResponseV4.md)
 - [GetPaymentsForPayoutResponseV4Summary](docs/GetPaymentsForPayoutResponseV4Summary.md)
 - [GetPayoutStatistics](docs/GetPayoutStatistics.md)
 - [GetPayoutsResponseV3](docs/GetPayoutsResponseV3.md)
 - [GetPayoutsResponseV3Links](docs/GetPayoutsResponseV3Links.md)
 - [GetPayoutsResponseV3Page](docs/GetPayoutsResponseV3Page.md)
 - [GetPayoutsResponseV3Summary](docs/GetPayoutsResponseV3Summary.md)
 - [GetPayoutsResponseV4](docs/GetPayoutsResponseV4.md)
 - [Individual](docs/Individual.md)
 - [IndividualName](docs/IndividualName.md)
 - [InvitationStatus](docs/InvitationStatus.md)
 - [InvitationStatusResponse](docs/InvitationStatusResponse.md)
 - [InvitePayeeRequest](docs/InvitePayeeRequest.md)
 - [Language](docs/Language.md)
 - [ListPaymentsResponse](docs/ListPaymentsResponse.md)
 - [ListPaymentsResponsePage](docs/ListPaymentsResponsePage.md)
 - [ListPaymentsResponseSummary](docs/ListPaymentsResponseSummary.md)
 - [ListSourceAccountResponse](docs/ListSourceAccountResponse.md)
 - [ListSourceAccountResponseLinks](docs/ListSourceAccountResponseLinks.md)
 - [ListSourceAccountResponsePage](docs/ListSourceAccountResponsePage.md)
 - [ListSourceAccountResponseV2](docs/ListSourceAccountResponseV2.md)
 - [ListSourceAccountResponseV2Page](docs/ListSourceAccountResponseV2Page.md)
 - [MarketingOptIn](docs/MarketingOptIn.md)
 - [Notifications](docs/Notifications.md)
 - [OfacStatus](docs/OfacStatus.md)
 - [OnboardedStatus](docs/OnboardedStatus.md)
 - [PagedPayeeInvitationStatusResponse](docs/PagedPayeeInvitationStatusResponse.md)
 - [PagedResponse](docs/PagedResponse.md)
 - [PagedResponsePage](docs/PagedResponsePage.md)
 - [Payee](docs/Payee.md)
 - [PayeeDelta](docs/PayeeDelta.md)
 - [PayeeDeltaResponse](docs/PayeeDeltaResponse.md)
 - [PayeeDeltaResponseLinks](docs/PayeeDeltaResponseLinks.md)
 - [PayeeDeltaResponsePage](docs/PayeeDeltaResponsePage.md)
 - [PayeeInvitationStatus](docs/PayeeInvitationStatus.md)
 - [PayeeInvitationStatusResponse](docs/PayeeInvitationStatusResponse.md)
 - [PayeeResponse](docs/PayeeResponse.md)
 - [PayeeResponseLinks](docs/PayeeResponseLinks.md)
 - [PayeeResponsePage](docs/PayeeResponsePage.md)
 - [PayeeResponseSummary](docs/PayeeResponseSummary.md)
 - [PayeeType](docs/PayeeType.md)
 - [PaymentAuditCurrencyV3](docs/PaymentAuditCurrencyV3.md)
 - [PaymentAuditCurrencyV4](docs/PaymentAuditCurrencyV4.md)
 - [PaymentChannel](docs/PaymentChannel.md)
 - [PaymentChannelCountry](docs/PaymentChannelCountry.md)
 - [PaymentChannelRule](docs/PaymentChannelRule.md)
 - [PaymentChannelRulesResponse](docs/PaymentChannelRulesResponse.md)
 - [PaymentDelta](docs/PaymentDelta.md)
 - [PaymentDeltaResponse](docs/PaymentDeltaResponse.md)
 - [PaymentEventResponseV3](docs/PaymentEventResponseV3.md)
 - [PaymentEventResponseV4](docs/PaymentEventResponseV4.md)
 - [PaymentInstruction](docs/PaymentInstruction.md)
 - [PaymentResponseV3](docs/PaymentResponseV3.md)
 - [PaymentResponseV4](docs/PaymentResponseV4.md)
 - [PaymentStatus](docs/PaymentStatus.md)
 - [PayorBrandingResponse](docs/PayorBrandingResponse.md)
 - [PayorCreateApiKeyRequest](docs/PayorCreateApiKeyRequest.md)
 - [PayorCreateApiKeyResponse](docs/PayorCreateApiKeyResponse.md)
 - [PayorCreateApplicationRequest](docs/PayorCreateApplicationRequest.md)
 - [PayorEmailOptOutRequest](docs/PayorEmailOptOutRequest.md)
 - [PayorLinksResponse](docs/PayorLinksResponse.md)
 - [PayorLinksResponseLinks](docs/PayorLinksResponseLinks.md)
 - [PayorLinksResponsePayors](docs/PayorLinksResponsePayors.md)
 - [PayorLogoRequest](docs/PayorLogoRequest.md)
 - [PayorRef](docs/PayorRef.md)
 - [PayorV1](docs/PayorV1.md)
 - [PayorV2](docs/PayorV2.md)
 - [PayoutStatusV3](docs/PayoutStatusV3.md)
 - [PayoutStatusV4](docs/PayoutStatusV4.md)
 - [PayoutSummaryAuditV3](docs/PayoutSummaryAuditV3.md)
 - [PayoutSummaryAuditV4](docs/PayoutSummaryAuditV4.md)
 - [PayoutSummaryResponse](docs/PayoutSummaryResponse.md)
 - [QueryBatchResponse](docs/QueryBatchResponse.md)
 - [QuoteFxSummary](docs/QuoteFxSummary.md)
 - [QuoteResponse](docs/QuoteResponse.md)
 - [RejectedPayment](docs/RejectedPayment.md)
 - [SetNotificationsRequest](docs/SetNotificationsRequest.md)
 - [SourceAccount](docs/SourceAccount.md)
 - [SourceAccountResponse](docs/SourceAccountResponse.md)
 - [SourceAccountResponseV2](docs/SourceAccountResponseV2.md)
 - [SourceAccountSummaryV3](docs/SourceAccountSummaryV3.md)
 - [SourceAccountSummaryV4](docs/SourceAccountSummaryV4.md)
 - [SupportedCountriesResponse](docs/SupportedCountriesResponse.md)
 - [SupportedCountry](docs/SupportedCountry.md)
 - [SupportedCurrency](docs/SupportedCurrency.md)
 - [SupportedCurrencyResponse](docs/SupportedCurrencyResponse.md)


## Documentation For Authorization


## OAuth2

- **Type**: OAuth
- **Flow**: application
- **Authorization URL**: 
- **Scopes**: 
 - ** **: Scopes not required


## basicAuth

- **Type**: HTTP basic authentication


## Author




