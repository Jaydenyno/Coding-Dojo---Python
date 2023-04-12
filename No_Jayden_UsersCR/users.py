from mysqlconnection import connectToMySQL

DATABASE = "users_schema"

class Users:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM user;"
        results = connectToMySQL(DATABASE).query_db(query)
        users = []
        for x in results:
            users.append(cls(x))
        return users
    
    @classmethod
    def save(cls, data):
        query = "INSERT INTO user (first_name, last_name, email) VALUES (%(first_name)s, %(last_name)s, %(email)s);"
        result = connectToMySQL(DATABASE).query_db(query, data)
        
        return result