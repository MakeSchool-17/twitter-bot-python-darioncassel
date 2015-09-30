import requests


def main():
    urls = prepare_urls()
    with open("corpus.txt", "w") as file:
        corpus = ""
        for url in urls:
            request_url = "http://api.diffbot.com/v3/article"
            params = {'token': '640f89858861a736e8c6dcdc9f454411',
                      'url': url,
                      'discussion': False}
            corpus += request(request_url, params)
        file.write(corpus)


def prepare_urls():
    urls = []
    lines = open("pages.txt").readlines()
    for line in lines:
        url = line.split("\n")[0]
        urls.append(url)
    return urls


def request(url, params):
    response = requests.get(url, params)
    response = response.json()['objects'][0]
    return response["text"]

if __name__ == "__main__":
    main()
    print("Complete")
