import socket
import threading
import time
import subprocess
import platform



class GetProfile:

    def __init__(self, chrome_path, profile_path):
        """
        This constructor automates the following steps:
        1. Open a Chrome browser with remote debugging enabled at a specified URL.
        2. Wait for 90 seconds for the user to complete the login to get profile.
        """

        self.chrome_path = chrome_path
        self.profile_path = profile_path
        url = r"https://chat.openai.com"
        free_port = self.find_available_port()
        self.launch_chrome_with_remote_debugging(free_port, url)

        print("You have 90 seconds to complete the login then chrome will exit")
        time.sleep(90)
        self.close_chrome()

    @staticmethod
    def find_available_port():
        """ This function finds and returns an available port number on the local machine by creating a temporary
            socket, binding it to an ephemeral port, and then closing the socket. """

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind(('', 0))
            s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            return s.getsockname()[1]

    def launch_chrome_with_remote_debugging(self, port, url):
        """ Launches a new Chrome instance with remote debugging enabled on the specified port and navigates to the
            provided url """

        def open_chrome():
            chrome_cmd = f"{self.chrome_path} --remote-debugging-port={port} --user-data-dir={self.profile_path} {url}"
            with subprocess.Popen(chrome_cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, shell=True):
                pass

        chrome_thread = threading.Thread(target=open_chrome)
        chrome_thread.start()

    def close_chrome(self):
        try:
            # 根据操作系统选择不同的命令
            if platform.system() == 'Windows':
                subprocess.run("taskkill /F /IM chrome.exe /T", check=True, shell=True)
            else:
                subprocess.run("killall 'Google Chrome'", check=True, shell=True)
            print("Chrome browser has been closed successfully.")
        except subprocess.CalledProcessError as e:
            print(f"Failed to close Chrome: {e}")


    