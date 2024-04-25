from flask import Flask, request, jsonify
from talkingheads import ChatGPTClient
from library.getprofile import GetProfile
def process_prompt(prompt):
    profile= GetProfile()
    profile_path = profile.profile_path
    chathead = ChatGPTClient(
    incognito=False,
    # headless=False,
    verbose=True,
    # uc_params = {"driver_executable_path":r"C:\Users\Light\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\Roaming\undetected_chromedriver\undetected_chromedriver.exe"},
    user_data_dir=profile_path
    )
    chathead.switch_model()
    response = chathead.interact(prompt)
    return response

app = Flask(__name__)
app.json.ensure_ascii = False
@app.route('/api', methods=['GET', 'POST'])
def interact():
    if request.method == 'POST':
        prompt = request.json.get('prompt')
    elif request.method == 'GET':
        prompt = request.args.get('prompt')
    
    if not prompt:
        return jsonify({'error': 'No prompt provided'}), 400
    
    response = process_prompt(prompt)
    return jsonify({'response': response}), 200, {'Content-Type': 'application/json; charset=utf-8'}

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=1317)
