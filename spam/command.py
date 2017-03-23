"""
Spam.

Usage:
    spam [--host=<addr>] [--port=<port>] [--email=<email>] [--show=<count>] [--batch=<batch>]
    spam --help
    spam --version

Options:
    --version               Show version
    --help                  Show this help
    -h, --host=<addr>       IMAP host to connect to [default: imap.gmail.com]
    -p, --port=<port>       IMAP SSL port to use [default: 993]
    -u, --email=<email>     Email to login with
    -s, --show=<count>      Show top N senders [default: 50]
    -b, --batch=<batch>     Fetch messes in batches of N [default: 250]

"""

from spam.tally import tally_inbox
from ascii_graph import Pyasciigraph
import getpass
import os
import docopt
import pkg_resources


def get_int(value, name):
    if not value.isdigit():
        print('Error: {0} must be an integer'.format(name))
        exit(1)
    else:
        return int(value)


def main():
    try:
        version = pkg_resources.get_distribution('spamfinder').version
    except Exception:
        version = 'Unknown'

    arguments = docopt.docopt(__doc__, version='Spam version {0}'.format(version))

    host = arguments['--host']

    port = get_int(arguments['--port'], 'Port')
    count = get_int(arguments['--show'], 'Count')
    batchsize = get_int(arguments['--batch'], 'Batch')

    user = arguments['--email']
    if user is None:
        user = input('Enter Email: ')

    password = getpass.getpass('Enter password: ')

    result, error_count = tally_inbox(host, port, user, password, batchsize)

    try:
        width, _ = os.get_terminal_size()
    except Exception:
        width = 80
    else:
        width = max(width, 80)

    print()

    graph = Pyasciigraph(line_length=width, min_graph_length=20)

    most_common = [
        ('{0}: {1}'.format(key[0], key[1]), value)
        for key, value in result.most_common(count)
    ]

    for line in graph.graph('Top senders:', most_common):
        print(line)


if __name__ == "__main__":
    main()
