import ftplib, sys

host = "ftp.ibiblio.org"
root = "/pub/docs/books/gutenberg/"


def get(fullname, output=sys.stdout):
    with ftplib.FTP(host,user="anonymous") as connecit:
        print("Hello",connecit.getwelcome())
        expected = connecit.size( fullname )
        print("Getting", fullname, "to", output, "size", expected)
        connecit.retrlines("RETR {0}".format(fullname))
    if output != sys.stdout:
        print()  # End the "dots"


get(root+"README")