# pages/change_password.py
import flet as ft
from config import COLORS, UI_STYLES, BACKGROUND_IMAGE_2, TEXTFIELD_STYLES, PAGE_CONTAINER_STYLES
from database import db


def change_password_page(page: ft.Page, username: str, on_back=None):

    old_password = ft.TextField(
        label="当前密码",
        width=TEXTFIELD_STYLES["width"],
        password=True,
        can_reveal_password=True,
        bgcolor=TEXTFIELD_STYLES["bgcolor"],
        color=TEXTFIELD_STYLES["color"],
        label_style=TEXTFIELD_STYLES["label_style"],
        border_color=TEXTFIELD_STYLES["border_color"],
        focused_border_color=TEXTFIELD_STYLES["focused_border_color"],
    )

    new_password = ft.TextField(
        label="新密码",
        width=TEXTFIELD_STYLES["width"],
        password=True,
        can_reveal_password=True,
        bgcolor=TEXTFIELD_STYLES["bgcolor"],
        color=TEXTFIELD_STYLES["color"],
        label_style=TEXTFIELD_STYLES["label_style"],
        border_color=TEXTFIELD_STYLES["border_color"],
        focused_border_color=TEXTFIELD_STYLES["focused_border_color"],
    )

    confirm_password = ft.TextField(
        label="确认新密码",
        width=TEXTFIELD_STYLES["width"],
        password=True,
        can_reveal_password=True,
        bgcolor=TEXTFIELD_STYLES["bgcolor"],
        color=TEXTFIELD_STYLES["color"],
        label_style=TEXTFIELD_STYLES["label_style"],
        border_color=TEXTFIELD_STYLES["border_color"],
        focused_border_color=TEXTFIELD_STYLES["focused_border_color"],
    )

    error_text = ft.Text("", color=ft.Colors.RED, size=12, visible=False)
    success_text = ft.Text("", color=ft.Colors.GREEN, size=12, visible=False)

    def do_change(e):
        old_pwd = old_password.value
        new_pwd = new_password.value
        confirm_pwd = confirm_password.value

        if not old_pwd or not new_pwd or not confirm_pwd:
            error_text.value = "请填写所有字段"
            error_text.visible = True
            success_text.visible = False
            page.update()
            return

        if new_pwd != confirm_pwd:
            error_text.value = "两次输入的新密码不一致"
            error_text.visible = True
            success_text.visible = False
            page.update()
            return

        if len(new_pwd) < 6:
            error_text.value = "新密码长度不能少于6个字符"
            error_text.visible = True
            success_text.visible = False
            page.update()
            return

        success = db.update_password(username, old_pwd, new_pwd)

        if success:
            error_text.visible = False
            success_text.value = "密码修改成功！请重新登录"
            success_text.visible = True
            page.update()

            import threading
            def delayed_logout():
                import time
                time.sleep(3)
                page.run_coroutine(lambda: page.go("/login"))

            threading.Thread(target=delayed_logout, daemon=True).start()
        else:
            error_text.value = "当前密码错误"
            error_text.visible = True
            success_text.visible = False
            page.update()

    def go_back(e):
        if on_back:
            on_back()
        else:
            page.go("/user")

    header = ft.Container(
        content=ft.Row(
            controls=[
                ft.TextButton(
                    "返回",
                    on_click=go_back,
                    style=ft.ButtonStyle(
                        color=ft.Colors.BLUE,
                    ),
                ),
                ft.Text("修改密码",
                        size=UI_STYLES["text"]["title"]["size"],
                        weight=UI_STYLES["text"]["title"]["weight"],
                        color=UI_STYLES["text"]["title"]["color"],
                        expand=True),
            ],
            alignment=ft.MainAxisAlignment.START,
        ),
        padding=ft.padding.all(15),
        bgcolor=ft.Colors.WHITE,
        shadow=ft.BoxShadow(spread_radius=1, blur_radius=5, color=ft.Colors.BLACK12),
    )

    form = ft.Column(
        controls=[
            old_password,
            new_password,
            confirm_password,
            error_text,
            success_text,
            ft.ElevatedButton(
                "确认修改",
                width=200,
                height=45,
                style=ft.ButtonStyle(
                    shape=UI_STYLES["button"]["primary"]["shape"],
                    bgcolor=UI_STYLES["button"]["primary"]["bgcolor"],
                    color=UI_STYLES["button"]["primary"]["color"],
                ),
                on_click=do_change,
            ),
        ],
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
                header,
                ft.Container(
                    expand=True,
                    width=float('inf'),
                    content=ft.Column(
                        controls=[form],
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        alignment=ft.MainAxisAlignment.CENTER,
                    ),
                    padding=ft.padding.all(40),
                ),
            ],
            spacing=0,
        ),
        padding=ft.padding.all(PAGE_CONTAINER_STYLES["content_card"]["padding"]),
        border_radius=PAGE_CONTAINER_STYLES["content_card"]["border_radius"],
    )

    return ft.Stack(
        expand=True,
        controls=[
            ft.Image(src=BACKGROUND_IMAGE_2,
                     width=PAGE_CONTAINER_STYLES["background_image"]["width"],
                     height=PAGE_CONTAINER_STYLES["background_image"]["height"],
                     fit=PAGE_CONTAINER_STYLES["background_image"]["fit"]),
            ft.Container(expand=True, width=float('inf'),
                         content=ft.Container(expand=True, width=float('inf'), content=content_card),
                         margin=ft.margin.all(PAGE_CONTAINER_STYLES["outer_margin"])),
        ]
    )