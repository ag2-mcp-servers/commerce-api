# generated by fastapi-codegen:
#   filename:  openapi.yaml
#   timestamp: 2025-06-28T18:15:05+00:00

from __future__ import annotations

from decimal import Decimal
from enum import Enum
from typing import Dict, List, Optional

from pydantic import BaseModel, Field, RootModel


class Type(Enum):
    Website = 'Website'
    Social = 'Social'
    Unknown = 'Unknown'


class WebLink(BaseModel):
    type: Optional[Type] = Field(None, description='The type of the weblink.')
    url: Optional[str] = Field(None, description='The full URL for the weblink.')


class DateTime(RootModel[str]):
    root: str = Field(
        ...,
        description='In Codat\'s data model, dates and times are represented using the <a class="external" href="https://en.wikipedia.org/wiki/ISO_8601" target="_blank">ISO 8601 standard</a>. Date and time fields are formatted as strings; for example:\n\n```\n2020-10-08T22:40:50Z\n2021-01-01T00:00:00\n```\n\n\n\nWhen syncing data that contains `DateTime` fields from Codat, make sure you support the following cases when reading time information:\n\n- Coordinated Universal Time (UTC): `2021-11-15T06:00:00Z`\n- Unqualified local time: `2021-11-15T01:00:00`\n- UTC time offsets: `2021-11-15T01:00:00-05:00`\n\n> Time zones\n> \n> Not all dates from Codat will contain information about time zones.  \n> Where it is not available from the underlying platform, Codat will return these as times local to the business whose data has been synced.',
        examples=['2022-10-23T00:00:00Z'],
        title='Date time',
    )


class HRef(BaseModel):
    href: Optional[str] = None


class Links(BaseModel):
    current: HRef
    next: Optional[HRef] = None
    previous: Optional[HRef] = None
    self: HRef


class ModifiedDates(BaseModel):
    modifiedDate: Optional[DateTime] = Field(
        None, description='The date on which this record was last modified in Codat.'
    )
    sourceModifiedDate: Optional[DateTime] = Field(
        None,
        description='The date on which this record was last modified in the originating system',
    )


class PagingInfo(BaseModel):
    field_links: Links = Field(..., alias='_links')
    pageNumber: int
    pageSize: int
    totalResults: int


class RecordRef(BaseModel):
    id: str = Field(
        ...,
        description='The unique identitifer of the record being referenced',
        examples=[
            '13d946f0-c5d5-42bc-b092-97ece17923ab',
            '9wg4lep4ush5cxs79pl8sozmsndbaukll3ind4g7buqbm1h2',
            7110701885,
            'EILBDVJVNUAGVKRQ',
        ],
    )
    type: str = Field(..., description='The type of record being referenced.')


class AddressType(Enum):
    Billing = 'Billing'
    Delivery = 'Delivery'
    Order = 'Order'
    Inventory = 'Inventory'
    Unknown = 'Unknown'


class CustomerRef(BaseModel):
    id: str = Field(
        ...,
        description='The unique identitifer of the customer being referenced',
        examples=[
            '13d946f0-c5d5-42bc-b092-97ece17923ab',
            '9wg4lep4ush5cxs79pl8sozmsndbaukll3ind4g7buqbm1h2',
            7110701885,
            'EILBDVJVNUAGVKRQ',
        ],
    )
    name: str = Field(..., description='Name of the customer being referenced.')


class DisputeStatus(Enum):
    Won = 'Won'
    Lost = 'Lost'
    Accepted = 'Accepted'
    Processing = 'Processing'
    ChargeRefunded = 'ChargeRefunded'
    EvidenceRequired = 'EvidenceRequired'
    InquiryEvidenceRequired = 'InquiryEvidenceRequired'
    InquiryProcessing = 'InquiryProcessing'
    InquiryClosed = 'InquiryClosed'
    WaitingThirdParty = 'WaitingThirdParty'
    Unknown = 'Unknown'


class LocationRef(BaseModel):
    id: str = Field(
        ...,
        description='The unique identitifer of the location being referenced.',
        examples=[
            '13d946f0-c5d5-42bc-b092-97ece17923ab',
            '9wg4lep4ush5cxs79pl8sozmsndbaukll3ind4g7buqbm1h2',
            7110701885,
            'EILBDVJVNUAGVKRQ',
        ],
    )
    name: str = Field(..., description='Name of the location being referenced.')


