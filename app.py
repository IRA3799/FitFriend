from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Home redirects to register page
@app.route("/")
def home():
    return redirect(url_for("register"))

# Register page
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        email = request.form.get("student_email")
        password = request.form.get("password")
        confirm = request.form.get("confirm_password")

        if password != confirm:
            return "Passwords do not match. Please enter again."
        return f"Registered with {email}"
    
    return render_template("register.html")


if __name__ == "__main__":
    app.run(debug=True)

