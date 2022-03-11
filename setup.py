import requests

URL = "https://ndownloader.figshare.com/files/10717177"

def main():
    """
    Quick script for downloading required data
    """

    req = requests.get(URL, stream=True)

    with open("surveys.csv", 'wb') as fd:
        for chunk in req.iter_content(chunk_size=128):
            fd.write(chunk)

    print("Data downloaded!")


if __name__ == '__main__':
    main()