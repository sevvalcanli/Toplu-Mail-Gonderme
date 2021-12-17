import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import sys
from PyQt5.QtWidgets import QWidget, QTextEdit, QLineEdit, QLabel, QPushButton, QHBoxLayout, QVBoxLayout, QApplication


class Pencere(QWidget):
    def __init__(self):
        super().__init__()  # Qwidget tüm özellikleri dahil eder

        self.init_ui()  # başlangıçta kullanıcı arayüzünü çalıştırır

    def init_ui(self):

        self.kullanici_adi_L = QLabel("Kullanıcı Adı:")
        self.kullanici_adi = QLineEdit()
        self.alici_L = QLabel("Alıcı: ")
        self.alici = QLineEdit()
        self.konu_L = QLabel("Konu:")
        self.konu = QLineEdit()
        self.yazi_L = QLabel("Mesaj: ")
        self.yazi = QTextEdit()
        self.gonder = QPushButton("GÖNDER")
        self.parola_L = QLabel("Şifre")
        self.parola = QLineEdit()
        self.parola.setEchoMode(QLineEdit.Password)

        v_box = QVBoxLayout()

        v_box.addWidget(self.alici_L)
        v_box.addWidget(self.alici)
        v_box.addWidget(self.konu_L)
        v_box.addWidget(self.konu)
        v_box.addWidget(self.yazi_L)
        v_box.addWidget(self.yazi)
        v_box.addStretch()
        v_box.addWidget(self.kullanici_adi_L)
        v_box.addWidget(self.kullanici_adi)
        v_box.addWidget(self.parola_L)
        v_box.addWidget(self.parola)
        v_box.addWidget(self.gonder)

        self.setWindowTitle("Mail Programı")
        self.setGeometry(400, 400, 400, 400)
        self.setLayout(v_box)
        self.show()

        self.gonder.clicked.connect(self.mail_gonder)

    def mail_gonder(self):
        mesaj = MIMEMultipart()  # mail yapısı oluşturuyor

        mesaj["From"] = self.kullanici_adi.text()
        mesaj["To"] = self.alici.text()
        mesaj["Subject"] = self.konu.text()

        mesaj_govdesi = MIMEText(self.yazi.toPlainText(), "plain")  # plain normal yazı stili

        mesaj.attach(mesaj_govdesi)

        try:
            mail = smtplib.SMTP("smtp.gmail.com", 587)  # gmail 587 portuna izin veriyor

            mail.ehlo()
            mail.starttls()  # bu ik fonksiyon zorunlu
            mail.login(self.kullanici_adi.text(), self.parola.text())
            mail.sendmail(mesaj["From"], mesaj["To"], mesaj.as_string())
            mail.close()
        except:
            sys.stderr.write("hata oluştu")
            sys.stderr.flush()


app = QApplication(sys.argv)
pencere = Pencere()
sys.exit(app.exec_())