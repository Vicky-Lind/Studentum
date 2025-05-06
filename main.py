# TODO: If other same user exists then replace?
# TODO: 

import sys
import time
import json

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
        
        self.staff_main_view = QW.QWidget()
        self.setup_staff_main_view()
        self.stacked_widget.addWidget(self.staff_main_view)
        
        self.showMaximized() 
    
    # Setup all elements
    def setup_startup_view(self):
        
        # Frame to hold the startup view
        layout = QW.QVBoxLayout(self.startup_view)
        
        # Logo image on screen
        scaled_image = QG.QPixmap('Studentum/assets/icon.png').scaled(600, 600, QC.Qt.KeepAspectRatio, QC.Qt.SmoothTransformation)
        logo_label = QW.QLabel(self.startup_view)
        layout.addWidget(logo_label)
        logo_label.setPixmap(scaled_image)
        logo_label.setAlignment(QC.Qt.AlignHCenter)
        
        # Frame to hold main content
        frame2 = QW.QFrame()
        layout.addWidget(frame2)
        layout2 = QW.QVBoxLayout(frame2)
        layout2.setAlignment(QC.Qt.AlignTop)
        frame2.setLayout(layout2)
        frame2.setStyleSheet(
            "background-color: white;"
        )
        
        # Title label "Log In"
        title_label = QW.QLabel()
        layout2.addWidget(title_label)
        title_label.setText("Log In")
        title_label.setAlignment(QC.Qt.AlignHCenter)
        title_label.setMaximumHeight(100)
        title_label.setStyleSheet(
            "font-size: 30px;"
            "font-family: Arial;"
            "font-weight: semi-bold;"
            "background-color: white;"
        )
        
        # Frame to hold buttons
        frame3 = QW.QFrame()
        layout2.addWidget(frame3)
        layout3 = QW.QHBoxLayout(frame3)
        layout3.setAlignment(QC.Qt.AlignTop | QC.Qt.AlignHCenter)
        frame3.setLayout(layout3)
        frame3.setStyleSheet(
            "background-color: white;"
        )
        
        # Student login button
        student_button = QW.QPushButton()
        layout3.addWidget(student_button)
        student_button.setText("Student")
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
        
        # Staff login button
        staff_button = QW.QPushButton()
        layout3.addWidget(staff_button)
        staff_button.setText("Staff")
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

        # Create staff account button
        create_staff_button = QW.QPushButton()
        layout2.addWidget(create_staff_button)
        create_staff_button.setText("Or create a staff account")
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
        
        # Connect buttons to functions
        student_button.clicked.connect(self.show_student_login_screen)
        staff_button.clicked.connect(self.show_staff_login_screen)
        create_staff_button.clicked.connect(self.show_staff_creation_screen)

    def setup_student_login_view(self):
        pass
    
    def setup_staff_login_screen(self):
        layout = QW.QVBoxLayout(self.staff_login_view)

        # Logo image on screen
        scaled_image = QG.QPixmap('Studentum/assets/icon.png').scaled(600, 600, QC.Qt.KeepAspectRatio, QC.Qt.SmoothTransformation)
        logo_label = QW.QLabel(self.staff_login_view)
        layout.addWidget(logo_label)
        logo_label.setPixmap(scaled_image)
        logo_label.setAlignment(QC.Qt.AlignHCenter)
        
        title_label = QW.QLabel()
        layout.addWidget(title_label)
        title_label.setText("Log In to Staff Account")
        title_label.setAlignment(QC.Qt.AlignHCenter)
        title_label.setMaximumHeight(100)
        title_label.setStyleSheet(
            "font-size: 30px;"
            "font-family: Arial;"
            "font-weight: semi-bold;"
            "background-color: white;"
        )

        # Frame to hold the form
        frame1 = QW.QFrame()
        layout.addWidget(frame1)
        layout1 = QW.QFormLayout(frame1)
        layout1.setAlignment(QC.Qt.AlignTop)
        layout1.setContentsMargins(600, 0, 600, 200)
        layout1.setSpacing(20)

        # Email label and input
        email_label = QW.QLabel("Email")
        email_label.setStyleSheet("""
            QLabel {
                font-size: 17px;
                font-family: Arial;
            }
        """)
        self.staff_email_LE = QW.QLineEdit()
        self.staff_email_LE.setPlaceholderText("Enter your email")
        self.staff_email_LE.setStyleSheet("""
            QLineEdit {
                background-color: #f0f0f0;
                border-radius: 10px;
                padding: 10px;
                font-size: 17px;
            }
        """)

        # Password label and input
        password_label = QW.QLabel("Password")
        password_label.setStyleSheet("""
            QLabel {
                font-size: 17px;
                font-family: Arial;
            }
        """)
        self.staff_password_LE = QW.QLineEdit()
        self.staff_password_LE.setPlaceholderText("Enter your password")
        self.staff_password_LE.setEchoMode(QW.QLineEdit.Password)
        self.staff_password_LE.setStyleSheet("""
            QLineEdit {
                background-color: #f0f0f0;
                border-radius: 10px;
                padding: 10px;
                font-size: 17px;
            }
        """)

        # Create a horizontal layout for the buttons
        button_layout = QW.QHBoxLayout()

        # Submit button
        login_button = QW.QPushButton("Log In")
        login_button.setCursor(QC.Qt.PointingHandCursor)
        login_button.setStyleSheet("""
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
        button_layout.addWidget(login_button)

        # Back button
        back_button = QW.QPushButton("Back")
        back_button.setCursor(QC.Qt.PointingHandCursor)
        back_button.setStyleSheet("""
            QPushButton {
                background-color: #ccc;
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
                background-color: #bbb;
            }
        """)
        button_layout.addWidget(back_button)

        # Add widgets to the form layout
        layout1.addRow(email_label, self.staff_email_LE)
        layout1.addRow(password_label, self.staff_password_LE)
        layout1.addRow(button_layout)

        # Connect buttons to their respective functions
        login_button.clicked.connect(self.check_staff_login)  # Call the login validation method
        back_button.clicked.connect(self.show_main_menu)  # Return to the main menu
    
    def setup_staff_creation_view(self):
        layout = QW.QVBoxLayout(self.staff_creation_view)

        # Logo image on screen
        scaled_image = QG.QPixmap('Studentum/assets/icon.png').scaled(600, 600, QC.Qt.KeepAspectRatio, QC.Qt.SmoothTransformation)
        logo_label = QW.QLabel(self.staff_creation_view)
        layout.addWidget(logo_label)
        logo_label.setPixmap(scaled_image)
        logo_label.setAlignment(QC.Qt.AlignHCenter)
        
        title_label = QW.QLabel()
        layout.addWidget(title_label)
        title_label.setText("Create a New Staff Account")
        title_label.setAlignment(QC.Qt.AlignHCenter)
        title_label.setMaximumHeight(100)
        title_label.setStyleSheet(
            "font-size: 30px;"
            "font-family: Arial;"
            "font-weight: semi-bold;"
            "background-color: white;"
        )

        # Frame to hold the form
        frame1 = QW.QFrame()
        layout.addWidget(frame1)
        layout1 = QW.QFormLayout(frame1)
        layout1.setAlignment(QC.Qt.AlignTop)
        layout1.setContentsMargins(600, 0, 600, 200)
        layout1.setSpacing(20)
        
        first_name_label = QW.QLabel("First Name")
        first_name_label.setStyleSheet("""
                QLabel {
                    font-size: 17px;
                    font-family: Arial;
                }
            """)
        last_name_label = QW.QLabel("Last Name")
        last_name_label.setStyleSheet("""
                QLabel {
                    font-size: 17px;
                    font-family: Arial;
                }
            """)
        email_label = QW.QLabel("Email")
        email_label.setStyleSheet("""
                QLabel {
                    font-size: 17px;
                    font-family: Arial;
                }
            """)
        password_label = QW.QLabel("Password")
        password_label.setStyleSheet("""
                QLabel {
                    font-size: 17px;
                    font-family: Arial;
                }
            """)
        mobile_label = QW.QLabel("Mobile Number")
        mobile_label.setStyleSheet("""
                QLabel {
                    font-size: 17px;
                    font-family: Arial;
                }
            """)
        self.first_name_LE = QW.QLineEdit()
        self.first_name_LE.setStyleSheet("""
            QLineEdit {
                background-color: #f0f0f0;
                border-radius: 10px;
                padding: 10px;
                font-size: 17px;
            }
        """)
        self.last_name_LE = QW.QLineEdit()
        self.last_name_LE.setStyleSheet("""
            QLineEdit {
                background-color: #f0f0f0;
                border-radius: 10px;
                padding: 10px;
                font-size: 17px;
            }
        """)
        self.email_LE = QW.QLineEdit()
        self.email_LE.setStyleSheet("""
            QLineEdit {
                background-color: #f0f0f0;
                border-radius: 10px;
                padding: 10px;
                font-size: 17px;
            }
        """)
        self.password_LE = QW.QLineEdit()
        self.password_LE.setEchoMode(QW.QLineEdit.Password)
        self.password_LE.setStyleSheet("""
            QLineEdit {
                background-color: #f0f0f0;
                border-radius: 10px;
                padding: 10px;
                font-size: 17px;
            }
        """)
        self.mobile_LE = QW.QLineEdit()
        self.mobile_LE.setStyleSheet("""
            QLineEdit {
                background-color: #f0f0f0;
                border-radius: 10px;
                padding: 10px;
                font-size: 17px;
            }
        """)
        self.mobile_LE.setInputMask("+999 99 999 9999")
        self.mobile_LE.setMaxLength(15)
        
        button_layout = QW.QHBoxLayout()

        # Submit button
        submit_button = QW.QPushButton("Create")
        submit_button.setCursor(QC.Qt.PointingHandCursor)
        submit_button.setStyleSheet("""
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
        button_layout.addWidget(submit_button)

        # Back button
        back_button = QW.QPushButton("Back")
        back_button.setCursor(QC.Qt.PointingHandCursor)
        back_button.setStyleSheet("""
            QPushButton {
                background-color: #ccc;
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
                background-color: #bbb;
            }
        """)
        button_layout.addWidget(back_button)
        
        # Add widgets to the layout
        layout1.addRow(first_name_label, self.first_name_LE)
        layout1.addRow(last_name_label, self.last_name_LE)
        layout1.addRow(email_label, self.email_LE)
        layout1.addRow(password_label, self.password_LE)
        layout1.addRow(mobile_label, self.mobile_LE)
        layout1.addRow(button_layout)
        
        # TODO: Disable submit button until all fields are filled
                 
        submit_button.clicked.connect(self.create_staff_account)
        submit_button.clicked.connect(self.show_staff_login_screen)
        
        back_button.clicked.connect(self.show_main_menu)
    
    def setup_staff_main_view(self):
        layout = QW.QVBoxLayout(self.staff_main_view)

        # Title label
        title_label = QW.QLabel("Staff Main View")
        title_label.setAlignment(QC.Qt.AlignCenter)
        title_label.setStyleSheet("font-size: 30px; font-family: Arial; font-weight: bold; color: #333;")
        layout.addWidget(title_label)

        # Toolbar layout
        toolbar_layout = QW.QHBoxLayout()

        # Add toolbar buttons
        quick_view_button = QW.QPushButton("Quick View")
        quick_view_button.setStyleSheet("""
            QPushButton {
                background-color: #3E71DF;
                color: white;
                font-size: 16px;
                font-family: Arial;
                border-radius: 10px;
                padding: 10px 20px;
            }
            QPushButton:hover {
                background-color: #4681FF;
            }
        """)
        toolbar_layout.addWidget(quick_view_button)

        statistics_button = QW.QPushButton("Statistics")
        statistics_button.setStyleSheet("""
            QPushButton {
                background-color: #3E71DF;
                color: white;
                font-size: 16px;
                font-family: Arial;
                border-radius: 10px;
                padding: 10px 20px;
            }
            QPushButton:hover {
                background-color: #4681FF;
            }
        """)
        toolbar_layout.addWidget(statistics_button)

        courses_button = QW.QPushButton("Courses")
        courses_button.setStyleSheet("""
            QPushButton {
                background-color: #3E71DF;
                color: white;
                font-size: 16px;
                font-family: Arial;
                border-radius: 10px;
                padding: 10px 20px;
            }
            QPushButton:hover {
                background-color: #4681FF;
            }
        """)
        toolbar_layout.addWidget(courses_button)

        students_button = QW.QPushButton("Students")
        students_button.setStyleSheet("""
            QPushButton {
                background-color: #3E71DF;
                color: white;
                font-size: 16px;
                font-family: Arial;
                border-radius: 10px;
                padding: 10px 20px;
            }
            QPushButton:hover {
                background-color: #4681FF;
            }
        """)
        toolbar_layout.addWidget(students_button)

        # Add a spacer to push the "Profile" button to the right
        toolbar_layout.addStretch()

        profile_button = QW.QPushButton("Profile")
        profile_button.setStyleSheet("""
            QPushButton {
                background-color: #3E71DF;
                color: white;
                font-size: 16px;
                font-family: Arial;
                border-radius: 10px;
                padding: 10px 20px;
            }
            QPushButton:hover {
                background-color: #4681FF;
            }
        """)
        toolbar_layout.addWidget(profile_button)

        # Add the toolbar layout to the main layout
        layout.addLayout(toolbar_layout)

        # Create a table to display student information
        self.student_table = QW.QTableWidget()
        self.student_table.setRowCount(5)  # Number of rows (fake students)
        self.student_table.setColumnCount(4)  # Number of columns (e.g., Name, Age, Email, Grade)
        self.student_table.setHorizontalHeaderLabels(["Name", "Age", "Email", "Grade"])
        self.student_table.horizontalHeader().setStretchLastSection(True)
        self.student_table.horizontalHeader().setSectionResizeMode(QW.QHeaderView.Stretch)
        self.student_table.setStyleSheet("""
            QTableWidget {
                font-size: 16px;
                font-family: Arial;
                border: 1px solid #ccc;
                border-radius: 5px;
            }
            QHeaderView::section {
                background-color: #f0f0f0;
                font-size: 16px;
                font-family: Arial;
                font-weight: bold;
                padding: 5px;
                border: 1px solid #ccc;
            }
        """)

        # Add fake student data to the table
        fake_students = [
            ["John Doe", "20", "john.doe@example.com", "A"],
            ["Jane Smith", "22", "jane.smith@example.com", "B"],
            ["Alice Johnson", "19", "alice.johnson@example.com", "A"],
            ["Bob Brown", "21", "bob.brown@example.com", "C"],
            ["Charlie White", "23", "charlie.white@example.com", "B"]
        ]
        for row, student in enumerate(fake_students):
            for col, value in enumerate(student):
                self.student_table.setItem(row, col, QW.QTableWidgetItem(value))

        layout.addWidget(self.student_table)

        # Add a logout button
        logout_button = QW.QPushButton("Logout")
        logout_button.setStyleSheet("""
            QPushButton {
                background-color: #ccc;
                color: black;
                font-size: 16px;
                font-family: Arial;
                border-radius: 10px;
                padding: 10px 20px;
            }
            QPushButton:hover {
                background-color: #bbb;
            }
        """)
        layout.addWidget(logout_button)
        logout_button.clicked.connect(self.show_main_menu)
    
    # Activate the view
    def show_main_menu(self):
        self.stacked_widget.setCurrentWidget(self.startup_view)
    
    def show_student_login_screen(self):
        self.stacked_widget.setCurrentWidget(self.student_login_view)
    
    def show_staff_login_screen(self):
        self.stacked_widget.setCurrentWidget(self.staff_login_view)
    
    def show_staff_creation_screen(self):
        self.stacked_widget.setCurrentWidget(self.staff_creation_view)

    def show_staff_main_view(self):
        self.stacked_widget.setCurrentWidget(self.staff_main_view)
    
    def create_staff_account(self):
        self.first_name_LE.text()
        data = {
            "first_name": self.first_name_LE.text(),
            "last_name": self.last_name_LE.text(),
            "email": self.email_LE.text(),
            "password": self.password_LE.text(),
            "mobile": self.mobile_LE.text()
        }
        try:
            with open('Studentum/staff.json', 'r') as f:
                existing_data = json.load(f)
        # If the file doesn't exist or is empty, start with an empty list
        except (FileNotFoundError, json.JSONDecodeError):
            existing_data = []

        # Append the new data
        existing_data.append(data)

        # Write the updated data back to the JSON file
        with open('Studentum/staff.json', 'w') as f:
            json.dump(existing_data, f, indent=4)
    
    def check_staff_login(self):
        # Get the entered email and password
        email = self.staff_email_LE.text()
        password = self.staff_password_LE.text()

        # Load the staff data from the JSON file
        try:
            with open('Studentum/staff.json', 'r') as f:
                staff_data = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            QW.QMessageBox.warning(self, "Error", "No staff accounts found. Please create an account first.")
            return

        # Check if the email and password match any entry
        for staff in staff_data:
            if staff.get("email") == email and staff.get("password") == password:
                QW.QMessageBox.information(self, "Success", "Login successful!")
                # Proceed to the staff main view
                self.show_staff_main_view()
                return

        # If no match is found, show an error message
        QW.QMessageBox.warning(self, "Error", "Invalid email or password. Please try again.")
        
#--------------------------------
if __name__ == "__main__":
    app = QW.QApplication(sys.argv)
    app.setStyle('fusion')
    
    pixmap = QG.QPixmap('Studentum/assets/icon.png')
    splash = QW.QSplashScreen(pixmap)
    splash.show()
    app.processEvents()
    time.sleep(3)                           # Let splashscreen load 2 s
    splash.hide()                    
        
    appWindow = MainWindow()                # Open main window
    appWindow.show()
    sys.exit(app.exec())