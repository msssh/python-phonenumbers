"""Auto-generated file, do not edit by hand. UG metadata"""
from phonenumbers.phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_UG = PhoneMetadata(id='UG', country_code=256, international_prefix='00[057]',
    general_desc=PhoneNumberDesc(national_number_pattern='\\d{9}', possible_number_pattern='\\d{5,9}'),
    fixed_line=PhoneNumberDesc(national_number_pattern='3\\d{8}|4(?:[1-6]\\d|7[136]|8[1356]|96)\\d{6}|20(?:[04]\\d|24)\\d{5}', possible_number_pattern='\\d{5,9}', example_number='312345678'),
    mobile=PhoneNumberDesc(national_number_pattern='7(?:[15789]\\d|0[0-7])\\d{6}', possible_number_pattern='\\d{9}', example_number='712345678'),
    toll_free=PhoneNumberDesc(national_number_pattern='800[123]\\d{5}', possible_number_pattern='\\d{9}', example_number='800123456'),
    premium_rate=PhoneNumberDesc(national_number_pattern='90[123]\\d{6}', possible_number_pattern='\\d{9}', example_number='901123456'),
    shared_cost=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    personal_number=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    voip=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    pager=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    uan=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    emergency=PhoneNumberDesc(national_number_pattern='999', possible_number_pattern='\\d{3}', example_number='999'),
    no_international_dialling=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    national_prefix='0',
    national_prefix_for_parsing='0',
    number_format=[NumberFormat(pattern='(\\d{3})(\\d{6})', format=u'\\1 \\2', leading_digits_pattern=['[7-9]|200|4(?:6[45]|[7-9])'], national_prefix_formatting_rule=u'0\\1'),
        NumberFormat(pattern='(\\d{2})(\\d{7})', format=u'\\1 \\2', leading_digits_pattern=['204|3|4(?:[1-5]|6[0-36-9])'], national_prefix_formatting_rule=u'0\\1'),
        NumberFormat(pattern='(2024)(\\d{5})', format=u'\\1 \\2', leading_digits_pattern=['202'], national_prefix_formatting_rule=u'0\\1')])
