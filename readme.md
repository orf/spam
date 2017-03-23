# spam

[![Build Status](https://travis-ci.org/orf/spam.svg?branch=master)](https://travis-ci.org/orf/spam)

This is a small utility that connects to an IMAP server and gives you a 
breakdown of who has sent you the most emails.
    
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
        -b, --batch=<batch>     Fetch messes in batches of N [default: 200]
    
    
[![asciicast](https://asciinema.org/a/b9pbyc4ntns1epr3tyvakcifk.png)](https://asciinema.org/a/b9pbyc4ntns1epr3tyvakcifk)