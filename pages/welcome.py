import asyncio
import flet as ft
from config import WELCOME_STYLES


def welcome_page(page: ft.Page, on_complete):
    is_completed = False

    def complete():
        nonlocal is_completed
        if not is_completed:
            is_completed = True
            on_complete()

    welcome = ft.Container(
        expand=True,
        width=float('inf'),
        bgcolor=WELCOME_STYLES["container"]["bgcolor"],
        content=ft.Stack(
            expand=True,
            controls=[
                ft.Container(
                    expand=True,
                    width=float('inf'),
                    content=ft.Column(
                        controls=[
                            ft.Text(
                                "欢迎^^",
                                size=WELCOME_STYLES["title"]["size"],
                                weight=WELCOME_STYLES["title"]["weight"],
                                color=WELCOME_STYLES["title"]["color"],
                                text_align=WELCOME_STYLES["title"]["text_align"],
                            ),
                            ft.Text(
                                "欢迎使用本应用",
                                size=WELCOME_STYLES["subtitle"]["size"],
                                color=WELCOME_STYLES["subtitle"]["color"],
                                text_align=WELCOME_STYLES["subtitle"]["text_align"],
                            ),
                        ],
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        alignment=ft.MainAxisAlignment.CENTER,
                        spacing=10,
                    ),
                ),
                ft.Container(
                    content=ft.ElevatedButton(
                        "跳过",
                        on_click=lambda e: complete(),
                        style=ft.ButtonStyle(
                            color=WELCOME_STYLES["skip_button"]["color"],
                            bgcolor=WELCOME_STYLES["skip_button"]["bgcolor"],
                            shape=WELCOME_STYLES["skip_button"]["shape"],
                        ),
                    ),
                    top=WELCOME_STYLES["skip_button"]["position"]["top"],
                    right=WELCOME_STYLES["skip_button"]["position"]["right"],
                ),
            ]
        ),
    )

    async def auto_next():
        await asyncio.sleep(WELCOME_STYLES["auto_next_delay"])
        complete()

    asyncio.create_task(auto_next())
    return welcome