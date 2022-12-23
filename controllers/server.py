import models.main_m as main_model
import views.main_v as main_view
import socket
import threading
import json

HOSTNAME = socket.gethostname()
HOST = socket.gethostbyname(HOSTNAME)
PORT = 12345
FORMAT = "utf8"

class App():
    def __init__(self, server):
        def handleClient(self, connection, address):
            # Connected by (address)
            while True:
                try:
                    # message structure: 
                    # group: "Login", "Query", "Archive" or "Exit"
                    # type: 1 of 13 functions
                    # data
                    msg = json.loads(connection.recv(1024).decode(FORMAT))
                    # data_send = json.dumps(data)
                    # connection.sendall(data_send.encode(FORMAT))
                    #if message == "":

                    if msg == "Exit":
                        connection.close()
                        break
                    elif msg=='': raise Exception

                except:
                    # Client might be forcibly disconnected!
                    connection.close()
                    break

        def runServer():
            while True:
                connection, address = server.accept()
                thread = threading.Thread(target = handleClient, args = (self, connection, address))
                thread.daemon = True
                thread.start()

        serverThread = threading.Thread(target = runServer)
        serverThread.daemon = True
        serverThread.start()

################### MAIN ################################

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()
try:
    app = App()
    app.mainloop()
except:
    server.close()