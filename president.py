from flask import Flask, render_template
from module import convert_to_dict
app = Flask(__name__)

presidents_list=convert_to_dict("president.csv")

@app.route('/')
def index():
    heading = '<h1>Welcome to the presidential Flask example!</h1>'
    test1 = '<p>' + presidents_list[0]['President']
    test2 = ", born in " + presidents_list[0]['Birthplace'] + '.</p>'
    return render_template('index.html', pairs=pairs_list, the_title="Presidents Index")






# keep this as is
if __name__ == '__main__':
    app.run(debug=True)

