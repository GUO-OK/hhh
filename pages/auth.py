import flet as ft
from config import COLORS,UI_STYLES, BACKGROUND_IMAGE_3, TEXTFIELD_STYLES, AUTH_STYLES, PAGE_CONTAINER_STYLES
from database import db


def login_page(page: ft.Page, on_login_success=None):
    username_input = ft.TextField(
        label="用户名",
        width=TEXTFIELD_STYLES["width"],
        bgcolor=TEXTFIELD_STYLES["bgcolor"],
        color=TEXTFIELD_STYLES["color"],
        label_style=TEXTFIELD_STYLES["label_style"],
        border_color=TEXTFIELD_STYLES["border_color"],
        focused_border_color=TEXTFIELD_STYLES["focused_border_color"],
    )

    password_input = ft.TextField(
        label="密码",
        width=TEXTFIELD_STYLES["width"],
        password=True,
        can_reveal_password=True,
        bgcolor=TEXTFIELD_STYLES["bgcolor"],
        color=TEXTFIELD_STYLES["color"],
        label_style=TEXTFIELD_STYLES["label_style"],
        border_color=TEXTFIELD_STYLES["border_color"],
        focused_border_color=TEXTFIELD_STYLES["focused_border_color"],
    )

    error_text = ft.Text("", color=AUTH_STYLES["error_text"]["color"],
                         size=AUTH_STYLES["error_text"]["size"], visible=False)

    def do_login(e):
        username = username_input.value
        password = password_input.value

        if not username or not password:
            error_text.value = "请填写用户名和密码"
            error_text.visible = True
            page.update()
            return

        user = db.verify_user(username, password)

        if user:
            error_text.visible = False
            if on_login_success:
                on_login_success(username)
        else:
            error_text.value = "用户名或密码错误"
            error_text.visible = True
            page.update()

    def go_to_register(e):
        page.go("/register")

    login_btn = ft.ElevatedButton(
        "登录",
        width=200,
        height=45,
        style=ft.ButtonStyle(
            shape=UI_STYLES["button"]["primary"]["shape"],
            bgcolor=UI_STYLES["button"]["primary"]["bgcolor"],
            color=UI_STYLES["button"]["primary"]["color"],
        ),
        on_click=do_login,
    )

    register_link = ft.TextButton(
        "还没有账号？立即注册",
        on_click=go_to_register,
        style=ft.ButtonStyle(color=COLORS["primary"]),
    )

    form = ft.Column(
        controls=[username_input, password_input, error_text, login_btn, register_link],
        spacing=UI_STYLES["spacing"]["medium"],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    )

    content_card = ft.Container(
        expand=True,
        width=float('inf'),
        content=ft.Column(
            expand=True,
            width=float('inf'),
            controls=[
                ft.Text("登录", size=UI_STYLES["text"]["title"]["size"],
                        weight=UI_STYLES["text"]["title"]["weight"],
                        color=UI_STYLES["text"]["title"]["color"]),
                ft.Text("请登录账号", size=UI_STYLES["text"]["subtitle"]["size"],
                        color=UI_STYLES["text"]["subtitle"]["color"]),
                form,
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=UI_STYLES["spacing"]["large"],
        ),
        padding=ft.padding.all(PAGE_CONTAINER_STYLES["content_card"]["padding"]),
        border_radius=PAGE_CONTAINER_STYLES["content_card"]["border_radius"],
    )

    return ft.Stack(
        expand=True,
        controls=[
            ft.Image(src=BACKGROUND_IMAGE_3,
                    width=PAGE_CONTAINER_STYLES["background_image"]["width"],
                    height=PAGE_CONTAINER_STYLES["background_image"]["height"],
                    fit=PAGE_CONTAINER_STYLES["background_image"]["fit"]),
            ft.Container(expand=True, width=float('inf'),
                        content=ft.Container(expand=True, width=float('inf'), content=content_card),
                        margin=ft.margin.all(PAGE_CONTAINER_STYLES["outer_margin"])),
        ]
    )


def register_page(page: ft.Page, on_register_success=None):
    """注册页面"""
    username_input = ft.TextField(
        label="用户名",
        width=TEXTFIELD_STYLES["width"],
        bgcolor=TEXTFIELD_STYLES["bgcolor"],
        color=TEXTFIELD_STYLES["color"],
        label_style=TEXTFIELD_STYLES["label_style"],
        border_color=TEXTFIELD_STYLES["border_color"],
        focused_border_color=TEXTFIELD_STYLES["focused_border_color"],
    )

    password_input = ft.TextField(
        label="密码",
        width=TEXTFIELD_STYLES["width"],
        password=True,
        can_reveal_password=True,
        bgcolor=TEXTFIELD_STYLES["bgcolor"],
        color=TEXTFIELD_STYLES["color"],
        label_style=TEXTFIELD_STYLES["label_style"],
        border_color=TEXTFIELD_STYLES["border_color"],
        focused_border_color=TEXTFIELD_STYLES["focused_border_color"],
    )

    confirm_password_input = ft.TextField(
        label="确认密码",
        width=TEXTFIELD_STYLES["width"],
        password=True,
        can_reveal_password=True,
        bgcolor=TEXTFIELD_STYLES["bgcolor"],
        color=TEXTFIELD_STYLES["color"],
        label_style=TEXTFIELD_STYLES["label_style"],
        border_color=TEXTFIELD_STYLES["border_color"],
        focused_border_color=TEXTFIELD_STYLES["focused_border_color"],
    )

    error_text = ft.Text("", color=AUTH_STYLES["error_text"]["color"],
                         size=AUTH_STYLES["error_text"]["size"], visible=False)

    def do_register(e):
        username = username_input.value
        password = password_input.value
        confirm_password = confirm_password_input.value

        if not username or not password:
            error_text.value = "请填写用户名和密码"
            error_text.visible = True
            page.update()
            return

        if password != confirm_password:
            error_text.value = "两次输入的密码不一致"
            error_text.visible = True
            page.update()
            return

        if len(username) < 3:
            error_text.value = "用户名长度不能少于3个字符"
            error_text.visible = True
            page.update()
            return

        if len(password) < 6:
            error_text.value = "密码长度不能少于6个字符"
            error_text.visible = True
            page.update()
            return

        if db.check_user_exists(username):
            error_text.value = "用户名已存在，请选择其他用户名"
            error_text.visible = True
            page.update()
            return

        success = db.register_user(username, password)

        if success:
            error_text.visible = False
            if on_register_success:
                on_register_success(username)
        else:
            error_text.value = "注册失败，请稍后重试"
            error_text.visible = True
            page.update()

    def go_to_login(e):
        page.go("/login")

    register_btn = ft.ElevatedButton(
        "注册",
        width=200,
        height=45,
        style=ft.ButtonStyle(
            shape=UI_STYLES["button"]["primary"]["shape"],
            bgcolor=UI_STYLES["button"]["primary"]["bgcolor"],
            color=UI_STYLES["button"]["primary"]["color"],
        ),
        on_click=do_register,
    )

    login_link = ft.TextButton(
        "已有账号？立即登录",
        on_click=go_to_login,
        style=ft.ButtonStyle(color=COLORS["primary"]),
    )

    form = ft.Column(
        controls=[username_input, password_input, confirm_password_input, error_text, register_btn, login_link],
        spacing=UI_STYLES["spacing"]["medium"],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    )

    content_card = ft.Container(
        expand=True,
        width=float('inf'),
        content=ft.Column(
            expand=True,
            width=float('inf'),
            controls=[
                ft.Text("注册", size=UI_STYLES["text"]["title"]["size"],
                        weight=UI_STYLES["text"]["title"]["weight"],
                        color=UI_STYLES["text"]["title"]["color"]),
                ft.Text("创建新账号，开始你的旅行", size=UI_STYLES["text"]["subtitle"]["size"],
                        color=UI_STYLES["text"]["subtitle"]["color"]),
                form,
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=UI_STYLES["spacing"]["large"],
        ),
        padding=ft.padding.all(PAGE_CONTAINER_STYLES["content_card"]["padding"]),
        border_radius=PAGE_CONTAINER_STYLES["content_card"]["border_radius"],
    )

    return ft.Stack(
        expand=True,
        controls=[
            ft.Image(src=BACKGROUND_IMAGE_3,
                    width=PAGE_CONTAINER_STYLES["background_image"]["width"],
                    height=PAGE_CONTAINER_STYLES["background_image"]["height"],
                    fit=PAGE_CONTAINER_STYLES["background_image"]["fit"]),
            ft.Container(expand=True, width=float('inf'),
                        content=ft.Container(expand=True, width=float('inf'), content=content_card),
                        margin=ft.margin.all(PAGE_CONTAINER_STYLES["outer_margin"])),
        ]
    )