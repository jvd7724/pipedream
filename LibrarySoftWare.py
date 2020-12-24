from PyQt5.QtWidgets import QDialog, QApplication, QMessageBox, QTableWidget, QTableWidgetItem
from PyQt5 import QtCore, QtGui, QtWidgets, uic
import sqlite3


class borrow_books(QtWidgets.QDialog):
    def __init__(self):
        super(borrow_books,self).__init__()
        uic.loadUi('D:/Project/borrow.ui',self)    
class add_librarian(QtWidgets.QDialog):
    def __init__(self):
        super(add_librarian,self).__init__()
        uic.loadUi('D:/Project/AddLibrarian.ui',self)
        self.SavePushButton.clicked.connect(self.insert_librarian)
        self.ExitPushButton.clicked.connect(self.close)

    def insert_librarian(self):
        sqlite_connection = sqlite3.connect("D:/Project/BookWormSoftWareDataBase.db")
        cur = sqlite_connection.cursor()
        fn = self.FirstNameLineEdit.text()
        ln = self.LastNameLineEdit.text()
        nc = self.NationalCodeLineEdit.text()
        pc = self.PersonnelCodeLineEdit.text()
        ed = self.EntryDateLineEdit.text()
        cur.execute(f"insert into TLibrarian (FirstName,LastName,NationalCode,PersonnelCode,EntryDate)\
            values('{fn}','{ln}','{nc}','{pc}','{ed}')")
        sqlite_connection.commit()
        msg = QMessageBox(self)
        msg.setText('The Librarian was Added Successfully')
        msg.setWindowTitle('Add Librarian')
        msg.exec()
        self.FirstNameLineEdit.setText('')
        self.LastNameLineEdit.setText('')
        self.NationalCodeLineEdit.setText('')
        self.PersonnelCodeLineEdit.setText('')
        self.EntryDateLineEdit.setText('')
        cur.close    
class Membership(QtWidgets.QDialog):
    def __init__(self):
        super(Membership,self).__init__()
        uic.loadUi('D:/Project/AddLibraryMember.ui',self)
        self.SavePushButton.clicked.connect(self.insert_Membership)
        self.ExitPushButton.clicked.connect(self.close)

    def insert_Membership(self):
        sqlite_connection = sqlite3.connect("D:/Project/BookWormSoftWareDataBase.db")
        cur = sqlite_connection.cursor()
        fn = self.FirstNameLineEdit.text()
        ln = self.LastNameLineEdit.text()
        nc = self.NationalCodeLineEdit.text()
        ry = self.RegisteryDateLineEdit.text()
        ed = self.ExpirityDateLineEdit.text()
        mp = self.MembershipTypeLineEdit.text()
        cy = self.CityLineEdit.text()
        st = self.StreetLineEdit.text()
        pc = self.PostalCodeLineEdit.text()
        ay = self.AlleyLineEdit.text()
        cur.execute(f"insert into TMembership (FirstName,LastName,NationalCode,RegisteryDate,ExpirityDate,MembershipType,City,Street,PostalCode,Alley)\
            values('{fn}','{ln}','{nc}','{ry}','{ed}','{mp}','{cy}','{st}','{pc}','{ay}')")
        sqlite_connection.commit()
        msg = QMessageBox(self)
        msg.setText('The Membership was Added Successfully')
        msg.setWindowTitle('Membership')
        msg.exec()
        self.FirstNameLineEdit.setText('')
        self.LastNameLineEdit.setText('')
        self.NationalCodeLineEdit.setText('')
        self.RegisteryDateLineEdit.setText('')
        self.ExpirityDateLineEdit.setText('')
        self.MembershipTypeLineEdit.setText('')
        self.CityLineEdit.setText('')
        self.StreetLineEdit.setText('')
        self.PostalCodeLineEdit.setText('')
        self.AlleyLineEdit.setText('')
        cur.close