class Field0(BaseModel):
    id: str = Field(
        ...,
        description='A unique, persistent identifier for this record',
        examples=[
            '13d946f0-c5d5-42bc-b092-97ece17923ab',
            '9wg4lep4ush5cxs79pl8sozmsndbaukll3ind4g7buqbm1h2',
            7110701885,
            'EILBDVJVNUAGVKRQ',
        ],
    )


class PaymentStatus(Enum):
    Pending = 'Pending'
    Authorized = 'Authorized'
    Paid = 'Paid'
    Failed = 'Failed'
    Cancelled = 'Cancelled'
    Unknown = 'Unknown'


class PaymentMethodRef(BaseModel):
    id: str = Field(
        ..., description='The unique identitifer of the location being referenced.'
    )
    name: str = Field(..., description='Name of the location being referenced.')


class PaymentMethodStatus(Enum):
    Active = 'Active'
    Archived = 'Archived'
    Unknown = 'Unknown'


class PhoneNumberType(Enum):
    Primary = 'Primary'
    Landline = 'Landline'
    Mobile = 'Mobile'
    Fax = 'Fax'
    Unknown = 'Unknown'


class Number(RootModel[Optional[str]]):
    root: Optional[str] = Field(
        None,
        description='A phone number.',
        examples=['+44 25691 154789', '(877) 492-8687', '01224 658 999'],
    )


class Currency(RootModel[str]):
    root: str = Field(
        ...,
        description='The currency data type in Codat is the [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) currency code, e.g. _GBP_.\n\n## Unknown currencies\n\nIn line with the ISO 4217 specification, the code _XXX_ is used when the data source does not return a currency for a transaction. \n\nThere are only a very small number of edge cases where this currency code is returned by the Codat system.',
        examples=['GBP', 'USD', 'EUR'],
        title='Currency',
    )


class TransactionType(Enum):
    Payment = 'Payment'
    Refund = 'Refund'
    Payout = 'Payout'
    FailedPayout = 'FailedPayout'
    Transfer = 'Transfer'
    PaymentFee = 'PaymentFee'
    PaymentFeeRefund = 'PaymentFeeRefund'
    Unknown = 'Unknown'


class OrderDiscountAllocation(BaseModel):
    name: Optional[str] = Field(
        None,
        description='Name of the discount in the commerce or point of sale platform.',
        examples=['Promotional Discount'],
    )
    totalAmount: Optional[float] = Field(
        None, description='Total amount of discount applied.', examples=[15.25]
    )


class ServiceChargeType(Enum):
    Generic = 'Generic'
    Shipping = 'Shipping'
    Overpayment = 'Overpayment'
    Unknown = 'Unknown'


class PaymentType(Enum):
    Cash = 'Cash'
    Card = 'Card'
    Invoice = 'Invoice'
    OnlineCard = 'OnlineCard'
    Swish = 'Swish'
    Vipps = 'Vipps'
    Mobile = 'Mobile'
    StoreCredit = 'StoreCredit'
    Paypal = 'Paypal'
    Custom = 'Custom'
    Prepaid = 'Prepaid'
    Unknown = 'Unknown'


class ProductPrice(BaseModel):
    currency: Optional[Currency] = None
    unitPrice: Optional[float] = None


class ProductRef(BaseModel):
    id: str = Field(
        ...,
        description='The unique identitifer of the product being referenced.',
        examples=[
            '13d946f0-c5d5-42bc-b092-97ece17923ab',
            '9wg4lep4ush5cxs79pl8sozmsndbaukll3ind4g7buqbm1h2',
            7110701885,
            'EILBDVJVNUAGVKRQ',
        ],
    )
    name: str = Field(..., description='Name of the product being referenced.')


class ProductVariantRef(BaseModel):
    id: str = Field(
        ...,
        description='The unique identitifer of the product variant being referenced.',
        examples=[
            '13d946f0-c5d5-42bc-b092-97ece17923ab',
            '9wg4lep4ush5cxs79pl8sozmsndbaukll3ind4g7buqbm1h2',
            7110701885,
            'EILBDVJVNUAGVKRQ',
        ],
    )
    name: str = Field(..., description='Name of the product variant being referenced.')


