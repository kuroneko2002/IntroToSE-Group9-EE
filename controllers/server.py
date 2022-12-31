import sys
sys.path.append("..")
from models import main_m as main_model
from views import main_v as main_view
import socket
import threading
import json

HOSTNAME = socket.gethostname()
HOST = socket.gethostbyname(HOSTNAME)
PORT = 12345
FORMAT = "utf8"

class App():
    def __init__(self, server):
        def sendData(connection, data):
            data_send = json.dumps(data)
            connection.sendall(data_send.encode(FORMAT))

        def handleClient(self, connection, address):
            # print(address + 'has connect to server!')
            # Connected by (address)
            user = ""
            while True:
                try:
                    # parse message
                    msg = json.loads(connection.recv(1024).decode(FORMAT))

                    if msg.group == "Login":
                        model_res = main_model.loginGroup(msg.type, msg.data)
                        data_send = main_view.loginGroup(msg.type, model_res)
                        
                        # store user if login succeed
                        if (data_send.err_mes == 'None'):
                            user = msg.data.user
                            # print(user + 'has login!')

                        sendData(connection, data_send)

                    elif msg.group == "Query":
                        model_res = main_model.queryGroup(msg.type, msg.data)
                        data_send = main_view.queryGroup(msg.type, model_res)
                        sendData(connection, data_send)

                    elif msg.group == "Archive":
                        model_res = main_model.archiveGroup(msg.type, msg.data)
                        data_send = main_view.archiveGroup(msg.type, model_res)
                        sendData(connection, data_send)
                        

                    elif msg == "Exit":
                        # require login next time
                        if(user != ""):
                            main_model.loginGroup('logout', {
                                "user": user
                            })
                            # print(user + 'has logout!')

                        print(address + 'has disconnect!')
                        connection.close()
                        break
                    elif msg=='': 
                        raise Exception

                except:
                    # Client might be forcibly disconnected! -> force logout!
                    if(user != ""):
                        main_model.loginGroup('logout', {
                            "user": user
                        })
                        # print(user + 'has logout!')
                    
                    print(address + 'has disconnect!')
                    connection.close()
                    break

        def runServer():
            while True:
                print('in while loop')
                connection, address = server.accept()
                # thread handling
                thread = threading.Thread(target = handleClient, args = (self, connection, address))
                thread.daemon = True
                thread.start()
        
        runServer()
        # end init

################### MAIN ################################

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen()
    try:
        app = App(server)
    except:
        print('server closed in main')
        server.close()