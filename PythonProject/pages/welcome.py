import asyncio
import flet as ft


def welcome_page(page: ft.Page, on_complete):
    # 创建欢迎页面内容
    welcome = ft.Container(
        expand=True,
        width=float('inf'),
        bgcolor=ft.Colors.WHITE,
        content=ft.Stack(
            expand=True,
            controls=[
                # 中间欢迎文字
                ft.Container(
                    expand=True,
                    width=float('inf'),
                    content=ft.Column(
                        controls=[
                            ft.Text(
                                "欢迎^^",
                                size=40,
                                weight=ft.FontWeight.BOLD,
                                color=ft.Colors.BLACK87,
                                text_align=ft.TextAlign.CENTER,
                            ),
                            ft.Text(
                                "欢迎使用本应用",
                                size=16,
                                color=ft.Colors.GREY_600,
                                text_align=ft.TextAlign.CENTER,
                            ),
                        ],
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        alignment=ft.MainAxisAlignment.CENTER,
                        spacing=10,
                    ),
                ),
                # 右上角跳过按钮
                ft.Container(
                    content=ft.ElevatedButton(
                        "跳过",
                        on_click=lambda e: on_complete(),
                        style=ft.ButtonStyle(
                            color=ft.Colors.WHITE,
                            bgcolor=ft.Colors.BLUE,
                            shape=ft.RoundedRectangleBorder(radius=8),
                        ),
                    ),
                    top=20,
                    right=20,
                ),
            ]
        ),
    )

    # 3秒后自动跳转
    async def auto_next():
        await asyncio.sleep(3)
        on_complete()

    # 创建异步任务
    asyncio.create_task(auto_next())

    return welcome