class ProductVariantStatus(Enum):
    Unknown = 'Unknown'
    Published = 'Published'
    Unpublished = 'Unpublished'


class TransactionSourceType(Enum):
    Fee = 'Fee'
    Order = 'Order'
    Payment = 'Payment'
    ServiceCharge = 'ServiceCharge'
    Unknown = 'Unknown'


class ProductInventoryLocation(BaseModel):
    locationRef: Optional[LocationRef] = None
    quantity: Optional[float] = None


class TaxComponentRef(BaseModel):
    id: str = Field(
        ...,
        description='The unique identitifer of the tax component being referenced.',
        examples=[
            '13d946f0-c5d5-42bc-b092-97ece17923ab',
            '9wg4lep4ush5cxs79pl8sozmsndbaukll3ind4g7buqbm1h2',
            7110701885,
            'EILBDVJVNUAGVKRQ',
        ],
    )
    name: str = Field(..., description='Name of the tax component being referenced.')


class Address(BaseModel):
    city: Optional[str] = Field(
        None, description='The third line of the address, or city'
    )
    country: Optional[str] = Field(None, description='The country for the address')
    line1: Optional[str] = Field(None, description='The first line of the address')
    line2: Optional[str] = Field(None, description='The second line of the address')
    postalCode: Optional[str] = Field(
        None, description='The postal (or zip) code for the address'
    )
    region: Optional[str] = Field(
        None, description='The fourth line of the address, or region'
    )
    type: Optional[AddressType] = None


class CreatedDate(BaseModel):
    createdDate: Optional[DateTime] = Field(
        None, description='The date the entity was created.'
    )


class Customer(Field0, CreatedDate, ModifiedDates):
    addresses: Optional[List[Address]] = Field(
        None, description='Addresses of the customer'
    )
    customerName: Optional[str] = Field(
        None, description='Name of the customer', examples=['Fred Smith']
    )
    defaultCurrency: Optional[Currency] = None
    emailAddress: Optional[str] = Field(
        None,
        description='Email address of the customer',
        examples=['fred.smith@myCompany.com'],
    )
    note: Optional[str] = Field(
        None, description='Any additional information about the customer'
    )
    phone: Optional[Number] = None


class Customers(PagingInfo):
    results: Optional[List[Customer]] = None


class Locations(Field0, ModifiedDates):
    address: Optional[Address] = Field(
        None, description='Address associated with the location'
    )
    name: Optional[str] = Field(None, description='Name of this location')


class LocationsResponse(PagingInfo):
    results: Optional[List[Locations]] = None


class Payment(Field0, CreatedDate, ModifiedDates):
    amount: Optional[float] = Field(
        None,
        description='Payment Amount (including gratuity)',
        examples=[194.12, -283.56, 0],
    )
    currency: Optional[Currency] = Field(
        None, description='Currency in which the payment was made'
    )
    dueDate: Optional[DateTime] = Field(
        None, description='Date by which payment must be made'
    )
    paymentMethodRef: Optional[PaymentMethodRef] = None
    paymentProvider: Optional[str] = Field(
        None,
        description='Service provider of the payment, if applicable.',
        examples=['Amazon Pay', 'Checkout.com', 'SagePay'],
    )
    status: Optional[PaymentStatus] = None


class PaymentMethod(Field0, ModifiedDates):
    name: Optional[str] = Field(
        None, description='The name of the PaymentMethod', examples=['Alipay']
    )
    status: Optional[PaymentMethodStatus] = None


class PaymentMethods(PagingInfo):
    results: Optional[List[PaymentMethod]] = None


class Payments(PagingInfo):
    results: Optional[List[Payment]] = None


class PhoneNumber(BaseModel):
    number: str = Field(
        ...,
        description='A phone number.',
        examples=['+44 25691 154789', '(877) 492-8687', '01224 658 999'],
    )
    type: PhoneNumberType


class ProductCategory(ModifiedDates):
    ancestorRefs: Optional[List[RecordRef]] = Field(
        None,
        description='A collection of parent product categories implicitly ordered with the immediate parent last in the list.',
    )
    hasChildren: Optional[bool] = Field(
        None,
        description='A boolean indicating whether there are other product categories beneath this one in the hierarchy.',
    )
    id: Optional[str] = Field(
        None,
        description='The unique identifier of the product category',
        examples=['"102"'],
    )
    name: Optional[str] = Field(
        None, description='The name of the product category', examples=['Entertainment']
    )


