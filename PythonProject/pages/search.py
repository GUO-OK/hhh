import flet as ft
from config import UI_STYLES, COLORS
from database import db


def result_page(page, search_params, on_back=None):
    """搜索结果页面"""

    # 获取搜索条件
    day_range = search_params.get("day_range", "未选择")
    route_type = search_params.get("route_type", "未选择")
    budget_level = search_params.get("budget_level", "未选择")

    # 查询数据库
    results = db.search_routes(
        day_range=day_range if day_range != "未选择" else None,
        route_type=route_type if route_type != "未选择" else None,
        budget_level=budget_level if budget_level != "未选择" else None,
    )

    # 搜索条件显示
    search_info = ft.Container(
        expand=True,
        width=float('inf'),
        content=ft.Row(
            expand=True,
            width=float('inf'),
            controls=[
                ft.Text(f"天数: {day_range}", size=16, color=COLORS["primary"]),
                ft.Text(f"校区: {route_type}", size=16, color=COLORS["primary"]),
                ft.Text(f"预算: {budget_level}", size=16, color=COLORS["primary"]),
            ],
            spacing=20,
            alignment=ft.MainAxisAlignment.CENTER,
        ),
        padding=15,
        bgcolor=ft.Colors.WHITE,
        border_radius=10,
        shadow=ft.BoxShadow(spread_radius=1, blur_radius=5, color=ft.Colors.BLACK12),
        margin=ft.margin.only(bottom=20),
    )

    # 结果显示容器
    results_container = ft.Column(spacing=15, scroll=ft.ScrollMode.AUTO)

    if results:
        for row in results:
            results_container.controls.append(
                ft.Container(
                    expand=True,
                    width=float('inf'),
                    content=ft.Column(
                        controls=[
                            ft.Text(f"keyword: {row.get('keyword', '')}", size=16, weight=ft.FontWeight.BOLD,
                                    color=COLORS["primary"]),
                            ft.Text(f"slug: {row.get('slug', '')}", size=14, color=COLORS["grey_600"]),
                            ft.Text(f"route_details: {row.get('route_details', '')}", size=14, color=COLORS["grey_600"]),
                            ft.Text(f"dining: {row.get('dining', '')}", size=14, color=COLORS["grey_600"]),
                            ft.Text(f"accommodation: {row.get('accommodation', '')}", size=14, color=COLORS["grey_600"]),
                            ft.Text(f"cost_estimation: {row.get('cost_estimation', '')}", size=14, color=COLORS["grey_600"]),
                            ft.Text(f"tags: {row.get('tags', '')}", size=14, color=COLORS["grey_600"]),
                        ],
                        spacing=8,
                    ),
                    padding=20,
                    bgcolor=ft.Colors.WHITE,
                    border_radius=15,
                    shadow=ft.BoxShadow(spread_radius=1, blur_radius=8, color=ft.Colors.BLACK12),
                )
            )
    else:
        results_container.controls.append(
            ft.Container(
                content=ft.Text("没有找到相关路线", size=18, color=COLORS["grey_600"]),
                padding=50,
                bgcolor=ft.Colors.WHITE,
                border_radius=15,

            )
        )

    # 返回完整页面
    return ft.Container(
        expand=True,
        width=float('inf'),
        content=ft.Column(
            expand=True,
            width=float('inf'),
            scroll=ft.ScrollMode.AUTO,
            controls=[
                # 顶部栏
                ft.Container(
                    expand=True,
                    width=float('inf'),
                    content=ft.Row(
                        expand=True,
                        width=float('inf'),
                        controls=[
                            ft.Text("搜索结果", size=24, weight=ft.FontWeight.BOLD, color=COLORS["primary"]),
                        ],
                        alignment=ft.MainAxisAlignment.START,
                        spacing=10,
                    ),
                    padding=ft.padding.all(15),
                    bgcolor=ft.Colors.WHITE,
                    shadow=ft.BoxShadow(spread_radius=1, blur_radius=5, color=ft.Colors.BLACK12),
                ),
                # 主要内容
                ft.Container(
                    expand=True,
                    width=float('inf'),
                    content=ft.Column(
                        controls=[
                            search_info,
                            results_container,
                        ],
                        spacing=20,
                    ),
                    padding=ft.padding.all(20),
                ),
            ],
            spacing=0,
        ),
        bgcolor=UI_STYLES["container"]["main"]["bgcolor"],
    )