from flask import Flask, request, abort
import config
import re
from environs import Env

env = Env()
env.read_env()

# Get the value of "vvs"
vvs_value = env('VVS')

app = Flask(__name__)

@app.before_request
def check_auth_token():
    if request.endpoint == 'update_vvs':
        auth_token = request.headers.get('Authorization')
        if auth_token != 'my-secret-token':
            abort(401, description='Unauthorized')

@app.route('/update_vvs', methods=['POST'])
def update_vvs():
    new_value = request.form.get('new_value')
    
    # Comment out the previous value
    config_file_path = "config.py"
    with open(config_file_path, "r") as f:
        file_content = f.read()
    pattern = r'(?<=\n\s*)"vvs":\s*r".*",\n'
    match = re.search(pattern, file_content)
    if match:
        start = match.start()
        end = match.end()
        file_content = file_content[:start] + "#" + file_content[start:end] + file_content[end:]
    with open(config_file_path, "w") as f:
        f.write(file_content)
    
    # Update the value of "vvs"
    config.val["vvs"] = new_value
    
    return "Value updated successfully"

if __name__ == '__main__':
    app.run()
