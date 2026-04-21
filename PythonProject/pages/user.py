import flet as ft
from config import COLORS, UI_STYLES


def user_page(page: ft.Page, is_logged_in=False, username=""):
    """用户页面 - 个人中心"""

    if not is_logged_in:
        return ft.Container(
            expand=True,
            width=float('inf'),
            bgcolor=UI_STYLES["container"]["main"]["bgcolor"],
            content=ft.Column(
                expand=True,
                width=float('inf'),
                controls=[
                    ft.Text("未登录", size=20, color=COLORS["grey_600"]),
                    ft.ElevatedButton(
                        "去登录",
                        on_click=lambda e: page.go("/login"),
                        style=ft.ButtonStyle(
                            shape=UI_STYLES["button"]["primary"]["shape"],
                            bgcolor=UI_STYLES["button"]["primary"]["bgcolor"],
                            color=UI_STYLES["button"]["primary"]["color"],
                        ),
                    ),
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                alignment=ft.MainAxisAlignment.CENTER,
                spacing=20,
            ),
        )

    # 头像（静态）
    avatar_container = ft.Container(
        content=ft.Text("", size=40, color=ft.Colors.WHITE),
        width=80,
        height=80,
        bgcolor=COLORS["accent"],
        border_radius=40,
    )

    # 用户名
    username_text = ft.Text(username, size=20, weight=ft.FontWeight.BOLD, color=COLORS["black"])

    # 用户信息行
    user_row = ft.Row(
        controls=[
            avatar_container,
            ft.Column(controls=[username_text], spacing=5),
        ],
        spacing=15,
        vertical_alignment=ft.CrossAxisAlignment.CENTER,
    )

    # 用户卡片
    user_card = ft.Container(
        content=user_row,
        padding=20,
        bgcolor=ft.Colors.WHITE,
        border_radius=15,
        margin=ft.margin.only(bottom=20),
        shadow=ft.BoxShadow(spread_radius=1, blur_radius=10, color=ft.Colors.BLACK12),
    )

    # 菜单项
    def menu_item(title):
        return ft.Container(
            content=ft.Row(
                controls=[
                    ft.Text(title, size=16, color=COLORS["black"]),
                    ft.Text(">", size=16, color=COLORS["grey_600"]),
                ],
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            ),
            padding=ft.padding.symmetric(vertical=15, horizontal=20),
            ink=True,
            on_click=lambda e: print(f"点击了{title}"),
        )

    # 退出登录按钮
    def logout(e):
        page.go("/login")
        page.update()

    logout_btn = ft.Container(
        content=ft.ElevatedButton(
            "退出登录",
            width=200,
            height=45,
            style=ft.ButtonStyle(
                shape=ft.RoundedRectangleBorder(radius=25),
                bgcolor=ft.Colors.RED_100,
                color=ft.Colors.RED_700,
            ),
            on_click=logout,
        ),
        margin=ft.margin.only(top=20),
    )

    # 菜单列表
    menu_card = ft.Container(
        content=ft.Column(
            controls=[
                menu_item("设置"),
                ft.Divider(height=1, color=ft.Colors.GREY_200),
                menu_item("反馈"),
                ft.Divider(height=1, color=ft.Colors.GREY_200),
                menu_item("收藏"),
            ],
            spacing=0,
        ),
        bgcolor=ft.Colors.WHITE,
        border_radius=15,
        shadow=ft.BoxShadow(spread_radius=1, blur_radius=10, color=ft.Colors.BLACK12),
    )

    # 完整页面
    return ft.Container(
        expand=True,
        width=float('inf'),
        bgcolor=UI_STYLES["container"]["main"]["bgcolor"],
        content=ft.Column(
            expand=True,
            width=float('inf'),
            controls=[
                ft.Container(
                    content=ft.Text("我的", size=28, weight=ft.FontWeight.BOLD, color=COLORS["primary"]),
                    padding=ft.padding.only(top=20, left=20, right=20, bottom=10),
                ),
                ft.Container(content=user_card, padding=ft.padding.symmetric(horizontal=16)),
                ft.Container(content=menu_card, padding=ft.padding.symmetric(horizontal=16),
                             margin=ft.margin.only(top=10)),
                logout_btn,
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        ),
    )