from talkingheads import ChatGPTClient
from library.getprofile import GetProfile


use_account = True  # False only can use GPT-3.5, if have verification set Ture manual pass it, No user pass input required.

if use_account:
    profile= GetProfile(relogin=False)# Only your profile cookie has expired. You need to set relogin = True.
    profile_path = profile.profile_path
    chathead = ChatGPTClient(
    incognito=False,
    verbose=True,
    user_data_dir=profile_path
    )
    if chathead.switch_model()==False:
        print("switch model failed")

else:
    chathead = ChatGPTClient(
    incognito=False,
    verbose=True,
    )

response = chathead.interact("你是什么版本的GPT")
print(response)