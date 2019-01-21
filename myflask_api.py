from flask import Flask, jsonify, request


app = Flask(__name__)

languages = [{'name':'Python'},{'name':'Java'},{'name':'Perl'}]

@app.route("/")
def welcome():
    return "Hello from Python"
    

@app.route('/profile/<username>')
def hello(username):
    return "<h2>Hii %s</h2>" %username

@app.route('/posts/<int:ids>', methods=['GET'])
def api(ids):
    return jsonify({"Post%d"%ids:'It works'})

#@app.route('/posts/<lang>', methods=['GET'])
#def language_get(lang):
#    languge = [i for i in languages if i['name']==lang]
#    return jsonify({"lang":languge[0]})


@app.route('/posts/', methods=['GET'])
def language_returnall():
    return jsonify({'languages':languages})


@app.route('/posts/', methods=['POST'])
def language_post():
    languge = {'name': request.json['name']}
    languages.append(languge)
    return jsonify({'languages':languages})


@app.route('/posts/<lang>', methods=['PUT'])
def language_editone(lang):
    language = [i for i in languages if i['name']==lang]
    language[0]['name'] = request.json['name']
    return jsonify({'languages':languages})


@app.route('/posts/<lang>', methods=['DELETE'])
def language_deleteone(lang):
    language = [i for i in languages if i['name']==lang]
    languages.remove(language[0])
    return jsonify({'languages':languages})


if __name__ == '__main__':
    app.run(debug=True)
