import os
from talkingheads import ChatGPTClient
from library.getprofile import GetProfile

profile_path = os.path.join(os.path.expanduser('~'), '.profile')

GetProfile(
    profile_path=profile_path,
    relogin=False
)

chathead = ChatGPTClient(
cold_start=True,
incognito=False,
credential_check=False,
verbose=True,
user_data_dir=profile_path
)
if chathead.switch_model()==False:
    print("switch model failed")
response = chathead.interact("你是什么版本的GPT")
print(response)