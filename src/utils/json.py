import json
from utils.file import File


class Json():
    def read(filename):
        content = File.read(filename)
        return json.loads(content)
