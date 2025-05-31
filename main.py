import socket
import time

COLOR_CODE = {
    "RESET": "\033[0m",
    "GREEN": "\033[32m",
    "RED": "\033[31m",
    "PURPLE": "\033[95m",
}

banner = '''
11111¶__________________1¶¶¶¶1________1¶
1111¶¶_____¶¶¶¶1______1¶¶_¶¶¶¶¶1_______¶¶
111¶¶_1_1_¶¶¶¶¶¶¶_1___¶__1¶¶¶¶¶¶111____1¶¶
111¶_1________11¶¶1___¶¶¶1__1_____1¶¶¶1__1¶
11¶1__1¶¶1______11_____1____¶¶__1¶¶1__¶¶__1¶
11¶1__111¶¶¶¶___¶1___________1¶¶1___¶__¶1__¶
11¶1____1_11___¶¶_____1¶1_________¶¶¶1__¶__¶1
111¶_1__¶____1¶¶______11¶1_____1¶¶1_¶¶¶1¶__¶1
111¶1__¶¶___11¶¶____¶¶¶_¶___1¶¶¶1___¶__¶___¶1
111¶¶__¶¶¶1_____¶¶1_____11¶¶¶1_¶__1¶¶_____¶11
1111¶__¶¶1¶¶¶1___¶___1¶¶¶¶1____¶¶¶¶¶_____¶¶11
1111¶__¶_1__¶¶¶¶¶¶¶¶¶11__¶__1¶¶¶1_¶_____¶¶111
1111¶1_¶¶¶__1___¶___1____¶¶¶¶¶1¶_¶¶____¶¶1111
1111¶1_¶¶¶¶¶¶¶1¶¶11¶¶1¶¶¶¶¶1___1¶¶_____¶11111
1111¶1_¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶1_¶____¶¶_____¶¶11111
1111¶1_¶¶¶¶¶¶¶¶¶¶¶¶1¶1____¶__1¶¶______¶111111
1111¶__1¶¶_¶_¶__¶___11____1¶¶¶______1¶1111111
1111¶___¶¶1¶_11_11__1¶__1¶¶¶1___11_1¶11111111
1111¶_____¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶1___11111¶¶111111111
▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬
                              IP Attack    
'''


def print_colored(text, color):
    print(COLOR_CODE[color] + text + COLOR_CODE["RESET"])


def get_target_ip():
    return input(COLOR_CODE['PURPLE'] + 'Enter the IP address for the attack: ' + COLOR_CODE['RESET'])


def send_tcp_request(ip, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((ip, port))
        print_colored('[+] Socket connected successfully', 'GREEN')
        sock.close()
    except socket.error as e:
        print_colored(f'[-] Socket connection failed: {e}', 'RED')


def main():
    print_colored(banner, 'PURPLE')
    ip_address = get_target_ip()
    port = 80
    num_requests = 100

    for _ in range(num_requests):
        send_tcp_request(ip_address, port)
        time.sleep(1)


if __name__ == "__main__":
    main()
