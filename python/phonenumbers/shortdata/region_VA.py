"""Auto-generated file, do not edit by hand. VA metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_VA = PhoneMetadata(id='VA', country_code=None, international_prefix=None,
    general_desc=PhoneNumberDesc(national_number_pattern='1\\d{2}', possible_number_pattern='\\d{3}', possible_length=(3,)),
    toll_free=PhoneNumberDesc(),
    premium_rate=PhoneNumberDesc(),
    emergency=PhoneNumberDesc(national_number_pattern='11[2358]', possible_number_pattern='\\d{3}', example_number='113', possible_length=(3,)),
    short_code=PhoneNumberDesc(national_number_pattern='11[2358]', possible_number_pattern='\\d{3}', example_number='113', possible_length=(3,)),
    standard_rate=PhoneNumberDesc(),
    carrier_specific=PhoneNumberDesc(),
    short_data=True)
