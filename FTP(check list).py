import ftplib


host = "ftp.ibiblio.org"
root = "/pub/docs/books/gutenberg/"


def list(path):
    with ftplib.FTP(host,user="anonymous") as connecit:
        print("Welcome", connecit.getwelcome())
        for name, details in connecit.mlsd(path):
            print(name, details['type'], details.get('size'))

list(root)
