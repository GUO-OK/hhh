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
            expand=True,  # Column 充满整个页面
            spacing=0,
            width=float('inf'),  # 确保 Column 宽度无限
            controls=[
                build_layout(page)
            ]
        )
    )


if __name__ == "__main__":
    ft.run(main)