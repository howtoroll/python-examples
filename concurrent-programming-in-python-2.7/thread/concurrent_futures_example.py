import sys
import concurrent.futures


URLS = ['http://www.1.com/',
        'http://www.2.com/',
        'http://www.3.com/',
        'http://www.4.com/',
        'http://www.5.com/']


def printURL(url):
    print "Print: " + url
    return "Done"


def main():
    # We can use a with statement to ensure threads are cleaned up promptly
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        # Start the load operations and mark each future with its URL
        future_to_url = {executor.submit(printURL, url): url for url in URLS}

        for future in concurrent.futures.as_completed(future_to_url):
            url = future_to_url[future]
            try:
                data = future.result()
            except Exception as exc:
                print exc
            else:
                print "finish data: " + data + ", url: " + url


if __name__ == "__main__":
    sys.exit(main())
