from owl.webserver import run, write_to_template
from owl.config import load_config

if __name__ == "__main__":
    data = load_config('config.json')
    if data['ENABLE_WEBSERVER']:
        print("\t Webserver starting webserver")
        run()
    else:
        print("\t Webserver not enabled")
