import subprocess
import threading

def date():
    a= subprocess.run(['date','+%D %T'],stdout=subprocess.PIPE)
    
    a= a.stdout
    a= str(a)
    a= a.replace("'", '')
    a= a.replace("b", '')
    a= a.replace("\\n", '')   
    return a

def bash_RUN(CMD):subprocess.Popen( CMD)


#to get the current working directory
job=False
target_hour="235700"
interface=str(input("Enter Interface Name, example eth0 : "))
host_ip=str(input("Enter Target IP, example 192.168.100.1 : "))
print(interface)


while True:
    rtm_hour= date().split(' ')
    rtm_hour=rtm_hour[1].replace(':','')
    
    if job==False and  int(rtm_hour) >= 000000:
        filename=date().replace('/','-')+".pcap"
        tcpdmp=['sudo','tcpdump','host', host_ip,'-i', interface, '-s', '96','-q', '-w',filename]
        print(tcpdmp)
        job=True
        capture=threading.Thread(target=bash_RUN,args=(tcpdmp,))
        capture.start()#TCPDUMP
        print('runing tcpdump filename: ',filename)       
       
    if int(rtm_hour) >= int(target_hour) and job == True:
        print("ok")
        subprocess.run(['killall','-9','tcpdump'])
        job=False
