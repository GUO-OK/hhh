import flet as ft

from pages.home import home_page_component
from pages.welcome import welcome_page
from pages.search import result_page
from pages.custom_AI import ai_custom_page
from pages.user import user_page
from pages.auth import login_page, register_page


class PageManager:
    """页面管理器 - 负责布局逻辑"""

    def __init__(self, main_page=None):
        self.main_page = main_page
        self.content_container = None
        self.current_page = "home"
        self.page_content = None
        self.is_logged_in = False
        self.current_user = None

        # 设置路由监听
        if self.main_page:
            self.main_page.on_route_change = self.route_change

    def on_login_success(self, username):
        """登录成功回调"""
        self.is_logged_in = True
        self.current_user = username
        # 登录成功后跳转到首页
        self.main_page.go("/")
        # 显示欢迎消息
        if self.main_page:
            self.main_page.snack_bar = ft.SnackBar(ft.Text(f"欢迎回来，{username}！"))
            self.main_page.snack_bar.open = True
            self.main_page.update()

    def on_register_success(self, username):
        """注册成功回调"""
        # 注册成功后跳转到登录页面
        if self.main_page:
            self.main_page.snack_bar = ft.SnackBar(ft.Text(f"注册成功，请登录"))
            self.main_page.snack_bar.open = True
            self.main_page.go("/login")
            self.main_page.update()

    def route_change(self, e):
        """路由变化处理"""
        route = self.main_page.route
        print(f"路由变化: {route}")

        if route == "/":
            # 首页
            self.page_content.content = home_page_component(on_search=self.on_search)
        elif route == "/ai":
            # AI页面
            self.page_content.content = ai_custom_page(self.main_page)
        elif route == "/user":
            # 用户页面
            self.page_content.content = user_page(self.main_page, self.is_logged_in, self.current_user)
        elif route == "/login":
            # 登录页面
            self.page_content.content = login_page(self.main_page, on_login_success=self.on_login_success)
        elif route == "/register":
            # 注册页面
            self.page_content.content = register_page(self.main_page, on_register_success=self.on_register_success)

        self.page_content.update()

    def show_welcome(self):
        """显示欢迎页面"""
        if self.content_container and self.main_page:
            self.content_container.content = welcome_page(
                self.main_page,
                on_complete=self.skip_welcome
            )
            self.content_container.update()

    def skip_welcome(self):
        """跳过欢迎页面，显示主内容"""
        if self.content_container:
            self.content_container.content = self.get_main_content()
            self.content_container.update()

    def on_search(self, search_params):
        """搜索回调 - 直接显示结果页面"""
        self.page_content.content = result_page(self.main_page, search_params, on_back=self.go_home)
        self.page_content.update()

    def go_home(self):
        """返回首页"""
        self.main_page.go("/")

    def get_main_content(self):
        """获取主内容（带导航的布局）"""
        self.page_content = ft.Container(
            expand=True,
            content=home_page_component(on_search=self.on_search)
        )

        return ft.Column(
            expand=True,
            spacing=0,
            controls=[
                self.page_content,
                self.get_footer_with_navigation(),
            ]
        )

    def get_footer_with_navigation(self):
        """底部导航栏"""

        def nav_to(page_name):
            self.main_page.go(f"/{page_name}")

        return ft.Container(
            height=60,
            content=ft.Row(
                alignment=ft.MainAxisAlignment.SPACE_AROUND,
                controls=[
                    ft.TextButton("首页", on_click=lambda e: nav_to("")),
                    ft.TextButton("趣味方案", on_click=lambda e: nav_to("ai")),
                    ft.TextButton("个人", on_click=lambda e: nav_to("user")),
                ]
            ),
            bgcolor=ft.Colors.BLUE_100,
        )

    def build_layout_with_welcome(self):
        """构建带欢迎页面的布局"""
        self.content_container = ft.Container(expand=True)

        if self.main_page:
            self.content_container.content = welcome_page(
                self.main_page,
                on_complete=self.skip_welcome
            )

        return self.content_container


def build_layout(page=None):
    """构建布局的工厂函数"""
    manager = PageManager(page)
    return manager.build_layout_with_welcome()