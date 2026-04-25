import flet as ft
import asyncio
from config import COLORS, SYSTEM_PROMPT, UI_STYLES, BACKGROUND_IMAGE_1, TEXTFIELD_STYLES, PAGE_CONTAINER_STYLES


def ai_custom_page(page: ft.Page):
    print("AI定制页面加载")

    destination = ft.TextField(
        label="目的地城市",
        width=TEXTFIELD_STYLES["width"],
        bgcolor=TEXTFIELD_STYLES["bgcolor"],
        color=TEXTFIELD_STYLES["color"],
        label_style=TEXTFIELD_STYLES["label_style"],
        border_color=TEXTFIELD_STYLES["border_color"],
        focused_border_color=TEXTFIELD_STYLES["focused_border_color"],
    )

    days = ft.TextField(
        label="出行天数",
        width=TEXTFIELD_STYLES["width"],
        bgcolor=TEXTFIELD_STYLES["bgcolor"],
        color=TEXTFIELD_STYLES["color"],
        label_style=TEXTFIELD_STYLES["label_style"],
        border_color=TEXTFIELD_STYLES["border_color"],
        focused_border_color=TEXTFIELD_STYLES["focused_border_color"],
    )

    people = ft.TextField(
        label="出行人数",
        width=TEXTFIELD_STYLES["width"],
        bgcolor=TEXTFIELD_STYLES["bgcolor"],
        color=TEXTFIELD_STYLES["color"],
        label_style=TEXTFIELD_STYLES["label_style"],
        border_color=TEXTFIELD_STYLES["border_color"],
        focused_border_color=TEXTFIELD_STYLES["focused_border_color"],
    )

    budget = ft.TextField(
        label="预算范围",
        width=TEXTFIELD_STYLES["width"],
        bgcolor=TEXTFIELD_STYLES["bgcolor"],
        color=TEXTFIELD_STYLES["color"],
        label_style=TEXTFIELD_STYLES["label_style"],
        border_color=TEXTFIELD_STYLES["border_color"],
        focused_border_color=TEXTFIELD_STYLES["focused_border_color"],
    )

    preference = ft.TextField(
        label="兴趣偏好",
        multiline=True,
        width=TEXTFIELD_STYLES["width"],
        bgcolor=TEXTFIELD_STYLES["bgcolor"],
        color=TEXTFIELD_STYLES["color"],
        label_style=TEXTFIELD_STYLES["label_style"],
        border_color=TEXTFIELD_STYLES["border_color"],
        focused_border_color=TEXTFIELD_STYLES["focused_border_color"],
    )

    result_text = ft.Text("", selectable=True, color=COLORS["black"], size=14)

    result_content = ft.Container(
        content=result_text,
        padding=ft.padding.all(15),
    )

    result_scroll = ft.Column(
        controls=[result_content],
        scroll=ft.ScrollMode.AUTO,
        expand=True,
    )

    result_container = ft.Container(
        content=result_scroll,
        bgcolor=ft.Colors.WHITE,
        border_radius=10,
        margin=ft.margin.only(top=10),
        width=float('inf'),
        height=400,
        visible=False,
    )

    loading_container = ft.Container(
        content=ft.Column(
            controls=[
                ft.ProgressRing(width=60, height=60, stroke_width=6, color=COLORS["primary"]),
                ft.Text("AI正在思考中，请稍候...", size=16, color=COLORS["primary"], weight=ft.FontWeight.BOLD),
                ft.Text("正在为你定制专属旅行计划", size=12, color=COLORS["primary"]),
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=20,
        ),
        padding=ft.padding.all(40),
        bgcolor=ft.Colors.WHITE,
        border_radius=10,
        margin=ft.margin.only(top=10),
        width=float('inf'),
        height=400,
        visible=False,
    )

    ds_client = None

    def get_client():
        nonlocal ds_client
        if ds_client is None:
            print("创建客户端")
            from services.deepseek import DeepSeekClient
            ds_client = DeepSeekClient(page)
            print("客户端创建完成")
        return ds_client

    # 异步生成函数
    async def generate_async(e):
        print("开始生成")

        if not destination.value or not days.value:
            print("缺少必要信息")
            page.snack_bar = ft.SnackBar(ft.Text("请填写目的地和天数"))
            page.snack_bar.open = True
            page.update()  # 同步更新
            return

        print(f"目的地: {destination.value}, 天数: {days.value}")

        btn = e.control
        result_text.value = ""
        loading_container.visible = True
        result_container.visible = False
        btn.text = "生成中..."
        btn.disabled = True
        page.update()

        try:
            print("开始调用API...")
            client = get_client()
            prompt = f"""{SYSTEM_PROMPT}

用户需求：
目的地：{destination.value}
天数：{days.value}
人群：{people.value if people.value else "不限"}
预算：{budget.value if budget.value else "不限"}
偏好：{preference.value if preference.value else "不限"}"""

            # 在线程池中运行同步代码
            reply, error = await asyncio.to_thread(client.send_message, prompt)

            loading_container.visible = False
            result_container.visible = True

            if error:
                result_text.value = f"出错了：{error}"
                result_text.color = ft.Colors.RED
            else:
                result_text.value = reply
                result_text.color = COLORS["black"]

        except Exception as e:
            print(f"生成异常: {e}")
            loading_container.visible = False
            result_container.visible = True
            result_text.value = f"出错了：{str(e)}"
            result_text.color = ft.Colors.RED
            import traceback
            traceback.print_exc()
        finally:
            btn.text = "生成旅行计划"
            btn.disabled = False
            page.update()  # 同步更新
            print("UI更新完成")

    generate_btn = ft.ElevatedButton(
        "生成旅行计划",
        width=180,
        height=45,
        style=ft.ButtonStyle(
            shape=UI_STYLES["button"]["primary"]["shape"],
            bgcolor=UI_STYLES["button"]["primary"]["bgcolor"],
            color=UI_STYLES["button"]["primary"]["color"],
        ),
        on_click=lambda e: asyncio.create_task(generate_async(e)),
    )

    form = ft.Column(
        controls=[
            destination,
            days,
            people,
            budget,
            preference,
            ft.Container(
                content=generate_btn,
                margin=ft.margin.only(top=20),
            ),
        ],
        spacing=UI_STYLES["spacing"]["medium"],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    )

    result_area = ft.Container(
        content=ft.Stack(
            controls=[
                loading_container,
                result_container,
            ],
        ),
        width=float('inf'),
    )

    content_card = ft.Container(
        expand=True,
        width=float('inf'),
        content=ft.Column(
            expand=True,
            width=float('inf'),
            scroll=ft.ScrollMode.AUTO,
            controls=[
                ft.Text("AI智能定制", size=UI_STYLES["text"]["title"]["size"],
                        weight=UI_STYLES["text"]["title"]["weight"],
                        color=UI_STYLES["text"]["title"]["color"]),
                ft.Text("填写你的旅行需求，AI将为你定制专属计划",
                        size=UI_STYLES["text"]["subtitle"]["size"],
                        color=UI_STYLES["text"]["subtitle"]["color"]),
                form,
                ft.Divider(height=1, color=ft.Colors.GREY_300),
                result_area,
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=UI_STYLES["spacing"]["large"],
        ),
        padding=ft.padding.all(PAGE_CONTAINER_STYLES["content_card"]["padding"]),
        border_radius=PAGE_CONTAINER_STYLES["content_card"]["border_radius"],
    )

    return ft.Stack(
        expand=True,
        controls=[
            ft.Image(src=BACKGROUND_IMAGE_1,
                     width=PAGE_CONTAINER_STYLES["background_image"]["width"],
                     height=PAGE_CONTAINER_STYLES["background_image"]["height"],
                     fit=PAGE_CONTAINER_STYLES["background_image"]["fit"]),
            ft.Container(expand=True, width=float('inf'),
                         content=ft.Container(expand=True, width=float('inf'), content=content_card),
                         margin=ft.margin.all(PAGE_CONTAINER_STYLES["outer_margin"])),
        ]
    )