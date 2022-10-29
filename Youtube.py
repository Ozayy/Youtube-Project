
import time

from pytube import YouTube
from pytube import Playlist
from PyQt5.QtGui import QPalette
from PyQt5.QtGui import QColor
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QApplication, QFileDialog
from untitled import Ui_MainWindow
from PyQt5 import  QtCore
import os
from PyQt5.QtWidgets import QMainWindow, QMessageBox
from proglog import ProgressBarLogger

from threading import Thread

from PyQt5.QtCore import  pyqtSignal
from PyQt5.QtCore import QPoint, QTimer
from PyQt5 import QtWidgets
import sqlite3
import moviepy.editor as mpe



class MyBarLogger(ProgressBarLogger):
    def __init__(self, main):
        super(MyBarLogger, self).__init__()
        self.sub = main


    def callback(self, **changes):

        for (parameter, value) in changes.items():
            print ('Parameter %s is now %s' % (parameter, value))
    def bars_callback(self, bar, attr, value ,old_value=None):


        percentage = int((value / self.bars[bar]['total']) * 100)
        self.sub.ui.progressBar.show()
        self.sub.ui.progressBar.setValue(percentage)






class Main(QMainWindow):
    signal_mesaj_video_indirme = pyqtSignal()
    signal_Msj = pyqtSignal()
    signal_listeye_yazma = pyqtSignal(str)
    signal_Msj_playlist = pyqtSignal()
    signal_Msj_4k_playlist = pyqtSignal()
    signal_Msj_file = pyqtSignal()
    signal_combobox = pyqtSignal()
    def __init__(self ,*args ,**kwargs):
        super(Main, self).__init__(*args ,**kwargs)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


        self.connect = sqlite3.connect('C:/Users/win10/Desktop/Klasor/deneme.db')
        self.im = self.connect.cursor()

        tablo = """CREATE TABLE IF NOT EXISTS Bilgiler(id INTEGER PRIMARY KEY AUTOINCREMENT,UserName VARHCAR(32),Password VARHCAR(32),is_active VARHCAR(32))"""
        self.im.execute(tablo)


        self.ui.pushButton.clicked.connect(self.home_page)


        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.ui.browse_konum.clicked.connect(self.dosya_yukle)
        self.ui.download_button.clicked.connect(self.videoYukle_Th)
        self.ui.download_button.clicked.connect(self.videoYuklee)

        self.ui.combobox_secim.activated.connect(self.deneme_)
        self.ui.mp4_radio.toggled.connect(self.veri_cek)
        self.ui.mp3_radio.toggled.connect(self.deneme_2)
        self.ui.combobox_secim.setEnabled(False)

        self.video_yuklenme = False
        self.signal_listeye_yazma.connect(self.listeye_yaz)


        self.signal_combobox.connect(self.combobox_thread)
        self.signal_Msj.connect(self.msj_goster)
        self.signal_Msj_playlist.connect(self.Mesaj_playlist)
        self.signal_Msj_4k_playlist.connect(self.mesaj_playlist_4k)
        self.signal_mesaj_video_indirme.connect(self.video_bittimi)
        self.signal_Msj_file.connect(self.dosya_hatasi)
        self.ui.progressBar.hide()
        self.ui.tableWidget.currentItemChanged.connect(self.doldur)
        self.ui.login_button.clicked.connect(self.ekranlara_yonlendirme)
        self.ui.table_goback.clicked.connect(self.ana_sayfa_geri)
        self.ui.table_approve.clicked.connect(self.tablo_duzenle)
        self.ui.add_table.clicked.connect(self.addData)
        self.ui.update_table.clicked.connect(self.updateData)
        self.ui.delete_table.clicked.connect(self.deleteData)
        self.ui.refresh_button.clicked.connect(self.temizle)
        self.ui.alanlari_temizle.clicked.connect(self.clear)

        self.ui.close.clicked.connect(lambda: self.close())
        self.ui.icona.clicked.connect(lambda: self.showMinimized())

        self.ui.deneme1.clicked.connect(self.a)
        self.setFixedSize(self.size())
        self.dragPos = self.pos()
        self.ui.stackedWidget.setCurrentIndex(0)




        def mouseMoveEvent(event):
            delta = QPoint(self.pos() + event.globalPos() - self.dragPos)
            self.move(self.pos() + event.globalPos() - self.dragPos)
            self.dragPos = event.globalPos()
            event.accept()

        self.ui.frame.mouseMoveEvent = mouseMoveEvent
        self.ui.link_line.setPlaceholderText("Lütfen link giriniz")

        self.timer = QTimer()
        self.timer.timeout.connect(self.videoYukle_Th)

        self.ui.mp4_radio.hide()
        self.ui.mp3_radio.hide()
        self.ui.comboBox.hide()

        self.ui.link_line.textChanged.connect(self.link_kontrol)
        self.ui.listWidget.hide()
    def home_page(self):
        self.ui.stackedWidget.setCurrentIndex(0)
        self.ui.User_login.clear()
        self.ui.Password_login.clear()

    def clear(self):
        self.ui.user_id_line.clear()
        self.ui.user_table_line.clear()
        self.ui.user_password_line.clear()

    def deneme_(self):
        if self.ui.combobox_secim.currentText() == "Playlist":
            self.ui.mp3_radio.hide()
            self.ui.mp4_radio.show()



        elif self.ui.combobox_secim.currentText() == "Tekvideo":
            self.ui.mp4_radio.show()
            self.ui.mp3_radio.show()




    def veri_cek(self):
        Thread(target=self.deneme_1,daemon=True).start()
    def combobox_thread(self):
        self.ui.comboBox.addItems(self.sorted_list)
        self.ui.comboBox.setDuplicatesEnabled(False)
        self.ui.comboBox.show()

    def deneme_1(self):
        url = self.ui.link_line.text()
        self.mp4_yukle = YouTube(url)

        self.streams = set()
        self.stream_list = []

        for stream in self.mp4_yukle.streams.filter(type="video"):
            #print(self.streams)

            self.streams.add(stream.resolution)

        for i in self.streams:
            self.stream_list.append(str(i))

        if self.stream_list.count("None"):
            self.stream_list.remove("None")
        self.sorted_list = sorted(self.stream_list, key=lambda x: int(x[:-1]) if x != "None" else int())

        self.ui.comboBox.clear()
        self.signal_combobox.emit()




    def deneme_2(self):
        self.ui.comboBox.hide()

    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()

    def videoYukle_Th(self):


        Thread(target=self.videoYukle, daemon=True).start()


    def dosya_hatasi(self):
        messagebox = QMessageBox()
        messagebox.setIcon(QMessageBox.Warning)
        messagebox.setWindowTitle("Dosya Hatası")
        messagebox.setText(
            "Lütfen ilgili klasörünüzdeki yarım kalmış olan mp3 ve mp4 dosyalarınızı silin,öyle indirin")
        messagebox.setStandardButtons(QMessageBox.Ok)
        buton_ok = messagebox.button(QMessageBox.Ok)
        buton_ok.setText("Tamam")
        messagebox.exec_()

    def video_bittimi(self):
        QMessageBox.information(self, 'Videolar indirildi', 'Playlist videolarının tamamı indirildi')


    def Mesaj_playlist(self):
        messagebox = QMessageBox()
        messagebox.setIcon(QMessageBox.Warning)
        messagebox.setWindowTitle("Playlist Hatası")
        messagebox.setText("Üzgünüm,Playlist bulunamadı")
        messagebox.setStandardButtons(QMessageBox.Ok)
        buton_ok = messagebox.button(QMessageBox.Ok)
        buton_ok.setText("Tamam")
        messagebox.exec_()

    def mesaj_playlist_4k(self):
        messagebox = QMessageBox()
        messagebox.setIcon(QMessageBox.Warning)
        messagebox.setWindowTitle("Playlist hatası")
        messagebox.setText(
            "😰 Üzgünüm,bu formatlarda playlist indirmeye izin vermiyor")
        messagebox.setStandardButtons(QMessageBox.Ok)
        buton_ok = messagebox.button(QMessageBox.Ok)
        buton_ok.setText("Tamam")
        messagebox.exec_()

    def msj_goster(self):
        messagebox = QMessageBox()
        messagebox.setIcon(QMessageBox.Warning)
        messagebox.setWindowTitle("Mp3 Hatası")
        messagebox.setText(
            "Bir mp3 dosyasını iki kere indiremezsiniz")
        messagebox.setStandardButtons(QMessageBox.Ok)
        buton_ok = messagebox.button(QMessageBox.Ok)
        buton_ok.setText("Tamam")
        messagebox.exec_()

    def videoYuklee(
            self):  # aşagıdakı fonksıyon videoYukle threadle calıstıgı ıcın messagebox hata verdırdı bunun yerıne başka bir fonksıyonla çağırdık
        if self.ui.label_4.text() == "":
            messagebox = QMessageBox()
            messagebox.setIcon(QMessageBox.Warning)
            messagebox.setWindowTitle("Hedef dizini")
            messagebox.setText(
                "Lütfen hedef dizinini boş bırakma")
            messagebox.setStandardButtons(QMessageBox.Ok)
            buton_ok = messagebox.button(QMessageBox.Ok)
            buton_ok.setText("Tamam")
            messagebox.exec_()
        elif self.ui.link_line.text() == "":
            messagebox = QMessageBox()
            messagebox.setIcon(QMessageBox.Warning)
            messagebox.setWindowTitle("Link hatası")
            messagebox.setText(
                "Lütfen link alanını boş bırakma")
            messagebox.setStandardButtons(QMessageBox.Ok)
            buton_ok = messagebox.button(QMessageBox.Ok)
            buton_ok.setText("Tamam")
            messagebox.exec_()
        elif self.ui.mp4_radio.isChecked() == False and self.ui.mp3_radio.isChecked() == False:
            messagebox = QMessageBox()
            messagebox.setIcon(QMessageBox.Warning)
            messagebox.setWindowTitle("Format Hatası")
            messagebox.setText(
                "Lütfen mp4 veya mp3 seçeneklerini seçiniz")
            messagebox.setStandardButtons(QMessageBox.Ok)
            buton_ok = messagebox.button(QMessageBox.Ok)
            buton_ok.setText("Tamam")
            messagebox.exec_()
        elif self.ui.label_9.text() == "":
            messagebox = QMessageBox()
            messagebox.setIcon(QMessageBox.Warning)
            messagebox.setWindowTitle("Hedef dizini hatası")
            messagebox.setText(
                "Lütfen hedef dizinini boş bırakma")
            messagebox.setStandardButtons(QMessageBox.Ok)
            buton_ok = messagebox.button(QMessageBox.Ok)
            buton_ok.setText("Tamam")
            messagebox.exec_()
            self.ui.progressBar.hide()

    def temizle(self):
        self.ui.listWidget.clear()
        self.ui.link_line.clear()
        self.ui.label_9.clear()
        self.ui.combobox_secim.setCurrentIndex(-1)

        #self.ui.mp4_radio.setEnabled(True)
        #self.ui.mp3_radio.setEnabled(True)

        self.ui.comboBox.clear()
        self.ui.comboBox.hide()
        self.ui.progressBar.setValue(0)
        self.ui.progressBar.hide()
        self.ui.mp4_radio.setCheckable(False)
        self.ui.mp3_radio.setCheckable(False)

        # self.ui.progressBar.setMinimum(0)
        # self.ui.progressBar.resetFormat()



    def link_kontrol(self):
        if not self.ui.link_line.text().startswith("https://www.youtube.com/"):
            messagebox = QMessageBox()
            messagebox.setIcon(QMessageBox.Warning)
            messagebox.setWindowTitle("Url hatası")
            messagebox.setText(
                "Lütfen geçerli youtube url adresi girin")
            messagebox.setStandardButtons(QMessageBox.Ok)
            buton_ok = messagebox.button(QMessageBox.Ok)
            buton_ok.setText("Tamam")
            messagebox.exec_()
        self.ui.mp4_radio.setCheckable(True)
        self.ui.mp3_radio.setCheckable(True)

        self.ui.combobox_secim.setEnabled(True)


        if self.ui.link_line.text() == "":

            pass

        else:

            pass

    def listeye_yaz(self, video_ismi):
        self.ui.listWidget.addItem(video_ismi)

    def ekranlara_yonlendirme(self):



        UserName = self.ui.User_login.text()
        passWord = self.ui.Password_login.text()
        is_active = self.ui.comboBox_2.currentText()

        if UserName == "" or passWord == "":
            messagebox = QMessageBox()
            messagebox.setIcon(QMessageBox.Warning)
            messagebox.setWindowTitle("Lütfen boş bırakmayın")
            messagebox.setText(
                "Username veya password boş bırakılmamalı")
            messagebox.setStandardButtons(QMessageBox.Ok)
            buton_ok = messagebox.button(QMessageBox.Ok)
            buton_ok.setText("Tamam")
            messagebox.exec_()
        read_1 = self.im.execute(
            """SELECT * FROM Bilgiler Where UserName = ? and Password = ? and is_active = "Aktif"  """,
            (UserName, passWord))
        rows_1 = read_1.fetchall()

        if rows_1:
            self.ui.stackedWidget.setCurrentIndex(2)

        read_1 = self.im.execute(
            """SELECT * FROM Bilgiler Where UserName = ? and Password = ? and is_active = "Pasif"  """,
            (UserName, passWord))
        rows_1 = read_1.fetchall()
        if rows_1:
            messagebox = QMessageBox()
            messagebox.setIcon(QMessageBox.Warning)
            messagebox.setWindowTitle("Hesabınız pasif")
            messagebox.setText("Hesabınız pasif durumda")
            messagebox.setStandardButtons(QMessageBox.Ok)
            buton_ok = messagebox.button(QMessageBox.Ok)
            buton_ok.setText("Tamam")
            messagebox.exec_()
        else:
            pass
        read_3 = self.im.execute("SELECT * FROM Bilgiler WHERE UserName = ? and Password = ?", (UserName, passWord))
        rows_2 = read_3.fetchall()

        if len(rows_2) < 1:
            messagebox = QMessageBox()
            messagebox.setIcon(QMessageBox.Warning)
            messagebox.setWindowTitle("Hatalı Giriş")
            messagebox.setText("Böyle bir kullanıcı bulunamadı")
            messagebox.setStandardButtons(QMessageBox.Ok)
            buton_ok = messagebox.button(QMessageBox.Ok)
            buton_ok.setText("Tamam")
            messagebox.exec_()
        else:
            pass
        read = self.im.execute("""SELECT * FROM Bilgiler WHERE UserName=? and Password=? """, (UserName, passWord)).fetchall()
        for reads in read:
            user = str(reads[1])
            pasw = str(reads[2])

            if user == "Admin" and pasw == "12345":
                self.ui.stackedWidget.setCurrentIndex(1)






    def dosya_yukle(self):
        file_dialog = QFileDialog()
        self.file_dialog_yukle = file_dialog.getExistingDirectory(self, "Select")  # dosyayı seçtik
        self.ui.label_9.setText(self.file_dialog_yukle)  # labele yazdırdık

    def ana_sayfa_geri(self):
        self.ui.stackedWidget.setCurrentIndex(0)
        self.ui.User_login.clear()
        self.ui.Password_login.clear()

    def a(self):
        self.ui.stackedWidget.setCurrentIndex(2)

    def tablo_duzenle(self):
        self.ui.tableWidget.setHorizontalHeaderLabels(('User_Id', 'UserName', 'Password', 'Status'))
        self.ui.tableWidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.ui.tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.ui.tableWidget.setAlternatingRowColors(True)
        pallete = self.ui.tableWidget.palette()
        pallete.setColor(QPalette.Background, QColor(60, 60, 60))
        pallete.setColor(QPalette.AlternateBase, QColor("darkkhaki"))
        pallete.setColor(QPalette.Base, QColor('#bbb'))

        self.ui.tableWidget.setPalette(pallete)
        read = self.im.execute("""SELECT * FROM Bilgiler""")
        rows = read.fetchall()


        self.ui.tableWidget.setRowCount(0)
        for row_number, row_data in enumerate(rows):
            self.ui.tableWidget.insertRow(row_number)
            for columb_number, data in enumerate(row_data):
                self.ui.tableWidget.setItem(row_number, columb_number, QtWidgets.QTableWidgetItem(str(data)))

        attr = ["Aktif", "Pasif", "Admin"]

    def doldur(self):

        row = self.ui.tableWidget.currentRow()  # eğer hiç bir satır seçilmezse currentRow -1 döndürüyor

        if row != -1:
            self.ui.user_id_line.setText(self.ui.tableWidget.item(row, 0).text())
            self.ui.user_table_line.setText(self.ui.tableWidget.item(row, 1).text())
            self.ui.user_password_line.setText(self.ui.tableWidget.item(row, 2).text())
            # self.ui.user_status_line.setText(self.ui.tableWidget.item(row, 3).text())
            # self.ui.comboBox.setCurrentText(self.ui.tableWidget.item(row,3).text())

    def addData(self):
        user = self.ui.user_table_line.text()
        password = self.ui.user_password_line.text()
        status = self.ui.comboBox_2.currentText()

        insert = """INSERT INTO Bilgiler (UserName,Password,is_active) VALUES (?,?,?)"""
        values = (user, password, status)

        cevap = QMessageBox.question(self, "KAYIT EKLE", "Kayıt eklemek istediğinize emin misiniz?", \
 \
                                     QMessageBox.Yes | QMessageBox.No)
        if cevap == QMessageBox.Yes:

            try:
                self.im.execute(insert, values)
                self.connect.commit()
                print("Veriler eklendi")
            except:
                print("eklemede hata var")
        else:
            pass

    def updateData(self):

        cevap = QMessageBox.question(self, "KAYIT GÜNCELLE", "Kaydı güncellemek istediğinize emin misiniz?", \
 \
                                     QMessageBox.Yes | QMessageBox.No)
        if cevap == QMessageBox.Yes:

            try:
                secili = self.ui.tableWidget.selectedItems()
                # _Id =int(secili[0].text())
                user = self.ui.user_table_line.text()
                status = self.ui.comboBox_2.currentText()
                Id = int(self.ui.user_id_line.text())

                self.im.execute("""UPDATE Bilgiler SET is_active=? WHERE id = ?""", (status, Id))

                self.connect.commit()
                print("Güncelleme başarılı")
            except Exception as Hata:
                print(str(Hata))
            else:
                pass

    def deleteData(self):
        cevap = QMessageBox.question(self, "KAYIT Sil", "Kaydı silmek istediğinizden emin misiniz?", \
 \
                                     QMessageBox.Yes | QMessageBox.No)
        if cevap == QMessageBox.Yes:
            silinecek = self.ui.user_id_line.text()

            try:
                self.im.execute("""DELETE FROM Bilgiler WHERE id = ?""", (silinecek))
                self.connect.commit()
                print("Silme başarılı")
            except Exception as Hata:
                print(str(Hata))
        else:
            pass

    def videoYukle(self):
        self.ui.listWidget.show()


        url = self.ui.link_line.text()

        self.veri_al_iki = self.ui.comboBox.currentText()
        try:

            if self.ui.mp4_radio.isChecked() == True:


                if self.ui.combobox_secim.currentText() == 'Playlist':


                    self.my_playlist = Playlist(url)

                    playlist_sayac = 0

                    if self.my_playlist:

                        self.ui.progressBar.show()

                        for self.playlist in self.my_playlist.videos:
                            self.playlist.register_on_progress_callback(self.progress_callback_playlist)
                            self.playlist.register_on_complete_callback(self.complete_callback_playlist)

                            a = self.playlist.streams.filter(res=f"{self.veri_al_iki}").first()


                            a.download(output_path=self.file_dialog_yukle)

                            playlist_sayac += 1

                            self.video_yuklenme = True

                            video_ismi = str(playlist_sayac) + ' - ' + self.playlist.title

                            self.signal_listeye_yazma.emit(video_ismi)

                        if self.video_yuklenme == True:
                            self.signal_mesaj_video_indirme.emit()
                    else:
                        self.signal_Msj_playlist.emit()
                        self.ui.download_button.setEnabled(True)
                        self.ui.mp3_radio.setEnabled(True)
                        self.ui.mp4_radio.setEnabled(True)



                elif self.ui.combobox_secim.currentText() == "Tekvideo":

                    vname = "clip.mp4"
                    aname = "audio.mp3"

                    self.mp4_yukle = YouTube(url)
                    self.mp4_yukle.register_on_progress_callback(self.progress_callback)
                    self.mp4_yukle.register_on_complete_callback(self.complete_callback)





                    #self.veri_al_iki = self.ui.comboBox.currentText()

                    if self.veri_al_iki == "240p" or self.veri_al_iki == "480p" or self.veri_al_iki == "1080p" or self.veri_al_iki == "1440p" or self.veri_al_iki =="2160p":
                        self.ui.download_button.setEnabled(False)
                        self.ui.mp3_radio.setEnabled(False)
                        self.ui.mp4_radio.setEnabled(False)


                        self.mp4_download_fake_title = self.mp4_yukle.streams.filter(res=f"{self.veri_al_iki}").first()


                        self.mp4_download = self.mp4_yukle.streams.filter(res=f"{self.veri_al_iki}").first().download(output_path=self.file_dialog_yukle)

                        # print(self.veri_al_iki)
                        if self.mp4_download:
                            self.ui.progressBar.show()
                            os.rename(self.mp4_download, vname)
                            audio = self.mp4_yukle.streams.filter(only_audio=True).first().download(output_path=self.file_dialog_yukle)
                            os.rename(audio, aname)
                            video = mpe.VideoFileClip(vname)
                            audioo = mpe.AudioFileClip(aname)
                            self.final = video.set_audio(audioo)

                            self.final.write_videofile(self.mp4_download.title(),logger=MyBarLogger(self))


                            os.remove(aname)
                            os.remove(vname)



                            self.video_yuklenme = False
                            self.signal_listeye_yazma.emit(self.mp4_download_fake_title.title)

                            self.ui.download_button.setEnabled(True)
                            self.ui.mp3_radio.setEnabled(True)
                            self.ui.mp4_radio.setEnabled(True)
                    elif self.veri_al_iki != "240p" or self.veri_al_iki != "480p" or self.veri_al_iki !="1080p" or self.veri_al_iki !="1440p" or self.veri_al_iki =="2160p":
                        self.ui.download_button.setEnabled(False)
                        self.ui.mp3_radio.setEnabled(False)
                        self.ui.mp4_radio.setEnabled(False)
                        self.mp4_yukle = YouTube(url)
                        self.mp4_yukle.register_on_progress_callback(self.progress_callback)
                        self.mp4_yukle.register_on_complete_callback(self.complete_callback)
                        self.mp4_download = self.mp4_yukle.streams.filter(res=f"{self.veri_al_iki}").first()
                        # print(self.veri_al_iki)
                        if self.mp4_download:

                            self.ui.progressBar.show()
                            self.mp4_download.download(output_path=self.file_dialog_yukle)

                            self.video_yuklenme = False
                            video_ismi = self.mp4_download.title
                            self.signal_listeye_yazma.emit(video_ismi)
                            print("mp4 indirildi")
                            self.ui.download_button.setEnabled(True)
                            self.ui.mp3_radio.setEnabled(True)
                            self.ui.mp4_radio.setEnabled(True)


        except KeyError:
            self.signal_Msj_4k_playlist.emit()
            self.ui.download_button.setEnabled(True)
            self.ui.mp3_radio.setEnabled(True)
            self.ui.mp4_radio.setEnabled(True)

        except AttributeError:
            pass
        except FileExistsError:
            self.signal_Msj_file.emit()
            self.ui.download_button.setEnabled(True)

        try:

            if self.ui.mp3_radio.isChecked() == True:
                self.mp3_yukle = YouTube(url)
                self.mp3_yukle.register_on_progress_callback(self.progress_callback_mp3)
                self.mp3_yukle.register_on_complete_callback(self.progress_callback_mp3_callback)

                mp3_download = self.mp3_yukle.streams.filter(only_audio=True).first()
                if mp3_download:
                    self.ui.progressBar.show()
                    mp3 = mp3_download.download(output_path=self.file_dialog_yukle)

                    # dosyayı mp3'e çevirdik
                    base, ext = os.path.splitext(mp3)
                    new_file = base + '.mp3'
                    os.rename(mp3, new_file)

                    # self.video_yuklenme = False

                    video_ismi = mp3_download.title
                    self.signal_listeye_yazma.emit(video_ismi)
        except FileExistsError:
            # self.video_yuklenme = False
            self.signal_Msj.emit()
    # region

    def progress_callback(self, stream, chunk, bytes_remaining):

        download = self.mp4_yukle
        contentsize = download.streams.get_highest_resolution().filesize
        size = contentsize - bytes_remaining
        steer = int(size / contentsize * 100)

        self.ui.progressBar.setValue(steer)


    def complete_callback(self, stream, file_handle):
        time.sleep(3)
        #self.ui.progressBar.hide()
        self.ui.progressBar.setValue(0)

    # endregion

    # region

    def progress_callback_playlist(self, stream, chunk, bytes_remaining):

        download = self.playlist
        contentsize = download.streams.get_highest_resolution().filesize

        size = contentsize - bytes_remaining
        steer = int(size / contentsize * 100)

        self.ui.progressBar.setValue(steer)

    def complete_callback_playlist(self, stream, file_handle):
        pass



    # endregion

    # region

    def progress_callback_mp3(self, stream, chunk, bytes_remaining):
        download = self.mp3_yukle
        contentsize = download.streams.get_audio_only().filesize

        size = contentsize - bytes_remaining
        steer = int(size / contentsize * 100)

        self.ui.progressBar.setValue(steer)

    def progress_callback_mp3_callback(self, stream, file_handle):
        time.sleep(3)
        self.ui.progressBar.hide()
        self.ui.progressBar.setValue(0)
    # endregion



app = QApplication([])

kullanicilar = Main()
kullanicilar.show()

app.exec_()
