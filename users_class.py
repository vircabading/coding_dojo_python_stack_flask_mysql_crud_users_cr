# import the function that will return an instance of a connection ////////
from mysqlconnection import connectToMySQL

target_db = 'users'                                                     # Designates the database we are using

# //// USERS CLASS ////////////////////////////////////////////////////////
class Users:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        
    # **** Get All Class Method *******************************************
    # @Returns: a list of instances of the class
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM " + target_db +";"

        results = connectToMySQL(target_db).query_db(query)             # Call the connectToMySQL function with the target db
        
        list_of_instances = []                                          # Initialize an empty list where we can store instances of the class
        
        for class_instance in results:                                  # Iterate over the db results and create instances of the cls objects
            list_of_instances.append( cls(class_instance) )             # Add each instance of the class to the list of instances
        return list_of_instances

    # **** Insert One Method ***********************************************
    # @returns ID of created user
    @classmethod
    def save(cls, data ):
        query = "INSERT INTO users ( first_name , last_name , email) VALUES ( %(first_name)s , %(last_name)s , %(email)s );"
        # data is a dictionary that will be passed into the save method from server.py
        return connectToMySQL(target_db).query_db( query, data )