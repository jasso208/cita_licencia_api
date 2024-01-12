
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
        except Exception as e:            
            return str(e)
        return ""
    




    def plantillaEnvioToken(self,token):
        html = ''
        html = html + '<!DOCTYPE html>'
        html = html + '<html lang="en" xmlns="http://www.w3.org/1999/xhtml" xmlns:o="urn:schemas-microsoft-com:office:office">'
        html = html + '<head>'
        html = html + '  <meta charset="utf-8">'
        html = html + '  <meta name="viewport" content="width=device-width,initial-scale=1">'
        html = html + '           <meta name="x-apple-disable-message-reformatting">'
        html = html + '  <title></title>'
        html = html + '  <style>'
        html = html + '    table, td, div, h1, p {'
        html = html + '      font-family: Arial, sans-serif;'
        html = html + '    }'
        html = html + '    @media screen and (max-width: 530px) {'
        html = html + '      .unsub {'
        html = html + '        display: block;'
        html = html + '        padding: 8px;'
        html = html + '        margin-top: 14px;'
        html = html + '        border-radius: 6px;'
        html = html + '        background-color: #555555;'
        html = html + '        text-decoration: none !important;'
        html = html + '        font-weight: bold;'
        html = html + '      }'
        html = html + '      .col-lge {'
        html = html + '        max-width: 100% !important;'
        html = html + '      }'
        html = html + '    }'
        html = html + '    @media screen and (min-width: 531px) {'
        html = html + '      .col-sml {'
        html = html + '        max-width: 27% !important;'
        html = html + '      }'
        html = html + '      .col-lge {'
        html = html + '        max-width: 73% !important;'
        html = html + '      }'
        html = html + '    }'
        html = html + '  </style>'
        html = html + '</head>'
        html = html + '            <body style="margin:0;padding:0;word-spacing:normal;background-color:#939297;">'
        html = html + '  <div role="article" aria-roledescription="email" lang="en" style="text-size-adjust:100%;-webkit-text-size-adjust:100%;-ms-text-size-adjust:100%;background-color:#939297;">'
        html = html + '    <table role="presentation" style="width:100%;border:none;border-spacing:0;">'
        html = html + '      <tr>'
        html = html + '        <td align="center" style="padding:0;">'
        html = html + '          <!--[if mso]>'
        html = html + '          <table role="presentation" align="center" style="width:600px;">'
        html = html + '          <tr>'
        html = html + '          <td>'
        html = html + '          <![endif]-->'
        html = html + '          <table role="presentation" style="width:94%;max-width:600px;border:none;border-spacing:0;text-align:left;font-family:Arial,sans-serif;font-size:16px;line-height:22px;color:#363636;">'
        html = html + '            <tr>'
        html = html + '              <td style="padding:40px 30px 30px 30px;text-align:center;font-size:24px;font-weight:bold;">'
        html = html + '                '
        html = html + '              </td>'
        html = html + '            </tr>'
        html = html + '            <tr>'
        html = html + '              <td style="padding:30px;background-color:#ffffff;">'
        html = html + '                '
        html = html + '				<h1 style="margin-top:0;margin-bottom:16px;font-size:26px;line-height:32px;font-weight:bold;letter-spacing:-0.02em;text-align:center;">'
        html = html + '					¡¡Confirma tu correo electrónico!!'
        html = html + '				</h1>'
        html = html + '				'
        html = html + '              </td>'
        html = html + '            </tr>'
        html = html + '            '
        html = html + '            <tr>'
        html = html + '              <td style="padding:35px 30px 11px 30px;font-size:0;background-color:#ffffff;border-bottom:1px solid #f0f0f5;border-color:rgba(201,201,207,.35);">                '
        html = html + '                <div class="col-sml" style="display:inline-block;width:100%;max-width:145px;vertical-align:top;text-align:left;font-family:Arial,sans-serif;font-size:14px;color:#363636;">'
        html = html + '                  <img src="https://www.licenciainternacional.com.mx/wp-content/uploads/2018/05/logo-texturizado.png" width="115" alt="" style="width:115px;max-width:80%;margin-bottom:20px;">'
        html = html + '                </div>'
        html = html + '                <div class="col-lge" style="display:inline-block;width:100%;max-width:395px;vertical-align:top;padding-bottom:20px;font-family:Arial,sans-serif;font-size:16px;line-height:22px;color:#363636;">'
        html = html + '                  <p style="margin-top:0;margin-bottom:12px;">Ingresa el siguiente codigo de autenticación en el portal de citas.</p>'
        html = html + '                  <h3>' + token + '</h3>'
        html = html + '                </div>'
        html = html + '                <!--[if mso]>'
        html = html + '                </td>'
        html = html + '                </tr>'
        html = html + '                </table>'
        html = html + '                <![endif]-->'
        html = html + '              </td>'
        html = html + '            </tr>'
        html = html + '            '
        html = html + '            <tr>'
        html = html + '              <td style="padding:30px;background-color:#ffffff;">'
        html = html + '                <p style="margin:0;">Este mail fue enviado desde el servidor del sitio web de: <a href="https://www.licenciainternacional.com.mx/" style="color:#C0392B;text-decoration:underline;">Licencia Internacional ANA Automóvil Club de México A. C.</a>, no es necesario responder este mail.</p>'
        html = html + '                <p style="margin:0;">IMPORTANTE: El contenido de este correo electrónico y cualquier archivo adjunto son confidenciales.</p>'
        html = html + '        </td>'
        html = html + '            </tr>'
        html = html + '            <tr>'
        html = html + '              <td style="padding:30px;text-align:center;font-size:12px;background-color:#404040;color:#cccccc;">'
        html = html + '                <p style="margin:0 0 8px 0;"><a href="https://www.facebook.com/ANAAutomovilClub/?__cft__[0]=AZXA_oAvUYvQTlJRSFY7W6leymKll7lOmv1nsI6kAz7GYy7s64F1x85k11qUjyXlrAraO-R4RVNy9YSSCLLYvVwBLfKnI1WUDLRhc4F5NlG2Z6lMliBozntw3v0W3nojz1c&__tn__=-UC%2CP-R" style="text-decoration:none;"><img src="https://assets.codepen.io/210284/facebook_1.png" width="40" height="40" alt="f" style="display:inline-block;color:#cccccc;"></a> <a href="https://twitter.com/ANAAutomvilClub" style="text-decoration:none;"><img src="https://assets.codepen.io/210284/twitter_1.png" width="40" height="40" alt="t" style="display:inline-block;color:#cccccc;"></a></p>'
        html = html + '                <p style="margin:0;font-size:14px;line-height:20px;">&reg; Todos los Derechos reservados, 2022<br></p>'
        html = html + '              </td>'
        html = html + '            </tr>'
        html = html + '          </table>'
        html = html + '          <!--[if mso]>'
        html = html + '          </td>'
        html = html + '          </tr>'
        html = html + '          </table>'
        html = html + '          <![endif]-->'
        html = html + '        </td>'
        html = html + '      </tr>'
        html = html + '    </table>'
        html = html + '  </div>'
        html = html + '</body>'
        html = html + '</html>'


        html = html.replace("\xa1", "")
        html = html.replace("\xbf", "")
        html = html.replace("\xd1", "N")
        html = html.replace("\xdc", "U")
        html = html.replace("\xf1", "n")
        html = html.replace("\x0a", "\n")

        html = html.replace("\xe1", "a")		
        html = html.replace("\xe9", "e")		
        html = html.replace("\xed", "i")		
        html = html.replace("\xf3", "o")				
        html = html.replace("\xfa", "u")


        html = html.replace("\xc1", "A")		
        html = html.replace("\xc9", "E")		
        html = html.replace("\xcd", "I")		
        html = html.replace("\xd3", "O")				
        html = html.replace("\xda", "U")

        return html
    