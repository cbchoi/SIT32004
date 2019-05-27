import socket

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432        # The port used by the server

client_state = ['ask_name', 'asked_name', 'ask_age', 'asked_age', 'termination', 'unknown']

cur_state = 'ask_name'

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    print("Greeing with server")
    input("Press enter to proceed")
    while True:
        if cur_state == 'ask_name':
            s.sendall(b'what is your name?')
            cur_state = 'asked_name'
        elif cur_state == 'asked_name':
            data = s.recv(1024)
            recv_str = data.decode('ascii') 
            if recv_str[:10] == 'My name is':
                cur_state = 'ask_age'
            print(recv_str)
        elif cur_state == 'ask_age':
            s.sendall(b'How old are you?')
            cur_state = 'asked_age'
        elif cur_state == 'asked_age':
            data = s.recv(1024)
            recv_str = data.decode('ascii') 
            print(recv_str)
            cur_state = 'wait'
        elif cur_state == 'termination':
            break
        elif cur_state == 'unknown':
            data = s.recv(1024)
            recv_str = data.decode('ascii') 
            cur_state = 'termination'
            s.sendall(b'Okay! Let\'s go!')
        else:
            data = s.recv(1024)
            recv_str = data.decode('ascii') 
            print(recv_str)
            cur_state = 'unknown'
            s.sendall(b'Sorry, what did you say?')
