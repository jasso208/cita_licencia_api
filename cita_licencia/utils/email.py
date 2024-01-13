
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
    html = '''<!DOCTYPE html>
<html lang="en" xmlns="http://www.w3.org/1999/xhtml" xmlns:o="urn:schemas-microsoft-com:office:office">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width,initial-scale=1">
           <meta name="x-apple-disable-message-reformatting">
  <title></title>
  <style>
    table, td, div, h1, p {
      font-family: Arial, sans-serif;
    }
    @media screen and (max-width: 530px) {
      .unsub {
        display: block;
        padding: 8px;
        margin-top: 14px;
        border-radius: 6px;
        background-color: #555555;
        text-decoration: none !important;
        font-weight: bold;
      }
      .col-lge {
        max-width: 100% !important;
      }
    }
    @media screen and (min-width: 531px) {
      .col-sml {
        max-width: 27% !important;
      }
      .col-lge {
        max-width: 73% !important;
      }
    }
  </style>
</head>
<body style="margin:0;padding:0;word-spacing:normal;background-color:#939297;">
  <div role="article" aria-roledescription="email" lang="en" style="text-size-adjust:100%;-webkit-text-size-adjust:100%;-ms-text-size-adjust:100%;background-color:#939297;">
    <table role="presentation" style="width:100%;border:none;border-spacing:0;">
      <tr>
        <td align="center" style="padding:0;">
          <!--[if mso]>
          <table role="presentation" align="center" style="width:600px;">
          <tr>
          <td>
          <![endif]-->
          <table role="presentation" style="width:94%;max-width:600px;border:none;border-spacing:0;text-align:left;font-family:Arial,sans-serif;font-size:16px;line-height:22px;color:#363636;">
            <tr>
              <td style="padding:40px 30px 30px 30px;text-align:center;font-size:24px;font-weight:bold;">
                
              </td>
            </tr>
            <tr>
              <td style="padding:30px;background-color:#ffffff;">
                
				<h1 style="margin-top:0;margin-bottom:16px;font-size:26px;line-height:32px;font-weight:bold;letter-spacing:-0.02em;text-align:center;">
					¡¡Confirma tu correo electrónico!!
				</h1>
				
              </td>
            </tr>
            
            <tr>
              <td style="padding:35px 30px 11px 30px;font-size:0;background-color:#ffffff;border-bottom:1px solid #f0f0f5;border-color:rgba(201,201,207,.35);">                
                <div class="col-sml" style="display:inline-block;width:100%;max-width:145px;vertical-align:top;text-align:left;font-family:Arial,sans-serif;font-size:14px;color:#363636;">
                  <img src="https://www.licenciainternacional.com.mx/wp-content/uploads/2018/05/logo-texturizado.png" width="115" alt="" style="width:115px;max-width:80%;margin-bottom:20px;">
                </div>
                <div class="col-lge" style="display:inline-block;width:100%;max-width:395px;vertical-align:top;padding-bottom:20px;font-family:Arial,sans-serif;font-size:16px;line-height:22px;color:#363636;">
                  <p style="margin-top:0;margin-bottom:12px;">Ingresa el siguiente codigo de autenticación en el portal de citas.</p>
                  <h3> {} </h3>
                </div>
                <!--[if mso]>
                </td>
                </tr>
                </table>
                <![endif]-->
              </td>
            </tr>
            
            <tr>
              <td style="padding:30px;background-color:#ffffff;">
                <p style="margin:0;">Este mail fue enviado desde el servidor del sitio web de: <a href="https://www.licenciainternacional.com.mx/" style="color:#C0392B;text-decoration:underline;">Licencia Internacional ANA Automóvil Club de México A. C.</a>, no es necesario responder este mail.</p>
                <p style="margin:0;">IMPORTANTE: El contenido de este correo electrónico y cualquier archivo adjunto son confidenciales.</p>
        </td>
            </tr>
            <tr>
              <td style="padding:30px;text-align:center;font-size:12px;background-color:#404040;color:#cccccc;">
                <p style="margin:0 0 8px 0;"><a href="https://www.facebook.com/ANAAutomovilClub/?__cft__[0]=AZXA_oAvUYvQTlJRSFY7W6leymKll7lOmv1nsI6kAz7GYy7s64F1x85k11qUjyXlrAraO-R4RVNy9YSSCLLYvVwBLfKnI1WUDLRhc4F5NlG2Z6lMliBozntw3v0W3nojz1c&__tn__=-UC%2CP-R" style="text-decoration:none;"><img src="https://assets.codepen.io/210284/facebook_1.png" width="40" height="40" alt="f" style="display:inline-block;color:#cccccc;"></a> <a href="https://twitter.com/ANAAutomvilClub" style="text-decoration:none;"><img src="https://assets.codepen.io/210284/twitter_1.png" width="40" height="40" alt="t" style="display:inline-block;color:#cccccc;"></a></p>
                <p style="margin:0;font-size:14px;line-height:20px;">&reg; Todos los Derechos reservados, 2022<br></p>
              </td>
            </tr>
          </table>
          <!--[if mso]>
          </td>
          </tr>
          </table>
          <![endif]-->
        </td>
      </tr>
    </table>
  </div>
</body>
</html>
'''.format(token)

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

