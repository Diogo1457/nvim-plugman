import os

class File():
    def read(filename):
        if not os.path.isfile(filename):
            return ""
        with open(filename, "rt") as f:
            content = f.read()
            f.close()
        return content


    def write(filename, content, mode="wt+"):
        with open(filename, mode) as f:
            f.write(content)
            f.close()

