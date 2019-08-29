
import subprocess, smtplib, os
import urllib.parse as urlparse

url = 'https://www.rentalhomes.com/refine?date_start=2019-08-22&date_end=2019-09-19&ref=home&search=ggg'
parsed = urlparse.urlparse(url)
print(urlparse.parse_qs(parsed.query))

# folder = "/home/w3e65/Desktop/"
# allValue = ""
# for file in os.listdir(folder):
#     print(file)
#     filepath = os.path.join(folder, file)
#     f = open(filepath, 'r')
#   #  print(f.read())
#     allValue += f.read();
#     # file1 = open("sub_url.txt", "w")  # write mode
#     # file1.write(f.read() + "\n")
#     # file1.close()
#     f.close()
#
# print(allValue)
#
# # print("hello")
# #
# # print(4 + 6)
# #
# # if 19 < 10:
# #     print("gg")
# # else:
# #     print("nn")
# #
# # i = 1
# # while i <= 6:
# #     print("this site is hacked")
# #     i += 1
#
#
# def send_mail(email, password, report):
#     server = smtplib.SMTP('smtp.gmail.com:587')
#     server.ehlo()
#     server.starttls()
#     server.login(email, password)
#     server.sendmail(email, email, report)
#     server.quit()
#
#
# #command = "cat ~/Desktop/bash.sh"
# #command = "cd /Downloads/ ;cat *.txt"
# #command = ["/bin/bash", "-c", "cd /Downloads/ ;cat *.txt"]
# # command = "/bin/bash -c cd /Downloads/ ;cat *.txt"
# # result = subprocess.check_output(command, shell=True)
# # print(result)
# send_mail("jordan.elmore23@gmail.com", "germany5", allValue)
