import urllib

import subprocess, smtplib, os
from urllib.parse import urlsplit, parse_qs
import requests

accessURl = []
directedURL = []

print(os.getcwd())
directory = "/home/w3e65/SecurityAutomation/Turbolist3r"

command = "cd /home/w3e65/SecurityAutomation/Turbolist3r ; python turbolist3r.py -d stays.io"
result = subprocess.check_output(command, shell=True)
payload = result.decode("utf-8")
with open('subdomain.txt', 'w') as f:
    f.write("%s" % payload)
print(result)


def checkHTTPstatus(command):
    withHTTPS = "https://" + command
    httpsCommand = "curl --connect-timeout 10 -o /dev/null -s -w \"%{http_code}\" " + withHTTPS

    try:
        result = subprocess.check_output(httpsCommand, shell=True, stderr=subprocess.STDOUT)
        status_code = str(result.decode("utf-8"))
        code = status_code.replace("'", "").strip(' \t\n\r')
        decimal_code = int(code, 10)
        if decimal_code == 200:
            accessURl.append(withHTTPS)


    except subprocess.CalledProcessError as e:
        print("000 as CalledProcessError")
        # raise RuntimeError("command '{}' return with error (code {}): {}".format(e.cmd, e.returncode, e.output))

    withHTTP = "http://" + command
    httpCommand = "curl --connect-timeout 10 -o /dev/null -s -w \"%{http_code}\" " + withHTTP
    try:
        result2 = subprocess.check_output(httpCommand, shell=True, stderr=subprocess.STDOUT)
        status_code1 = str(result2.decode("utf-8"))
        code1 = status_code1.replace("'", "").strip(' \t\n\r')
        decimal_code1 = int(code1, 10)
        if decimal_code1 == 200:
            accessURl.append(withHTTP)

    except subprocess.CalledProcessError as e:
        print("000 as CalledProcessError")
        # raise RuntimeError("command '{}' return with error (code {}): {}".format(e.cmd, e.returncode, e.output))


with open('subdomain.txt') as fp:
    with open('all_sub_domain.txt', 'w') as f:
        for line in fp:
            if (not line.__contains__("-") and not line.__contains__("|") and not line.__contains__(
                    "!") and not line.__contains__("~") and not line.__contains__(" ")):
                subdomain = line.replace("[92m", "")
                subdomain = subdomain.replace("[0m", "")
                f.write("%s \n" % subdomain)
                checkHTTPstatus(subdomain)

with open('access_sub_domain.txt', 'w') as file:
    for x in accessURl:
        file.write("%s \n" % x)


def scanDirectoryndResultAnalysis():
    with open('all_possible_directory.txt', 'w') as dir:
        with open('access_sub_domain.txt') as file:
            for line in file:
                with open('directory_payload.txt') as payload_file:
                    for payload in payload_file:
                        first = str(line).strip(' \t\n\r')
                        second = str(payload).strip(' \t\n\r')
                        directory_url = first + "/" + second
                        carl = "curl --connect-timeout 10 -o /dev/null -s -w \"%{http_code}\" " + directory_url

                        try:
                            result = subprocess.check_output(carl, shell=True, stderr=subprocess.STDOUT)
                            status_code = str(result.decode("utf-8"))
                            code = status_code.replace("'", "").strip(' \t\n\r')
                            decimal_code = int(code, 10)
                            if decimal_code == 200:
                                directedURL.append(directory_url)
                                dir.write("%s \n" % directedURL)

                        except subprocess.CalledProcessError as e:
                            print("000 as CalledProcessError")


scanDirectoryndResultAnalysis()
print(directedURL)
