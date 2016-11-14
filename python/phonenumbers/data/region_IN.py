"""Auto-generated file, do not edit by hand. IN metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_IN = PhoneMetadata(id='IN', country_code=91, international_prefix='00',
    general_desc=PhoneNumberDesc(national_number_pattern='008\\d{9}|1\\d{7,12}|[2-9]\\d{9,10}', possible_number_pattern='\\d{6,13}', possible_length=(8, 9, 10, 11, 12, 13), possible_length_local_only=(6, 7, 8)),
    fixed_line=PhoneNumberDesc(national_number_pattern='(?:11|2[02]|33|4[04]|79)[2-7]\\d{7}|80[2-467]\\d{7}|(?:1(?:2[0-249]|3[0-25]|4[145]|[59][14]|6[014]|7[1257]|8[01346])|2(?:1[257]|3[013]|4[01]|5[0137]|6[0158]|78|8[1568]|9[14])|3(?:26|4[1-3]|5[34]|6[01489]|7[02-46]|8[159])|4(?:1[36]|2[1-47]|3[15]|5[12]|6[0-26-9]|7[0-24-9]|8[013-57]|9[014-7])|5(?:1[025]|[36][25]|22|4[28]|5[12]|[78]1|9[15])|6(?:12|[2345]1|57|6[13]|7[14]|80)|7(?:12|2[14]|3[134]|4[47]|5[15]|[67]1|88)|8(?:16|2[014]|3[126]|6[136]|7[078]|8[34]|91))[2-7]\\d{6}|(?:(?:1(?:2[35-8]|3[346-9]|4[236-9]|[59][0235-9]|6[235-9]|7[34689]|8[257-9])|2(?:1[134689]|3[24-8]|4[2-8]|5[25689]|6[2-4679]|7[13-79]|8[2-479]|9[235-9])|3(?:01|1[79]|2[1-5]|4[25-8]|5[125689]|6[235-7]|7[157-9]|8[2-467])|4(?:1[14578]|2[5689]|3[2-467]|5[4-7]|6[35]|73|8[2689]|9[2389])|5(?:[16][146-9]|2[14-8]|3[1346]|4[14-69]|5[46]|7[2-4]|8[2-8]|9[246])|6(?:1[1358]|2[2457]|3[2-4]|4[235-7]|[57][2-689]|6[24-578]|8[1-6])|8(?:1[1357-9]|2[235-8]|3[03-57-9]|4[0-24-9]|5\\d|6[2457-9]|7[1-6]|8[1256]|9[2-4]))\\d|7(?:(?:1[013-9]|2[0235-9]|3[2679]|4[1-35689]|5[2-46-9]|[67][02-9]|9\\d)\\d|8(?:2[0-6]|[013-8]\\d)))[2-7]\\d{5}', possible_number_pattern='\\d{6,10}', example_number='1123456789', possible_length=(10,), possible_length_local_only=(6, 7, 8)),
    mobile=PhoneNumberDesc(national_number_pattern='(?:7(?:0\\d{3}|2(?:[0235679]\\d{2}|[14][017-9]\\d|8(?:[0-59]\\d|6[089]|78))|3(?:[05-8]\\d{2}|1(?:[089]\\d|7[5-8])|2(?:[0-49][089]|[5-8]\\d)|3[017-9]\\d|4(?:[07-9]\\d|11)|9(?:[016-9]\\d|[2-5][089]))|4(?:0\\d{2}|1(?:[015-9]\\d|[23][089]|4[08])|2(?:09|[1-7][089]|[89]\\d)|3(?:[0-8][089]|9\\d)|4(?:[089]\\d|11|7[02-8])|[56]\\d[089]|7(?:[089]\\d|11|7[02-8])|8(?:[0-24-7][089]|[389]\\d)|9(?:[0-6][089]|7[089]|[89]\\d))|5(?:[0346-8]\\d{2}|1(?:[09]\\d|11)|2(?:[04-9]\\d|[123][089])|5[017-9]\\d|9[0-6][089])|6(?:0(?:[0-47]\\d|[5689][089])|(?:1[0-257-9]|3[19]|5[4589]|[6-9]\\d)\\d|2(?:[0-4]\\d|50))|7(?:0(?:0[2-9]|10)|(?:[1-79]\\d|8[1-9])\\d)|8(?:[0-79]\\d{2}|8(?:[08]\\d|11|7[02-9]|9[012]))|9(?:0(?:0[01]|[3-8]\\d|90)|7(?:[26-8]\\d|9[07-9])|8[0246-9]\\d|9(?:[04-9]\\d|11|2[234])))|8(?:0(?:[01589]\\d{2}|6[67]\\d|7(?:[2-7]\\d|86|90))|1(?:[02-57-9]\\d{2}|1(?:[0135-9]\\d|22|44)|6[089]\\d)|2(?:0[08]|[236-9]\\d|5[1-9])\\d|3(?:[0357-9]\\d{2}|170|28[0-6]|4[1-9]\\d)|[45]\\d{3}|6(?:[02457-9]\\d{2}|6(?:[08]\\d|7[02-8]|9[01]))|7(?:0[07]|[1-69]\\d|70)\\d|8(?:[0-26-9]\\d|44|5[2-9])\\d|9(?:[035-9]\\d|19|2[2-9]|4[0-8])\\d)|9\\d{4})\\d{5}', possible_number_pattern='\\d{10}', example_number='9987654321', possible_length=(10,)),
    toll_free=PhoneNumberDesc(national_number_pattern='00800\\d{7}|1(?:600\\d{6}|80(?:0\\d{4,9}|3\\d{9}))', possible_number_pattern='\\d{8,13}', example_number='1800123456', possible_length=(8, 9, 10, 11, 12, 13)),
    premium_rate=PhoneNumberDesc(national_number_pattern='186[12]\\d{9}', possible_number_pattern='\\d{13}', example_number='1861123456789', possible_length=(13,)),
    shared_cost=PhoneNumberDesc(national_number_pattern='1860\\d{7}', possible_number_pattern='\\d{11}', example_number='18603451234', possible_length=(11,)),
    personal_number=PhoneNumberDesc(),
    voip=PhoneNumberDesc(),
    pager=PhoneNumberDesc(),
    uan=PhoneNumberDesc(national_number_pattern='140\\d{7}', possible_number_pattern='\\d{10}', example_number='1409305260', possible_length=(10,)),
    voicemail=PhoneNumberDesc(),
    no_international_dialling=PhoneNumberDesc(national_number_pattern='00800\\d{7}|1(?:600\\d{6}|8(?:0(?:0\\d{4,9}|3\\d{9})|6(?:0\\d{7}|[12]\\d{9})))', possible_number_pattern='\\d{8,13}', example_number='1800123456', possible_length=(8, 9, 10, 11, 12, 13)),
    national_prefix='0',
    national_prefix_for_parsing='0',
    number_format=[NumberFormat(pattern='(\\d{5})(\\d{5})', format='\\1 \\2', leading_digits_pattern=['7(?:[02-578]|6[0-35-9]|9[07-9])|8(?:0[015-9]|2[02356-9]|3[0-57-9]|[1459]|6[02-9]|7[01-69]|8[0-24-9])|9', '7(?:[08]|2(?:[0235679]|[14][017-9]|8[0-79]|9[389])|3(?:[025-9]|1[07-9]|[34][017-9])|4(?:[0-35689]|[47][017-9])|5(?:[02346-9]|1[019]|5[017-9])|6(?:[06-9]|1[0-257-9]|2[0-5]|3[19]|5[4589])|7(?:[0-79]|8[1-9])|9(?:0|7[2-9]|8[0246-9]|9[0-24-9]))|8(?:0(?:[01589]|6[67]|7[2-9])|1(?:[02-57-9]|1[0135-9]|6[089])|2(?:0[08]|[236-9]|5[1-9])|3(?:[0357-9]|17|28|4[1-9])|[45]|6(?:[02457-9]|6[07-9])|7(?:0[07]|[1-69])|8(?:[0-26-9]|44|5[2-9])|9(?:[035-9]|19|2[2-9]|4[0-8]))|9', '7(?:0|2(?:[0235679]|[14][017-9]|8(?:[0-569]|78)|9[389])|3(?:[05-8]|1(?:[089]|7[5-9])|2(?:[5-8]|[0-49][089])|3[017-9]|4(?:[07-9]|11)|9(?:[01689]|[2345][089]|40|7[0189]))|4(?:[056]|1(?:[0135-9]|[23][089]|2[089]|4[08])|2(?:09|[1-7][089]|[89])|3(?:[0-8][089]|9)|4(?:[089]|11|7[02-8])|7(?:[089]|11|7[02-8])|8(?:[0-24-7][089]|[389])|9(?:[0-7][089]|[89]))|5(?:[0346-9]|1[019]|2(?:[03-9]|[12][089])|5[017-9])|6(?:[06-9]|1[0-257-9]|2[0-5]|3[19]|5[4589])|7(?:0(?:[02-9]|10)|[1-79]|8[1-9])|8(?:[0-79]|8(?:0[0189]|11|8[013-9]|9[012]))|9(?:0|7(?:[2-8]|9[7-9])|8[0246-9]|9(?:[04-9]|11|2[234])))|8(?:0(?:[01589]|6[67]|7(?:[2-7]|86|90))|1(?:[02-57-9]|1(?:[0135-9]|22|44)|6[089])|2(?:0[08]|[236-9]|5[1-9])|3(?:[0357-9]|170|28[0-6]|4[1-9])|[45]|6(?:[02457-9]|6(?:[08]|7[02-8]|9[01]))|7(?:0[07]|[1-69])|8(?:[0-26-9]|44|5[2-9])|9(?:[035-9]|19|2[2-9]|4[0-8]))|9'], national_prefix_formatting_rule='0\\1', national_prefix_optional_when_formatting=True),
        NumberFormat(pattern='(\\d{2})(\\d{4})(\\d{4})', format='\\1 \\2 \\3', leading_digits_pattern=['11|2[02]|33|4[04]|79[1-9]|80[2-46]'], national_prefix_formatting_rule='0\\1', national_prefix_optional_when_formatting=True),
        NumberFormat(pattern='(\\d{3})(\\d{3})(\\d{4})', format='\\1 \\2 \\3', leading_digits_pattern=['1(?:2[0-249]|3[0-25]|4[145]|[569][14]|7[1257]|8[1346]|[68][1-9])|2(?:1[257]|3[013]|4[01]|5[0137]|6[0158]|78|8[1568]|9[14])|3(?:26|4[1-3]|5[34]|6[01489]|7[02-46]|8[159])|4(?:1[36]|2[1-47]|3[15]|5[12]|6[0-26-9]|7[0-24-9]|8[013-57]|9[014-7])|5(?:1[025]|[36][25]|22|4[28]|5[12]|[78]1|9[15])|6(?:12|[2345]1|57|6[13]|7[14]|80)'], national_prefix_formatting_rule='0\\1', national_prefix_optional_when_formatting=True),
        NumberFormat(pattern='(\\d{3})(\\d{3})(\\d{4})', format='\\1 \\2 \\3', leading_digits_pattern=['7(?:12|2[14]|3[134]|4[47]|5[15]|[67]1|88)', '7(?:12|2[14]|3[134]|4[47]|5(?:1|5[2-6])|[67]1|88)'], national_prefix_formatting_rule='0\\1', national_prefix_optional_when_formatting=True),
        NumberFormat(pattern='(\\d{3})(\\d{3})(\\d{4})', format='\\1 \\2 \\3', leading_digits_pattern=['8(?:16|2[014]|3[126]|6[136]|7[078]|8[34]|91)'], national_prefix_formatting_rule='0\\1', national_prefix_optional_when_formatting=True),
        NumberFormat(pattern='(\\d{4})(\\d{3})(\\d{3})', format='\\1 \\2 \\3', leading_digits_pattern=['1(?:[23579]|[468][1-9])|[2-8]'], national_prefix_formatting_rule='0\\1', national_prefix_optional_when_formatting=True),
        NumberFormat(pattern='(\\d{2})(\\d{3})(\\d{4})(\\d{3})', format='\\1 \\2 \\3 \\4', leading_digits_pattern=['008'], national_prefix_formatting_rule='0\\1', national_prefix_optional_when_formatting=True),
        NumberFormat(pattern='(1600)(\\d{2})(\\d{4})', format='\\1 \\2 \\3', leading_digits_pattern=['160', '1600'], national_prefix_formatting_rule='\\1', national_prefix_optional_when_formatting=True),
        NumberFormat(pattern='(1800)(\\d{4,5})', format='\\1 \\2', leading_digits_pattern=['180', '1800'], national_prefix_formatting_rule='\\1', national_prefix_optional_when_formatting=True),
        NumberFormat(pattern='(18[06]0)(\\d{2,4})(\\d{4})', format='\\1 \\2 \\3', leading_digits_pattern=['18[06]', '18[06]0'], national_prefix_formatting_rule='\\1', national_prefix_optional_when_formatting=True),
        NumberFormat(pattern='(140)(\\d{3})(\\d{4})', format='\\1 \\2 \\3', leading_digits_pattern=['140'], national_prefix_formatting_rule='\\1', national_prefix_optional_when_formatting=True),
        NumberFormat(pattern='(\\d{4})(\\d{3})(\\d{3})(\\d{3})', format='\\1 \\2 \\3 \\4', leading_digits_pattern=['18[06]', '18(?:0[03]|6[12])'], national_prefix_formatting_rule='\\1', national_prefix_optional_when_formatting=True)],
    leading_zero_possible=True,
    mobile_number_portable_region=True)
