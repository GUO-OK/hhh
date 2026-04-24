import flet as ft

# def header_component():
#     return ft.Container(
#         height=60,
#         content=ft.Row(
#             alignment=ft.MainAxisAlignment.CENTER,
#             controls=[
#                 ft.Text("上面", size=20, weight=ft.FontWeight.BOLD),
#             ]
#         ),
#         bgcolor=ft.Colors.BLUE_100,
#     )

def home_page_component():
    return ft.Container(
        expand=True,
        width=float('inf'),
        content=ft.Column(
            expand=True,
            width=float('inf'),
            controls=[
                ft.Text("主内容区域", size=20, weight=ft.FontWeight.BOLD),
                ft.ElevatedButton(
                    "按钮",
                    on_click=lambda e: print("点击了按钮"),
                    style=ft.ButtonStyle(padding=20),
                ),
                ft.TextField(
                    hint_text="输入框",
                    width=300,
                    border_radius=10,
                ),
                ft.Container(
                    content=ft.Text("这是更多内容"),
                    padding=20,
                ),
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=20,
        ),
        bgcolor=ft.Colors.GREY_100,
    )

def about_page_component():
    return ft.Container(
        expand=True,
        width=float('inf'),
        content=ft.Column(
            controls=[
                ft.Text("关于页面", size=30, weight=ft.FontWeight.BOLD),
                ft.Text("这是一个测试应用", size=16),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=20,
        ),
        bgcolor=ft.Colors.WHITE,
    )

def settings_page_component():
    return ft.Container(
        expand=True,
        width=float('inf'),
        content=ft.Column(
            controls=[
                ft.Text("设置", size=30, weight=ft.FontWeight.BOLD),
                ft.Switch(label="启用通知", value=True),
                ft.Slider(min=0, max=100, value=50),
                ft.Dropdown(
                    options=[
                        ft.dropdown.Option("选项1"),
                        ft.dropdown.Option("选项2"),
                        ft.dropdown.Option("选项3"),
                    ],
                    hint_text="请选择",
                    width=200,
                ),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=20,
        ),
    )