from flask import Flask, render_template, request, jsonify
from game import get_all_situations

app = Flask(__name__)
app.config['SECRET_KEY'] = '7b7e30111ddc1f8a5b1d80934d336798'


@app.route('/')
def index():
    return render_template('index.html', data=None)


@app.route('/api/run', methods=['GET', 'POST'])
def form():
    # Get request from js.
    if request.method == 'POST':
        # Get data from js.
        data = request.get_json()
        t = data['t']
        situation = data['situation']
        if situation == 'null':
            situation = get_all_situations()[0]
        else:
            pass
        
        print(situation)

        # Return data to js.
        return jsonify({'t': t, 'situation': situation.to_dict()})


if __name__ == '__main__':
    app.run(debug=True)
