import threading
import paramiko
import subprocess

def ssh_cmd(ip,user,passwd,command):
    client=paramiko.SSHClient()
    #r0ach>>> for key auth use
    #client.load_host.keys("path to key ")
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(ip,username=user,password=passwd)
    ssh_session=client.get_transport().open_session()
    if ssh_session.active:
        command=command.decode()
        ssh.session.exec_command(command)
        print ssh_session.recv(1024)
    return
ip="enter your ip"
ssh_cmd(ip,'r0ach','r0ach_N3v4r_di3z','help')
