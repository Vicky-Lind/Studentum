import sys
import time

import PyQt5.QtWidgets as QW
import PyQt5.QtGui as QG
import PyQt5.QtCore as QC

class MainWindow(QW.QMainWindow):
    def __init__(self):
        super().__init__()

        # Main Window
        self.setWindowTitle("Studentum")
        self.setWindowIcon(QG.QIcon('Studentum/assets/icon-small.ico'))
        self.setStyleSheet(
            "background-color: white;"
        )
        
        # Create a QStackedWidget to manage screens
        self.stacked_widget = QW.QStackedWidget()
        self.setCentralWidget(self.stacked_widget)
        
        # Create the startup screen
        self.startup_view = QW.QWidget()
        self.setup_startup_view()
        self.stacked_widget.addWidget(self.startup_view)
        
        # Create the student login screen
        self.student_login_view = QW.QWidget()
        self.setup_student_login_view()
        self.stacked_widget.addWidget(self.student_login_view)
        
        # Create the staff login screen
        self.staff_login_view = QW.QWidget()
        self.setup_staff_login_screen()
        self.stacked_widget.addWidget(self.staff_login_view)
        
        # Create the staff account creation screen
        self.staff_creation_view = QW.QWidget()
        self.setup_staff_creation_view()
        self.stacked_widget.addWidget(self.staff_creation_view)
        
        self.showMaximized() 
    def setup_startup_view(self):
        # Configure the startup view
        layout = QW.QVBoxLayout(self.startup_view)

        # Logo image on screen
        scaled_image = QG.QPixmap('Studentum/assets/icon.png').scaled(600, 600, QC.Qt.KeepAspectRatio, QC.Qt.SmoothTransformation)
        logo_label = QW.QLabel()
        logo_label.setPixmap(scaled_image)
        logo_label.setAlignment(QC.Qt.AlignHCenter)
        layout.addWidget(logo_label)

        # Frame to hold main content
        frame2 = QW.QFrame()
        layout.addWidget(frame2)
        layout2 = QW.QVBoxLayout(frame2)
        layout2.setAlignment(QC.Qt.AlignTop)
        frame2.setLayout(layout2)

        # Title label "Log In"
        title_label = QW.QLabel("Log In")
        title_label.setAlignment(QC.Qt.AlignHCenter)
        title_label.setMaximumHeight(100)
        title_label.setStyleSheet(
            "font-size: 30px;"
            "font-family: Arial;"
            "font-weight: semi-bold;"
            "background-color: white;"
        )
        layout2.addWidget(title_label)

        # Frame to hold buttons
        frame3 = QW.QFrame()
        layout2.addWidget(frame3)
        layout3 = QW.QHBoxLayout(frame3)
        layout3.setAlignment(QC.Qt.AlignTop | QC.Qt.AlignHCenter)
        frame3.setLayout(layout3)

        # Student login button
        student_button = QW.QPushButton("Student")
        student_button.setFixedSize(250, 125)
        student_button.setCursor(QC.Qt.PointingHandCursor)
        student_button.setStyleSheet("""
            QPushButton {
                background-color: #3E71DF;
                color: white;
                font-size: 20px;
                font-family: Arial;
                border-radius: 20px;
                padding-left: 50px;
                padding-right: 50px;
                padding-top: 20px;
                padding-bottom: 20px;
                margin: 30px;
            } QPushButton:hover {
                background-color: #4681FF;
            }
        """)
        layout3.addWidget(student_button)

        # Staff login button
        staff_button = QW.QPushButton("Staff")
        staff_button.setFixedSize(250, 125)
        staff_button.setCursor(QC.Qt.PointingHandCursor)
        staff_button.setStyleSheet("""
            QPushButton {
                background-color: #3E71DF;
                color: white;
                font-size: 20px;
                font-family: Arial;
                border-radius: 20px;
                padding-left: 50px;
                padding-right: 50px;
                padding-top: 20px;
                padding-bottom: 20px;
                margin: 30px;
            } QPushButton:hover {
                background-color: #4681FF;
            }
        """)
        layout3.addWidget(staff_button)

        # Create staff account button
        create_staff_button = QW.QPushButton("Or create a staff account")
        create_staff_button.setCursor(QC.Qt.PointingHandCursor)
        create_staff_button.setStyleSheet("""
            QPushButton {
                color: #9c9c9c;
                font-size: 15px;
                font-family: Arial;
                border: none;
            } QPushButton:hover {
                color: #545454;
            }
        """)
        layout2.addWidget(create_staff_button)

        # Connect buttons to functions
        student_button.clicked.connect(self.show_student_login_screen)
        staff_button.clicked.connect(self.show_staff_login_screen)
        create_staff_button.clicked.connect(self.show_staff_creation_screen)
    
    def setup_student_login_view(self):
        self.stacked_widget.setCurrentWidget(self.student_login_view)
        
    
    def setup_staff_login_screen(self):
        pass
    
    def setup_staff_creation_view(self):
        pass
    
    def show_main_menu(self):
        self.stacked_widget.setCurrentWidget(self.startup_view)
    def show_student_login_screen(self):
        self.stacked_widget.setCurrentWidget(self.student_login_view)
    def show_staff_login_screen(self):
        self.stacked_widget.setCurrentWidget(self.staff_login_view)
    def show_staff_creation_screen(self):
        self.stacked_widget.setCurrentWidget(self.staff_creation_view)
#--------------------------------

if __name__ == "__main__":
    app = QW.QApplication(sys.argv)
    app.setStyle('fusion')
    
    # pixmap = QG.QPixmap('Studentum/assets/icon.png')
    # splash = QW.QSplashScreen(pixmap)
    # splash.show()
    # app.processEvents()
    # time.sleep(3)                           # Let splashscreen load 2 s
    # splash.hide()                    
        
    appWindow = MainWindow()                # Open main window
    appWindow.show()
    sys.exit(app.exec())