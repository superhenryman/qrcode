from flask import Flask, request, render_template, send_file
import qrcode
from io import BytesIO

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        data = request.form.get("data")  # Get data from the form
        if data:
            # Generate the QR code
            qr = qrcode.QRCode(version=1, box_size=10, border=5)
            qr.add_data(data)
            qr.make(fit=True)

            img = qr.make_image(fill_color="black", back_color="white")

            # Save QR code to an in-memory file
            buffer = BytesIO()
            img.save(buffer, format="PNG")
            buffer.seek(0)

            return send_file(buffer, mimetype="image/png", as_attachment=True, download_name="qrcode.png")
    
    return render_template("index.html")  # Render the HTML form

if __name__ == "__main__":
    app.run(debug=True)

def generate():
    qr = qr.QRCode(version=1, box_size=10, border=5)

    data = input("Please write what you want the QRCode to be: ").strip()

    qr.add_data(data)

    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")

    img.save("qr.code.png")