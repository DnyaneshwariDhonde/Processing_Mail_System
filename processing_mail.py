

import smtplibgt
import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Function to send an email
def send_email(sender_email, receiver_email, subject, body, smtp_server, smtp_port, password):
    try:
        # Set up the MIME
        message = MIMEMultipart()
        message['From'] = sender_email
        message['To'] = receiver_email
        message['Subject'] = subject
        message.attach(MIMEText(body, 'plain'))
        
        # Set up the server
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()  # Use TLS for security
        server.login(sender_email, password)
        
        # Send email
        text = message.as_string()
        server.sendmail(sender_email, receiver_email, text)
        server.quit()
        print("Email sent successfully!")
    except Exception as e:
        print(f"Error: {e}")

# Function to schedule the email
def schedule_email(send_time, sender_email, receiver_email, subject, body, smtp_server, smtp_port, password):
    # Get the current time
    current_time = time.time()
    
    # Calculate the time difference in seconds
    time_difference = send_time - current_time
    if time_difference > 0:
        print(f"Email will be sent in {time_difference} seconds.")
        time.sleep(time_difference)  # Wait until the specified send time
        send_email(sender_email, receiver_email, subject, body, smtp_server, smtp_port, password)
    else:
        print("The send time has already passed!")

# Example usage

# Replace these variables with your details
sender_email = "youremail@example.com"
receiver_email = "receiveremail@example.com"
subject = "Test Email"
body = "This is a test email sent at a scheduled time."
smtp_server = "smtp.gmail.com"
smtp_port = 587  # For Gmail
password = "yourpassword"  # Use app password if using Gmail

# Set a time in the future for when to send the email (e.g., 10 seconds from now)
send_time = time.time() + 10  # 10 seconds from now

# Schedule the email
schedule_email(send_time, sender_email, receiver_email, subject, body, smtp_server, smtp_port, password)
