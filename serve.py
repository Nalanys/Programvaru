"""Module for serving an API."""

from flask import Flask, send_file
import csv

def lst_to_string(lst):
    str1 = ""
    for ele in lst:
        str1+= ele + " "
    return str1

def serve(options):
    """Serve an API."""

    # Create a Flask application
    app = Flask(__name__)

    @app.route("/")
    def index():
        """Return the index page of the website."""
        return send_file("../www/index.html")

    @app.route("/greeting/<name>")
    def greeting(name):
        """Return a greeting for the user."""
        return "Hello, {}!".format(name)

    @app.route("/data")
    def data():
        ret_str = ""
        CSV = open("/home/pa1450/code/PA1450/application/commands/COVID-19-master/archived_data/archived_daily_case_updates/01-22-2020_1200.csv")
        with CSV as csvfile:
            readCSV = csv.reader(csvfile, delimiter=",")
            for row in readCSV:
                ret_str += lst_to_string(row)
            return ret_str
        
    app.run(host=options.address, port=options.port, debug=True)

def create_parser(subparsers):
    """Create an argument parser for the "serve" command."""
    parser = subparsers.add_parser("serve")
    parser.set_defaults(command=serve)
    # Add optional parameters to control the server configuration
    parser.add_argument("-p", "--port", default=8080, type=int, help="The port to listen on")
    parser.add_argument("--address", default="0.0.0.0", help="The address to listen on")
