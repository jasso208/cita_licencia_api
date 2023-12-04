
from django.conf import settings
import smtplib
import email.message

class Email():
    """
        Función para envio de email en formato html.
            Return:
                1: cuando el envio fue exitoso.
                0: cuando se presentaron errores para enviar correo.

    """
    def sendMail(self,body,email_cliente,asunto):
        try:
            server = smtplib.SMTP('smtp.gmail.com:587')
            msg = email.message.Message()
            msg['Subject'] = asunto

            msg['From']=settings.EMAIL_HOST_USER
            msg['To']=email_cliente
            password = settings.EMAIL_HOST_PASSWORD
            print(password)
            msg.add_header('Content-Type', 'text/html')
            msg.set_payload(body)
            s = smtplib.SMTP('smtp.gmail.com:587')
            s.starttls()
            # Login Credentials for sending the mail
            s.login(msg['From'], password)
            s.sendmail(msg['From'], [msg['To']], msg.as_string())
        except:
            return "0"
        return "1"


