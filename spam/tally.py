import imaplib
from email.parser import HeaderParser
from email.header import decode_header
from email.utils import parseaddr
from collections import Counter
from tqdm import tqdm

parser = HeaderParser()


def tally_inbox(host, port, user, password, batchsize):
    TALLY, ERRORS = Counter(), 0

    if batchsize is None:
        batchsize = 200

    print("Connecting to {0}:{1}".format(host, port))
    client = imaplib.IMAP4_SSL(host, port)

    print("Attempting to authenticate...")
    try:
        client.login(user, password)
    except imaplib.IMAP4.error as e:
        print(b"\n".join(e.args))
        print("If you're using GMail with 2-factor authentication then you need to create an app-specific password")
        print("Visit https://security.google.com/settings/security/apppasswords to do so")
        exit(1)

    res, data = client.select()
    total_messages = int(data[0])
    print("Selected INBOX: {0} messages".format(total_messages))
    # res, data = await client.search('ALL')
    chunks = [(number, number + (batchsize - 1)) for number in range(1, total_messages + 1, batchsize)]
    print("Fetching messages in {0} chunks of {1}".format(len(chunks), batchsize))

    for start, end in tqdm(chunks):
        res, data = client.fetch("{0}:{1}".format(start, end), '(BODY.PEEK[HEADER])')
        for message in data:
            if not isinstance(message, tuple):
                continue

            try:
                headers = message[1]
                msg = parser.parsestr(headers.decode())
                realname, emailaddr = parseaddr(msg["From"])
                result = decode_header(realname)
                realname, encoding = result[0]
                if isinstance(realname, bytes):
                    realname = realname.decode(encoding)

                if realname or emailaddr:
                    TALLY[(realname, emailaddr)] += 1
            except Exception:
                pass

    return TALLY, ERRORS
