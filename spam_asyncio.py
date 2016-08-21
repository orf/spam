import asyncio
from aioimaplib import aioimaplib
import getpass

try:
    import uvloop

    asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
except ImportError:
    pass

import logging

root = logging.getLogger()
root.setLevel(logging.DEBUG)

aioimaplib_logger = logging.getLogger('aioimaplib.aioimaplib')
sh = logging.StreamHandler()
sh.setLevel(logging.NOTSET)
sh.setFormatter(logging.Formatter("%(asctime)s %(levelname)s [%(module)s:%(lineno)d] %(message)s"))
aioimaplib_logger.addHandler(sh)



def get_input(name, default=None, type=None, func=input):
    return default
    msg = "{0} [{1}]: ".format(name, default) if default else "{0}: ".format(name)
    while True:
        response = func(msg)
        if response:
            if type:
                try:
                    response = type(response)
                except ValueError:
                    print("Please enter a {0}".format(type.__name__))
                    continue

            return response

        elif default:
            return default


async def tally_inbox(host, port, user, password, loop):
    client = aioimaplib.IMAP4_SSL(host, port, loop=loop)
    await client.wait_hello_from_server()

    response = await client.login(user, password)

    if response.result != 'OK':
        print("\n".join(response.lines))
        print("If you're using GMail with 2-factor authentication then you need to create an app-specific password")
        print("Visit https://security.google.com/settings/security/apppasswords to do so")
        exit(1)

    res, data = await client.select()
    total_messages = int(data[0])
    print("Selected INBOX: {0} messages".format(total_messages))
    # res, data = await client.search('ALL')
    chunks = [(number, number + 10) for number in range(1, total_messages + 1, 10)]
    for start, end in chunks:
        res, data = await client.fetch('{0}:{1}'.format(start, end), '(BODY.PEEK[HEADER])')
        print(len(data))


if __name__ == "__main__":
    HOST = get_input("Host", "imap.gmail.com")
    PORT = get_input("Port", aioimaplib.IMAP4_SSL_PORT, type=int)

    USERNAME = "tom@tomforb.es"  # get_input("Username")
    PASSWORD = "dbyjpbgsqrhgzles"  # get_input("Password", func=getpass.getpass)

    loop = asyncio.get_event_loop()
    loop.run_until_complete(tally_inbox(HOST, PORT, USERNAME, PASSWORD, loop))
