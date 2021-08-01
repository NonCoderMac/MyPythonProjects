"""Program to display Ghanaian day names for languages selected"""

def ghana_name(lang, sex, day):
    #ensuring no input error from user
    lang = lang.lower()
    sex = sex.lower()
    day = day.lower()

    #creating reference dictionary database
    ref = {
        'akan' : {'male' : {'sunday' : 'Kwasi', 'monday' : 'Kwadwo', 'tuesday' : 'Kwabena', 'wednesday' : 'Kwaku', 'thursday' : 'Yaw', 'friday' : 'Kofi', 'saturday' : 'Kwame'},
                  'female' : {'sunday' : 'Esi', 'monday' : 'Adwoa', 'tuesday' : 'Abena', 'wednesday' : 'Akua', 'thursday' : 'Yaa', 'friday' : 'Afia', 'saturday' : 'Ama'}},
        'ewe' : {'male' : {'sunday' : 'Koshi', 'monday' : 'Kodzo', 'tuesday' : 'Komla', 'wednesday' : 'Koku', 'thursday' : 'Yao', 'friday' : 'Koffi', 'saturday' : 'Komi'},
                  'female' : {'sunday' : 'Koshiwo', 'monday' : 'Adzo', 'tuesday' : 'Abla', 'wednesday' : 'Aku', 'thursday' : 'Yawo', 'friday' : 'Afi', 'saturday' : 'Ami'}},
        'ga' : {'male' : {'sunday' : 'Kwashi', 'monday' : 'Kojo', 'tuesday' : 'Kobla', 'wednesday' : 'Kwaku', 'thursday' : 'Kwao', 'friday' : 'Kofi', 'saturday' : 'Kwami'},
                  'female' : {'sunday' : 'Akoshia', 'monday' : 'Ajua', 'tuesday' : 'Abla', 'wednesday' : 'Akua', 'thursday' : 'Aba', 'friday' : 'Afi', 'saturday' : 'Ama'}}}

    #outputing feedback
    try:
        return ref[lang][sex][day]

    except:
        print ("Please re-check entered info. Something is not right")


