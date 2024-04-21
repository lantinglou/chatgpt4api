from talkingheads import GeminiClient
# chathead = GeminiClient(
#     cold_start=True,
#     incognito=False,
#     headless=False,
#     verbose=True,
#     user_data_dir='/Users/lantinglou/Downloads/profile'
# )
chathead = GeminiClient(
    verbose=True,
    incognito=False,
    headless=True,
    user_data_dir='/Users/lantinglou/Downloads/profile'
)
response = chathead.interact("hi,who are you")

print(response)