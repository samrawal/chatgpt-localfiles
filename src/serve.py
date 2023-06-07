from flask import Flask, jsonify, request, send_file, Response
from flask_cors import CORS
import os
import sys
import utils

app = Flask(__name__)
CORS(app)  # This will enable CORS for all routes
base_path = ""


@app.route("/get_filenames", methods=["GET"])
def get_filenames():
    filepath = base_path + "/" + request.args.get("subdirectory_path", "")
    filepaths = utils.get_filenames(filepath)
    if len(filepaths) > 100:
        return (
            jsonify(
                {
                    "error": "More than 100 files in the directory provided. Please specify a subdirectory instead."
                }
            ),
            400,
        )
    return jsonify(filepaths)


@app.route("/list_directories", methods=["GET"])
def list_directories():
    path = base_path + "/" + request.args.get("path", "")
    directories = utils.list_directories(path)
    return jsonify(directories)


@app.route("/get_file_content", methods=["GET"])
def get_file_content():
    filepath = request.args.get("filepath")
    if not filepath:
        return jsonify({"error": "No filepath provided"}), 400

    try:
        content = utils.read_file(os.path.join(base_path, filepath))
    except Exception as e:
        return jsonify({"error": "Unable to read file", "details": str(e)}), 500

    return jsonify({"content": content})
@app.route("/.well-known/ai-plugin.json", methods=["GET"])
def plugin_manifest():
    host = request.headers["Host"]
    with open("ai-plugin.json") as f:
        text = f.read()
        return Response(text, mimetype="text/json")


@app.route("/openapi.yaml", methods=["GET"])
def openapi_spec():
    host = request.headers["Host"]
    with open("openapi.yaml") as f:
        text = f.read()
        # text = text.replace("PLUGIN_HOSTNAME", f"https://{host}")
        return Response(text, mimetype="text/yaml")


@app.route("/icon.png", methods=["GET"])
def get_icon():
    return send_file("stack_icon.png", mimetype="image/png")



def run_server(basepath=None):
    global base_path
    if basepath:
        base_path = basepath
    app.run(host="0.0.0.0", port=9900)


if __name__ == "__main__":
    basepath = sys.argv[1] if len(sys.argv) > 1 else os.getcwd()
    run_server(basepath)