class TaxComponent(Field0, ModifiedDates):
    isCompound: Optional[bool] = Field(
        None,
        description='The Boolean flag to indicate when a Tax Rate Component compounds on a sale.',
        examples=[True, False],
    )
    name: Optional[str] = Field(
        None,
        description='Name of the Tax Rate Component in the source commerce platform.',
        examples=['Sales Tax'],
    )
    rate: Optional[float] = Field(
        None,
        description='Rate of taxation represented as a fraction of the net price (typically in the range 0.00 - 1.00).',
        examples=[0.15, 0.2],
    )


class TaxComponents(BaseModel):
    taxComponents: Optional[List[TaxComponent]] = None


class AccountBalance(BaseModel):
    available: Optional[Decimal] = Field(
        None, description="The account's current balance"
    )
    currency: Optional[Currency] = Field(
        None, description='The currency of the account'
    )
    pending: Optional[Decimal] = Field(
        None, description='Funds that are not yet available in the balance'
    )
    reserved: Optional[Decimal] = Field(None, description='Funds reserved as holdings')


class PaymentRef(Field0, CreatedDate, ModifiedDates):
    amount: Optional[float] = Field(
        None,
        description='Payment Amount (including gratuity).',
        examples=[194.12, -283.56, 0],
    )
    currency: Optional[Currency] = Field(
        None, description='Currency in which the payment was made.'
    )
    dueDate: Optional[DateTime] = Field(
        None, description='Date by which payment must be made'
    )
    paymentProvider: Optional[str] = Field(
        None,
        description='Service provider of the payment, if applicable.',
        examples=['Amazon Pay', 'Checkout.com', 'SagePay'],
    )
    status: Optional[PaymentStatus] = None
    type: Optional[PaymentType] = None


class TransactionSourceRef(RecordRef):
    type: Optional[TransactionSourceType] = None


class ProductInventory(BaseModel):
    locations: Optional[List[ProductInventoryLocation]] = None
    totalQuantity: Optional[float] = None


class TaxComponentAllocation(BaseModel):
    rate: Optional[float] = Field(
        None,
        description='Tax amount on order line sale as available from source commerce platform.',
    )
    taxComponentRef: Optional[TaxComponentRef] = None


class CompanyInfo(CreatedDate, ModifiedDates):
    accountBalances: Optional[List[AccountBalance]] = Field(
        None,
        description="The available and current cash balances for the company's accounts",
    )
    addresses: Optional[List[Address]] = Field(
        None, description='Addresses associated with the company'
    )
    baseCurrency: Optional[Currency] = None
    commercePlatformRef: Optional[str] = Field(
        None,
        description='Identifier or reference for the company in the commerce platform',
    )
    companyLegalName: Optional[str] = Field(
        None,
        description='The full legal name of the company',
        examples=['Codat Limited'],
    )
    companyName: Optional[str] = Field(
        None, description='The name of the company', examples=['Codat']
    )
    phoneNumbers: Optional[List[PhoneNumber]] = Field(
        None, description='Phone numbers associated with the company'
    )
    registrationNumber: Optional[str] = Field(
        None, description='The registration number of the company', examples=[10480375]
    )
    sourceUrls: Optional[Dict[str, str]] = Field(
        None,
        description="URL addresses for the originating system. For example, potential use cases include 'deeplinking' to the originating system",
        examples=[
            {
                'url1': 'https://connect.sandbox.com/v2/customers',
                'url2': 'https://connect.sandbox.com/v2/disputes',
            }
        ],
    )
    webLinks: Optional[List[WebLink]] = Field(
        None, description='Weblinks associated with the company'
    )


class Dispute(Field0, CreatedDate, ModifiedDates):
    currency: Currency = Field(..., description='Currency of the disputed transaction.')
    disputedTransactions: Optional[TransactionSourceRef] = Field(
        None, description='Link to the source event which triggered this transaction.'
    )
    dueDate: Optional[DateTime] = Field(
        None, description='Date when the next action in the dispute resolution is due'
    )
    reason: Optional[str] = Field(
        None, description='Reason for the dispute', examples=['Unhappy with product']
    )
    status: Optional[DisputeStatus] = None
    totalAmount: Optional[float] = Field(
        None,
        description='Total transaction amount that is under dispute.',
        examples=[194.12, -283.56, 0],
    )


