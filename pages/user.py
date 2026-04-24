import flet as ft
from config import COLORS, UI_STYLES, BACKGROUND_IMAGE_2, USER_STYLES, CARD_STYLES, PAGE_CONTAINER_STYLES

def user_page(page: ft.Page, is_logged_in=False, username=""):

    def go_to_favorites(e):
        page.go("/favorites")

    def go_to_change_password(e):
        page.go("/change_password")

    if not is_logged_in:
        content_card = ft.Container(
            expand=True,
            width=float('inf'),
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
            padding=ft.padding.all(PAGE_CONTAINER_STYLES["content_card"]["padding"]),
            border_radius=PAGE_CONTAINER_STYLES["content_card"]["border_radius"],
        )
    else:
        avatar_container = ft.Container(
            content=ft.Text("", size=USER_STYLES["avatar"]["text_size"],
                          color=USER_STYLES["avatar"]["text_color"]),
            width=USER_STYLES["avatar"]["width"],
            height=USER_STYLES["avatar"]["height"],
            bgcolor=USER_STYLES["avatar"]["bgcolor"],
            border_radius=USER_STYLES["avatar"]["border_radius"],
        )

        username_text = ft.Text(username,
                               size=USER_STYLES["username"]["size"],
                               weight=USER_STYLES["username"]["weight"],
                               color=USER_STYLES["username"]["color"])

        user_row = ft.Row(
            controls=[avatar_container, ft.Column(controls=[username_text], spacing=5)],
            spacing=15,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
        )

        user_card = ft.Container(
            content=user_row,
            padding=CARD_STYLES["user_card"]["padding"],
            bgcolor=CARD_STYLES["user_card"]["bgcolor"],
            border_radius=CARD_STYLES["user_card"]["border_radius"],
            margin=ft.margin.only(bottom=CARD_STYLES["user_card"]["margin_bottom"]),
            shadow=CARD_STYLES["user_card"]["shadow"],
        )

        def menu_item(title):
            container = ft.Container(
                content=ft.Row(
                    controls=[
                        ft.Text(title,
                                size=USER_STYLES["menu_item"]["text_size"],
                                color=USER_STYLES["menu_item"]["text_color"]),
                        ft.Text(">", size=USER_STYLES["menu_item"]["text_size"],
                                color=USER_STYLES["menu_item"]["arrow_color"]),
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                ),
                padding=ft.padding.symmetric(
                    vertical=USER_STYLES["menu_item"]["padding_vertical"],
                    horizontal=USER_STYLES["menu_item"]["padding_horizontal"]
                ),
                ink=True,
            )
            if title == "收藏":
                container.on_click = go_to_favorites
            elif title == "修改密码":
                container.on_click = go_to_change_password
            else:
                container.on_click = lambda e: print(f"点击了{title}")
            return container

        def logout(e):
            page.go("/login")
            page.update()

        logout_btn = ft.Container(
            content=ft.ElevatedButton(
                "退出登录",
                width=USER_STYLES["logout_button"]["width"],
                height=USER_STYLES["logout_button"]["height"],
                style=ft.ButtonStyle(
                    shape=USER_STYLES["logout_button"]["shape"],
                    bgcolor=USER_STYLES["logout_button"]["bgcolor"],
                    color=USER_STYLES["logout_button"]["color"],
                ),
                on_click=logout,
            ),
            margin=ft.margin.only(top=20),
        )

        menu_card = ft.Container(
            content=ft.Column(
                controls=[
                    menu_item("修改密码"),
                    ft.Divider(height=1, color=ft.Colors.GREY_200),
                    menu_item("收藏"),
                    ft.Divider(height=1, color=ft.Colors.GREY_200),
                ],
                spacing=0,
            ),
            bgcolor=CARD_STYLES["menu_card"]["bgcolor"],
            border_radius=CARD_STYLES["menu_card"]["border_radius"],
            shadow=CARD_STYLES["menu_card"]["shadow"],
        )

        content_card = ft.Container(
            expand=True,
            width=float('inf'),
            content=ft.Column(
                expand=True,
                width=float('inf'),
                controls=[
                    ft.Container(
                        content=ft.Text("我的",
                                      size=USER_STYLES["section_title"]["size"],
                                      weight=USER_STYLES["section_title"]["weight"],
                                      color=USER_STYLES["section_title"]["color"]),
                        padding=ft.padding.only(top=20, left=20, right=20, bottom=10),
                    ),
                    ft.Container(content=user_card, padding=ft.padding.symmetric(horizontal=16)),
                    ft.Container(content=menu_card, padding=ft.padding.symmetric(horizontal=16),
                               margin=ft.margin.only(top=10)),
                    logout_btn,
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
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