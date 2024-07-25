import http.server
import socketserver
from jinja2 import Template
from datetime import datetime


def write_to_template(data):

    with open('owl/template.html.jinja') as f:
        tmpl = Template(f.read())

    current_dateTime = datetime.now()
    output_from_parsed_template = tmpl.render(domain_list=data, updated_on=current_dateTime)
    with open("./index.html", "w") as fh:
        fh.write(output_from_parsed_template)


def run(server_port=8000):
    port = server_port
    Handler = http.server.SimpleHTTPRequestHandler

    with socketserver.TCPServer(("", port), Handler) as httpd:
        print("serving at port", port)
        httpd.serve_forever()


if __name__ == "__main__":
    # write_to_template()
    run()
