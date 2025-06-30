from flask import Flask, jsonify
import random
import string
app = Flask(__name__)
def generate_password():
   length = 12
   upper = random.choice(string.ascii_uppercase)
   lower = random.choice(string.ascii_lowercase)
   digit = random.choice(string.digits)
   special = random.choice('!@#$%^&*')
   all_chars = string.ascii_letters + string.digits + '!@#$%^&*'
   remaining = [random.choice(all_chars) for _ in range(length - 4)]
   password_list = list(upper + lower + digit + special + ''.join(remaining))
   random.shuffle(password_list)
   return ''.join(password_list)
@app.route('/generate-password', methods=['GET'])
def get_password():
   return jsonify({'password': generate_password()})
# ...existing code...
@app.route('/', methods=['GET'])
def home():
    return 'Password API is running.'
# ...existing code...
import os 
port = int(os.environ.get("PORT", 5000))
app.run(host="0.0.0.0", port=port)
