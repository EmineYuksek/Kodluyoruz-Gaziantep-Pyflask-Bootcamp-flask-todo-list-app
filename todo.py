
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Users/okkes/Desktop/ToDoApp/todo.db'
db = SQLAlchemy(app)





@app.route("/")
def index():
    todos = ToDo.query.all()  #tablomuzdaki tüm verileri alıyoruz(all()). Burada todos sözlük yapısında




    return render_template("index.html", todos = todos) #todos u gönderdik

@app.route("/add", methods=["POST"])
def addToDo():
    title = request.form.get("title") # html de name i title olan değerin içeriği eklendi
    content = request.form.get("content")

    newToDo = ToDo(title = title, content = content, complete=False)  #her yeni başlayan todomuz false olarak başlayacak

    db.session.add(newToDo) #oluşturduğumuz metodu db ye gönderdik
    db.session.commit()  #veritabanında değişiklik yapıldığını belirttik
    return redirect(url_for("index")) #işlem sonrasında tekrar index sayfasına dönmek için yönlendirme yapıldı



@app.route('/complete/<string:id>', methods=["GET"])
def completeToDo(id):
    todo = ToDo.query.filter_by(id=id).first()

    if (todo.complete == False):
        todo.complete = True
    else:
        todo.complete = False

    db.session.commit()
    return redirect(url_for("index"))



@app.route("/delete/<string:id>")
def deleteToDo(id):
    todo = ToDo.query.filter_by(id=id).first()
    db.session.delete(todo)
    db.session.commit()  #veritabanında herhangi bir değişiklik yaptığımızda commit kullanmamız gerekir.

    return redirect(url_for("index"))

@app.route("/detail/<string:id>")
def detailToDo(id):
    todo = ToDo.query.filter_by(id=id).first()

    return render_template("detail.html", todo = todo)


class ToDo(db.Model):
    #veritabanı içeriği

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    content = db.Column(db.Text)
    complete = db.Column(db.Boolean)






if __name__=="__main__":
    app.run(debug=True)