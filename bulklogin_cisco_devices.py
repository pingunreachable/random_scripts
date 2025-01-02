from pexpect import pxssh
import getpass
import datetime

username = raw_input('Username: ') #Grabs username
password = getpass.getpass() #Grabs password using getpass module
dtg = datetime.datetime.now() #Current Date and Time
print(dtg) #Remove this if you wish

with open ('ipaddresses.txt') as file: #Opens ipaddresses text file. You will have to create this
    for hostip in file: #Loop interating through host ip addresses in the opened file

        try:
            hostname = hostip
            s = pxssh.pxssh(timeout=4, options={"StrictHostKeyChecking": "no"}) 
            s.login(hostname, username, password, auto_prompt_reset=False) #login 
            s.sendline('term leng 0') #Commands to run
            s.prompt() #Syncs the prompt 
            s.sendline('sh int status')
            s.prompt()
            s.sendline('sh ver')
            s.prompt()
            print (s.before) #Prints output
            s.logout() #Logs out of network device

            archive = open("%s %s" %(hostname,dtg),"w") #Creates text file to dump output into
            print(archive) #Remove this if you wish
            archive.write(s.before) #Writes to file
            archive.close() #Closes file

        except pxssh.ExceptionPxssh: #Exception condition
            print('Login Fail')
            break
