import ssl
import certifi
import flet as ft

ssl._create_default_https_context = lambda: ssl.create_default_context(cafile=certifi.where())

def main(page: ft.Page):
    page.title = "旅游计划助手"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    # 创建一个输入框
    input_text = ft.TextField(
        hint_text="输入地点，例如：北京",
        width=300
    )

    # 创建一个按钮
    def on_search_click(e):
        input_text.value = f"你输入了：{input_text.value}"
        page.update()

    search_btn = ft.Button(  # 注意：参数名变了
        content=ft.Text("搜索"),  # ✅ 用 content 包裹 Text
        on_click=on_search_click
    )

    # 把组件加到页面上
    page.add(
        ft.Text("旅游计划助手", size=30, weight=ft.FontWeight.BOLD),
        input_text,
        search_btn
    )


# 运行应用
ft.run(main)