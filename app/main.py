import os
from flask import Flask, jsonify

app = Flask(__name__)


tenant_id = os.getenv("TENANT_ID", "DEFAULT")


@app.route("/api", methods=["GET"])
def get_valor():
    return jsonify({"valor": tenant_id})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)