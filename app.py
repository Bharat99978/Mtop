from flask import Flask, request, jsonify
import subprocess

app = Flask(__name__)

@app.route('/run', methods=['POST'])
def run_code():
    code = request.json.get("code", "")
    try:
        # Execute the code and capture output
        result = subprocess.run(["python3", "-c", code], capture_output=True, text=True, check=True)
        output = result.stdout
    except subprocess.CalledProcessError as e:
        output = e.stderr  # Get error output if code fails

    return jsonify({"output": output})

if __name__ == '__main__':
    app.run(debug=True)
