"""
Spam.

Usage:
    spam [--host=<addr>] [--port=<port>] [--email=<email>]
    spam --help
    spam --version

Options:
    --version               Show version
    --help                  Show this help
    -h, --host=<addr>       IMAP host to connect to [default: imap.gmail.com]
    -p, --port=<port>       IMAP SSL port to use [default: 993]
    -u, --email=<email>     Email to login with

"""

from spam.tally import tally_inbox
from ascii_graph import Pyasciigraph
import getpass
import os
import docopt
import pkg_resources


def main():
    try:
        version = pkg_resources.get_distribution('spamfinder').version
    except Exception:
        version = 'Unknown'

    arguments = docopt.docopt(__doc__, version='Spam version {0}'.format(version))

    host = arguments['--host']

    port = arguments['--port']
    if not port.isdigit():
        print('Error: Port must be an integer')
        exit(1)
    else:
        port = int(port)

    user = arguments['--email']
    if user is None:
        user = input('Enter Email: ')

    password = getpass.getpass('Enter password: ')

    result, error_count = tally_inbox(host, port, user, password)

    try:
        width, _ = os.get_terminal_size()
    except Exception:
        width = 80
    else:
        width = max(width, 80)

    graph = Pyasciigraph(line_length=width, min_graph_length=20)

    most_common = [
        ("{0}: {1}".format(key[0], key[1]), value)
        for key, value in result.most_common(50)
    ]

    for line in graph.graph('Most common senders', most_common):
        print(line)


if __name__ == "__main__":
    main()
