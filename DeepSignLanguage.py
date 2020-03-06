from tkinter import *
from tkinter import ttk
import tkinter as tk
import sys
import tkinter.messagebox
import mysql.connector
from mysql.connector import Error
import librosa
import IPython.display as ipd
from tkinter import filedialog
from pathlib import Path

datUser = 'admin'
datPassword = '12345'

class DemoLogin:
    def __init__(self, induk):
        self.induk = induk
         
        self.induk.protocol("WM_DELETE_WINDOW", self.Tutup)
        self.induk.resizable(False, False)
         
        self.aturKomponen()

        self.entUser.focus_set()

    def aturKomponen(self):

        frameUtama = Frame(self.induk, bd=3, bg='#9933FF', height=327, width=780, relief='raised')
        frameUtama.place(x=110, y=185)
        
        frData = Frame(frameUtama, bg='#9933FF', height=100, width=200, relief='raised')
        frData.place(x=230, y=80)
         
        Label(frData, text='User Name:',  height=1, width=20, bg='#9933FF').grid(row=0, column=0, sticky=E)
        self.entUser = Entry(frData, bd=3)
        self.entUser.grid(row=0, column=2)

        Label(frData, text='Password:',  height=1, width=20, bg='#9933FF').grid(row=1, column=0, sticky=E)
        self.entPass = Entry(frData, bd=3, show='*')
        self.entPass.grid(row=1, column=2)
         
        self.cek = IntVar() 
         
        self.cbShowPass = Checkbutton(frData, text='See Password', bg='#9933FF',
            variable=self.cek, command=self.lihatPassword)
        self.cbShowPass.grid(row=3, column=2, sticky=W)

        self.btnBack = Button(frameUtama, text='Clear', compound='top', width=10, bd=5, bg='#9933FF', command=self.aturKomponen)
        self.btnBack.place(x=265, y=230)

        self.btnNext = Button(frameUtama, text='Next', compound='top', width=10, bd=5, bg='#9933FF', command=self.prosesLogin)
        self.btnNext.place(x=415, y=230)
		
    def prosesLogin(self, event=None):
        '''
        nmUser = self.entUser.get()
        passUser = self.entPass.get()

        if nmUser=='':
            tkinter.messagebox.showwarning('Wrong Message', 'Username cannot be empty!', parent=self.induk)
            self.entUser.focus_set()
        elif passUser=='':
            tkinter.messagebox.showwarning('Wrong Message', 'Passwords cannot be empty!', parent=self.induk)
            self.entPass.focus_set()
        elif (nmUser==datUser) and (passUser==datPassword):
            tkinter.messagebox.showinfo("Login", "Welcome!!!")
        '''
     #  memanggil form admin setelah berhasil di autentication
        app4.aturKomponenAdmin()
        '''
        else:
            tkinter.messagebox.showwarning('Wrong Message', 'Incorrect Username or Password !!', parent=self.induk)
            self.Hapus()
        '''
    def lihatPassword(self, event=None):
        nilaiCek = self.cek.get()
         
        if nilaiCek== 1:
            self.entPass['show'] = ''
        else:
            self.entPass['show'] = '*'
         
    def Tutup(self, event=None):
        self.induk.destroy()
         
    def Hapus(self, event=None):
        self.entUser.delete(0, END)
        self.entPass.delete(0, END)
        self.entUser.focus_set()	
		
class AboutApp():
    def __init__(self, induk):
        self.induk = induk
        self.aturKomponenAboutApp()

    def aturKomponenAboutApp(self):
        frameUtama = Frame(self.induk, bd=17, bg='#9933FF', relief='raised')
        frameUtama.place(x=110, y=185, height=327)
        
        frData = Frame(frameUtama, bd=2, bg='#9933FF')
        frData.pack(fill=BOTH, expand=YES)
        
        text = """hey hey... 
        Aplikasi ini digunakan untuk melakukan pengolahan data dari suara, gambar dan video dari 
        gerakan bahasa isyarat tuna rungu
        """
        Label(frData, text=text, bg='#9933FF', font='Verdana 10 bold', height=327, width=82).pack()