class Disputes(PagingInfo):
    results: Optional[List[Dispute]] = None


class ProductCategories(PagingInfo):
    results: Optional[List[ProductCategory]] = None


class Transaction(Field0, CreatedDate, ModifiedDates):
    currency: Optional[str] = Field(
        None,
        description='The currency data type in Codat is the [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) currency code, e.g. _GBP_.\n\n## Unknown currencies\n\nIn line with the ISO 4217 specification, the code _XXX_ is used when the data source does not return a currency for a transaction. \n\nThere are only a very small number of edge cases where this currency code is returned by the Codat system.',
        examples=['GBP', 'USD', 'EUR'],
        title='Currency',
    )
    subType: Optional[str] = Field(
        None,
        description='Non-standardised transaction type data from the commerce platform',
        examples=['CardPayment', 'Invoice payment'],
    )
    totalAmount: Optional[float] = Field(
        None, description='The total transaction amount', examples=[194.12, -283.56, 0]
    )
    transactionSourceRef: Optional[TransactionSourceRef] = Field(
        None, description='Link to the source event which triggered this transaction'
    )
    type: Optional[TransactionType] = None
    sourceCreatedDate: Optional[DateTime] = Field(
        None,
        description='The date on which this record was created in the originating system',
    )


class Transactions(PagingInfo):
    results: Optional[List[Transaction]] = None


class OrderLineItem(Field0):
    discountAllocations: Optional[List[OrderDiscountAllocation]] = None
    productRef: Optional[ProductRef] = None
    productVariantRef: Optional[ProductVariantRef] = None
    quantity: Optional[float] = Field(
        None,
        description='Number of units of the product sold.\nFor refunds, quantity is a negative value.\n',
    )
    taxPercentage: Optional[float] = Field(
        None,
        description='Percentage rate (from 0 to 100) of any sale tax applied to the unit amount.',
        examples=[0, 12.5, '45.00'],
    )
    taxes: Optional[List[TaxComponentAllocation]] = Field(
        None, description='Taxes breakdown as applied to order lines.'
    )
    totalAmount: Optional[float] = Field(
        None,
        description='Total price of the line item, including discounts, tax and minus any refunds.',
    )
    totalTaxAmount: Optional[float] = Field(
        None, description='Total amount of tax applied to the line item.'
    )
    unitPrice: Optional[float] = Field(
        None, description='Price per unit of goods or service.'
    )


class ServiceCharge(BaseModel):
    description: Optional[str] = Field(
        None,
        description='Service charges for this order.',
        examples=['A service charge'],
    )
    quantity: Optional[int] = Field(
        None,
        description='The number of times the charge is charged.',
        examples=[1, 12, 45],
    )
    taxAmount: Optional[float] = Field(
        None,
        description='Amount of the service charge that is tax.',
        examples=[0, 12.5, 45],
    )
    taxPercentage: Optional[float] = Field(
        None,
        description='Percentage rate (from 0 to 100) of any tax applied to the service charge.',
        examples=[0, 12.5, 45],
    )
    taxes: Optional[List[TaxComponentAllocation]] = Field(
        None, description='Taxes breakdown as applied to service charges.'
    )
    totalAmount: Optional[float] = Field(
        None,
        description='Total service charge, including taxes.',
        examples=[0, 12.5, 45],
    )
    type: Optional[ServiceChargeType] = None


