from flask import Flask

import potsdb, requests, traceback

app = Flask(__name__)

# @app.route('/')
def index() -> str:
    url = "http://opentsdb:4242"
    http_response = requests.get(url)
    print("Status code is: ")
    print(http_response.status_code)

    client = potsdb.Client('opentsdb', check_host=True, port=4242)
    
    print("Connection checked!\n")

    try:
        client.close()
    except Exception:
        traceback.print_exc()

    print("Client closed!\n")

    return "Ok"

if __name__ == "__main__":
    # app.run(host='0.0.0.0')
    index()