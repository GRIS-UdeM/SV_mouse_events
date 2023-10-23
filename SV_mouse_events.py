import macmouse
import time
import socket
import subprocess

VERSION = "0.0.1"

UDP_IP = "127.0.0.1"
UDP_PORT = 18021

def main():

    print("SV_mouse_events version:", VERSION)
    print("UDP target IP:", UDP_IP)
    print("UDP target port:", UDP_PORT)

    cmd = ["pgrep", "SV_mouse_events"]
    process = subprocess.Popen(cmd, -1, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    pid, err = process.communicate()

    if pid != "":
        quit()
    
    while True:
        msg = "1" if macmouse.is_pressed(macmouse.LEFT) else "0"
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.sendto(bytes(msg, "utf-8"), (UDP_IP, UDP_PORT))

        time.sleep(0.1)

if __name__ == "__main__":
    main()

