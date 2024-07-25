from owl.webserver import run
from owl.config import load_config

if __name__ == "__main__":
    data = load_config('config.json')
    if data['ENABLE_WEBSERVER']:
        print(f"{'':#<40}")
        print("\tWebserver starting...")
        print(f"{'':#<40}")
        port = data['WEBSERVER_PORT']
        run(port)
    else:
        print("\t Webserver not enabled")