class AboutGedung():
    def __init__(self, induk):
        self.induk = induk
        self.aturKomponenAboutGedung()

    def aturKomponenAboutGedung(self):
        frameUtama = Frame(self.induk, bd=17, bg='#9933FF', relief='raised')
        frameUtama.place(x=110, y=185, height=327)
        
        frData = Frame(frameUtama, bd=2, bg='#9933FF')
        frData.pack(fill=BOTH, expand=YES)
        
        text = """hey hey... 
        Aplikasi ini untuk mendeteksi dan mengklasifikasi audio, gambar dan video dengan
        menggunakan metode Deep Learning
        """
        Label(frData, text=text, bg='#9933FF', font='Verdana 10 bold', height=327, width=82).pack()
        
class Admin:
    def __init__(self, induk):
        self.induk = induk
        self.aturKomponenRegistrasi()
        self.aturKomponenAdmin()
        self.aturAudio()
        self.aturFasilitas()
        self.aturCat()	

    def loadFile(self):
        filename = filedialog.askopenfilename(initialdir="/",title="Select File ", filetypes=(("WAV Files","*.wav"),("all files","*.*")))
        path = Path(filename)
        self.entryNm.insert(0, path.name)
        self.entryPath.insert(0, path)
        

#Tambahkan ke dalam DB data yang sudah di dapatkan


    def insertAgenda(self):
        idAgenda = self.entryId.get()
        namaAgenda = self.entryNm.get()
        hargaAgenda = self.entryPath.get()
		
        if(idAgenda=="" or namaAgenda=="" or hargaAgenda==""):
            tkinter.messagebox.showwarning("insert status", "Data Tetap")

        else:
            con = mysql.connector.connect(host="localhost", user="root", password="", database="penyewaan_gedung")
            cursor = con.cursor()
            cursor.execute("insert into agenda values('"+ idAgenda +"','"+ namaAgenda +"','"+ hargaAgenda +"')")
            cursor.execute("commit");
            #result = cursor.fetchall()
			
            self.entryId.delete(0, 'end')
            self.entryNm.delete(0, 'end')
            self.entryPath.delete(0, 'end')
            self.showAgenda()			
            tkinter.messagebox.showwarning("insert status", "inserted successfully")
            con.close();
			
    def deleteAgenda(self):
        if(self.entryId.get() == ""):
            tkinter.messagebox.showwarning("delete status", "ID is compolsary for delete")

        else:
            con = mysql.connector.connect(host="localhost", user="root", password="", database="penyewaan_gedung")
            cursor = con.cursor()
            cursor.execute("delete from agenda where idAgenda='"+ self.entryId.get() +"'")
            cursor.execute("commit");
            #result = cursor.fetchall()
			
            self.entryId.delete(0, 'end')
            self.entryNm.delete(0, 'end')
            self.entryPath.delete(0, 'end')
            self.showAgenda()			
            tkinter.messagebox.showwarning("delete status", "delete successfully")
            con.close();

    def updateAgenda(self):
        idAgenda = self.entryId.get()
        namaAgenda = self.entryNm.get()
        hargaAgenda = self.entryPath.get()
		
        if(idAgenda=="" or namaAgenda=="" or hargaAgenda==""):
            tkinter.messagebox.showwarning("update status", "Data Berhasil Di Update")

        else:
            con = mysql.connector.connect(host="localhost", user="root", password="", database="penyewaan_gedung")
            cursor = con.cursor()
            cursor.execute("update agenda set namaAgenda='"+ namaAgenda +"', hargaAgenda='"+ hargaAgenda +"' where idAgenda='"+ idAgenda +"'")
            cursor.execute("commit");
            #result = cursor.fetchall()
			
            self.entryId.delete(0, 'end')
            self.entryNm.delete(0, 'end')
            self.entryPath.delete(0, 'end')
            self.showAgenda()			
            tkinter.messagebox.showwarning("update status", "updated successfully")
            con.close();

    def getAgenda(self):
        if(self.entryId.get() == ""):
            tkinter.messagebox.showwarning("fetch status", "ID is compolsary for fetch")

        else:
            con = mysql.connector.connect(host="localhost", user="root", password="", database="penyewaan_gedung")
            cursor = con.cursor()
            cursor.execute("select * from agenda where idAgenda='"+ self.entryId.get() +"'")
            rows = cursor.fetchall()
			
            for row in rows:
                self.entryNm.insert(0, row[1])
                self.entryPath.insert(0, row[2])

            con.close();
			
    def showAgenda(self):
        con = mysql.connector.connect(host="localhost", user="root", password="", database="penyewaan_gedung")
        cursor = con.cursor()
        cursor.execute("select * from agenda")
        rows = cursor.fetchall()
        self.list.delete(0, self.list.size())
			
        for row in rows:
            insertData = str(row[0])+ '        '+ row[1] + '         '+ str(row[2])
            self.list.insert(self.list.size()+1, insertData)

        con.close();

    
		
    def insertFasilitas(self):
        idFasilitas = self.entryIdF.get()
        namaFasilitas = self.entryNmF.get()
        hargaFasilitas = self.entryPathF.get()
		
        if(idFasilitas=="" or namaFasilitas=="" or hargaFasilitas==""):
            tkinter.messagebox.showwarning("insert status", "Data Tetap")

        else:
            con = mysql.connector.connect(host="localhost", user="root", password="", database="penyewaan_gedung")
            cursor = con.cursor()
            cursor.execute("insert into fasilitas values('"+ idFasilitas +"','"+ namaFasilitas +"','"+ hargaFasilitas +"')")
            cursor.execute("commit");
            #result = cursor.fetchall()
			
            self.entryIdF.delete(0, 'end')
            self.entryNmF.delete(0, 'end')
            self.entryPathF.delete(0, 'end')
            self.showFasilitas()			
            tkinter.messagebox.showwarning("insert status", "inserted successfully")
            con.close();
			
    def deleteFasilitas(self):
        if(self.entryIdF.get() == ""):
            tkinter.messagebox.showwarning("delete status", "ID is compolsary for delete")

        else:
            con = mysql.connector.connect(host="localhost", user="root", password="", database="penyewaan_gedung")
            cursor = con.cursor()
            cursor.execute("delete from fasilitas where idFasilitas='"+ self.entryIdF.get() +"'")
            cursor.execute("commit");
            #result = cursor.fetchall()
			
            self.entryIdF.delete(0, 'end')
            self.entryNmF.delete(0, 'end')
            self.entryPathF.delete(0, 'end')
            self.showFasilitas()			
            tkinter.messagebox.showwarning("delete status", "delete successfully")
            con.close();

    def updateFasilitas(self):
        idFasilitas = self.entryIdF.get()
        namaFasilitas = self.entryNmF.get()
        hargaFasilitas = self.entryPathF.get()
		
        if(idFasilitas=="" or namaFasilitas=="" or hargaFasilitas==""):
            tkinter.messagebox.showwarning("update status", "Data Berhasil Di Update")

        else:
            con = mysql.connector.connect(host="localhost", user="root", password="", database="penyewaan_gedung")
            cursor = con.cursor()
            cursor.execute("update fasilitas set namaFasilitas='"+ namaFasilitas +"', hargaFasilitas='"+ hargaFasilitas +"' where idFasilitas='"+ idFasilitas +"'")
            cursor.execute("commit");
            #result = cursor.fetchall()
			
            self.entryIdF.delete(0, 'end')
            self.entryNmF.delete(0, 'end')
            self.entryPathF.delete(0, 'end')
            self.showFasilitas()			
            tkinter.messagebox.showwarning("update status", "updated successfully")
            con.close();

    def getFasilitas(self):
        if(self.entryIdF.get() == ""):
            tkinter.messagebox.showwarning("fetch status", "ID is compolsary for fetch")

        else:
            con = mysql.connector.connect(host="localhost", user="root", password="", database="penyewaan_gedung")
            cursor = con.cursor()
            cursor.execute("select * from fasilitas where idFasilitas='"+ self.entryIdF.get() +"'")
            rows = cursor.fetchall()
			
            for row in rows:
                self.entryNmF.insert(0, row[1])
                self.entryPathF.insert(0, row[2])

            con.close();
			
    def showFasilitas(self):
        con = mysql.connector.connect(host="localhost", user="root", password="", database="penyewaan_gedung")
        cursor = con.cursor()
        cursor.execute("select * from fasilitas")
        rows = cursor.fetchall()
        self.list.delete(0, self.list.size())
			
        for row in rows:
            insertData = str(row[0])+ '        '+ row[1] + '         '+ str(row[2])
            self.list.insert(self.list.size()+1, insertData)

        con.close();

    def insertCat(self):
        idCat = self.entryIdC.get()
        namaCat = self.entryNmC.get()
        hargaCat = self.entryPathC.get()
		
        if(idCat=="" or namaCat=="" or hargaCat==""):
            tkinter.messagebox.showwarning("insert status", "Data Tetap")

        else:
            con = mysql.connector.connect(host="localhost", user="root", password="", database="penyewaan_gedung")
            cursor = con.cursor()
            cursor.execute("insert into cathering values('"+ idCat +"','"+ namaCat +"','"+ hargaCat +"')")
            cursor.execute("commit")
            #result = cursor.fetchall()
			
            self.entryIdC.delete(0, 'end')
            self.entryNmC.delete(0, 'end')
            self.entryPathC.delete(0, 'end')
            self.showCat()			
            tkinter.messagebox.showwarning("insert status", "inserted successfully")
            con.close();
			
    def deleteCat(self):
        if(self.entryIdC.get() == ""):
            tkinter.messagebox.showwarning("delete status", "ID is compolsary for delete")

        else:
            con = mysql.connector.connect(host="localhost", user="root", password="", database="penyewaan_gedung")
            cursor = con.cursor()
            cursor.execute("delete from cathering where idCat='"+ self.entryIdC.get() +"'")
            cursor.execute("commit")
            #result = cursor.fetchall()
			
            self.entryIdC.delete(0, 'end')
            self.entryNmC.delete(0, 'end')
            self.entryPathC.delete(0, 'end')
            self.showCat()			
            tkinter.messagebox.showwarning("delete status", "delete successfully")
            con.close();

    def updateCat(self):
        idCat = self.entryIdC.get()
        namaCat = self.entryNmC.get()
        hargaCat = self.entryPathC.get()
		
        if(idCat=="" or namaCat=="" or hargaCat==""):
            tkinter.messagebox.showwarning("update status", "Data Berhasil Di Update")

        else:
            con = mysql.connector.connect(host="localhost", user="root", password="", database="penyewaan_gedung")
            cursor = con.cursor()
            cursor.execute("update cathering set namaCat='"+ namaCat +"', hargaCat='"+ hargaCat +"' where idCat='"+ idCat +"'")
            cursor.execute("commit");
            #result = cursor.fetchall()
			
            self.entryIdF.delete(0, 'end')
            self.entryNmF.delete(0, 'end')
            self.entryPathF.delete(0, 'end')
            self.showFasilitas()			
            tkinter.messagebox.showwarning("update status", "updated successfully")
            con.close();


    def getCat(self):
        if(self.entryIdC.get() == ""):
            tkinter.messagebox.showwarning("fetch status", "ID is compolsary for fetch")

        else:
            con = mysql.connector.connect(host="localhost", user="root", password="", database="penyewaan_gedung")
            cursor = con.cursor()
            cursor.execute("select * from cathering where idCat='"+ self.entryIdC.get() +"'")
            rows = cursor.fetchall()
			
            for row in rows:
                self.entryNmC.insert(0, row[1])
                self.entryPathC.insert(0, row[2])

            con.close();
			
    def showCat(self):
        con = mysql.connector.connect(host="localhost", user="root", password="", database="penyewaan_gedung")
        cursor = con.cursor()
        cursor.execute("select * from cathering")
        rows = cursor.fetchall()
        self.list.delete(0, self.list.size())
			
        for row in rows:
            insertData = str(row[0])+ '        '+ row[1] + '         '+ str(row[2])
            self.list.insert(self.list.size()+1, insertData)

        con.close();	
        
    def insertMember(self):
        nama_penyewa = self.entnama.get()
        no_ktp = self.entnok.get()
        total = self.enttot.get()
        #lama_penyewaan = self.entw.get()
        #namaAgenda = self.entryPath.get()
        #namaFasilitas = self.fasilitas1.get()
        #namaCat = self.hargaCat.get()
        #uang = self.uang.get()
        #kembalian = self.kembalian.get()
		
        if(nama_penyewa=="" or no_ktp=="" or total==""):
            tkinter.messagebox.showwarning("insert status", "Data Tetap")

        else:
            con = mysql.connector.connect(host="localhost", user="root", password="", database="penyewaan_gedung")
            cursor = con.cursor()
            cursor.execute("insert into member values('"+ nama_penyewa +"','"+ no_ktp +"','"+ total +"')")
            cursor.execute("commit");
			
            self.entnama.delete(0, 'end')
            self.entnok.delete(0, 'end')
            self.entw.delete(0, 'end')
            self.entryPath.delete(0, 'end')
            self.fasilitas1.delete(0, 'end')
            self.hargaCat.delete(0, 'end')
            self.enttot.delete(0, 'end')
            self.uang.delete(0, 'end')
            self.kembalian.delete(0, 'end')
            self.entryPath1.delete(0, 'end')
            self.entryPath2.delete(0, 'end')
            self.entryPath3.delete(0, 'end')
		
            self.showMember()			
            tkinter.messagebox.showwarning("insert status", "inserted successfully")
            con.close();	

    def showMember(self):
        con = mysql.connector.connect(host="localhost", user="root", password="", database="penyewaan_gedung")
        cursor = con.cursor()
        cursor.execute("select * from member")
        rows = cursor.fetchall()
        self.list.delete(0, self.list.size())
			
        for row in rows:
            insertData = row[0]+ '        '+ row[1] + '         '+ str(row[2])
            self.list.insert(self.list.size()+1, insertData)

        con.close();

