from talkingheads import ChatGPTClient
import sys, os, platform

profile_path = os.path.join(os.path.expanduser('~'), '.profile')

# if first argument is l / -l, or profile don't exists get one
if len(sys.argv)>0:
    first_argument = sys.argv[1]
    if first_argument in ('l', '-l'):
        login = True
if os.path.exists(profile_path)==False or login==True:
    from library.loginchatgpt import GetProfile
    system = platform.system()
    if system == 'Windows':
        chrome_path = r'"C:\Program Files\Google\Chrome\Application\chrome.exe"'
    elif system == 'Darwin':
        chrome_path = r'"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"'
    chatgpt = GetProfile(chrome_path, profile_path)

chathead = ChatGPTClient(
cold_start=True,
incognito=False,
credential_check=False,
verbose=True,
user_data_dir=profile_path
)
if chathead.switch_model():
    response = chathead.interact("你是什么版本的GPT")
    print(response)