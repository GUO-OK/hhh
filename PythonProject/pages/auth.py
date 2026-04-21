import flet as ft
from config import COLORS, UI_STYLES
from database import db


def login_page(page: ft.Page, on_login_success=None):
    """登录页面"""

    # 创建登录表单控件
    username_input = ft.TextField(
        label="用户名",
        width=350,
        bgcolor="#FFFFFF",
        color=COLORS["black"],
        label_style=UI_STYLES["dropdown"]["label_style"],
        border_color=UI_STYLES["dropdown"]["border_color"],
        focused_border_color=UI_STYLES["dropdown"]["focused_border_color"],
    )

    password_input = ft.TextField(
        label="密码",
        width=350,
        password=True,
        can_reveal_password=True,
        bgcolor="#FFFFFF",
        color=COLORS["black"],
        label_style=UI_STYLES["dropdown"]["label_style"],
        border_color=UI_STYLES["dropdown"]["border_color"],
        focused_border_color=UI_STYLES["dropdown"]["focused_border_color"],
    )

    error_text = ft.Text("", color=ft.Colors.RED, size=12, visible=False)

    def do_login(e):
        """执行登录"""
        username = username_input.value
        password = password_input.value

        if not username or not password:
            error_text.value = "请填写用户名和密码"
            error_text.visible = True
            page.update()
            return

        # 查询数据库验证用户
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
        """跳转到注册页面"""
        page.go("/register")

    # 登录按钮
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

    # 注册链接
    register_link = ft.TextButton(
        "还没有账号？立即注册",
        on_click=go_to_register,
        style=ft.ButtonStyle(color=COLORS["primary"]),
    )

    # 表单布局
    form = ft.Column(
        controls=[
            username_input,
            password_input,
            error_text,
            login_btn,
            register_link,
        ],
        spacing=UI_STYLES["spacing"]["medium"],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    )

    # 返回完整页面
    return ft.Container(
        expand=True,
        width=float('inf'),
        content=ft.Column(
            expand=True,
            width=float('inf'),
            controls=[
                ft.Text(
                    "登录",
                    size=UI_STYLES["text"]["title"]["size"],
                    weight=UI_STYLES["text"]["title"]["weight"],
                    color=UI_STYLES["text"]["title"]["color"],
                ),
                ft.Text(
                    "欢迎回来，请登录你的账号",
                    size=UI_STYLES["text"]["subtitle"]["size"],
                    color=UI_STYLES["text"]["subtitle"]["color"],
                ),
                form,
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=UI_STYLES["spacing"]["large"],
        ),
        bgcolor=UI_STYLES["container"]["main"]["bgcolor"],
    )


def register_page(page: ft.Page, on_register_success=None):
    """注册页面"""

    # 创建注册表单控件
    username_input = ft.TextField(
        label="用户名",
        width=350,
        bgcolor="#FFFFFF",
        color=COLORS["black"],
        label_style=UI_STYLES["dropdown"]["label_style"],
        border_color=UI_STYLES["dropdown"]["border_color"],
        focused_border_color=UI_STYLES["dropdown"]["focused_border_color"],
    )

    password_input = ft.TextField(
        label="密码",
        width=350,
        password=True,
        can_reveal_password=True,
        bgcolor="#FFFFFF",
        color=COLORS["black"],
        label_style=UI_STYLES["dropdown"]["label_style"],
        border_color=UI_STYLES["dropdown"]["border_color"],
        focused_border_color=UI_STYLES["dropdown"]["focused_border_color"],
    )

    confirm_password_input = ft.TextField(
        label="确认密码",
        width=350,
        password=True,
        can_reveal_password=True,
        bgcolor="#FFFFFF",
        color=COLORS["black"],
        label_style=UI_STYLES["dropdown"]["label_style"],
        border_color=UI_STYLES["dropdown"]["border_color"],
        focused_border_color=UI_STYLES["dropdown"]["focused_border_color"],
    )

    error_text = ft.Text("", color=ft.Colors.RED, size=12, visible=False)

    def do_register(e):
        """执行注册"""
        username = username_input.value
        password = password_input.value
        confirm_password = confirm_password_input.value

        # 验证输入
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

        # 检查用户是否已存在
        if db.check_user_exists(username):
            error_text.value = "用户名已存在，请选择其他用户名"
            error_text.visible = True
            page.update()
            return

        # 注册新用户
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
        """跳转到登录页面"""
        page.go("/login")

    # 注册按钮
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

    # 登录链接
    login_link = ft.TextButton(
        "已有账号？立即登录",
        on_click=go_to_login,
        style=ft.ButtonStyle(color=COLORS["primary"]),
    )

    # 表单布局
    form = ft.Column(
        controls=[
            username_input,
            password_input,
            confirm_password_input,
            error_text,
            register_btn,
            login_link,
        ],
        spacing=UI_STYLES["spacing"]["medium"],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    )

    # 返回完整页面
    return ft.Container(
        expand=True,
        width=float('inf'),
        content=ft.Column(
            expand=True,
            width=float('inf'),
            controls=[
                ft.Text(
                    "注册",
                    size=UI_STYLES["text"]["title"]["size"],
                    weight=UI_STYLES["text"]["title"]["weight"],
                    color=UI_STYLES["text"]["title"]["color"],
                ),
                ft.Text(
                    "创建新账号，开始你的旅行",
                    size=UI_STYLES["text"]["subtitle"]["size"],
                    color=UI_STYLES["text"]["subtitle"]["color"],
                ),
                form,
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=UI_STYLES["spacing"]["large"],
        ),
        bgcolor=UI_STYLES["container"]["main"]["bgcolor"],
    )