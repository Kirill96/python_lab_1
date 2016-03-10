"""Regular expr. lib"""
#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

import re

def valid_email():
    """Validation email adress"""
    true_email_adress = "devid29615@gmail.com"
    #false_email_adress = "fsada se@he..rrr  d..s/"
    template = re.compile("^([A-Za-z0-9-_](\.?[A-Za-z0-9-_])*)"
                          "@([a-z]+\.(net|com|info|org|([a-z][a-z])))$")
    result = template.match(true_email_adress)
    #result = template.match(false_email_adress)
    if result:
        return True
    else:
        return False


def  valid_number():
    """Validation number"""
    #true_number = "1231.3543"
    false_number = "1.7fc9"
    template = re.compile("^-?[0-9]+[.|,][0-9]+$")
    #result = template.match(true_number)
    result = template.match(false_number)
    if result:
        return True
    else:
        return False


def url():
    """Definition parts of url"""
    _url_1 = "https://user102782:pass826162AZ22"\
             "@yahoo.com/rap?blackstar=mafia12#bsuir"
    #_url_2 = "https://yahoo.com/rap#bsuir"
    #_url_3 = "https://255.12.144.202/rap"
    template = re.compile("(?P<scheme>[a-z]+)://((?P<login>[\w]+):"
                          "(?P<password>[\w]+)@)?(?P<host>[.\w]+)/"
                          "(?P<urlPath>[\w]+)\??(?P<params>[a-z]+="
                          "[\w]+)?#?(?P<anchor>!?[a-z]+)?")
    result = template.search(_url_1)
    if result == None:
        print "Error"
    print "scheme: ", result.group("scheme")
    print "login: ", result.group("login")
    print "password: ", result.group("password")
    if result.group("host") == None:
        pass
    else:
        print "host: ", result.group("host")
    print "urlPath: ", result.group("urlPath")
    print "params: ", result.group("params")
    print "anchor: ", result.group("anchor")
