# spam

This is a small utility that connects to an IMAP server and gives you a 
breakdown of who has sent you the most emails.
    
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
    