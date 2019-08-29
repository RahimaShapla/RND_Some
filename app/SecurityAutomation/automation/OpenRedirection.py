import subprocess

directedURL = []

def open_redirection_of_subdomain():
    with open('access_sub_domain.txt') as file:
        with open('redirection_payload.txt') as redir_file:
            for line in file:
                for payload in redir_file:
                    first = str(line).strip(' \t\n\r')
                    second = str(payload).strip(' \t\n\r')
                    directory_url = second + "/" + first
                    carl = "curl --connect-timeout 10 -o /dev/null -s -w \"%{http_code}\" " + directory_url

                    try:
                        result = subprocess.check_output(carl, shell=True, stderr=subprocess.STDOUT)
                        status_code = str(result.decode("utf-8"))
                        code = status_code.replace("'", "").strip(' \t\n\r')
                        decimal_code = int(code, 10)
                        if decimal_code == 200:
                            directedURL.append(directory_url)
                            # dir.write("%s \n" % directedURL)

                    except subprocess.CalledProcessError as e:
                        print("000 as CalledProcessError")


open_redirection_of_subdomain()
print(directedURL)
