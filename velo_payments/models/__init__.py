# flake8: noqa

# import all models into this package
# if you have many models here with many references from one model to another this may
# raise a RecursionError
# to avoid this, import only the models that you directly need like:
# from from velo_payments.model.pet import Pet
# or import this package, but before doing it, use:
# import sys
# sys.setrecursionlimit(n)

from velo_payments.model.accepted_payment_v3 import AcceptedPaymentV3
from velo_payments.model.access_token_response import AccessTokenResponse
from velo_payments.model.access_token_validation_request import AccessTokenValidationRequest
from velo_payments.model.auth_response import AuthResponse
from velo_payments.model.auto_top_up_config import AutoTopUpConfig
from velo_payments.model.auto_top_up_config2 import AutoTopUpConfig2
from velo_payments.model.category import Category
from velo_payments.model.challenge_v3 import ChallengeV3
from velo_payments.model.challenge_v4 import ChallengeV4
from velo_payments.model.company_v3 import CompanyV3
from velo_payments.model.company_v4 import CompanyV4
from velo_payments.model.create_funding_account_request_v2 import CreateFundingAccountRequestV2
from velo_payments.model.create_individual_v3 import CreateIndividualV3
from velo_payments.model.create_individual_v3_name import CreateIndividualV3Name
from velo_payments.model.create_individual_v4 import CreateIndividualV4
from velo_payments.model.create_payee_address_v3 import CreatePayeeAddressV3
from velo_payments.model.create_payee_address_v4 import CreatePayeeAddressV4
from velo_payments.model.create_payee_v3 import CreatePayeeV3
from velo_payments.model.create_payee_v4 import CreatePayeeV4
from velo_payments.model.create_payees_csv_request_v3 import CreatePayeesCSVRequestV3
from velo_payments.model.create_payees_csv_request_v4 import CreatePayeesCSVRequestV4
from velo_payments.model.create_payees_csv_response_v3 import CreatePayeesCSVResponseV3
from velo_payments.model.create_payees_csv_response_v3_rejected_csv_rows import CreatePayeesCSVResponseV3RejectedCsvRows
from velo_payments.model.create_payees_csv_response_v4 import CreatePayeesCSVResponseV4
from velo_payments.model.create_payees_request_v3 import CreatePayeesRequestV3
from velo_payments.model.create_payees_request_v4 import CreatePayeesRequestV4
from velo_payments.model.create_payment_channel_v3 import CreatePaymentChannelV3
from velo_payments.model.create_payment_channel_v4 import CreatePaymentChannelV4
from velo_payments.model.create_payor_link_request import CreatePayorLinkRequest
from velo_payments.model.create_payout_request_v3 import CreatePayoutRequestV3
from velo_payments.model.create_webhook_request import CreateWebhookRequest
from velo_payments.model.debit_event import DebitEvent
from velo_payments.model.debit_event_all_of import DebitEventAllOf
from velo_payments.model.debit_status_changed import DebitStatusChanged
from velo_payments.model.debit_status_changed_all_of import DebitStatusChangedAllOf
from velo_payments.model.error import Error
from velo_payments.model.error_data import ErrorData
from velo_payments.model.error_response import ErrorResponse
from velo_payments.model.failed_payee_v3 import FailedPayeeV3
from velo_payments.model.failed_payee_v4 import FailedPayeeV4
from velo_payments.model.failed_submission_v3 import FailedSubmissionV3
from velo_payments.model.failed_submission_v4 import FailedSubmissionV4
from velo_payments.model.funding_account_response import FundingAccountResponse
from velo_payments.model.funding_account_response2 import FundingAccountResponse2
from velo_payments.model.funding_account_type import FundingAccountType
from velo_payments.model.funding_audit import FundingAudit
from velo_payments.model.funding_event import FundingEvent
from velo_payments.model.funding_event_type import FundingEventType
from velo_payments.model.funding_payor_status_audit_response import FundingPayorStatusAuditResponse
from velo_payments.model.funding_request_v1 import FundingRequestV1
from velo_payments.model.funding_request_v2 import FundingRequestV2
from velo_payments.model.funding_request_v3 import FundingRequestV3
from velo_payments.model.fx_summary import FxSummary
from velo_payments.model.fx_summary_v3 import FxSummaryV3
from velo_payments.model.get_fundings_response import GetFundingsResponse
from velo_payments.model.get_fundings_response_links import GetFundingsResponseLinks
from velo_payments.model.get_payee_list_response_company_v3 import GetPayeeListResponseCompanyV3
from velo_payments.model.get_payee_list_response_company_v4 import GetPayeeListResponseCompanyV4
from velo_payments.model.get_payee_list_response_individual_v3 import GetPayeeListResponseIndividualV3
from velo_payments.model.get_payee_list_response_individual_v4 import GetPayeeListResponseIndividualV4
from velo_payments.model.get_payee_list_response_v3 import GetPayeeListResponseV3
from velo_payments.model.get_payee_list_response_v4 import GetPayeeListResponseV4
from velo_payments.model.get_payments_for_payout_response_v3 import GetPaymentsForPayoutResponseV3
from velo_payments.model.get_payments_for_payout_response_v3_page import GetPaymentsForPayoutResponseV3Page
from velo_payments.model.get_payments_for_payout_response_v3_summary import GetPaymentsForPayoutResponseV3Summary
from velo_payments.model.get_payments_for_payout_response_v4 import GetPaymentsForPayoutResponseV4
from velo_payments.model.get_payments_for_payout_response_v4_summary import GetPaymentsForPayoutResponseV4Summary
from velo_payments.model.get_payout_statistics import GetPayoutStatistics
from velo_payments.model.get_payouts_response import GetPayoutsResponse
from velo_payments.model.get_payouts_response_v3 import GetPayoutsResponseV3
from velo_payments.model.get_payouts_response_v3_links import GetPayoutsResponseV3Links
from velo_payments.model.get_payouts_response_v3_page import GetPayoutsResponseV3Page
from velo_payments.model.iban import Iban
from velo_payments.model.individual_v3 import IndividualV3
from velo_payments.model.individual_v3_name import IndividualV3Name
from velo_payments.model.individual_v4 import IndividualV4
from velo_payments.model.inline_response400 import InlineResponse400
from velo_payments.model.inline_response401 import InlineResponse401
from velo_payments.model.inline_response403 import InlineResponse403
from velo_payments.model.inline_response404 import InlineResponse404
from velo_payments.model.inline_response409 import InlineResponse409
from velo_payments.model.inline_response412 import InlineResponse412
from velo_payments.model.instruct_payout_request import InstructPayoutRequest
from velo_payments.model.invitation_status_v3 import InvitationStatusV3
from velo_payments.model.invitation_status_v4 import InvitationStatusV4
from velo_payments.model.invite_payee_request_v3 import InvitePayeeRequestV3
from velo_payments.model.invite_payee_request_v4 import InvitePayeeRequestV4
from velo_payments.model.invite_user_request import InviteUserRequest
from velo_payments.model.iso_country_code import IsoCountryCode
from velo_payments.model.iso_currency import IsoCurrency
from velo_payments.model.kyc_state import KycState
from velo_payments.model.link_for_response import LinkForResponse
from velo_payments.model.list_funding_accounts_response import ListFundingAccountsResponse
from velo_payments.model.list_funding_accounts_response2 import ListFundingAccountsResponse2
from velo_payments.model.list_payments_response_v3 import ListPaymentsResponseV3
from velo_payments.model.list_payments_response_v3_page import ListPaymentsResponseV3Page
from velo_payments.model.list_payments_response_v4 import ListPaymentsResponseV4
from velo_payments.model.list_source_account_response import ListSourceAccountResponse
from velo_payments.model.list_source_account_response_links import ListSourceAccountResponseLinks
from velo_payments.model.list_source_account_response_page import ListSourceAccountResponsePage
from velo_payments.model.list_source_account_response_v2 import ListSourceAccountResponseV2
from velo_payments.model.list_source_account_response_v2_links import ListSourceAccountResponseV2Links
from velo_payments.model.list_source_account_response_v3 import ListSourceAccountResponseV3
from velo_payments.model.list_source_account_response_v3_links import ListSourceAccountResponseV3Links
from velo_payments.model.localisation_details import LocalisationDetails
from velo_payments.model.mfa_details import MFADetails
from velo_payments.model.mfa_type import MFAType
from velo_payments.model.name_v3 import NameV3
from velo_payments.model.name_v4 import NameV4
from velo_payments.model.notification import Notification
from velo_payments.model.notifications import Notifications
from velo_payments.model.notifications2 import Notifications2
from velo_payments.model.ofac_status_v4 import OfacStatusV4
from velo_payments.model.onboarded_status_v3 import OnboardedStatusV3
from velo_payments.model.onboarded_status_v32 import OnboardedStatusV32
from velo_payments.model.onboarded_status_v4 import OnboardedStatusV4
from velo_payments.model.onboarded_status_v42 import OnboardedStatusV42
from velo_payments.model.onboarding_status_changed import OnboardingStatusChanged
from velo_payments.model.page_for_response import PageForResponse
from velo_payments.model.page_resource_funding_payor_status_audit_response_funding_payor_status_audit_response import PageResourceFundingPayorStatusAuditResponseFundingPayorStatusAuditResponse
from velo_payments.model.paged_payee_invitation_status_response_v3 import PagedPayeeInvitationStatusResponseV3
from velo_payments.model.paged_payee_invitation_status_response_v3_page import PagedPayeeInvitationStatusResponseV3Page
from velo_payments.model.paged_payee_invitation_status_response_v4 import PagedPayeeInvitationStatusResponseV4
from velo_payments.model.paged_payee_response_v3 import PagedPayeeResponseV3
from velo_payments.model.paged_payee_response_v3_links import PagedPayeeResponseV3Links
from velo_payments.model.paged_payee_response_v3_page import PagedPayeeResponseV3Page
from velo_payments.model.paged_payee_response_v3_summary import PagedPayeeResponseV3Summary
from velo_payments.model.paged_payee_response_v4 import PagedPayeeResponseV4
from velo_payments.model.paged_payments_response_v3 import PagedPaymentsResponseV3
from velo_payments.model.paged_user_response import PagedUserResponse
from velo_payments.model.paged_user_response_links import PagedUserResponseLinks
from velo_payments.model.paged_user_response_page import PagedUserResponsePage
from velo_payments.model.password_request import PasswordRequest
from velo_payments.model.payable_issue_v3 import PayableIssueV3
from velo_payments.model.payable_issue_v4 import PayableIssueV4
from velo_payments.model.payable_status_changed import PayableStatusChanged
from velo_payments.model.payee_address_v3 import PayeeAddressV3
from velo_payments.model.payee_address_v4 import PayeeAddressV4
from velo_payments.model.payee_delta_response_v3 import PayeeDeltaResponseV3
from velo_payments.model.payee_delta_response_v3_links import PayeeDeltaResponseV3Links
from velo_payments.model.payee_delta_response_v3_page import PayeeDeltaResponseV3Page
from velo_payments.model.payee_delta_response_v4 import PayeeDeltaResponseV4
from velo_payments.model.payee_delta_response_v4_links import PayeeDeltaResponseV4Links
from velo_payments.model.payee_delta_v3 import PayeeDeltaV3
from velo_payments.model.payee_delta_v4 import PayeeDeltaV4
from velo_payments.model.payee_detail_response_v3 import PayeeDetailResponseV3
from velo_payments.model.payee_detail_response_v4 import PayeeDetailResponseV4
from velo_payments.model.payee_details_changed import PayeeDetailsChanged
from velo_payments.model.payee_event import PayeeEvent
from velo_payments.model.payee_event_all_of import PayeeEventAllOf
from velo_payments.model.payee_event_all_of_reasons import PayeeEventAllOfReasons
from velo_payments.model.payee_invitation_status_response_v3 import PayeeInvitationStatusResponseV3
from velo_payments.model.payee_invitation_status_response_v4 import PayeeInvitationStatusResponseV4
from velo_payments.model.payee_payor_ref_v3 import PayeePayorRefV3
from velo_payments.model.payee_payor_ref_v4 import PayeePayorRefV4
from velo_payments.model.payee_type import PayeeType
from velo_payments.model.payee_type2 import PayeeType2
from velo_payments.model.payee_user_self_update_request import PayeeUserSelfUpdateRequest
from velo_payments.model.payment_audit_currency import PaymentAuditCurrency
from velo_payments.model.payment_audit_currency_v3 import PaymentAuditCurrencyV3
from velo_payments.model.payment_channel_country import PaymentChannelCountry
from velo_payments.model.payment_channel_rule import PaymentChannelRule
from velo_payments.model.payment_channel_rules_response import PaymentChannelRulesResponse
from velo_payments.model.payment_delta import PaymentDelta
from velo_payments.model.payment_delta_response import PaymentDeltaResponse
from velo_payments.model.payment_delta_response_v1 import PaymentDeltaResponseV1
from velo_payments.model.payment_delta_v1 import PaymentDeltaV1
from velo_payments.model.payment_event import PaymentEvent
from velo_payments.model.payment_event_all_of import PaymentEventAllOf
from velo_payments.model.payment_event_response import PaymentEventResponse
from velo_payments.model.payment_event_response_v3 import PaymentEventResponseV3
from velo_payments.model.payment_instruction_v3 import PaymentInstructionV3
from velo_payments.model.payment_rails import PaymentRails
from velo_payments.model.payment_rejected_or_returned import PaymentRejectedOrReturned
from velo_payments.model.payment_rejected_or_returned_all_of import PaymentRejectedOrReturnedAllOf
from velo_payments.model.payment_response_v3 import PaymentResponseV3
from velo_payments.model.payment_response_v4 import PaymentResponseV4
from velo_payments.model.payment_response_v4_payout import PaymentResponseV4Payout
from velo_payments.model.payment_status_changed import PaymentStatusChanged
from velo_payments.model.payment_status_changed_all_of import PaymentStatusChangedAllOf
from velo_payments.model.payment_v3 import PaymentV3
from velo_payments.model.payor_address import PayorAddress
from velo_payments.model.payor_address_v2 import PayorAddressV2
from velo_payments.model.payor_aml_transaction import PayorAmlTransaction
from velo_payments.model.payor_aml_transaction_v3 import PayorAmlTransactionV3
from velo_payments.model.payor_branding_response import PayorBrandingResponse
from velo_payments.model.payor_create_api_key_request import PayorCreateApiKeyRequest
from velo_payments.model.payor_create_api_key_response import PayorCreateApiKeyResponse
from velo_payments.model.payor_create_application_request import PayorCreateApplicationRequest
from velo_payments.model.payor_email_opt_out_request import PayorEmailOptOutRequest
from velo_payments.model.payor_links_response import PayorLinksResponse
from velo_payments.model.payor_links_response_links import PayorLinksResponseLinks
from velo_payments.model.payor_links_response_payors import PayorLinksResponsePayors
from velo_payments.model.payor_logo_request import PayorLogoRequest
from velo_payments.model.payor_v1 import PayorV1
from velo_payments.model.payor_v2 import PayorV2
from velo_payments.model.payout_company_v3 import PayoutCompanyV3
from velo_payments.model.payout_individual_v3 import PayoutIndividualV3
from velo_payments.model.payout_name_v3 import PayoutNameV3
from velo_payments.model.payout_payee_v3 import PayoutPayeeV3
from velo_payments.model.payout_payor import PayoutPayor
from velo_payments.model.payout_payor_ids import PayoutPayorIds
from velo_payments.model.payout_principal import PayoutPrincipal
from velo_payments.model.payout_schedule import PayoutSchedule
from velo_payments.model.payout_schedule2 import PayoutSchedule2
from velo_payments.model.payout_status import PayoutStatus
from velo_payments.model.payout_status_v3 import PayoutStatusV3
from velo_payments.model.payout_summary_audit import PayoutSummaryAudit
from velo_payments.model.payout_summary_audit_v3 import PayoutSummaryAuditV3
from velo_payments.model.payout_summary_response_v3 import PayoutSummaryResponseV3
from velo_payments.model.payout_type import PayoutType
from velo_payments.model.ping import Ping
from velo_payments.model.ping_response import PingResponse
from velo_payments.model.query_batch_response_v3 import QueryBatchResponseV3
from velo_payments.model.query_batch_response_v4 import QueryBatchResponseV4
from velo_payments.model.quote_fx_summary_v3 import QuoteFxSummaryV3
from velo_payments.model.quote_response_v3 import QuoteResponseV3
from velo_payments.model.region_v2 import RegionV2
from velo_payments.model.register_sms_request import RegisterSmsRequest
from velo_payments.model.rejected_payment_v3 import RejectedPaymentV3
from velo_payments.model.resend_token_request import ResendTokenRequest
from velo_payments.model.reset_password_request import ResetPasswordRequest
from velo_payments.model.role import Role
from velo_payments.model.role_update_request import RoleUpdateRequest
from velo_payments.model.schedule_payout_request import SchedulePayoutRequest
from velo_payments.model.schedule_status import ScheduleStatus
from velo_payments.model.schedule_status2 import ScheduleStatus2
from velo_payments.model.self_mfa_type_unregister_request import SelfMFATypeUnregisterRequest
from velo_payments.model.self_update_password_request import SelfUpdatePasswordRequest
from velo_payments.model.set_notifications_request import SetNotificationsRequest
from velo_payments.model.source_account_response import SourceAccountResponse
from velo_payments.model.source_account_response_v2 import SourceAccountResponseV2
from velo_payments.model.source_account_response_v3 import SourceAccountResponseV3
from velo_payments.model.source_account_summary import SourceAccountSummary
from velo_payments.model.source_account_summary_v3 import SourceAccountSummaryV3
from velo_payments.model.source_account_type import SourceAccountType
from velo_payments.model.source_account_v3 import SourceAccountV3
from velo_payments.model.source_event import SourceEvent
from velo_payments.model.supported_countries_response import SupportedCountriesResponse
from velo_payments.model.supported_countries_response_v2 import SupportedCountriesResponseV2
from velo_payments.model.supported_country import SupportedCountry
from velo_payments.model.supported_country_v2 import SupportedCountryV2
from velo_payments.model.supported_currency_response_v2 import SupportedCurrencyResponseV2
from velo_payments.model.supported_currency_v2 import SupportedCurrencyV2
from velo_payments.model.transfer_request import TransferRequest
from velo_payments.model.transfer_request2 import TransferRequest2
from velo_payments.model.transmission_type import TransmissionType
from velo_payments.model.transmission_types import TransmissionTypes
from velo_payments.model.transmission_types2 import TransmissionTypes2
from velo_payments.model.unregister_mfa_request import UnregisterMFARequest
from velo_payments.model.update_payee_details_request_v3 import UpdatePayeeDetailsRequestV3
from velo_payments.model.update_payee_details_request_v4 import UpdatePayeeDetailsRequestV4
from velo_payments.model.update_remote_id_request_v3 import UpdateRemoteIdRequestV3
from velo_payments.model.update_remote_id_request_v4 import UpdateRemoteIdRequestV4
from velo_payments.model.update_webhook_request import UpdateWebhookRequest
from velo_payments.model.user_details_update_request import UserDetailsUpdateRequest
from velo_payments.model.user_info import UserInfo
from velo_payments.model.user_response import UserResponse
from velo_payments.model.user_status import UserStatus
from velo_payments.model.user_type import UserType
from velo_payments.model.user_type2 import UserType2
from velo_payments.model.validate_password_response import ValidatePasswordResponse
from velo_payments.model.verification_code import VerificationCode
from velo_payments.model.watchlist_status_v3 import WatchlistStatusV3
from velo_payments.model.watchlist_status_v4 import WatchlistStatusV4
from velo_payments.model.webhook_response import WebhookResponse
from velo_payments.model.webhooks_response import WebhooksResponse
from velo_payments.model.withdraw_payment_request import WithdrawPaymentRequest