class add_books_author(QtWidgets.QDialog):
    def __init__(self):
        super(add_books_author,self).__init__()
        uic.loadUi('D:/Project/AddBooksAuthor.ui',self)
        self.ExitPushButton.clicked.connect(self.close)
        self.SavePushButton.clicked.connect(self.insert_author_books)

    def insert_author_books(self):
        sqlite_connection = sqlite3.connect("D:/Project/BookWormSoftWareDataBase.db")
        cur = sqlite_connection.cursor()
        fn = self.FirstNameLineEdit.text()
        ln = self.LastNameLineEdit.text()
        nc = self.NationalCodeineEdit.text()
        od = self.ORCIDLineEdit.text()
        cur.execute(f"insert into TAuthor (FirstName,LastName,NationalCode,ORCIDcode)\
            values('{fn}','{ln}','{nc}','{od}')")
        sqlite_connection.commit()
        msg = QMessageBox(self)
        msg.setText('The Author was Added Successfully')
        msg.setWindowTitle('Books Author')
        msg.exec()
        self.FirstNameLineEdit.setText('')
        self.LastNameLineEdit.setText('')
        self.NationalCodeineEdit.setText('')
        self.ORCIDLineEdit.setText('')
        cur.close()
class main_form(QtWidgets.QMainWindow):
    def __init__(self):
        super(main_form,self).__init__()
        uic.loadUi('D:/Project/Main_form.ui',self)
        self.actoinAddBooks.triggered.connect(self.show_add_books)
        self.actionAdd_Books_Author.triggered.connect(self.show_add_books_author)
        self.actionAdd_Library_Member.triggered.connect(self.show_Membership)
        self.actionAdd_Librarian.triggered.connect(self.show_add_librarian)
        self.actionBook_Borrow.triggered.connect(self.show_borrow_books)
        self.actionExit.triggered.connect(self.close)
   

    def show_borrow_books(self):
        self.bb = borrow_books()
        self.bb.setModal(True)
        self.bb.show()


    def show_Membership(self):
        self.mp = Membership()
        self.mp.setModal(True)
        self.mp.show()

    def show_add_librarian(self):
        self.an = add_librarian()
        self.an.setModal(True)
        self.an.show()





    def show_add_books_author(self):
        self.Au = add_books_author()
        self.Au.setModal(True)
        self.Au.show()

    
    def show_add_books(self):
        print('Add Books clicked')
        self.A =add_books()
        self.A.setModal(True)
        self.A.show()
class widget(QtWidgets.QWidget):
    def __init__(self):
        super(widget,self).__init__()
        uic.loadUi('D:/Project/UserPass.ui',self)
        self.LoginPushButton.clicked.connect(self.show_main_form)
        self.LoginPushButton.clicked.connect(self.close)
        self.ExitPushButton.clicked.connect(self.close)   
    def show_main_form(self):
        print('Login PushButton clicked')
        self.w = main_form()
        self.w.show()        
class add_books(QtWidgets.QDialog):
    def __init__(self):
        super(add_books,self).__init__()
        uic.loadUi('D:/Project/add_books.ui',self)
        self.ExitPushButton.clicked.connect(self.close)
        self.SavePushButton.clicked.connect(self.insert_records)




    def insert_records(self):
        sqlite_connection = sqlite3.connect("D:/Project/BookWormSoftWareDataBase.db")
        cur = sqlite_connection.cursor()
        ti = self.TitleLineEdit.text()
        au = self.AuthorLineEdit.text()
        ed = self.EditionLineEdit.text()
        bt = self.BookTypeLineEdit.text()
        Isb= self.ISBNLineEdit.text()
        pr = self.PriceLineEdit.text()
        py = self.PublicationYearLineEdit.text()
        cur.execute(f"insert into TBooks (Title,Author,Edition,BookType,ISBN,Price,PublicationYear)\
            values('{ti}','{au}','{ed}','{bt}','{Isb}','{pr}','{py}')")
        sqlite_connection.commit()
        msg = QMessageBox(self)
        msg.setText('The Book was Added Successfully')
        msg.setWindowTitle('Add Books')
        msg.exec()
        self.TitleLineEdit.setText('')
        self.PublisherLineEdit.setText('')
        self.EditionLineEdit.setText('')
        self.BookTypeLineEdit.setText('')
        self.ISBNLineEdit.setText('')
        self.PriceLineEdit.setText('')
        self.PublicationYearLineEdit.setText('')
        cur.close()        
app =QApplication([])
w = widget()
w.show()
app.exec()
