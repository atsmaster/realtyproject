import configparser


class CommProperty:
    service_key = ""

    def __init__(self):
        self.load_service_key()

    def load_service_key(self):
        properties = configparser.ConfigParser()
        properties.read('C:/workspace_python/config.ini')
        service_key = properties.get('DATAGO', 'SERVICE_KEY')
        self.service_key = service_key

