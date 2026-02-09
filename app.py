from flask import Flask, render_template, request, redirect, url_for, flash
from bank import Bank

app = Flask(__name__)
app.secret_key = "123456"

bank = Bank()

@app.route("/")
def index():
    return render_template("dashboard.html")

@app.route("/create", methods=["GET", "POST"])
def create():
    if request.method == "POST":
        acc = bank.Createaccount(
            request.form["name"],
            int(request.form["age"]),   # ✅ IMPORTANT
            request.form["email"],
            request.form["pin"]
        )
        flash(f"Account Created! Account No: {acc}")
        return redirect(url_for("index"))
    return render_template("create.html")

@app.route("/deposit", methods=["GET", "POST"])
def deposit():
    if request.method == "POST":
        msg = bank.depositmoney(
            request.form["accountNo"],
            request.form["pin"],
            int(request.form["amount"])
        )
        flash(msg)
        return redirect(url_for("index"))
    return render_template("deposit.html")

@app.route("/withdraw", methods=["GET", "POST"])
def withdraw():
    if request.method == "POST":
        msg = bank.withdrawmoney(
            request.form["accountNo"],
            request.form["pin"],
            int(request.form["amount"])
        )
        flash(msg)
        return redirect(url_for("index"))
    return render_template("withdraw.html")

@app.route("/details", methods=["GET", "POST"])
def details():
    user = None
    if request.method == "POST":
        user = bank.showdetails(
            request.form["accountNo"],
            request.form["pin"]
        )
        if not user:
            flash("Account not found")
    return render_template("details.html", user=user)

@app.route("/update", methods=["GET", "POST"])
def update():
    if request.method == "POST":
        msg = bank.update_account(
            request.form["accountNo"],
            request.form["pin"],
            request.form["name"],
            request.form["email"],
            request.form["new_pin"]
        )
        flash(msg)
        return redirect(url_for("index"))
    return render_template("update.html")

@app.route("/delete", methods=["GET", "POST"])
def delete():
    if request.method == "POST":
        msg = bank.delete_account(
            request.form["accountNo"],
            request.form["pin"]
        )
        flash(msg)
        return redirect(url_for("index"))
    return render_template("delete.html")

if __name__ == "__main__":
    app.run(debug=True)