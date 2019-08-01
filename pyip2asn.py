#!/usr/bin/env python

import requests, pprint
from bs4 import BeautifulSoup

def get_asn_dictionary(verbose = False):
    ''' This module gets the latest AS Number to Desctiption from www.bgplookingglass.com'''
    
    asn_pages = [
                 "http://www.bgplookingglass.com/list-of-autonomous-system-numbers",
                 "http://www.bgplookingglass.com/list-of-autonomous-system-numbers-2",
                 "http://www.bgplookingglass.com/4-byte-asn-names-list"
                ]
    
    asn_dct ={}
    for asn_page in asn_pages:
        if verbose:
            print("parsing %s" % (asn_page))
            print("--------------------------")
            print("")
        r = requests.get(asn_page)
        soup = BeautifulSoup(r.text, 'html.parser')
        table = soup.find("pre")
        lst = table.find_all(text=True)
        for asn in lst:
            if asn[9:13] == "    ":
                marker = 13
            else:
                marker =8
            try: 
                as_number = int(asn[2:marker].strip())
                as_desc = asn[marker:].strip()
                asn_dct[as_number] = as_desc
            except:
                continue
    if verbose:        
        print("All parsing complete")
    return asn_dct


########################################################################
#######################################################################

import dns.resolver

def ip2asn(ip_address,asn_desc_dict={}):
    
    # Check if ASN description dictionary is provided, if not populate it
    if asn_desc_dict == {}:
        print("You din't provide ASN Description Dictionary, it slows down the process thousands of times")
        asn_desc_dict = get_asn_dictionary(verbose=False)
    
    octs = ip_address.split(".")
    query =  "%s.%s.%s.origin.asn.cymru.com" % (octs[2], octs[1], octs[0])
    answers = dns.resolver.query(query, 'TXT')
    try:
        asn = int(str(answers[0]).split("|")[0][1:].strip())
        return (asn,asn_desc_dict[asn])
    except:
        print 
        

print ip2asn("90.223.203.193")
