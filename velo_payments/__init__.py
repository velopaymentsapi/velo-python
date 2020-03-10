# coding: utf-8

# flake8: noqa

"""
    Velo Payments APIs

    ## Terms and Definitions  Throughout this document and the Velo platform the following terms are used:  * **Payor.** An entity (typically a corporation) which wishes to pay funds to one or more payees via a payout. * **Payee.** The recipient of funds paid out by a payor. * **Payment.** A single transfer of funds from a payor to a payee. * **Payout.** A batch of Payments, typically used by a payor to logically group payments (e.g. by business day). Technically there need be no relationship between the payments in a payout - a single payout can contain payments to multiple payees and/or multiple payments to a single payee. * **Sandbox.** An integration environment provided by Velo Payments which offers a similar API experience to the production environment, but all funding and payment events are simulated, along with many other services such as OFAC sanctions list checking.  ## Overview  The Velo Payments API allows a payor to perform a number of operations. The following is a list of the main capabilities in a natural order of execution:  * Authenticate with the Velo platform * Maintain a collection of payees * Query the payor’s current balance of funds within the platform and perform additional funding * Issue payments to payees * Query the platform for a history of those payments  This document describes the main concepts and APIs required to get up and running with the Velo Payments platform. It is not an exhaustive API reference. For that, please see the separate Velo Payments API Reference.  ## API Considerations  The Velo Payments API is REST based and uses the JSON format for requests and responses.  Most calls are secured using OAuth 2 security and require a valid authentication access token for successful operation. See the Authentication section for details.  Where a dynamic value is required in the examples below, the {token} format is used, suggesting that the caller needs to supply the appropriate value of the token in question (without including the { or } characters).  Where curl examples are given, the –d @filename.json approach is used, indicating that the request body should be placed into a file named filename.json in the current directory. Each of the curl examples in this document should be considered a single line on the command-line, regardless of how they appear in print.  ## Authenticating with the Velo Platform  Once Velo backoffice staff have added your organization as a payor within the Velo platform sandbox, they will create you a payor Id, an API key and an API secret and share these with you in a secure manner.  You will need to use these values to authenticate with the Velo platform in order to gain access to the APIs. The steps to take are explained in the following:  create a string comprising the API key (e.g. 44a9537d-d55d-4b47-8082-14061c2bcdd8) and API secret (e.g. c396b26b-137a-44fd-87f5-34631f8fd529) with a colon between them. E.g. 44a9537d-d55d-4b47-8082-14061c2bcdd8:c396b26b-137a-44fd-87f5-34631f8fd529  base64 encode this string. E.g.: NDRhOTUzN2QtZDU1ZC00YjQ3LTgwODItMTQwNjFjMmJjZGQ4OmMzOTZiMjZiLTEzN2EtNDRmZC04N2Y1LTM0NjMxZjhmZDUyOQ==  create an HTTP **Authorization** header with the value set to e.g. Basic NDRhOTUzN2QtZDU1ZC00YjQ3LTgwODItMTQwNjFjMmJjZGQ4OmMzOTZiMjZiLTEzN2EtNDRmZC04N2Y1LTM0NjMxZjhmZDUyOQ==  perform the Velo authentication REST call using the HTTP header created above e.g. via curl:  ```   curl -X POST \\   -H \"Content-Type: application/json\" \\   -H \"Authorization: Basic NDRhOTUzN2QtZDU1ZC00YjQ3LTgwODItMTQwNjFjMmJjZGQ4OmMzOTZiMjZiLTEzN2EtNDRmZC04N2Y1LTM0NjMxZjhmZDUyOQ==\" \\   'https://api.sandbox.velopayments.com/v1/authenticate?grant_type=client_credentials' ```  If successful, this call will result in a **200** HTTP status code and a response body such as:  ```   {     \"access_token\":\"19f6bafd-93fd-4747-b229-00507bbc991f\",     \"token_type\":\"bearer\",     \"expires_in\":1799,     \"scope\":\"...\"   } ``` ## API access following authentication Following successful authentication, the value of the access_token field in the response (indicated in green above) should then be presented with all subsequent API calls to allow the Velo platform to validate that the caller is authenticated.  This is achieved by setting the HTTP Authorization header with the value set to e.g. Bearer 19f6bafd-93fd-4747-b229-00507bbc991f such as the curl example below:  ```   -H \"Authorization: Bearer 19f6bafd-93fd-4747-b229-00507bbc991f \" ```  If you make other Velo API calls which require authorization but the Authorization header is missing or invalid then you will get a **401** HTTP status response.   # noqa: E501

    The version of the OpenAPI document: 2.20.29
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

__version__ = "2.20.29"

# import apis into sdk package
from velo_payments.api.countries_api import CountriesApi
from velo_payments.api.currencies_api import CurrenciesApi
from velo_payments.api.funding_manager_api import FundingManagerApi
from velo_payments.api.funding_manager_private_api import FundingManagerPrivateApi
from velo_payments.api.get_payout_api import GetPayoutApi
from velo_payments.api.instruct_payout_api import InstructPayoutApi
from velo_payments.api.login_api import LoginApi
from velo_payments.api.payee_invitation_api import PayeeInvitationApi
from velo_payments.api.payees_api import PayeesApi
from velo_payments.api.payment_audit_service_api import PaymentAuditServiceApi
from velo_payments.api.payors_api import PayorsApi
from velo_payments.api.payors_private_api import PayorsPrivateApi
from velo_payments.api.payout_history_api import PayoutHistoryApi
from velo_payments.api.quote_payout_api import QuotePayoutApi
from velo_payments.api.submit_payout_api import SubmitPayoutApi
from velo_payments.api.tokens_api import TokensApi
from velo_payments.api.users_api import UsersApi
from velo_payments.api.withdraw_payout_api import WithdrawPayoutApi

# import ApiClient
from velo_payments.api_client import ApiClient
from velo_payments.configuration import Configuration
from velo_payments.exceptions import OpenApiException
from velo_payments.exceptions import ApiTypeError
from velo_payments.exceptions import ApiValueError
from velo_payments.exceptions import ApiKeyError
from velo_payments.exceptions import ApiException
# import models into sdk package
from velo_payments.models.accepted_payment import AcceptedPayment
from velo_payments.models.access_token_response import AccessTokenResponse
from velo_payments.models.access_token_validation_request import AccessTokenValidationRequest
from velo_payments.models.auth_response import AuthResponse
from velo_payments.models.auto_top_up_config import AutoTopUpConfig
from velo_payments.models.challenge import Challenge
from velo_payments.models.company import Company
from velo_payments.models.company2 import Company2
from velo_payments.models.company_response import CompanyResponse
from velo_payments.models.company_v1 import CompanyV1
from velo_payments.models.create_funding_account_request import CreateFundingAccountRequest
from velo_payments.models.create_individual import CreateIndividual
from velo_payments.models.create_individual2 import CreateIndividual2
from velo_payments.models.create_individual2_name import CreateIndividual2Name
from velo_payments.models.create_payee import CreatePayee
from velo_payments.models.create_payee2 import CreatePayee2
from velo_payments.models.create_payee_address import CreatePayeeAddress
from velo_payments.models.create_payee_address2 import CreatePayeeAddress2
from velo_payments.models.create_payees_csv_request import CreatePayeesCSVRequest
from velo_payments.models.create_payees_csv_request2 import CreatePayeesCSVRequest2
from velo_payments.models.create_payees_csv_response import CreatePayeesCSVResponse
from velo_payments.models.create_payees_csv_response2 import CreatePayeesCSVResponse2
from velo_payments.models.create_payees_csv_response_rejected_csv_rows import CreatePayeesCSVResponseRejectedCsvRows
from velo_payments.models.create_payees_request import CreatePayeesRequest
from velo_payments.models.create_payees_request2 import CreatePayeesRequest2
from velo_payments.models.create_payment_channel import CreatePaymentChannel
from velo_payments.models.create_payment_channel2 import CreatePaymentChannel2
from velo_payments.models.create_payor_link_request import CreatePayorLinkRequest
from velo_payments.models.create_payout_request import CreatePayoutRequest
from velo_payments.models.currency_type import CurrencyType
from velo_payments.models.error import Error
from velo_payments.models.error_response import ErrorResponse
from velo_payments.models.failed_submission import FailedSubmission
from velo_payments.models.failed_submission2 import FailedSubmission2
from velo_payments.models.funding_account_response import FundingAccountResponse
from velo_payments.models.funding_audit import FundingAudit
from velo_payments.models.funding_event import FundingEvent
from velo_payments.models.funding_event_type import FundingEventType
from velo_payments.models.funding_payor_status_audit_response import FundingPayorStatusAuditResponse
from velo_payments.models.funding_request_v1 import FundingRequestV1
from velo_payments.models.funding_request_v2 import FundingRequestV2
from velo_payments.models.fx_summary_v3 import FxSummaryV3
from velo_payments.models.fx_summary_v4 import FxSummaryV4
from velo_payments.models.get_fundings_response import GetFundingsResponse
from velo_payments.models.get_fundings_response_all_of import GetFundingsResponseAllOf
from velo_payments.models.get_payments_for_payout_response_v3 import GetPaymentsForPayoutResponseV3
from velo_payments.models.get_payments_for_payout_response_v3_page import GetPaymentsForPayoutResponseV3Page
from velo_payments.models.get_payments_for_payout_response_v3_summary import GetPaymentsForPayoutResponseV3Summary
from velo_payments.models.get_payments_for_payout_response_v4 import GetPaymentsForPayoutResponseV4
from velo_payments.models.get_payments_for_payout_response_v4_summary import GetPaymentsForPayoutResponseV4Summary
from velo_payments.models.get_payout_statistics import GetPayoutStatistics
from velo_payments.models.get_payouts_response_v3 import GetPayoutsResponseV3
from velo_payments.models.get_payouts_response_v3_links import GetPayoutsResponseV3Links
from velo_payments.models.get_payouts_response_v3_page import GetPayoutsResponseV3Page
from velo_payments.models.get_payouts_response_v4 import GetPayoutsResponseV4
from velo_payments.models.individual import Individual
from velo_payments.models.individual2 import Individual2
from velo_payments.models.individual_response import IndividualResponse
from velo_payments.models.individual_v1 import IndividualV1
from velo_payments.models.individual_v1_name import IndividualV1Name
from velo_payments.models.inline_response400 import InlineResponse400
from velo_payments.models.inline_response400_errors import InlineResponse400Errors
from velo_payments.models.inline_response401 import InlineResponse401
from velo_payments.models.inline_response401_errors import InlineResponse401Errors
from velo_payments.models.inline_response403 import InlineResponse403
from velo_payments.models.inline_response403_errors import InlineResponse403Errors
from velo_payments.models.inline_response409 import InlineResponse409
from velo_payments.models.inline_response409_errors import InlineResponse409Errors
from velo_payments.models.invitation_status import InvitationStatus
from velo_payments.models.invitation_status_response import InvitationStatusResponse
from velo_payments.models.invite_payee_request import InvitePayeeRequest
from velo_payments.models.invite_payee_request2 import InvitePayeeRequest2
from velo_payments.models.invite_user_request import InviteUserRequest
from velo_payments.models.kyc_state import KycState
from velo_payments.models.language import Language
from velo_payments.models.language2 import Language2
from velo_payments.models.link_for_response import LinkForResponse
from velo_payments.models.list_funding_accounts_response import ListFundingAccountsResponse
from velo_payments.models.list_payments_response import ListPaymentsResponse
from velo_payments.models.list_payments_response_page import ListPaymentsResponsePage
from velo_payments.models.list_payments_response_v4 import ListPaymentsResponseV4
from velo_payments.models.list_source_account_response import ListSourceAccountResponse
from velo_payments.models.list_source_account_response_links import ListSourceAccountResponseLinks
from velo_payments.models.list_source_account_response_page import ListSourceAccountResponsePage
from velo_payments.models.list_source_account_response_v2 import ListSourceAccountResponseV2
from velo_payments.models.location_type import LocationType
from velo_payments.models.mfa_details import MFADetails
from velo_payments.models.mfa_type import MFAType
from velo_payments.models.marketing_opt_in import MarketingOptIn
from velo_payments.models.notifications import Notifications
from velo_payments.models.ofac_status import OfacStatus
from velo_payments.models.ofac_status2 import OfacStatus2
from velo_payments.models.onboarded_status import OnboardedStatus
from velo_payments.models.onboarded_status2 import OnboardedStatus2
from velo_payments.models.page_for_response import PageForResponse
from velo_payments.models.page_resource_funding_payor_status_audit_response_funding_payor_status_audit_response import PageResourceFundingPayorStatusAuditResponseFundingPayorStatusAuditResponse
from velo_payments.models.paged_payee_invitation_status_response import PagedPayeeInvitationStatusResponse
from velo_payments.models.paged_payee_invitation_status_response2 import PagedPayeeInvitationStatusResponse2
from velo_payments.models.paged_payee_invitation_status_response_page import PagedPayeeInvitationStatusResponsePage
from velo_payments.models.paged_payee_response import PagedPayeeResponse
from velo_payments.models.paged_payee_response2 import PagedPayeeResponse2
from velo_payments.models.paged_payee_response2_summary import PagedPayeeResponse2Summary
from velo_payments.models.paged_payee_response_links import PagedPayeeResponseLinks
from velo_payments.models.paged_payee_response_page import PagedPayeeResponsePage
from velo_payments.models.paged_payee_response_summary import PagedPayeeResponseSummary
from velo_payments.models.paged_response import PagedResponse
from velo_payments.models.paged_response_page import PagedResponsePage
from velo_payments.models.paged_user_response import PagedUserResponse
from velo_payments.models.paged_user_response_links import PagedUserResponseLinks
from velo_payments.models.paged_user_response_page import PagedUserResponsePage
from velo_payments.models.password_request import PasswordRequest
from velo_payments.models.payee import Payee
from velo_payments.models.payee2 import Payee2
from velo_payments.models.payee_address import PayeeAddress
from velo_payments.models.payee_address2 import PayeeAddress2
from velo_payments.models.payee_delta import PayeeDelta
from velo_payments.models.payee_delta2 import PayeeDelta2
from velo_payments.models.payee_delta_response import PayeeDeltaResponse
from velo_payments.models.payee_delta_response2 import PayeeDeltaResponse2
from velo_payments.models.payee_delta_response2_links import PayeeDeltaResponse2Links
from velo_payments.models.payee_delta_response_links import PayeeDeltaResponseLinks
from velo_payments.models.payee_delta_response_page import PayeeDeltaResponsePage
from velo_payments.models.payee_invitation_status import PayeeInvitationStatus
from velo_payments.models.payee_invitation_status_response import PayeeInvitationStatusResponse
from velo_payments.models.payee_invitation_status_response2 import PayeeInvitationStatusResponse2
from velo_payments.models.payee_payment_channel import PayeePaymentChannel
from velo_payments.models.payee_payment_channel2 import PayeePaymentChannel2
from velo_payments.models.payee_payor_ref import PayeePayorRef
from velo_payments.models.payee_payor_ref_v2 import PayeePayorRefV2
from velo_payments.models.payee_payor_ref_v3 import PayeePayorRefV3
from velo_payments.models.payee_response import PayeeResponse
from velo_payments.models.payee_response2 import PayeeResponse2
from velo_payments.models.payee_response_v2 import PayeeResponseV2
from velo_payments.models.payee_response_v3 import PayeeResponseV3
from velo_payments.models.payee_type import PayeeType
from velo_payments.models.payment_audit_currency_v3 import PaymentAuditCurrencyV3
from velo_payments.models.payment_audit_currency_v4 import PaymentAuditCurrencyV4
from velo_payments.models.payment_channel_country import PaymentChannelCountry
from velo_payments.models.payment_channel_rule import PaymentChannelRule
from velo_payments.models.payment_channel_rules_response import PaymentChannelRulesResponse
from velo_payments.models.payment_delta import PaymentDelta
from velo_payments.models.payment_delta_response import PaymentDeltaResponse
from velo_payments.models.payment_event_response_v3 import PaymentEventResponseV3
from velo_payments.models.payment_event_response_v4 import PaymentEventResponseV4
from velo_payments.models.payment_instruction import PaymentInstruction
from velo_payments.models.payment_rails import PaymentRails
from velo_payments.models.payment_response_v3 import PaymentResponseV3
from velo_payments.models.payment_response_v4 import PaymentResponseV4
from velo_payments.models.payment_response_v4_payout import PaymentResponseV4Payout
from velo_payments.models.payor_address import PayorAddress
from velo_payments.models.payor_address_v2 import PayorAddressV2
from velo_payments.models.payor_aml_transaction_v3 import PayorAmlTransactionV3
from velo_payments.models.payor_aml_transaction_v4 import PayorAmlTransactionV4
from velo_payments.models.payor_branding_response import PayorBrandingResponse
from velo_payments.models.payor_create_api_key_request import PayorCreateApiKeyRequest
from velo_payments.models.payor_create_api_key_response import PayorCreateApiKeyResponse
from velo_payments.models.payor_create_application_request import PayorCreateApplicationRequest
from velo_payments.models.payor_email_opt_out_request import PayorEmailOptOutRequest
from velo_payments.models.payor_links_response import PayorLinksResponse
from velo_payments.models.payor_links_response_links import PayorLinksResponseLinks
from velo_payments.models.payor_links_response_payors import PayorLinksResponsePayors
from velo_payments.models.payor_logo_request import PayorLogoRequest
from velo_payments.models.payor_v1 import PayorV1
from velo_payments.models.payor_v2 import PayorV2
from velo_payments.models.payout_payor_v4 import PayoutPayorV4
from velo_payments.models.payout_principal_v4 import PayoutPrincipalV4
from velo_payments.models.payout_status_v3 import PayoutStatusV3
from velo_payments.models.payout_status_v4 import PayoutStatusV4
from velo_payments.models.payout_summary_audit_v3 import PayoutSummaryAuditV3
from velo_payments.models.payout_summary_audit_v4 import PayoutSummaryAuditV4
from velo_payments.models.payout_summary_response import PayoutSummaryResponse
from velo_payments.models.payout_type_v4 import PayoutTypeV4
from velo_payments.models.query_batch_response import QueryBatchResponse
from velo_payments.models.query_batch_response2 import QueryBatchResponse2
from velo_payments.models.quote_fx_summary import QuoteFxSummary
from velo_payments.models.quote_response import QuoteResponse
from velo_payments.models.region import Region
from velo_payments.models.register_sms_request import RegisterSmsRequest
from velo_payments.models.rejected_payment import RejectedPayment
from velo_payments.models.resend_token_request import ResendTokenRequest
from velo_payments.models.reset_password_request import ResetPasswordRequest
from velo_payments.models.role import Role
from velo_payments.models.role_update_request import RoleUpdateRequest
from velo_payments.models.self_mfa_type_unregister_request import SelfMFATypeUnregisterRequest
from velo_payments.models.self_update_password_request import SelfUpdatePasswordRequest
from velo_payments.models.set_notifications_request import SetNotificationsRequest
from velo_payments.models.source_account import SourceAccount
from velo_payments.models.source_account_response import SourceAccountResponse
from velo_payments.models.source_account_response_v2 import SourceAccountResponseV2
from velo_payments.models.source_account_summary_v3 import SourceAccountSummaryV3
from velo_payments.models.source_account_summary_v4 import SourceAccountSummaryV4
from velo_payments.models.supported_countries_response import SupportedCountriesResponse
from velo_payments.models.supported_countries_response2 import SupportedCountriesResponse2
from velo_payments.models.supported_country import SupportedCountry
from velo_payments.models.supported_country2 import SupportedCountry2
from velo_payments.models.supported_currency import SupportedCurrency
from velo_payments.models.supported_currency_response import SupportedCurrencyResponse
from velo_payments.models.transfer_request import TransferRequest
from velo_payments.models.unregister_mfa_request import UnregisterMFARequest
from velo_payments.models.update_remote_id_request import UpdateRemoteIdRequest
from velo_payments.models.user_details_update_request import UserDetailsUpdateRequest
from velo_payments.models.user_info import UserInfo
from velo_payments.models.user_response import UserResponse
from velo_payments.models.user_response2 import UserResponse2
from velo_payments.models.user_response2_roles import UserResponse2Roles
from velo_payments.models.user_status import UserStatus
from velo_payments.models.user_type import UserType
from velo_payments.models.user_type2 import UserType2
from velo_payments.models.validate_password_response import ValidatePasswordResponse
from velo_payments.models.watchlist_status import WatchlistStatus

