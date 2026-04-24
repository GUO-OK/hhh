import flet as ft

from pages.home import home_page_component
from pages.welcome import welcome_page
from pages.search import result_page
from pages.custom_AI import ai_custom_page
from pages.user import user_page
from pages.auth import login_page, register_page

from config import UI_STYLES, COLORS, NAV_STYLES

class PageManager:
    def __init__(self, main_page=None):
        self.main_page = main_page
        self.content_container = None
        self.current_page = "home"
        self.page_content = None
        self.is_logged_in = False
        self.current_user = None
        if self.main_page:
            self.main_page.on_route_change = self.route_change

    def on_login_success(self, username):
        self.is_logged_in = True
        self.current_user = username
        self.main_page.go("/user")
        if self.main_page:
            self.main_page.snack_bar = ft.SnackBar(ft.Text(f"欢迎回来，{username}！"))
            self.main_page.snack_bar.open = True
            self.main_page.update()

    def on_register_success(self, username):
        if self.main_page:
            self.main_page.snack_bar = ft.SnackBar(ft.Text(f"注册成功，请登录"))
            self.main_page.snack_bar.open = True
            self.main_page.go("/login")
            self.main_page.update()

    def route_change(self, e):
        route = self.main_page.route
        print(f"路由变化: {route}")

        if route == "/":
            self.page_content.content = home_page_component(on_search=self.on_search)
        elif route == "/ai":
            self.page_content.content = ai_custom_page(self.main_page)
        elif route == "/user":
            self.page_content.content = user_page(self.main_page, self.is_logged_in, self.current_user)
        elif route == "/login":
            self.page_content.content = login_page(self.main_page, on_login_success=self.on_login_success)
        elif route == "/register":
            self.page_content.content = register_page(self.main_page, on_register_success=self.on_register_success)
        elif route == "/favorites":
            from pages.favorites import favorites_page
            self.page_content.content = favorites_page(self.main_page, self.current_user,lambda: self.main_page.go("/user"))
        elif route == "/change_password":
            from pages.change_password import change_password_page
            self.page_content.content = change_password_page(self.main_page, self.current_user,lambda: self.main_page.go("/user"))
        self.page_content.update()

    def show_welcome(self):
        if self.content_container and self.main_page:
            self.content_container.content = welcome_page(
                self.main_page,
                on_complete=self.skip_welcome
            )
            self.content_container.update()

    def skip_welcome(self):
        if self.content_container and self.content_container.content is not None:
            # current_content = self.content_container.content
            self.content_container.content = None
            self.content_container.content = self.get_main_content()
            self.content_container.update()

    def on_search(self, search_params):
        self.page_content.content = result_page(
            self.main_page,
            search_params,
            on_back=self.go_home,
            username=self.current_user,
            is_logged_in=self.is_logged_in
        )
        self.page_content.update()

    def go_home(self):
        self.main_page.go("/")

    def get_main_content(self):
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
        def nav_to(page_name):
            self.main_page.go(f"/{page_name}")
        button_style = ft.ButtonStyle(
            color=NAV_STYLES["footer"]["button_color"],
            bgcolor=ft.Colors.TRANSPARENT,
            # overlay_color=ft.Colors.with_opacity(0.2, ft.Colors.WHITE),
        )
        return ft.Container(
            height=NAV_STYLES["footer"]["height"],
            content=ft.Row(
                alignment=ft.MainAxisAlignment.SPACE_AROUND,
                controls=[
                    ft.TextButton("首页",on_click=lambda e: nav_to(""),style=button_style,
                    ),
                    ft.TextButton(
                        "趣味方案",
                        on_click=lambda e: nav_to("ai"),
                        style=button_style,
                    ),
                    ft.TextButton(
                        "个人",
                        on_click=lambda e: nav_to("user"),
                        style=button_style,
                    ),
                ]
            ),
            bgcolor=NAV_STYLES["footer"]["bgcolor"],
        )

    def build_layout_with_welcome(self):
        self.content_container = ft.Container(expand=True)
        if self.main_page:
            self.content_container.content = welcome_page(
                self.main_page,
                on_complete=self.skip_welcome
            )
        return self.content_container

def build_layout(page=None):
    manager = PageManager(page)
    return manager.build_layout_with_welcome()