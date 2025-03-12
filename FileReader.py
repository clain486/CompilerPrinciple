class FileReader:
    def __init__(self, filename):
        self.filename = filename
        self.data = ""
        with open(self.filename, "r", encoding="utf-8") as f:
            self.data = f.read()

    def __str__(self):
        return self.data

    def content(self):
        return self.data
