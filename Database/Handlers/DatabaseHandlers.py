from Database.db import Database

db = Database()

class DatabaseHandlers:
    @staticmethod
    def user(user_id): # return users by USER_ID
        sql_query = f"SELECT * FROM users WHERE user_id = {user_id}"
        result = db.fetch_data(sql_query)
        return result
    
    @staticmethod
    def registration(user_id): # registration users by USER_ID
        user = DatabaseHandlers.user(user_id)
        if not user:
            sql_query = "INSERT INTO users (user_id, user_level) VALUES (%s, %s)"
            data_to_insert = [
                (user_id, 0),
            ]
            db.execute_query(sql_query, data_to_insert)
            db.close_connection()