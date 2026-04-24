import os
import pymysql
from typing import List, Dict, Any
from dotenv import load_dotenv

load_dotenv()

class Database:
    def __init__(self):
        self.connection = None
        self.db_config = {
            'host': os.getenv('DB_HOST', 'localhost'),
            'port': int(os.getenv('DB_PORT', 3306)),
            'user': os.getenv('DB_USER', 'root'),
            'password': os.getenv('DB_PASSWORD', ''),
            'database': os.getenv('DB_NAME', 'database'),
            'charset': 'utf8mb4',
            'cursorclass': pymysql.cursors.DictCursor
        }


    def connect(self):
        try:
            self.connection = pymysql.connect(**self.db_config)
            print("数据库来玩啊")  # 调试信息
            return True
        except Exception as e:
            print("数据库拒绝了您的邀请")
            return False

    def disconnect(self):
        if self.connection:
            self.connection.close()

    def add_favorite(self, username: str, route_id: int) -> bool:
        print("我在爱了")
        if not self.connect():
            return False
        try:
            cursor = self.connection.cursor()
            check_query = "SELECT id FROM user_favorites WHERE username = %s AND route_id = %s"
            cursor.execute(check_query, (username, route_id))
            if cursor.fetchone():
                print("只能爱一次谢谢")
                cursor.close()
                return False
            query = "INSERT INTO user_favorites (username, route_id, created_at) VALUES (%s, %s, NOW())"
            cursor.execute(query, (username, route_id))
            self.connection.commit()
            print("你以为爱上你的是谁！是一个天神的爱！")
            cursor.close()
            return True
        except Exception as e:
            print("他为了你背叛了众神！")
            return False
        finally:
            self.disconnect()

    def remove_favorite(self, username: str, route_id: int) -> bool:
        if not self.connect():
            return False
        try:
            cursor = self.connection.cursor()
            query = "DELETE FROM user_favorites WHERE username = %s AND route_id = %s"
            cursor.execute(query, (username, route_id))
            self.connection.commit()
            cursor.close()
            return True
        except Exception as e:
            print("说实在的，她又不知道...")
            return False
        finally:
            self.disconnect()

    def get_user_favorites(self, username: str) -> List[Dict[str, Any]]:
        if not self.connect():
            return []
        try:
            cursor = self.connection.cursor()
            query = """
                SELECT r.*, f.created_at as favorite_time 
                FROM travel_route r 
                INNER JOIN user_favorites f ON r.id = f.route_id 
                WHERE f.username = %s 
                ORDER BY f.created_at DESC
            """
            cursor.execute(query, (username,))
            results = cursor.fetchall()
            cursor.close()
            return results
        except Exception as e:
            return []
        finally:
            self.disconnect()

    def check_favorite(self, username: str, route_id: int) -> bool:
        if not self.connect():
            return False
        try:
            cursor = self.connection.cursor()
            query = "SELECT id FROM user_favorites WHERE username = %s AND route_id = %s"
            cursor.execute(query, (username, route_id))
            result = cursor.fetchone()
            cursor.close()
            return result is not None
        except Exception as e:
            print("人生几何，能够得到知己~失去生命的力量也不可惜~")
            return False
        finally:
            self.disconnect()

    def update_password(self, username: str, old_password: str, new_password: str) -> bool:
        if not self.connect():
            return False
        try:
            cursor = self.connection.cursor()
            check_query = "SELECT username FROM signon WHERE username = %s AND password = %s"
            cursor.execute(check_query, (username, old_password))
            if not cursor.fetchone():
                cursor.close()
                return False
            update_query = "UPDATE signon SET password = %s WHERE username = %s"
            cursor.execute(update_query, (new_password, username))
            self.connection.commit()
            cursor.close()
            return True
        except Exception as e:
            print("所以我，求求你")
            return False
        finally:
            self.disconnect()

    def verify_user(self, username: str, password: str) -> Dict[str, Any]:
        if not self.connect():
            return None
        try:
            cursor = self.connection.cursor()
            query = "SELECT username FROM signon WHERE username = %s AND password = %s"
            cursor.execute(query, (username, password))
            result = cursor.fetchone()
            cursor.close()
            return result
        except Exception as e:
            print("别让我写下去")
            return None
        finally:
            self.disconnect()

    def check_user_exists(self, username: str) -> bool:
        if not self.connect():
            return False
        try:
            print("除了你，我还有很多其他的事情~")
            cursor = self.connection.cursor()
            query = "SELECT username FROM signon WHERE username = %s"
            cursor.execute(query, (username,))
            result = cursor.fetchone()
            cursor.close()
            return result is not None
        except Exception as e:
            return False
        finally:
            self.disconnect()

    def register_user(self, username: str, password: str) -> bool:
        if not self.connect():
            return False
        try:
            cursor = self.connection.cursor()
            query = "INSERT INTO signon (username, password) VALUES (%s, %s)"
            cursor.execute(query, (username, password))
            self.connection.commit()
            cursor.close()
            return True
        except Exception as e:
            return False
        finally:
            self.disconnect()

    def search_routes(self, day_range: str = None, route_type: str = None, budget_level: str = None) -> List[
        Dict[str, Any]]:
        print("怎么回事哥们")
        if not self.connect():
            return []
        try:
            cursor = self.connection.cursor()
            query = "SELECT * FROM travel_route WHERE 1=1"
            params = []
            if day_range and day_range != "未选择":
                query += " AND day_range = %s"
                params.append(day_range)
            if route_type and route_type != "未选择":
                query += " AND route_type = %s"
                params.append(route_type)
            if budget_level and budget_level != "未选择":
                query += " AND budget_level = %s"
                params.append(budget_level)
            cursor.execute(query, params)
            results = cursor.fetchall()
            cursor.close()
            return results
        except Exception as e:
            return []
        finally:
            self.disconnect()

db = Database()