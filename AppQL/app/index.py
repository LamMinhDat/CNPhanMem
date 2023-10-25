from flask import Flask, render_template
import dao

app = Flask(__name__)

@app.route("/")
def index():
    cates = dao.get_categories()
    prods = dao.get_products()
    return render_template('index.html' , categories= cates, products= prods)

if __name__ == '__main__':
    app.run(debug=True)