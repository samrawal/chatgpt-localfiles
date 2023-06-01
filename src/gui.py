import rumps
import threading
import sys
import serve

class PythonServer(rumps.App):
    def __init__(self):
        super(PythonServer, self).__init__("Python Server")

        window = rumps.Window(message='Enter the base directory to share with ChatGPT:', title='ChatGPT Code Share', default_text='', dimensions=(320, 20), cancel=True)
        window.icon = None
        response = window.run()

        if len(response.text) == 0:
            exit()

        self.server_thread = threading.Thread(target=serve.run_server, args=(response.text.strip(),))
        self.server_thread.start()
        self.title = "🚀 Code Sharing On"
        #rumps.notification(title='Python Server', subtitle='Server Status', message='Server is running!')


if __name__ == "__main__":
    PythonServer().run()
