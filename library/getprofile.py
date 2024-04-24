import socket, threading, time, subprocess, platform, os

class GetProfile:
    def __init__(self, relogin=False):
        """
        This constructor initializes the class by setting the profile path and login requirements,
        and performs conditional login if necessary.
        """
        self.profile_path = os.path.join(os.path.expanduser('~'), '.profile')
        self.conditional_login(relogin)

    def conditional_login(self, relogin: bool = False):
        """Conditionally launches Chrome based on the login requirement and profile existence."""
        if not os.path.exists(self.profile_path) or relogin:
            system = platform.system()
            if system == 'Windows':
                self.chrome_path = r'"C:\Program Files\Google\Chrome\Application\chrome.exe"'
            elif system == 'Darwin':
                self.chrome_path = r'"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"'
            else:
                raise Exception("Unsupported operating system.")
            url = r"https://chat.openai.com"
            free_port = self.find_available_port()
            self.launch_chrome_with_remote_debugging(free_port, url)
            print("You have 90s to manually pass verification or complete the login and switch default model, then Chrome will exit.")
            time.sleep(90)
            self.close_chrome()

    @staticmethod
    def find_available_port():
        """Finds and returns an available port number on the local machine."""
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind(('', 0))
            s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            return s.getsockname()[1]

    def launch_chrome_with_remote_debugging(self, port, url):
        """Launches a new Chrome instance with remote debugging enabled on the specified port and navigates to the URL."""
        chrome_cmd = f"{self.chrome_path} --remote-debugging-port={port} --user-data-dir={self.profile_path} {url}"
        subprocess.Popen(chrome_cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, shell=True)

    def close_chrome(self):
        """Closes the Chrome browser."""
        try:
            if platform.system() == 'Windows':
                subprocess.run("taskkill /F /IM chrome.exe /T", check=True, shell=True)
            else:
                subprocess.run("killall 'Google Chrome'", check=True, shell=True)
            print("Chrome browser has been closed successfully.")
        except subprocess.CalledProcessError as e:
            print(f"Failed to close Chrome: {e}")