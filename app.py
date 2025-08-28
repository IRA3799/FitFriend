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
            return "Passwords do not match!"
        return f"Registered with {email}"
    
    return render_template("register.html")

# Dummy routes for navbar buttons
@app.route("/find-partner")
def find_partner():
    return "🔎 Find Partner Page"

@app.route("/activity")
def activity():
    return "📊 My Activity Page"

@app.route("/profile")
def profile():
    return "👤 Profile Page"

@app.route("/logout")
def logout():
    return "👋 Logged out!"


if __name__ == "__main__":
    app.run(debug=True)

