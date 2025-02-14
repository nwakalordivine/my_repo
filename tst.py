# Building a simple API using flask

from flask import Flask, request, jsonify

app=Flask(__name__)
# to create the flask app

# defining route
@app.route("/")
def hello():
    return "<h2>Hi Donald</h2>"

@app.route('/time', methods=['GET'])
def time():
    user_input = request.args.get("currently", "12:20am")
    return jsonify({"Time": f"Hello Mentor, this is {user_input}"}) 

@app.route('/weather', methods=['GET'])
def weather():
    user_weather_input = request.args.get("weather", "10 degree F")
    return jsonify({"weather": f"it's {user_weather_input} today"}) 

@app.route('/contact', methods=['GET'])
def contact():
    user_name_input = request.args.get("name", "Mentor")
    return jsonify({"contact": f"Hello {user_name_input}, incase you forgot.. my contact is 01234567899"}) 

@app.route('/profession', methods=['GET'])
def profession():
    return jsonify({"profession prefrence": "I plan to build my career mainly in Python, AI, and Machine Learning."}) 

@app.route('/rate', methods=['GET'])
def rate():
    return jsonify({"rate": "Hello Mentor, how did i perform writing this API"}) 

# code for running the app
if __name__ == "__main__":
    app.run(debug=True)  