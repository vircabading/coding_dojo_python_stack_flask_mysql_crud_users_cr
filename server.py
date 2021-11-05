from flask import render_template, session, redirect, request
from flask_app import app                                               # Import flask app


from users_class import Users                                           # Import



# //// SHOW /////////////////////////////////////

@app.route('/')                                                         # Main Page
def index():
    print("******** in index *******************")
    return render_template("index.html")

@app.route('/users/new')                                                # **** FORM **** Create 1 New Users Page
def users_new():
    print("******** in New Users *******************")
    return render_template("create.html")

@app.route('/users/<int:id>/update')                                      # **** FORM **** Edit 1 User Page
def users_id_updqte(id):
    print("********* In Users ID Edit ****************")
    data = {
        'id': id
    }
    user = Users.get_one(data)                                          # Retrieve an instance of the user with the given ID
    return render_template("users_id_update.html", user=user)

# //// CREATE ////////////////////////////////////

@app.route('/users/new/post', methods=['POST'])                         # Retrieve the input values from create form
def users_new_post():
    print("**** In Users New Post Retrieval **************")
    data = {                                                            # Create Data Dictionary from values in form
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email']
    }
    print(data)
    Users.save(data)                                                    # Insert data retrieved into users database
    return redirect("/users")

# //// RETRIEVE ////////////////////////////////////

@app.route('/users/')
@app.route('/users')                                                    # Read All Users Page
def users():
    print("**** Retrieving Users *******************")
    all_users = Users.get_all()                                         # Get all instances of users from the database
    for idx in range(len(all_users)):
        print(f"Index: {idx} ::: User Name: {all_users[idx].first_name} {all_users[idx].last_name}")
    return render_template("read_all.html", all_users = all_users)

@app.route('/users/<int:id>')
def users_id (id):
    data = {
        'id': id
    }
    user = Users.get_one(data)
    print ("*********** In users id ******************")
    print(user)
    return render_template("users_read_one.html", user=user)

# //// UPDATE ////////////////////////////////////

@app.route('/users/<int:id>/update/post', methods=['POST'])
def users_id_update_post(id):
    print ("*********** In Users ID Edit POST *****************")
    data = {
        'id': id,
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email']
    }
    Users.update_one(data)
    return redirect('/users')

# //// DELETE ////////////////////////////////////

@app.route('/users/<int:id>/delete')
def users_id_delete(id):
    print("******** IN DELETE ********************")
    data = {
        'id': id
    }
    Users.delete(data)
    return redirect('/users')

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


# **** Ensure that if the user types in any route other than the ones specified, 
#           they receive an error message saying "Sorry! No response. Try again ****
@app.errorhandler(404) 
def invalid_route(e): 
    return "Sorry! No response. Try again."

if __name__=="__main__":   
    app.run(debug=True)    