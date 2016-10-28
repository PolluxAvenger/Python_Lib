# coding=utf-8

import tldextract

domain_list = ['www.jx.cn', 'www.nc.jx.cn', 'http://zap.co.it', 'http://www.bjzx.gov.cn/zhu.htm', 'http://www.beijing.gov.cn', 'http://www.bjrd.gov.cn/']

for item in domain_list:
    print('-----------' + item + '--------------')
    extracted = tldextract.extract(item)
    print(extracted.suffix)
    print(extracted.domain)
    print(extracted.subdomain)