class ProductVariant(Field0, CreatedDate, ModifiedDates):
    barcode: Optional[str] = Field(
        None,
        description='Unique product number of the variant. This might be a barcode, UPC, ISBN, etc.',
        examples=['564158468416486458646886484', 'CSE370'],
    )
    inventory: Optional[List[ProductInventory]] = Field(
        None,
        description='Information about the total inventory as well as the locations inventory is in.',
    )
    isTaxEnabled: Optional[bool] = Field(
        None, description='Whether sales taxes are enabled for this product variant.'
    )
    name: Optional[str] = Field(
        None,
        description='Name of the product recorded in the commerce or point of sale platform.',
        examples=['Red Coat', 'Black Coat', 'Large Brown Hat'],
    )
    prices: Optional[List[ProductPrice]] = Field(
        None, description='Prices for the product variants in different currencies.'
    )
    shippingRequired: Optional[bool] = Field(
        None,
        description='Indicates whether or not the product requires physical delivery.',
    )
    sku: Optional[str] = Field(
        None,
        description='SKU (stock keeping unit) of the variant, as defined by the merchant.',
        examples=['Coat-Red-Lrg', 'Coat-Black-Md', 'LargeBrownHat', 'A725BA2'],
    )
    status: Optional[ProductVariantStatus] = None
    unitOfMeasure: Optional[str] = Field(
        None,
        description='Unit of measure for the variant, such as `kg` or `meters`.',
        examples=['kg', 'm', 'meters'],
    )
    vatPercentage: Optional[float] = Field(
        None,
        description='VAT rate for the product variant if sales taxes are enabled.',
        examples=[12.5, 0, 20],
    )


class Order(CreatedDate, ModifiedDates):
    id: str = Field(
        ...,
        description='A unique, persistent identifier for this record',
        examples=[
            '13d946f0-c5d5-42bc-b092-97ece17923ab',
            '9wg4lep4ush5cxs79pl8sozmsndbaukll3ind4g7buqbm1h2',
            7110701885,
            'EILBDVJVNUAGVKRQ',
        ],
    )
    closedDate: Optional[DateTime] = Field(
        None,
        description='Date on which order was closed after the product was shipped, paid for, and any refund period had elapsed.',
    )
    country: Optional[str] = Field(
        None,
        description='The Codat country property is returned as it was provided in the underlying platform by the company without any formatting on our part.\n\nDepending on the platform the value of this property will either be an <a href="https://en.wikipedia.org/wiki/List_of_ISO_3166_country_codes" target="_blank">ISO 3166</a> code (2-alpha or 3-alpha) or free-form text returned as a string name in our model. \n\nFor POST operations against platforms that demand a specific format for the country code, we have documented accepted values in the [options](https://docs.codat.io/codat-api#/operations/get-companies-companyId-connections-connectionId-push) endpoint.',
        examples=['GBR', 'USA', 'ABW'],
    )
    currency: Optional[Currency] = None
    customerRef: Optional[CustomerRef] = None
    locationRef: Optional[LocationRef] = None
    orderLineItems: Optional[List[OrderLineItem]] = None
    orderNumber: Optional[str] = Field(
        None,
        description='Friendly reference for the order in the commerce or point of sale platform.',
    )
    payments: Optional[List[PaymentRef]] = None
    serviceCharges: Optional[List[ServiceCharge]] = None
    totalAmount: Optional[float] = Field(
        None,
        description='Total amount of the order, including tax, net of any discounts and refunds.',
    )
    totalDiscount: Optional[float] = Field(
        None, description='Total amount of discount applied to the order.'
    )
    totalGratuity: Optional[float] = Field(
        None, description='Extra amount added to a bill.'
    )
    totalRefund: Optional[float] = Field(
        None,
        description='Total amount refunded issued by a merchant on an order (always a negative value).',
    )
    totalTaxAmount: Optional[float] = Field(
        None, description='Total amount of tax applied to the order.'
    )


class Orders(PagingInfo):
    results: Optional[List[Order]] = None


class Product(Field0):
    categorization: Optional[str] = Field(
        None,
        description='Retail category that the product is assigned to',
        examples=['Hardware', 'Software', 'Support Services'],
    )
    description: Optional[str] = Field(
        None,
        description='Description of the product recorded in the commerce or point of sale platform.',
        examples=[
            '1tb Western Digital Hard Drive',
            'Install of Windows 11 (Professional Edition)',
            '1 hour of support from an agent (phone or remote)',
        ],
    )
    isGiftCard: Optional[bool] = Field(
        None,
        description='Whether the product represents a gift card or voucher that\ncan be redeemed in the commerce or POS platform\n',
    )
    name: Optional[str] = Field(
        None,
        description='Name of the product in the commerce or POS system',
        examples=['Hard Drive', 'Windows Installation', 'Software Support (Hourly)'],
    )
    variants: Optional[List[ProductVariant]] = None


class Products(PagingInfo):
    results: Optional[List[Product]] = None
