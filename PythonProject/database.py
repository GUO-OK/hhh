import pymysql
from typing import List, Dict, Any


class Database:
    """数据库管理类"""

    def __init__(self):
        self.connection = None

    def connect(self):
        """连接数据库"""
        try:
            self.connection = pymysql.connect(
                host='localhost',
                port=3306,
                user='root',
                password='123456',
                database='database',
                charset='utf8mb4',
                cursorclass=pymysql.cursors.DictCursor
            )
            print("数据库连接成功")  # 调试信息
            return True
        except Exception as e:
            print(f"数据库连接失败: {e}")
            return False

    def disconnect(self):
        """断开数据库连接"""
        if self.connection:
            self.connection.close()

    def verify_user(self, username: str, password: str) -> Dict[str, Any]:
        """验证用户登录 - 查询 signon 表"""
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
            print(f"查询失败: {e}")
            return None
        finally:
            self.disconnect()

    def check_user_exists(self, username: str) -> bool:
        """检查用户是否存在"""
        if not self.connect():
            return False

        try:
            cursor = self.connection.cursor()
            query = "SELECT username FROM signon WHERE username = %s"
            cursor.execute(query, (username,))
            result = cursor.fetchone()
            cursor.close()
            return result is not None
        except Exception as e:
            print(f"查询失败: {e}")
            return False
        finally:
            self.disconnect()

    def register_user(self, username: str, password: str) -> bool:
        """注册新用户 - 插入 signon 表"""
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
            print(f"注册失败: {e}")
            return False
        finally:
            self.disconnect()

    def search_routes(self, day_range: str = None, route_type: str = None, budget_level: str = None) -> List[
        Dict[str, Any]]:
        """根据搜索条件查询路线"""
        print(f"搜索参数: day_range={day_range}, route_type={route_type}, budget_level={budget_level}")  # 调试信息

        if not self.connect():
            return []

        try:
            cursor = self.connection.cursor()

            query = "SELECT * FROM travel_route WHERE 1=1"
            params = []

            if day_range and day_range != "未选择":
                query += " AND day_range = %s"
                params.append(day_range)
                print(f"添加天数条件: {day_range}")

            if route_type and route_type != "未选择":
                query += " AND route_type = %s"
                params.append(route_type)
                print(f"添加校区条件: {route_type}")

            if budget_level and budget_level != "未选择":
                query += " AND budget_level = %s"
                params.append(budget_level)
                print(f"添加预算条件: {budget_level}")

            print(f"执行SQL: {query}")
            print(f"参数: {params}")

            cursor.execute(query, params)
            results = cursor.fetchall()

            print(f"查询到 {len(results)} 条结果")  # 调试信息

            cursor.close()
            return results

        except Exception as e:
            print(f"查询失败: {e}")
            return []
        finally:
            self.disconnect()

# 创建全局数据库实例
db = Database()