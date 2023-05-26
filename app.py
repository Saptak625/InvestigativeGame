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
        t = int(data['t'])
        max_t = int(data['max_t'])
        situation = data['situation']
        print(f'_{situation}_')
        if situation == 'null':
            print('null')
            situation = get_all_situations()[0]
        else:
            decision = int(data['decision'])
            # print(f'_{situation}_')
            situation = [i for i in get_all_situations() if i.name == situation][0]
            desc, new = situation.run(decision, t=t, max_t=max_t)
            return jsonify({'t': t+1, 'situation': new.to_dict() if new else new, 'desc': desc})
        
        # print(f'_{situation}_')

        # Return data to js.
        return jsonify({'t': t+1, 'situation': situation.to_dict(), 'desc': ''})


if __name__ == '__main__':
    app.run(debug=True)
