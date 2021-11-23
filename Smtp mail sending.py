import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import sys

mesaj = MIMEMultipart()
mesaj["From"] = "ttalhanazli@gmail.com"
mesaj["To"] = "murat_mixs@hotmail.com"
mesaj["Subject"] = "Smtp mail gonderme"

yazi = "Pythondan gonderiyorum"

mesaj_govdesi = MIMEText(yazi,"plain")
mesaj.attach(mesaj_govdesi)

try:
    mail = smtplib.SMTP("smtp.gamil.com",587)
    mail.ehlo()
    mail.starttls()
    mail.login("ttalhanazli@gmail.com","tmww1183")
    mail.sendmail(mesaj["From"],mesaj["To"],mesaj.as_string())
    print("mail basariyla gonderildi")
    mail.close()

except:
    sys.stderr.write("Mail gonderilemedi")
    sys.stderr.flush()