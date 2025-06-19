from flask import Flask, request, render_template, redirect, url_for
from flask_mail import Mail, Message  # For sending emails

app = Flask(__name__)

# Configuration for email (replace with your actual details)
app.config['MAIL_SERVER'] = 'your_mail_server.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = 'your_email@example.com'
app.config['MAIL_PASSWORD'] = 'your_email_password'

mail = Mail(app)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']

        # Basic validation
        if not name or not email or not message:
            return "Please fill in all the fields."
        if '@' not in email:
            return "Invalid email address."

        # Send email
        msg = Message("New Contact Form Submission",
                      sender=app.config['MAIL_USERNAME'],
                      recipients=['your_receiving_email@example.com'])
        msg.body = f"Name: {name}\nEmail: {email}\nMessage: {message}"
        try:
            mail.send(msg)
            return "Thank you for your message! We will get back to you soon."
        except Exception as e:
            return f"An error occurred while sending the email: {e}"

    return render_template('contact_form.html') # You might have your HTML in a template file

if __name__ == '__main__':
    app.run(debug=True)