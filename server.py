from flask import Flask, render_template, session, redirect, request
from users_class import Users                                           # Impo

app = Flask(__name__)
app.secret_key = "TiYSKDNRitA!"                                         # This is Your Secret Key Do Not Reveal it to Anyone!

@app.route('/')                                                         # Main Page
def index():
    print("******** in index *******************")


    return render_template("index.html")

@app.route('/users')                                                    # Read All Users Page
def users():
    print("**** Retrieving Users *******************")
    all_user_instances = Users.get_all()                                # Get all instances of users from the database
    for idx in range(len(all_user_instances)):
        print(f"Index: {idx} ::: User Name: {all_user_instances[idx].first_name} {all_user_instances[idx].last_name}")

    return render_template("read_all.html", all_user_instances = all_user_instances)

@app.route('/users/new')                                                # Create New Users Page
def users_new():
    print("******** in New Users *******************")


    return render_template("create.html")

# @app.route('/create_friend', methods=["POST"])
# def create_friend():
#     # First we make a data dictionary from our request.form coming from our template.
#     # The keys in data need to line up exactly with the variables in our query string.
#     data = {
#         "first_name": request.form["fname"],
#         "last_name" : request.form["lname"],
#         "occupation" : request.form["occ"]
#     }
#     # We pass the data dictionary into the save method from the Friend class.
#     Friend.save(data)
#     # Don't forget to redirect after saving to the database.
#     return redirect('/')

# @app.route('/increment_by', methods=['POST'])
# def increment_by():

#     return redirect("/")

# **** Ensure that if the user types in any route other than the ones specified, 
#           they receive an error message saying "Sorry! No response. Try again ****
@app.errorhandler(404) 
def invalid_route(e): 
    return "Sorry! No response. Try again."

if __name__=="__main__":   
    app.run(debug=True)    