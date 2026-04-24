# pages/favorites.py
import flet as ft
from config import COLORS, BACKGROUND_IMAGE_2, SEARCH_STYLES, CARD_STYLES, PAGE_CONTAINER_STYLES
from database import db


def favorites_page(page: ft.Page, username: str, on_back=None):
    favorites = db.get_user_favorites(username)

    favorites_container = ft.Column(spacing=15, scroll=ft.ScrollMode.AUTO)

    def remove_favorite(route_id, card_container):
        if db.remove_favorite(username, route_id):
            if card_container in favorites_container.controls:
                favorites_container.controls.remove(card_container)
                page.update()

                page.snack_bar = ft.SnackBar(ft.Text("已取消收藏"))
                page.snack_bar.open = True
                page.update()

                if not favorites_container.controls:
                    favorites_container.controls.append(get_empty_state())
                    page.update()

    def get_empty_state():
        return ft.Container(
            content=ft.Column(
                controls=[
                    ft.Text("❤️", size=80, color=COLORS["grey_600"]),
                    ft.Text("暂无收藏",
                            size=SEARCH_STYLES["empty_result"]["size"],
                            color=SEARCH_STYLES["empty_result"]["color"]),
                    ft.Text("去首页探索更多精彩路线吧~",
                            size=14,
                            color=COLORS["grey_600"]),
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=20,
            ),
            padding=SEARCH_STYLES["empty_result"]["padding"],
            bgcolor=SEARCH_STYLES["empty_result"]["bgcolor"],
            border_radius=SEARCH_STYLES["empty_result"]["border_radius"],
            width=float('inf'),
        )

    # def create_remove_callback(route_id, card_container):
    #     return lambda e: remove_favorite(route_id, card_container)

    def build_favorite_card(route):
        route_id = route.get('id')

        remove_button = ft.TextButton(
            "取消收藏",
            style=ft.ButtonStyle(
                color=ft.Colors.RED,
            ),
        )

        card_container = ft.Container(
            expand=True,
            width=float('inf'),
            content=ft.Column(
                controls=[
                    ft.Row(
                        controls=[
                            ft.Text(f"📍 {route.get('keyword', '')}",
                                    size=SEARCH_STYLES["result_text"]["title_size"],
                                    weight=SEARCH_STYLES["result_text"]["title_weight"],
                                    color=SEARCH_STYLES["result_text"]["title_color"],
                                    expand=True),
                            remove_button,
                        ],
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    ),
                    ft.Text(f"📅 happy时间：{route.get('day_range', '')} | 💰 类型：{route.get('budget_level', '')}",
                            size=SEARCH_STYLES["result_text"]["detail_size"],
                            color=SEARCH_STYLES["result_text"]["detail_color"]),
                    ft.Text(f"🏷️ 我是你的关键词~：{route.get('tags', '')}",
                            size=SEARCH_STYLES["result_text"]["detail_size"],
                            color=SEARCH_STYLES["result_text"]["detail_color"]),
                    ft.Text(f"📝 大致路线：{route.get('route_details', '')}",
                            size=SEARCH_STYLES["result_text"]["detail_size"],
                            color=SEARCH_STYLES["result_text"]["detail_color"]),
                    ft.Text(f"🍽️ 吃什么呢？：{route.get('dining', '')}",
                            size=SEARCH_STYLES["result_text"]["detail_size"],
                            color=SEARCH_STYLES["result_text"]["detail_color"]),
                    ft.Text(f"🏨 住哪里好？{route.get('accommodation', '')}",
                            size=SEARCH_STYLES["result_text"]["detail_size"],
                            color=SEARCH_STYLES["result_text"]["detail_color"]),
                    ft.Text(f"💰 钱包预算{route.get('cost_estimation', '')}",
                            size=SEARCH_STYLES["result_text"]["detail_size"],
                            color=SEARCH_STYLES["result_text"]["detail_color"]),
                ],
                spacing=10,
            ),
            padding=CARD_STYLES["result_card"]["padding"],
            bgcolor=CARD_STYLES["result_card"]["bgcolor"],
            border_radius=CARD_STYLES["result_card"]["border_radius"],
            shadow=CARD_STYLES["result_card"]["shadow"],
        )

        remove_button.on_click = lambda e, rid=route_id, container=card_container: remove_favorite(rid, container)

        return card_container

    if favorites:
        for route in favorites:
            favorites_container.controls.append(build_favorite_card(route))
    else:
        favorites_container.controls.append(get_empty_state())

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
                ft.Text("我的收藏",
                        size=SEARCH_STYLES["header"]["size"],
                        weight=SEARCH_STYLES["header"]["weight"],
                        color=SEARCH_STYLES["header"]["color"],
                        expand=True),
            ],
            alignment=ft.MainAxisAlignment.START,
        ),
        padding=ft.padding.all(15),
        bgcolor=ft.Colors.WHITE,
        shadow=ft.BoxShadow(spread_radius=1, blur_radius=5, color=ft.Colors.BLACK12),
    )

    content_card = ft.Container(
        expand=True,
        width=float('inf'),
        content=ft.Column(
            expand=True,
            width=float('inf'),
            scroll=ft.ScrollMode.AUTO,
            controls=[
                header,
                ft.Container(
                    expand=True,
                    width=float('inf'),
                    content=favorites_container,
                    padding=ft.padding.all(20),
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