# pengaturan halaman admin
    def aturKomponenAdmin(self):
        frameUtama = Frame(self.induk, bd=3, bg='#9933FF', height=327, width=780, relief='raised')
        frameUtama.place(x=110, y=185)

        self.imageAudio = PhotoImage(file='audio.png')
        self.btnAudio = Button(frameUtama, image=self.imageAudio, bd=5, command=self.aturAudio)
        self.btnAudio.place(x=50, y=100)  

        self.imgfasilitas = PhotoImage(file='picture.png')
        self.btnFasilitas = Button(frameUtama, image=self.imgfasilitas, bd=5, command=self.aturFasilitas)
        self.btnFasilitas.place(x=230, y=100)

        self.imgcath = PhotoImage(file='video.png')
        self.btnCath = Button(frameUtama, image=self.imgcath, bd=5, command=self.aturCat)
        self.btnCath.place(x=420, y=100)

        self.imgmember = PhotoImage(file='member.png')
        self.btnMember = Button(frameUtama, image=self.imgmember, bd=5, command=self.aturKomponenRegistrasi)
        self.btnMember.place(x=600, y=100)  
		

    def aturAudio(self):
        frameUtama = Frame(self.induk, bd=3, bg='#9933FF', height=327, width=780, relief='raised')
        frameUtama.place(x=110, y=185)

        self.labelLoad = Label(frameUtama, text='Load Audio', bg='#9933FF')
        self.labelLoad.place(x=100, y=50)

        self.buttonLoad = Button(frameUtama, text='Load file', bg='#0066CC', height=2, width=7,command=self.loadFile)
        self.buttonLoad.place(x=200, y=50)
        self.labelNm = Label(frameUtama, text='Nama File', bg='#9933FF')
        self.labelNm.place(x=100, y=100)
        self.entryNm = Entry(frameUtama)
        self.entryNm.place(x=200, y=100)

        self.labelPath = Label(frameUtama, text='Path', bg='#9933FF')
        self.labelPath.place(x=100, y=130)
        self.entryPath = Entry(frameUtama)
        self.entryPath.place(x=200, y=130)
		
        self.buttonInsert = Button(frameUtama, text='Insert', bg='#0066CC', height=2, width=7, command=self.insertAgenda)
        self.buttonInsert.place(x=100, y=200)
        self.buttonUpdate = Button(frameUtama, text='Update', bg='#0066CC', height=2, width=7, command=self.updateAgenda)
        self.buttonUpdate.place(x=160, y=200)
        self.buttonDelete = Button(frameUtama, text='Delete', bg='#0066CC', height=2, width=7, command=self.deleteAgenda)
        self.buttonDelete.place(x=220, y=200)
        self.buttonGet = Button(frameUtama, text='Get', bg='#0066CC', height=2, width=7, command=self.getAgenda)
        self.buttonGet.place(x=280, y=200)
        self.buttonGet = Button(frameUtama, text='Back', bg='#0066CC', height=2, width=10, command=self.aturKomponenAdmin)
        self.buttonGet.place(x=670, y=258)
		
		
        self.list = Listbox(frameUtama)
        self.list.place(x=350, y=50, height=200, width=400)
        self.showAgenda()

    def aturFasilitas(self):
        frameUtama = Frame(self.induk, bd=3, bg='#9933FF', height=327, width=780, relief='raised')
        frameUtama.place(x=110, y=185)

        self.labelLoadF = Label(frameUtama, text='Load', bg='#9933FF')
        self.labelLoadF.place(x=100, y=50) 
        self.entryIdF = Entry(frameUtama)
        self.entryIdF.place(x=200, y=50)

        self.labelNmF = Label(frameUtama, text='Nama File', bg='#9933FF')
        self.labelNmF.place(x=100, y=80) 
        self.entryNmF = Entry(frameUtama)
        self.entryNmF.place(x=200, y=80)

        self.labelPathF = Label(frameUtama, text='Path', bg='#9933FF')
        self.labelPathF.place(x=100, y=110) 
        self.entryPathF = Entry(frameUtama)
        self.entryPathF.place(x=200, y=110)
		
        self.buttonInsert = Button(frameUtama, text='Insert', bg='#0066CC', height=2, width=7, command=self.insertFasilitas)
        self.buttonInsert.place(x=100, y=200)
        self.buttonUpdate = Button(frameUtama, text='Update', bg='#0066CC', height=2, width=7, command=self.updateFasilitas)
        self.buttonUpdate.place(x=160, y=200)
        self.buttonDelete = Button(frameUtama, text='Delete', bg='#0066CC', height=2, width=7, command=self.deleteFasilitas)
        self.buttonDelete.place(x=220, y=200)
        self.buttonGet = Button(frameUtama, text='Get', bg='#0066CC', height=2, width=7, command=self.getFasilitas)
        self.buttonGet.place(x=280, y=200)
        self.buttonGet = Button(frameUtama, text='Back', bg='#0066CC', height=2, width=10, command=self.aturKomponenAdmin)
        self.buttonGet.place(x=670, y=258)
		
        self.list = Listbox(frameUtama)
        self.list.place(x=350, y=50, height=200, width=400)
        self.showFasilitas()
		
    def aturCat(self):
        frameUtama = Frame(self.induk, bd=3, bg='#9933FF', height=327, width=780, relief='raised')
        frameUtama.place(x=110, y=185)

        self.labelLoadC = Label(frameUtama, text='id', bg='#9933FF')
        self.labelLoadC.place(x=100, y=50) 
        self.entryIdC = Entry(frameUtama)
        self.entryIdC.place(x=200, y=50)

        self.labelNmC = Label(frameUtama, text='Nama Chatering', bg='#9933FF')
        self.labelNmC.place(x=100, y=80) 
        self.entryNmC = Entry(frameUtama)
        self.entryNmC.place(x=200, y=80)

        self.labelPathC = Label(frameUtama, text='Harga', bg='#9933FF')
        self.labelPathC.place(x=100, y=110) 
        self.entryPathC = Entry(frameUtama)
        self.entryPathC.place(x=200, y=110)
		
        self.buttonInsert = Button(frameUtama, text='Insert', bg='#0066CC', height=2, width=7, command=self.insertCat)
        self.buttonInsert.place(x=100, y=200)
        self.buttonUpdate = Button(frameUtama, text='Update', bg='#0066CC', height=2, width=7, command=self.updateCat)
        self.buttonUpdate.place(x=160, y=200)
        self.buttonDelete = Button(frameUtama, text='Delete', bg='#0066CC', height=2, width=7, command=self.deleteCat)
        self.buttonDelete.place(x=220, y=200)
        self.buttonGet = Button(frameUtama, text='Get', bg='#0066CC', height=2, width=7, command=self.getCat)
        self.buttonGet.place(x=280, y=200)
        self.buttonGet = Button(frameUtama, text='Back', bg='#0066CC', height=2, width=10, command=self.aturKomponenAdmin)
        self.buttonGet.place(x=670, y=258)
		
        self.list = Listbox(frameUtama)
        self.list.place(x=350, y=50, height=200, width=400)
        self.showCat()

	#REGISTRASI		
    def aturKomponenRegistrasi(self):
		
        frameUtama = Frame(self.induk, bd=3, bg='#9933FF', height=327, width=780, relief='raised')
        frameUtama.place(x=110, y=185)
		
        Label(frameUtama, text='REGISTRASI', font='arial 14 bold', bg='#9933FF').place(x=205, y=10)
        
        frData = Frame(frameUtama, bg='#9933FF', height=0, width=0, relief='raised')
        frData.place(x=10, y=60)
         
        Label(frData, text='Nama Penyewa', bg='#9933FF').grid(row=0, column=0, sticky=E)
        Label(frData, text=':', bg='#9933FF').grid(row=0, column=1, sticky=W)
        self.entnama = Entry(frData)
        self.entnama.grid(row=0, column=2)

        Label(frData, text='No.KTP', bg='#9933FF').grid(row=1, column=0, sticky=E)
        Label(frData, text=':', bg='#9933FF').grid(row=1, column=1, sticky=W)
        self.entnok = Entry(frData)
        self.entnok.grid(row=1, column=2)

        Label(frData, text='Lama Penyewaan', bg='#9933FF').grid(row=2, column=0, sticky=E)
        Label(frData, text=':', bg='#9933FF').grid(row=2, column=1, sticky=W)
        self.entw = Entry(frData)
        self.entw.grid(row=2, column=2)		
		
        Label(frData, text='Agenda', bg='#9933FF').grid(row=3, column=0, sticky=E)
        Label(frData, text=':', bg='#9933FF').grid(row=3, column=1, sticky=W)
        self.entryPath = Entry(frData)
        self.entryPath.grid(row=3, column=2)  

        Label(frData, text='Harga: ', bg='#9933FF').grid(row=3, column=3, sticky=E)
        self.entryPath1 = Entry(frData)
        self.entryPath1.grid(row=3, column=4)  

        Label(frData, text='Chatering', bg='#9933FF').grid(row=4, column=0, sticky=E)
        Label(frData, text=':', bg='#9933FF').grid(row=4, column=1, sticky=W)  
        self.hargaCat = Entry(frData)
        self.hargaCat.grid(row=4, column=2, sticky=W)

        Label(frData, text='Harga: ', bg='#9933FF').grid(row=4, column=3, sticky=E)
        self.entryPath2 = Entry(frData)
        self.entryPath2.grid(row=4, column=4) 

        Label(frData, text='Fasilitas', bg='#9933FF').grid(row=5, column=0, sticky=E)
        Label(frData, text=':', bg='#9933FF').grid(row=5, column=1, sticky=W)  
        self.fasilitas1 = Entry(frData)
        self.fasilitas1.grid(row=5, column=2, sticky=W)

        Label(frData, text='Harga: ', bg='#9933FF').grid(row=5, column=3, sticky=E)
        self.entryPath3 = Entry(frData)
        self.entryPath3.grid(row=5, column=4) 

        Label(frData, text='Total Harga:', bg='#9933FF').grid(row=6, column=3, sticky=E)
        self.enttot = Entry(frData)
        self.enttot.grid(row=6, column=4, sticky=W)  

        Label(frData, text='Uang Penyewa: ', bg='#9933FF').grid(row=7, column=3, sticky=E)
        self.uang = Entry(frData)
        self.uang.grid(row=7, column=4, sticky=W) 

        Label(frData, text='Kembalian: ', bg='#9933FF').grid(row=8, column=3, sticky=E)
        self.kembalian = Entry(frData)
        self.kembalian.grid(row=8, column=4, sticky=W) 
		
        frTombol = Frame(frameUtama, bg='#9933FF')
        frTombol.place(x=137, y=260)
		
        self.btnCount = Button(frTombol, text='Sum', bg='#0066CC', height=2, width=10, command=self.hitung)
        self.btnCount.pack(side=LEFT, fill=BOTH, expand=YES)  

        self.btnCount = Button(frTombol, text='Change', bg='#0066CC', height=2, width=10, command=self.Kembalian)
        self.btnCount.pack(side=LEFT, fill=BOTH, expand=YES) 

        self.btnCount = Button(frTombol, text='Save', bg='#0066CC', height=2, width=10, command=self.insertMember)
        self.btnCount.pack(side=LEFT, fill=BOTH, expand=YES)

        self.btnBatal = Button(frTombol, text='Back', bg='#0033FF', height=2, width=10, command=self.aturKomponenAdmin)
        self.btnBatal.pack(side=LEFT, fill=BOTH, expand=YES)
				
        self.list = Listbox(frameUtama)
        self.list.place(x=500, y=40, height=260, width=250)
        self.showMember()

    def hitung(self):
        j = float(self.entw.get())
        x = float(self.entryPath1.get())
        y = float(self.entryPath2.get())
        z = float(self.entryPath3.get())

        self.hasil = (j*x) + (y) + (z)
        self.enttot.insert(0, self.hasil)	

    def Kembalian(self):
        x = float(self.uang.get())
        y = float(self.enttot.get())

        self.hasil1 = (x - y)
        self.kembalian.insert(0, self.hasil1)	
				
