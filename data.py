import hashlib

# Just a POCO
class UrlData:
    def __init__(self, url):
        self.url = url
        self.hashUrl = hashlib.md5(url.encode()).hexdigest()
        self.job_description = []
        self.job_description_tokens = []
        self.job_title = ""

    def set_job_description(self, text):
        self.job_description = text
        self.job_description_tokens = text.split(" ")

    def test(self):
        print("this is a test")