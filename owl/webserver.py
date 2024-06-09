from config import load_config
import http.server
import socketserver
from jinja2 import Template


def write_to_template():
    data = load_config('../config.json')

    with open('template.html.jinja') as f:
        tmpl = Template(f.read())

    output_from_parsed_template = tmpl.render(domain_list=data['domains'])
    with open("index.html", "w") as fh:
        fh.write(output_from_parsed_template)


def run(server_port=8000):
    port = server_port
    Handler = http.server.SimpleHTTPRequestHandler

    with socketserver.TCPServer(("", port), Handler) as httpd:
        print("serving at port", port)
        httpd.serve_forever()


if __name__ == "__main__":
    write_to_template()
    run()
