from flask import Flask, render_template, request, send_file
from stego import encrypt_image, decrypt_image
import os

# 1️⃣ Create Flask app FIRST
app = Flask(__name__)

# 2️⃣ Create folders
UPLOADS = "uploads"
OUTPUTS = "outputs"
os.makedirs(UPLOADS, exist_ok=True)
os.makedirs(OUTPUTS, exist_ok=True)


# 3️⃣ Home page
@app.route("/")
def index():
    return render_template("index.html")


# 4️⃣ Encode route
@app.route("/encode", methods=["GET", "POST"])
def encode():
    if request.method == "POST":
        img = request.files["image"]
        msg = request.form["message"]
        pwd = request.form["password"]

        input_path = os.path.join(UPLOADS, img.filename)
        output_path = os.path.join(OUTPUTS, "encrypted.png")

        img.save(input_path)
        encrypt_image(input_path, msg, pwd, output_path)

        return send_file(output_path, as_attachment=True)

    return render_template("encode.html")


# 5️⃣ Decode route
@app.route("/decode", methods=["GET", "POST"])
def decode():
    if request.method == "POST":
        img = request.files["image"]
        pwd = request.form["password"]

        input_path = os.path.join(UPLOADS, img.filename)
        img.save(input_path)

        message = decrypt_image(input_path, pwd)

        if message is None:
            return "Wrong password ❌"

        return f"Secret Message: {message}"

    return render_template("decode.html")


# 6️⃣ Run server
if __name__ == "__main__":
    app.run(debug=True)
