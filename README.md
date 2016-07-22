# Introduction

### Warning: This module is in early development stage as of 13/07/2016. It may have few bugs.

`pyip2asn` is a python module that takes an IPv4 address as an argument and returns Autonomous System Number (ASN) and AS Description as a python tuple.

Under the hood it uses Cymru ip to asn database to map `IPv4` addresses to AS Numbers. Cymru database is queried via DNS and reponse is parsed.

AS Description is scraped from http://www.bgplookingglass.com and then AS description is combined with the DNS result from Cymru database. 

You need internet connection to be able to use `pyip2asn`


# Example

``` 
In [1]:import pyip2asn

In [2]:# Generate ASN Description Dictionary in order to speed up the IPv4 to ASN lookup.
In [3]: asn_dict = pyip2asn.get_asn_dictionary()

In [4]: pyip2asn.ip2asn("8.8.8.8",asn_dict)
Out[4]: (15169, u'GOOGLE - Google Inc.')

```

## Foot Note:

I've discovered another python module that uses GeoIPLite database to map ip addresses/host names to (AS Numbers, AS Decriptions) after I wrote the `pyip2asn` 

quoring from that library:
```
>>> gi = pygeoip.GeoIP('/path/to/GeoIPASNum.dat')
>>> gi.org_by_name('cnn.com')
'AS5662 Turner Broadcasting'
```
or

```
>>> gi.org_by_addr("90.223.167.43")
u'AS5607 BSKYB-BROADBAND-AS'
```
-`pygeoip` allows AS mapping both based on IPv4 and domain name. `pyip2asn` only does for IPv4 address for teh time being. 
-`pygeiop` requires GeoIP ASN database to be downloaded, `pyip2asn` do not necessarily need some library to be downloaded. (however it is much slower if not downloaded)
