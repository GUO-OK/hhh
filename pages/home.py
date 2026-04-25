import flet as ft
from config import UI_STYLES, COLORS,BACKGROUND_IMAGE_1

def home_page_component(on_search=None):
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

    form = ft.Row(
        scroll=ft.ScrollMode.AUTO,
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
        padding=ft.padding.all(40),
        bgcolor=ft.Colors.with_opacity(0, ft.Colors.WHITE),
        border_radius=20,
    )


    return ft.Stack(
        expand=True,
        controls=[
            ft.Image(
                src=BACKGROUND_IMAGE_1,
                width=float('inf'),
                height=float('inf'),
                fit="cover",
            ),
            ft.Container(
                expand=True,
                width=float('inf'),
                # bgcolor=ft.Colors.with_opacity(0.1, ft.Colors.WHITE),
                content=ft.Container(
                    expand=True,
                    width=float('inf'),
                    content=content_card,
                ),
                margin=ft.margin.all(20),
            ),
        ]
    )

