from flask import Flask, render_template, request, redirect, Response
from flask_cors import CORS, cross_origin
import main_script as sc
app = Flask(__name__)
cors = CORS(app)


news_obj = sc.NewsAnalyzer()

@app.route('/output_prob1', methods = ['POST'])
def output_prob1():
    data = request.get_json()
    return str(news_obj.prob1(float(data['t1']),float(data['t2'])))
@app.route('/output_prob2', methods = ['POST'])
def output_prob2():
    return str(news_obj.prob2())
@app.route('/output_prob3', methods = ['POST'])
def output_prob3():
    data = request.get_json()
    return str(news_obj.prob3(int(data['n'])))




if __name__ == "__main__":
    app.run(host= '0.0.0.0')

