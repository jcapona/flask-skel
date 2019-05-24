from flask import Flask, request, abort, jsonify


app = Flask(__name__)


@app.route('/api/v1/')
def root():
    return jsonify({'field': 'response'})


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def other_routes(path):
    abort(400, {'message': 'Invalid route'})


@app.errorhandler(400)
def custom400(error=None):
    msg = error.description['message'] if error else 'Bad request'
    return jsonify({'error':  msg})


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000, use_reloader=False, threaded=True)

