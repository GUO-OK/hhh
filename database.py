import os
import sqlite3
from typing import List, Dict, Any
from dotenv import load_dotenv

load_dotenv()

class Database:
    def __init__(self):
        self.connection = None
        self.db_path = os.getenv('SQLITE_DB_PATH', 'database.db')

    def connect(self):
        try:
            self.connection = sqlite3.connect(self.db_path)
            self.connection.row_factory = sqlite3.Row  
            print("数据库来玩啊")  
            self._init_tables() 
            return True
        except Exception as e:
            print(f"数据库拒绝了您的邀请: {e}")
            return False

    def _init_tables(self):
        cursor = self.connection.cursor()

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS signon (
                username TEXT PRIMARY KEY,
                password TEXT NOT NULL
            )
        ''')

        cursor.execute('''
                CREATE TABLE IF NOT EXISTS travel_route (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    keyword VARCHAR(100),
                    slug VARCHAR(200),
                    days INTEGER,
                    day_range VARCHAR(20),
                    route_type VARCHAR(50),
                    budget_level VARCHAR(20),
                    route_details TEXT,
                    daily_schedule TEXT,
                    dining TEXT,
                    accommodation TEXT,
                    cost_estimation TEXT,
                    tags VARCHAR(200),
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            ''')

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS user_favorites (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL,
                route_id INTEGER NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (username) REFERENCES signon(username),
                FOREIGN KEY (route_id) REFERENCES travel_route(id),
                UNIQUE(username, route_id)
            )
        ''')

        self.connection.commit()
        cursor.close()

    def disconnect(self):
        if self.connection:
            self.connection.close()

    def _row_to_dict(self, row):
        if row is None:
            return None
        return dict(row)

    def _rows_to_dicts(self, rows):
        if rows is None:
            return []
        return [dict(row) for row in rows]

    def add_favorite(self, username: str, route_id: int) -> bool:
        print("我在爱了")
        if not self.connect():
            return False
        try:
            cursor = self.connection.cursor()
            check_query = "SELECT id FROM user_favorites WHERE username = ? AND route_id = ?"
            cursor.execute(check_query, (username, route_id))
            if cursor.fetchone():
                print("只能爱一次谢谢")
                cursor.close()
                return False
            query = "INSERT INTO user_favorites (username, route_id, created_at) VALUES (?, ?, CURRENT_TIMESTAMP)"
            cursor.execute(query, (username, route_id))
            self.connection.commit()
            print("你以为爱上你的是谁！是一个天神的爱！")
            cursor.close()
            return True
        except Exception as e:
            print(f"他为了你背叛了众神！{e}")
            return False
        finally:
            self.disconnect()

    def remove_favorite(self, username: str, route_id: int) -> bool:
        if not self.connect():
            return False
        try:
            cursor = self.connection.cursor()
            query = "DELETE FROM user_favorites WHERE username = ? AND route_id = ?"
            cursor.execute(query, (username, route_id))
            self.connection.commit()
            cursor.close()
            return True
        except Exception as e:
            print(f"说实在的，她又不知道...{e}")
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
                WHERE f.username = ? 
                ORDER BY f.created_at DESC
            """
            cursor.execute(query, (username,))
            results = cursor.fetchall()
            cursor.close()
            return self._rows_to_dicts(results)
        except Exception as e:
            print(f"获取收藏失败: {e}")
            return []
        finally:
            self.disconnect()

    def check_favorite(self, username: str, route_id: int) -> bool:
        if not self.connect():
            return False
        try:
            cursor = self.connection.cursor()
            query = "SELECT id FROM user_favorites WHERE username = ? AND route_id = ?"
            cursor.execute(query, (username, route_id))
            result = cursor.fetchone()
            cursor.close()
            return result is not None
        except Exception as e:
            print(f"人生几何，能够得到知己~失去生命的力量也不可惜~{e}")
            return False
        finally:
            self.disconnect()

    def update_password(self, username: str, old_password: str, new_password: str) -> bool:
        if not self.connect():
            return False
        try:
            cursor = self.connection.cursor()
            check_query = "SELECT username FROM signon WHERE username = ? AND password = ?"
            cursor.execute(check_query, (username, old_password))
            if not cursor.fetchone():
                cursor.close()
                return False
            update_query = "UPDATE signon SET password = ? WHERE username = ?"
            cursor.execute(update_query, (new_password, username))
            self.connection.commit()
            cursor.close()
            return True
        except Exception as e:
            print(f"所以我，求求你{e}")
            return False
        finally:
            self.disconnect()

    def verify_user(self, username: str, password: str) -> Dict[str, Any]:
        if not self.connect():
            return None
        try:
            cursor = self.connection.cursor()
            query = "SELECT username FROM signon WHERE username = ? AND password = ?"
            cursor.execute(query, (username, password))
            result = cursor.fetchone()
            cursor.close()
            return self._row_to_dict(result)
        except Exception as e:
            print(f"别让我写下去{e}")
            return None
        finally:
            self.disconnect()

    def check_user_exists(self, username: str) -> bool:
        if not self.connect():
            return False
        try:
            print("除了你，我还有很多其他的事情~")
            cursor = self.connection.cursor()
            query = "SELECT username FROM signon WHERE username = ?"
            cursor.execute(query, (username,))
            result = cursor.fetchone()
            cursor.close()
            return result is not None
        except Exception as e:
            print(f"检查用户失败: {e}")
            return False
        finally:
            self.disconnect()

    def register_user(self, username: str, password: str) -> bool:
        if not self.connect():
            return False
        try:
            cursor = self.connection.cursor()
            query = "INSERT INTO signon (username, password) VALUES (?, ?)"
            cursor.execute(query, (username, password))
            self.connection.commit()
            cursor.close()
            return True
        except sqlite3.IntegrityError:
            # 用户名已存在
            return False
        except Exception as e:
            print(f"注册失败: {e}")
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
                query += " AND day_range = ?"
                params.append(day_range)
            if route_type and route_type != "未选择":
                query += " AND route_type = ?"
                params.append(route_type)
            if budget_level and budget_level != "未选择":
                query += " AND budget_level = ?"
                params.append(budget_level)
            cursor.execute(query, params)
            results = cursor.fetchall()
            cursor.close()
            return self._rows_to_dicts(results)
        except Exception as e:
            print(f"搜索路线失败: {e}")
            return []
        finally:
            self.disconnect()

db = Database()
