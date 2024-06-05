from flask import Flask
import random
import time

app = Flask(__name__)

def generate_random_number():
    time.sleep(10)
    return random.randint(100, 1000)


@app.route('/')
def generate_number():
    random_number = generate_random_number()
    return f"Generated number: {random_number}"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

