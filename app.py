from flask import Flask, render_template, request
import qrcode
from datetime import date
import os

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Collect form data
        patient_name = request.form["name"]
        patient_age = request.form["age"]
        patient_allergies = request.form["allergies"].split()
        patient_bloodgrp = request.form["bloodgrp"]
        main_contact = request.form["main_contact"]
        known_diseases = request.form["diseases"].split()
        emergency_contact = request.form["emergency_contact"]
        last_updated = date.today()

        # Prepare data for QR
        data = f"""Patient's name: {patient_name}
Patient's age: {patient_age}
Patient's allergies: {patient_allergies}
Patient's blood group: {patient_bloodgrp}
Main contact number: {main_contact}
Known diseases: {known_diseases}
Emergency contact number: {emergency_contact}
Last updated: {last_updated}
"""

        # Ensure the static folder exists
        os.makedirs("static", exist_ok=True)

        # Generate and save QR code
        qr_img = qrcode.make(data)
        qr_img.save(os.path.join("static", "qr.png"))

        return render_template("index.html", qr_generated=True)

    return render_template("index.html", qr_generated=False)

if __name__ == "__main__":
    app.run(debug=True)
