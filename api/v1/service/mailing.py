from os import getenv

from fastapi_mail import ConnectionConfig, FastMail, MessageSchema

fm = FastMail(
    ConnectionConfig(
        MAIL_USERNAME = getenv("MAIL_USERNAME"),
        MAIL_PASSWORD = getenv("MAIL_PASSWORD"),
        MAIL_FROM = getenv("MAIL_DEFAULT_SENDER"),
        MAIL_SERVER = getenv("MAIL_SERVER", "smtp.gmail.com"),
        MAIL_PORT = getenv("MAIL_PORT", 465),
        MAIL_TLS = getenv("MAIL_USE_TLS", "False") == "True",
        MAIL_SSL = getenv("MAIL_USE_SSL", "True") == "True",
        USE_CREDENTIALS = getenv("MAIL_USE_CREDENTIALS", "True") == "True",
        VALIDATE_CERTS = getenv("MAIL_VALIDATE_CERTS", "True") == "True",
    )
)

async def send_email(email: str, subject: str, body: str):
    await fm.send_message(
        MessageSchema(
            subject = subject,
            recipients = [email],
            body = body,
            subtype = "html"
        )
    )
