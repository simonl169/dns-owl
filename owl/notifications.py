import requests
from config import load_config


class Notifier:
    def __init__(self):
        self.data = load_config('../config.json')
        self.ntfy_server = self.data['NOTIFY_SERVER']

    def send_success(self, message: str = "Generic success message"):
        message = "🟢 Success: " + message
        requests.post(self.ntfy_server, data=message.encode(encoding='utf-8'))

    def send_warning(self, message: str = "Generic warning message"):
        message = "⚠️ Warning: " + message
        requests.post(self.ntfy_server, data=message.encode(encoding='utf-8'))

    def send_error(self, message: str = "Generic error message"):
        message = "🚩 Error: " + message
        requests.post(self.ntfy_server, data=message.encode(encoding='utf-8'))


if __name__ == "__main__":

    test_notifier = Notifier()
    test_notifier.send_success()
    test_notifier.send_warning()
    test_notifier.send_error()

    # test_notifier = None
    # if test_notifier:
    #     print('ladida')
