import flet as ft

def main(page: ft.Page):
    # 设置页面标题
    page.title = "Travel App"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    
    # 添加一个简单的文本
    hello_text = ft.Text("欢迎使用 Travel App!", size=30, color=ft.Colors.BLUE)
    
    # 添加一个按钮
    def button_clicked(e):
        hello_text.value = "按钮被点击了!"
        page.update()
    
    button = ft.ElevatedButton("点击我", on_click=button_clicked)
    
    # 添加到页面
    page.add(
        hello_text,
        ft.Container(height=20),  # 间距
        button
    )

# 启动应用
ft.app(target=main)
