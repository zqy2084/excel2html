from flask import Flask, render_template
import flask_restful

from core.excel_handler import excel_reader


EXCEL_FILE = 'datas/test_data.xls'

app = Flask(__name__)
api = flask_restful.Api(app)

@app.route("/")
def index():
    return render_template('index.html')

class ExcealReader(flask_restful.Resource):
    def get(self):
        # return only the first sheet data
        return excel_reader(EXCEL_FILE)[0]

api.add_resource(ExcealReader, '/data')

if __name__ == '__main__':
    app.run(debug=True)
