from talkingheads import ChatGPTClient
from library.getprofile import GetProfile

"""First, you need to get your profile."""
"""If login expired or pass verification failed, delete .profile in your home directory and run again."""

profile= GetProfile(
    login=True,
)

profile_path = profile.profile_path
chathead = ChatGPTClient(
headless=False,
incognito=False,
verbose=True,
# uc_params = {"driver_executable_path":"/Users/lantinglou/Library/Application Support/undetected_chromedriver/undetected_chromedriver"}, #aviod download uc erverytime
user_data_dir=profile_path
)
chathead.switch_model() #  either GPT-3.5 or GPT-4, empty for default of your account

prompt = "你是什么版本的GPT"
response = chathead.interact(prompt)
print(response)