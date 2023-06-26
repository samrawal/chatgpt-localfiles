import rumps
import threading
import sys
import serve
from PyQt5.QtWidgets import QFileDialog, QApplication
import sys


class PythonServer(rumps.App):
    def __init__(self):
        super(PythonServer, self).__init__("Python Server")

        app = QApplication(sys.argv)
        folder_selected = QFileDialog.getExistingDirectory(
            None, "Select Folder"
        )  # Open the folder picker dialog

        if not folder_selected:
            exit()

        self.server_thread = threading.Thread(
            target=serve.run_server, args=(folder_selected,)
        )
        self.server_thread.start()
        self.title = "\ud83d\ude80 File Sharing"
        # rumps.notification(title='Python Server', subtitle='Server Status', message='Server is running!')


if __name__ == "__main__":
    PythonServer().run()
