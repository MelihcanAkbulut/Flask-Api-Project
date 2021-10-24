from flask import Flask,request, jsonify
import business

app = Flask(__name__)

@app.route("/")
def index():
    return "Home"


@app.route('/api/v1/malware', methods = ['GET','POST'])
def malware():
    if request.method == 'GET':
        data = business.listAllMalware()
        return data
    if request.method == 'POST':
        business.scan()
        return jsonify(data = "Kaynaklar tarandı ve eksikler veri tabanına kayıt edildi")


@app.route('/api/v1/malware/count', methods = ['GET'])
def count():
    countMalware = business.count()
    return jsonify(data = "Veri tabanındaki malware kayıt sayısı {}".format(countMalware))


@app.route('/api/v1/malware/<int:id>', methods = ['GET','DELETE'])
def processId(id:int):
    if request.method == 'GET':
        detail = business.malwareDetail(id=id)
        return detail
    if request.method == 'DELETE':
        business.deleteMalware(id=id)
        return jsonify(data = "{} id'li malware silindi".format(id))


if __name__ == "__main__":
    app.run(debug=True)