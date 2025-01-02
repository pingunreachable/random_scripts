from pexpect import pxssh
import getpass
import datetime

username = raw_input('Username: ')
password = getpass.getpass()
dtg = datetime.datetime.now()
print(dtg)

with open ('ipaddresses.txt') as file:
    for hostip in file:

        try:
            hostname = hostip
            s = pxssh.pxssh(timeout=5, options={"StrictHostKeyChecking": "no"})
            s.login(hostname, username, auto_prompt_reset=False)
            s.sendline(username)
            s.sendline(password)
            s.sendline('config paging disable')
            s.prompt()
            s.sendline('sh wlan summary')
            s.prompt()
            s.sendline('logout')
            s.sendline('\n')
            print (s.before)


            archive = open("%s%s" %(hostname,dtg),"w")
            print(archive)
            archive.write(s.before)
            archive.close()

        except pxssh.ExceptionPxssh:
            print('Login Fail')
            break
