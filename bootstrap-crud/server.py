from flask import Flask, render_template, request, redirect, url_for
from model_module import db, Cliente

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
db.init_app(app)
db.create_all(app=app)

@app.route("/remove_client/<int:id>")
def remove_client_route(id):
    client = Cliente.query.filter_by(_id=id).first()
    db.session.delete(client)
    db.session.commit()
    return redirect(url_for("list_client_route"))


@app.route("/add_client", methods=['POST','GET'])
def add_client():
    if request.method == "POST":
        email = (request.form.get("email"))
        if email:
            c = Cliente(email)
            db.session.add(c)
            db.session.commit()
        # return to list_client_route
        action = redirect(url_for("list_client_route"))
    else:
        action = render_template("add_client.html")

    return action


@app.route("/")
def list_client_route():
    clients = Cliente.query.all()
    return render_template("list_client.html", clients=clients)


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