def plantillaConfirmacionCita(self,cita):
    html = '''
<!DOCTYPE html>
<html lang="en" xmlns="http://www.w3.org/1999/xhtml" xmlns:o="urn:schemas-microsoft-com:office:office">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width,initial-scale=1">
  <meta name="x-apple-disable-message-reformatting">
  <title></title>
  <style>
    table, td, div, h1, p {
      font-family: Arial, sans-serif;
    }
    @media screen and (max-width: 530px) {
      .unsub {
        display: block;
        padding: 8px;
        margin-top: 14px;
        border-radius: 6px;
        background-color: #555555;
        text-decoration: none !important;
        font-weight: bold;
      }
      .col-lge {
        max-width: 100% !important;
      }
    }
    @media screen and (min-width: 531px) {
      .col-sml {
        max-width: 27% !important;
      }
      .col-lge {
        max-width: 73% !important;
      }
    }
  </style>
</head>
<body style="margin:0;padding:0;word-spacing:normal;background-color:#939297;">
  <div role="article" aria-roledescription="email" lang="en" style="text-size-adjust:100%;-webkit-text-size-adjust:100%;-ms-text-size-adjust:100%;background-color:#939297;">
    <table role="presentation" style="width:100%;border:none;border-spacing:0;">
      <tr>
        <td align="center" style="padding:0;">
          <!--[if mso]>
          <table role="presentation" align="center" style="width:600px;">
          <tr>
          <td>
          <![endif]-->
          <table role="presentation" style="width:94%;max-width:600px;border:none;border-spacing:0;text-align:left;font-family:Arial,sans-serif;font-size:16px;line-height:22px;color:#363636;">
            <tr>
              <td style="padding:40px 30px 30px 30px;text-align:center;font-size:24px;font-weight:bold;">
                
              </td>
            </tr>
            <tr>
              <td style="padding:30px;background-color:#ffffff;">
                <h1 style="margin-top:0;margin-bottom:16px;font-size:26px;line-height:32px;font-weight:bold;letter-spacing:-0.02em;text-align:center;">¡¡Felicidades, ya diste el primer paso!!</h1>
                <p style="margin:0;">Hola!! {} {} {} Se ha generado correctamente tu cita para el tramite de Licencia Internacional, del sitio web <a href="https://www.licenciainternacional.com.mx/" style="color:#C0392B;text-decoration:underline;">Licencia Internacional ANA Automóvil Club de México A. C.</a></p>
              </td>
            </tr>
            
            <tr>
              <td style="padding:35px 30px 11px 30px;font-size:0;background-color:#ffffff;border-bottom:1px solid #f0f0f5;border-color:rgba(201,201,207,.35);">
                <!--[if mso]>
                <table role="presentation" width="100%">
                <tr>
                <td style="width:145px;" align="left" valign="top">
                <![endif]-->
                <div class="col-sml" style="display:inline-block;width:100%;max-width:145px;vertical-align:top;text-align:left;font-family:Arial,sans-serif;font-size:14px;color:#363636;">
                  <img src="https://www.licenciainternacional.com.mx/wp-content/uploads/2018/05/logo-texturizado.png" width="115" alt="" style="width:115px;max-width:80%;margin-bottom:20px;">
                </div>
                <!--[if mso]>
                </td>
                <td style="width:395px;padding-bottom:20px;" valign="top">
                <![endif]-->
                <div class="col-lge" style="display:inline-block;width:100%;max-width:395px;vertical-align:top;padding-bottom:20px;font-family:Arial,sans-serif;font-size:16px;line-height:22px;color:#363636;">
                  <p style="margin-top:0;margin-bottom:12px;">Si recibiste este mail es por que generaste una cita y tu informacion nos llego correctamente.</p>
                  <p>Es importante que cuente con la siguiente información:</p>

                  <p>La Licencia Internacional tiene de vigencia de un año no hay por un periodo mayor, si su licencia mexicana vence antes, su Licencia Internacional tendrá  esta misma fecha de vencimiento.</p>

                  <p> La Licencia Internacional es aceptada en más de 180 países, excepto ASIA (China, Japón, Tailandia, Corea, Filipinas, Malasia, Singapur, Laos, Vietnam, Indonesia) IRLANDA, BOLIVIA Y PARAGUAY. Si usted viaja a alguno de estos países, puedes cancelar su cita o puedes solicitar mas informacion acerca  del trámite.</p>

                  <p> Para el trámite del PIC debe presentar una copia a color de:</p>
                     
                     <br> PASAPORTE CON VIGENCIA MINIMA DE UN AÑO
                     <br>LICENCIA MEXICANA FISICA (NO DIGITAL)CON VIGENCIA MINIMA DE UN AÑO (AMBOS LADOS)
                     <br>INE o FM (AMBOS LADOS) VIGENTE
                     <br>COMPROBANTE DE DOMICILIO RECIENTE (Teléfono, Agua, Luz, Predial, Etc. Excepto cuantas bancarias
                     <br>1 FOTOGRAFIA TAMAÑO PASAPORTE A COLOR (4.5 x 3.5)
                     <br>Si requiere factura deberá presentar su Constancia de Situación Fiscal actualizada
                     
                     <p>El costo es de $1,300.00 + IVA, si requiere factura.</p>

                     <p>El pago es en efectivo a la entrega de su PIC y tiene un año de vigencia.</p>
                     
                     <p>La Dirección es: Durango 81-402, Col. Roma Norte, CDMX</p>

                     <p>Saludos y seguimos a sus órdenes.</p>


                  <p style="margin-top:0;margin-bottom:18px;">Si tienes alguna duda puedes comunicarte con nosotros, en nuesgtros diferentes medios: WhatsApp, Linea telefonnica al: 5555337176 o enviándonos un mail</p>
                  <p style="margin:0;"><a href="mailto:info@licenciainternacional.com.mx" style="background: #ff3884; text-decoration: none; padding: 10px 25px; color: #ffffff; border-radius: 4px; display:inline-block; mso-padding-alt:0;text-underline-color:#ff3884"><!--[if mso]><i style="letter-spacing: 25px;mso-font-width:-100%;mso-text-raise:20pt">&nbsp;</i><![endif]--><span style="mso-text-raise:10pt;font-weight:bold;">Enviar Mail</span><!--[if mso]><i style="letter-spacing: 25px;mso-font-width:-100%">&nbsp;</i><![endif]--></a></p>
                </div>
                <!--[if mso]>
                </td>
                </tr>
                </table>
                <![endif]-->
              </td>
            </tr>
            
            <tr>
              <td style="padding:30px;background-color:#ffffff;">
                <p style="margin:0;">Este mail fue enviado desde el servidor del sitio web de: <a href="https://www.licenciainternacional.com.mx/" style="color:#C0392B;text-decoration:underline;">Licencia Internacional ANA Automóvil Club de México A. C.</a>, no es necesario responder este mail.</p>
                <p style="margin:0;">IMPORTANTE: El contenido de este correo electrónico y cualquier archivo adjunto son confidenciales.</p>
        </td>
            </tr>
            <tr>
              <td style="padding:30px;text-align:center;font-size:12px;background-color:#404040;color:#cccccc;">
                <p style="margin:0 0 8px 0;"><a href="https://www.facebook.com/ANAAutomovilClub/?__cft__[0]=AZXA_oAvUYvQTlJRSFY7W6leymKll7lOmv1nsI6kAz7GYy7s64F1x85k11qUjyXlrAraO-R4RVNy9YSSCLLYvVwBLfKnI1WUDLRhc4F5NlG2Z6lMliBozntw3v0W3nojz1c&__tn__=-UC%2CP-R" style="text-decoration:none;"><img src="https://assets.codepen.io/210284/facebook_1.png" width="40" height="40" alt="f" style="display:inline-block;color:#cccccc;"></a> <a href="https://twitter.com/ANAAutomvilClub" style="text-decoration:none;"><img src="https://assets.codepen.io/210284/twitter_1.png" width="40" height="40" alt="t" style="display:inline-block;color:#cccccc;"></a></p>
                <p style="margin:0;font-size:14px;line-height:20px;">&reg; Todos los Derechos reservados, 2022<br></p>
              </td>
            </tr>
          </table>
          <!--[if mso]>
          </td>
          </tr>
          </table>
          <![endif]-->
        </td>
      </tr>
    </table>
  </div>
</body>
</html>
'''.format(cita.cliente.nombre, cita.cliente.apellido_p, cita.cliente.apellido_m)
    
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
