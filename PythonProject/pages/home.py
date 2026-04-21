import flet as ft
from config import UI_STYLES, COLORS,BACKGROUND_IMAGE


def home_page_component(on_search=None):
    # 天数选择
    day_range = ft.Dropdown(
        label="旅行天数",
        hint_text="请选择天数",
        options=[
            ft.dropdown.Option("1-2"),
            ft.dropdown.Option("3-5"),
            ft.dropdown.Option("6-7"),
        ],
        label_style=UI_STYLES["dropdown"]["label_style"],
        width=UI_STYLES["dropdown"]["width"],
        border_color=UI_STYLES["dropdown"]["border_color"],
        focused_border_color=UI_STYLES["dropdown"]["focused_border_color"],
        color=COLORS["black"],
    )

    # 路线类型选择
    route_type = ft.Dropdown(
        label="校区/路线类型",
        hint_text="请选择校区",
        options=[
            ft.dropdown.Option("崂山校区"),
            ft.dropdown.Option("鱼山校区"),
            ft.dropdown.Option("浮山校区"),
            ft.dropdown.Option("西海岸校区"),
        ],
        label_style=UI_STYLES["dropdown"]["label_style"],
        width=UI_STYLES["dropdown"]["width"],
        border_color=UI_STYLES["dropdown"]["border_color"],
        focused_border_color=UI_STYLES["dropdown"]["focused_border_color"],
        color=COLORS["black"],
    )

    # 预算选择
    budget_level = ft.Dropdown(
        label="预算级别",
        hint_text="请选择预算",
        options=[
            ft.dropdown.Option("经济型"),
            ft.dropdown.Option("舒适型"),
            ft.dropdown.Option("豪华型"),
        ],
        label_style=UI_STYLES["dropdown"]["label_style"],
        width=UI_STYLES["dropdown"]["width"],
        border_color=UI_STYLES["dropdown"]["border_color"],
        focused_border_color=UI_STYLES["dropdown"]["focused_border_color"],
        color=COLORS["black"],
    )

    # 搜索按钮
    search_btn = ft.ElevatedButton(
        "智能推荐",
        width=150,
        height=45,
        style=ft.ButtonStyle(
            shape=UI_STYLES["button"]["primary"]["shape"],
            bgcolor=UI_STYLES["button"]["primary"]["bgcolor"],
            color=UI_STYLES["button"]["primary"]["color"],
        ),
    )

    def on_search_click(e):
        if on_search:
            on_search({
                "day_range": day_range.value,
                "route_type": route_type.value,
                "budget_level": budget_level.value,
            })

    search_btn.on_click = on_search_click

    # 表单布局
    form = ft.Row(
        controls=[
            day_range,
            route_type,
            budget_level,
            search_btn,
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=UI_STYLES["spacing"]["medium"],
        wrap=True,
    )

    content_card = ft.Container(
        expand=True,
        width=float('inf'),
        content=ft.Column(
            expand=True,
            width=float('inf'),
            controls=[
                ft.Text(
                    "智能路线推荐",
                    size=UI_STYLES["text"]["title"]["size"],
                    weight=UI_STYLES["text"]["title"]["weight"],
                    color=UI_STYLES["text"]["title"]["color"],
                ),
                ft.Text(
                    "请选择搜索条件",
                    size=UI_STYLES["text"]["subtitle"]["size"],
                    color=UI_STYLES["text"]["subtitle"]["color"],
                ),
                form,
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=UI_STYLES["spacing"]["large"],
        ),
        padding=ft.padding.all(40),  # 内边距
        bgcolor=ft.Colors.with_opacity(0, ft.Colors.WHITE),  # 白色半透明背景
        border_radius=20,  # 圆角
    )

    # 使用 Stack 实现背景图片
    return ft.Stack(
        expand=True,
        controls=[
            # 背景图片层
            ft.Image(
                src=BACKGROUND_IMAGE,
                width=float('inf'),
                height=float('inf'),
                fit="cover",
            ),
            # 内容层（居中显示）
            ft.Container(
                expand=True,
                width=float('inf'),
                # bgcolor=ft.Colors.with_opacity(0.1, ft.Colors.WHITE),
                content=ft.Container(
                    expand=True,
                    width=float('inf'),
                    content=content_card,
                ),
                margin=ft.margin.all(20),  # 外边距
            ),
        ]
    )

