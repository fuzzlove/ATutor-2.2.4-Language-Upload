# ATutor 2.2.4 Arbitrary File Upload / RCE (CVE-2019-12169)

- Exploit Title: ATutor 2.2.4 Arbitrary File Upload / RCE [CVE-2019-12169]
- Date: 5/24/19
- Exploit Author: liquidsky (JMcPeters)
- Vendor Homepage: https://atutor.github.io/
- Software Link: https://sourceforge.net/projects/atutor/files/latest/download
- Version: 2.2.4
- Tested on: Windows 8 / Apache / MySQL (XAMPP)
- CVE : CVE-2019-12169 | https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-12169
- Author Site: http://incidentsecurity.com | https://github.com/fuzzlove

 Description: ATutor 2.2.4 allows Arbitrary File Upload and Directory Traversal
 resulting in remote code execution via a ".." pathname in a ZIP archive to the mods/_core/languages/language_import.php (aka Import New Language) or mods/_standard/patcher/index_admin.php (aka Patcher) component.

 Greetz: wetw0rk, offsec ^^

 Notes: This application is no longer being maintained so there is no fix for this issue.

 update: if you wish to test this manually I have included the poc.zip for a better understanding.


 -   CVE-2019-12170: https://github.com/fuzzlove/ATutor-Instructor-Backup-Arbitrary-File
 -   CVE-2019-12169: https://github.com/fuzzlove/ATutor-2.2.4-Language-Exploit
