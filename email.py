import smtplib

from definitions import EMAIL_HOST, EMAIL_PASSWORD, EMAIL_PORT, EMAIL_USERNAME, PREMIUM_CHANNEL_INVITE_LINK


def send_confirmation_email(user_id, email):
    message = f"""
    Subject: Subscription Confirmation

    Dear User,

    Your subscription to our VIP service has been confirmed.

    Here is your invite link to the premium channel: {PREMIUM_CHANNEL_INVITE_LINK}

    Enjoy your VIP experience!

    Best regards,
    The Team
    """
    with smtplib.SMTP(EMAIL_HOST, EMAIL_PORT) as smtp:
        smtp.starttls()
        smtp.login(EMAIL_USERNAME, EMAIL_PASSWORD)
        smtp.sendmail(EMAIL_USERNAME, email, message)