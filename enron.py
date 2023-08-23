"""
Read emails from a file and store its data points 
"""
import sys
import string
import re
import csv
import argparse



class Server: 
    """
    __init__(self, path)
    Server reads a file with emails and sorts their data into variables
    """
    def __init__(self, path):
        
        a = open(path)
        emailp = a.read()

        self.emails = []

        for email in emailp:
            emailp.append(re.sub('["]','', email))
        for email in emailp:
            self.emails.append(email)

        x = self.emails

        for email in x:
            Email.message_id.append(re.compile(r"Message-ID:\s(.*)")).search(x)[1] 
            Email.date.append(re.compile(r"Date:\s(.*)")).search(x)[1]
            Email.subject.append(re.compile(r"Subject:\s(.*)")).search(x)[1]
            Email.sender.append(re.compile(r"From:\s(.*)")).search(x)[1]
            Email.reciever.append(re.compile(r"To:\s(.*)")).search(x)[1]
            Email.body.append(re.compile(r"$")).search(x)[1] # :(



class Email:
    """
    __init__(self, message_id, date, subject, sender, reciever, body)
    Email collects the data points from the file passed to Server and stores them in its attributes
    """
    def __init__(self, message_id, date, subject, sender, reciever, body):
        self.message_id = message_id
        self.date = date
        self.subject = subject
        self.sender = sender
        self.reciever = reciever
        self.body = body



def main(path):
    """
    Returns the length of the number of total emails in the file
    """
    myServer = Server(path)
    x = len(myServer.emails)
    return x


def parse_args(args_list):
    """
    Error message if path was not specified from the console
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('required', type = str, help = 'Path to text file is required')

    args = parser.parse_args(args_list)
    return args


if __name__ == "__main__":
    arguments = parse_args(sys.argv[1:])
    main(arguments.required)
    