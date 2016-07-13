# Introduction

### Warning: This module is in a very early development stage as of 13/07/2016. It may have few bugs.

`pyip2asn` is a python module takes a IPv4 address and returns Autonomous System Number (ASN) and AS Description.

Under the hood it uses cymru ip to asn database to map `IPv4` addresses to AS Numbers. Cymru database is queried via DNS and reposne is parsed.

AS Description is scraped from http://www.bgplookingglass.com web page and then combined with the DNS result from Cymru database. 

You need internet conenction to be able to use `pyip2asn`

# Example



