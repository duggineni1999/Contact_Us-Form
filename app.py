from flask import Flask, render_template, request, redirect, url_for
from flask_mail import Mail, Message

app = Flask(__name__)

# Flask-Mail configuration
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USERNAME'] = 'saianirudhduggineni58@gmail.com'  # Your Gmail address
app.config['MAIL_PASSWORD'] = 'srgk ckze qrbo uqog'  # Your app-specific password

mail = Mail(app)

def is_valid_input(data):
    return data is not None and data.strip() != ""

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        full_name = request.form['fullname']
        subject_name = request.form['subject_name']
        sender_email = request.form['email_id']  # Sender's email from the form
        message_text = request.form['message_text']

        if not all(map(is_valid_input, [full_name, subject_name, sender_email, message_text])):
            return render_template("Contact_Us.html", error="Invalid input. Please fill in all required fields.")

        try:
            # Create email message
            message_body = f"Name: {full_name}\nEmail: {sender_email}\nMessage: {message_text}"
            subject = subject_name

            # Set the fixed recipient
            recipient_email = 'saianirudhd1999@gmail.com'

            msg = Message(subject=subject, recipients=[recipient_email], sender=sender_email)
            msg.body = message_body

            # Send the email
            mail.send(msg)

            # Redirect to a success page
            return redirect(url_for('success'))

        except Exception as e:
            print(f"An error occurred while sending the email: {e}")
            return render_template("Contact_Us.html", error="An error occurred while sending the email.")

    return render_template("Contact_Us.html")

@app.route("/success")
def success():
    return render_template("message.html")

if __name__ == '__main__':
    app.run(debug=True)
