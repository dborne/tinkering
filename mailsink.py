import smtpd
import asyncore
import os
import datetime


def touchfolder(*folders):
    folder = '/'.join(folders)
    if not os.path.exists(folder):
        os.makedirs(folder)
base = 'mail'


class mailsink(smtpd.SMTPServer):
    def process_message(self, peer, mailfrom, rcpttos, data):
        mailfrom = str(mailfrom)
        print('recieved message from %s\n' % str(peer))
        stamp = datetime.datetime.utcnow().strftime('%Y.%m.%d.%H.%M.%S')
        for rcpt in rcpttos:
            who, where = rcpt.split('@', 1)
            if where in ('dborne.com', 'annasarts.com'):
                touchfolder(base, where, who)
                f = open('/'.join([base, where, who, mailfrom, stamp]), 'w')
                f.write('message from: %s\n' % str(peer))
                f.write('addressed from: %s\n' % str(mailfrom))
                f.write('addressed to: %s\n' % str(rcpttos))
                f.write('data\n-----------------\n\n %s\n' % str(data))
                f.close()
        return

if __name__ == '__main__':
    print('setting up server')
    server = mailsink(('0.0.0.0', 25), None)
    try:
        asyncore.loop()
    except KeyboardInterrupt:
        print('interrupted, shutting down\n')
        server.close()
