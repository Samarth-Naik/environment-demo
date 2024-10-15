from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def display_env_var():
    # Get the value of an environment variable (e.g., "MY_ENV_VAR")
    env_var = os.getenv('MY_ENV_VAR')
    return f'The value of MY_ENV_VAR is: {env_var}'

if __name__ == '__main__':
    app.run(debug=True)
