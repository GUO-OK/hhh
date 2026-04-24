import flet as ft

from controller import build_layout


def main(page: ft.Page):
    page.padding = 0
    page.spacing = 0
    page.title = "乡旅与海E模式"
    # 调用布局构建函数
    # img = ft.Image(
    #     src="resource/img/test.png",
    #     width=400,
    # )
    # page.add(img)

    page.add(
        ft.Column(
            expand=True,
            spacing=0,
            width=float('inf'),
            controls=[
                build_layout(page)
            ]
        )
    )


if __name__ == "__main__":
    ft.run(main)