import ftplib

host = "ftp.psu.ac.th"
root = "/pub/"


def list(path):
    with ftplib.FTP(host,user="5635512124") as connecit:
        print("Welcome", connecit.getwelcome())
        for name, details in connecit.mlsd(path):
            print(name, details['type'], details.get('size'))

list(root)
