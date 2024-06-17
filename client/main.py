import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget
import requests
from requests.exceptions import RequestException, Timeout, ConnectionError

class MainWindow(QMainWindow):
    """
    Main window class for the TroubleShooter Client application.
    This class sets up the GUI and handles server ping functionality.
    """

    def __init__(self):
        """
        Initialize the main window and its UI components.
        """
        super().__init__()
        self.initUI()

    def initUI(self):
        """
        Initialize the UI components of the main window.
        Sets up the window properties and layout.
        """
        self.setWindowTitle('TroubleShooter Client')
        self.setGeometry(100, 100, 800, 600)

        layout = QVBoxLayout()
        button = QPushButton('Ping Server', self)
        button.clicked.connect(self.ping_server)

        layout.addWidget(button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def ping_server(self):
        """
        Ping the server to check its status.
        Makes an HTTP GET request to the server's /ping endpoint.
        """
        try:
            response = requests.get('http://127.0.0.1:5000/ping', timeout=5)
            if response.status_code == 200:
                print('Server is up!')
            else:
                print('Server is down!')
        except Timeout:
            print('Error: The request timed out')
        except ConnectionError:
            print('Error: Failed to connect to the server')
        except RequestException as e:
            print(f'Error: An error occurred: {e}')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())
