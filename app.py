from  flask import Flask, render_template, request, jsonify
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

app = Flask(__name__)

EMAIL_REMETENTE = "wiltonsilva25@gmail.com"
EMAIL_SENHA_APP = "fmzn jdjs sqlm qjef"
EMAIL_DESTINO = "info@aislans-musikschule.de"

@app.route("/", methods =["GET", "POST"])
def formular():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        phone = request.form.get("phone")
        option = request.form.get("optionSelect")
        kurse = request.form.get("kurse")
        patient_name = request.form.get("patientName")
        for_whom = request.form.get("forWhom")
        baby_name = request.form.get("babyName")
        baby_age = request.form.get("babyAge")
        message = request.form.get("message")

        body_html = f"""
        <html>
           <head>
             <style>
               body {{
                 font-family: Arial, sans-serif;
                 background-color: #f7f7f7;
                 color: #333;
                 line-height: 1.6;
               }}
               .container {{
               background-color: #ffffff;
               padding: 20px;
               border-radius: 12px;
               box-shadow: 0 4px 12px rgba(0,0,0,0.1);
               max-width:600px;
               margin: auto;
               }}
               h2 {{
                 color: #4facfe;
                 text-align: center;
               }}
               h3 {{
                 color: #333;
                 border-bottom: 1px solid #ddd;
                 padding-bottom: 4px;
               }}
               p {{
                 margin: 6px
               }}
               .label {{
                 font-weight: bold;
                 color: #555;
               }}
               .footer {{
                 font-size: 0.9rem;
                 color: #888;
                 margin-top: 20px;
                 text-align: center;
               }}
              </style>
             </head>
             <body>
               <div class="container">
                 <h2>Neue Anmeldung für Aislans Musikschule</h2>

                 <h3>Persönliche Angaben</h3>
                 <p><span class="label">Name:</span> {name or '_'}</p>
                 <p><span class="label">E-mail:</span> {email or '_'}</p>
                 <p><span class="label">Handynummer:</span> {phone or '_'}</p>
                 
                 <h3>Gewählte Option</h3>
                 <p><span class="label">Option:</span> {option or '_'}</p>
                 <p><span class="label">Kurs:</span> {kurse or '_'}</p>

                 <h3>Patient / Kind</h3>
                 <p><span class="label">Name des Patienten:</span> {patient_name or '_'}</p>
                 <p><span class="label">Für wen:</span> {for_whom or '_'}</p>
                 <p><span class="label">Name des Kindes:</span> {baby_name or '_'}</p>
                 <p><span class="label">Alter des Kindes:</span> {baby_age or '_'}</p>

                 <h3>Nachricht</h3>
                 <p>{message or '_'}</p>

                 <div class="footer">
                   Bitte kontaktieren Sie den Teilnehmer zeitnah.
                </div>
               </div>
            </body>
        </html>
        """

        msg = MIMEMultipart()
        msg['From'] = EMAIL_REMETENTE
        msg['To'] = EMAIL_DESTINO
        msg['Subject'] = "Neues Anmeldeformular"
        msg.attach(MIMEText(body_html, 'html'))

        try: 
            server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
            server.login(EMAIL_REMETENTE, EMAIL_SENHA_APP)
            server.send_message(msg)
            server.quit()
            return jsonify({"status": "success"})
        except Exception as e:
            print("Fehler beim Senden der E-Mail", e)
            return jsonify({"status": "error"})
    else:
        return render_template("formular.html")
    
if __name__ == "__main__":
    app.run