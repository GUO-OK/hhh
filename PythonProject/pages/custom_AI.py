import flet as ft
from config import COLORS, SYSTEM_PROMPT, UI_STYLES
from services.deepseek import DeepSeekClient


def ai_custom_page(page: ft.Page):
    # 输入框（使用 home.py 的样式）
    destination = ft.TextField(
        label="目的地城市",
        width=350,
        bgcolor="#FFFFFF",
        color=COLORS["black"],
        label_style=UI_STYLES["dropdown"]["label_style"],
        border_color=UI_STYLES["dropdown"]["border_color"],
        focused_border_color=UI_STYLES["dropdown"]["focused_border_color"],
    )

    days = ft.TextField(
        label="出行天数",
        width=350,
        bgcolor="#FFFFFF",
        color=COLORS["black"],
        label_style=UI_STYLES["dropdown"]["label_style"],
        border_color=UI_STYLES["dropdown"]["border_color"],
        focused_border_color=UI_STYLES["dropdown"]["focused_border_color"],
    )

    people = ft.TextField(
        label="出行人群",
        width=350,
        bgcolor="#FFFFFF",
        color=COLORS["black"],
        label_style=UI_STYLES["dropdown"]["label_style"],
        border_color=UI_STYLES["dropdown"]["border_color"],
        focused_border_color=UI_STYLES["dropdown"]["focused_border_color"],
    )

    budget = ft.TextField(
        label="预算范围",
        width=350,
        bgcolor="#FFFFFF",
        color=COLORS["black"],
        label_style=UI_STYLES["dropdown"]["label_style"],
        border_color=UI_STYLES["dropdown"]["border_color"],
        focused_border_color=UI_STYLES["dropdown"]["focused_border_color"],
    )

    preference = ft.TextField(
        label="兴趣偏好",
        multiline=True,
        width=350,
        bgcolor="#FFFFFF",
        color=COLORS["black"],
        label_style=UI_STYLES["dropdown"]["label_style"],
        border_color=UI_STYLES["dropdown"]["border_color"],
        focused_border_color=UI_STYLES["dropdown"]["focused_border_color"],
    )

    result_text = ft.Text("", selectable=True, color=COLORS["black"], size=14)

    ds_client = DeepSeekClient(page)

    def generate(e):
        if not destination.value or not days.value:
            page.snack_bar = ft.SnackBar(ft.Text("请填写目的地和天数"))
            page.snack_bar.open = True
            page.update()
            return

        # 使用 config.py 中的 SYSTEM_PROMPT
        prompt = f"""{SYSTEM_PROMPT}

用户需求：
目的地：{destination.value}
天数：{days.value}
人群：{people.value if people.value else "不限"}
预算：{budget.value if budget.value else "不限"}
偏好：{preference.value if preference.value else "不限"}"""

        btn = e.control
        btn.text = "生成中..."
        btn.disabled = True
        page.update()

        reply, error = ds_client.send_message(prompt)

        if error:
            result_text.value = f"出错了：{error}"
            result_text.color = ft.Colors.RED
        else:
            result_text.value = reply
            result_text.color = COLORS["black"]

        btn.text = "生成旅行计划"
        btn.disabled = False
        page.update()

    # 生成按钮（使用 home.py 的按钮样式）
    generate_btn = ft.ElevatedButton(
        "生成旅行计划",
        width=150,
        height=45,
        style=ft.ButtonStyle(
            shape=UI_STYLES["button"]["primary"]["shape"],
            bgcolor=UI_STYLES["button"]["primary"]["bgcolor"],
            color=UI_STYLES["button"]["primary"]["color"],
        ),
        on_click=generate,
    )

    # 表单布局（使用 home.py 的样式）
    form = ft.Column(
        controls=[
            destination,
            days,
            people,
            budget,
            preference,
            ft.Container(
                content=generate_btn,
                margin=ft.margin.only(top=10),
            ),
        ],
        spacing=UI_STYLES["spacing"]["medium"],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        alignment=ft.MainAxisAlignment.CENTER,
    )

    # 返回完整页面（使用 home.py 的容器样式）
    return ft.Container(
        expand=True,
        width=float('inf'),
        content=ft.Column(
            expand=True,
            width=float('inf'),
            scroll=ft.ScrollMode.AUTO,
            controls=[
                ft.Text(
                    "AI智能定制",
                    size=UI_STYLES["text"]["title"]["size"],
                    weight=UI_STYLES["text"]["title"]["weight"],
                    color=UI_STYLES["text"]["title"]["color"],
                ),
                ft.Text(
                    "填写你的旅行需求，AI将为你定制专属计划",
                    size=UI_STYLES["text"]["subtitle"]["size"],
                    color=UI_STYLES["text"]["subtitle"]["color"],
                ),
                form,
                ft.Divider(height=1, color=ft.Colors.GREY_300),
                ft.Container(
                    content=result_text,
                    padding=ft.padding.all(15),
                    bgcolor=ft.Colors.WHITE,
                    border_radius=10,
                    margin=ft.margin.only(top=10),
                ),
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=UI_STYLES["spacing"]["large"],
        ),
        bgcolor=UI_STYLES["container"]["main"]["bgcolor"],
    )