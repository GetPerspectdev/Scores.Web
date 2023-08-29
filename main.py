import os
from flask import Flask, jsonify, request
from design_pattern import get_github

app = Flask(__name__)


@app.route("/hello", methods=["GET"])
def say_hello():
    return jsonify({"msg": "Hello from Flask"})

@app.route("/code/design/patterns", methods=["GET"])
def get_design_patterns():
    args = request.args
    github_repo = args['github_repo']
    dev_key = args.get('dev_key', '')
    branch = args.get('branch', 'main')
    debug = os.environ.get("DEBUG", False)
    print(args)
    return get_github(github_repo, dev_key, branch, debug)


if __name__ == "__main__":
    debug = os.environ.get("DEBUG", False)
    app.run(host="0.0.0.0", port=5050, debug=debug)