class Home:
	def __init__(self, a):
		self.induk = a
		self.tampilan()
		
	def tampilan(self):
		self.gambar = PhotoImage(file='sign language.png')
		Label(self.induk, image=self.gambar, bg='#9933FF', bd=0).place(x=104,y=179)


if __name__ == '__main__':
	root = Tk()

	app = DemoLogin(root)
	app4 = Admin(root)
	app2 = AboutApp(root)
	app3 = AboutGedung(root)
	app5 = Home(root)

	root.geometry('950x540')
	root.title('Image Processing APP')
	root.configure(bg='#999999')
	root.resizable(0,0)
	root.iconbitmap('logo.ico')
	
	background_image = PhotoImage(file='background.png')
	background_label = Label(root, image=background_image)
	background_label.place(relwidth=1, relheight=1)

	frTombolHome = Frame(root)
	frTombolHome.place(x=0, y=0)

    # pengaturan tombol halaman utama

	btnhome = Button(frTombolHome, text='Training', bg='#0033CC', height=2, width=35, command=app4.aturKomponenAdmin)
	btnhome.pack(side=LEFT, fill=BOTH, expand=YES)
	btnlogin = Button(frTombolHome, text='Testing', bg='#0066CC', height=2, width=35, command=app4.aturKomponenAdmin)
	btnlogin.pack(side=LEFT, fill=BOTH, expand=YES)
	#btnadmin = Button(frTombolHome, text='Admin', bg='#9933FF', height=2, width=27, command=app4.aturKomponenAdmin)
	#btnadmin.pack(side=LEFT, fill=BOTH, expand=YES)
	btnapp1 = Button(frTombolHome, text='About the Research', bg='#9900FF', height=2, width=30, command=app3.aturKomponenAboutGedung)
	btnapp1.pack(side=LEFT, fill=BOTH, expand=YES)
	btnapp = Button(frTombolHome, text='About Application', bg='#9900CC', height=2, width=30, command=app2.aturKomponenAboutApp)
	btnapp.pack(side=LEFT, fill=BOTH, expand=YES)

	root.mainloop()