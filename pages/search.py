import flet as ft
from config import COLORS, BACKGROUND_IMAGE_2, CARD_STYLES, SEARCH_STYLES, PAGE_CONTAINER_STYLES
from services.database import db

def result_page(page, search_params, on_back=None, username=None, is_logged_in=False):
    print(f"search_params: {search_params}")

    day_range = search_params.get("day_range", "未选择")
    route_type = search_params.get("route_type", "未选择")
    budget_level = search_params.get("budget_level", "未选择")

    print(f"day_range={day_range}, route_type={route_type}, budget_level={budget_level}")

    results = db.search_routes(
        day_range=day_range if day_range != "未选择" else None,
        route_type=route_type if route_type != "未选择" else None,
        budget_level=budget_level if budget_level != "未选择" else None,
    )

    print(f"搜索到的结果数量: {len(results)}")
    if results:
        print(f"第一条数据: {results[0]}")
    else:
        print("没有搜索到任何结果")
        db.connect()
        cursor = db.connection.cursor()
        cursor.execute("SELECT COUNT(*) FROM travel_route")
        total = cursor.fetchone()[0]
        print(f"数据库中总共有 {total} 条路线数据")
        db.disconnect()

    def toggle_favorite(route_id, btn, route_name):
        if not is_logged_in:
            page.snack_bar = ft.SnackBar(ft.Text("请先登录后再收藏"))
            page.snack_bar.open = True
            page.update()
            return
        if db.check_favorite(username, route_id):
            if db.remove_favorite(username, route_id):
                btn.text = "收藏"
                btn.style.color = COLORS["primary"]
                page.snack_bar = ft.SnackBar(ft.Text(f"已取消收藏: {route_name}"))
                page.snack_bar.open = True
                print(f"咋不能用")
        else:
            if db.add_favorite(username, route_id):
                btn.text = "已收藏"
                btn.style.color = ft.Colors.RED
                page.snack_bar = ft.SnackBar(ft.Text(f"已添加收藏: {route_name}"))
                page.snack_bar.open = True
                print(f"成")

        page.update()

    search_info = ft.Container(
        expand=True,
        width=float('inf'),
        content=ft.Column(
            scroll=ft.ScrollMode.AUTO,
            expand=True,
            width=float('inf'),
            controls=[
                ft.Container(
                    content=ft.Text(f"天数: {day_range}", size=16, color=COLORS["primary"]),
                ),
                ft.Container(
                    content=ft.Text(f"校区: {route_type}", size=16, color=COLORS["primary"]),
                ),
                ft.Container(
                    content=ft.Text(f"预算: {budget_level}", size=16, color=COLORS["primary"]),
                ),
            ],
            spacing=20,
            alignment=ft.MainAxisAlignment.CENTER,
        ),
        padding=CARD_STYLES["search_info"]["padding"],
        bgcolor=CARD_STYLES["search_info"]["bgcolor"],
        border_radius=CARD_STYLES["search_info"]["border_radius"],
        shadow=CARD_STYLES["search_info"]["shadow"],
        margin=ft.margin.only(bottom=CARD_STYLES["search_info"]["margin_bottom"]),
    )

    results_container = ft.Column(spacing=15, scroll=ft.ScrollMode.AUTO)

    if results:
        for row in results:
            route_id = row.get('id')
            route_name = row.get('keyword', '')
            is_favorited = db.check_favorite(username, route_id) if is_logged_in and username else False
            favorite_btn = ft.TextButton(
                content=ft.Text("已收藏" if is_favorited else "收藏"),
                style=ft.ButtonStyle(
                    color=ft.Colors.RED if is_favorited else COLORS["primary"],
                ),
            )

            def make_on_click(rid, btn, name):
                return lambda e: toggle_favorite(rid, btn, name)
            favorite_btn.on_click = make_on_click(route_id, favorite_btn, route_name)
            # favorite_btn.on_click = lambda e, rid=route_id, btn=favorite_btn, name=route_name: toggle_favorite(rid, btn, name)
            results_container.controls.append(
                ft.Container(
                    expand=True,
                    width=float('inf'),
                    content=ft.Column(
                        scroll=ft.ScrollMode.AUTO,
                        controls=[
                            ft.Row(scroll=ft.ScrollMode.AUTO,
                                controls=[
                                    ft.Text(f"📍 {row.get('keyword', '')}",
                                            size=SEARCH_STYLES["result_text"]["title_size"],
                                            weight=SEARCH_STYLES["result_text"]["title_weight"],
                                            color=SEARCH_STYLES["result_text"]["title_color"],
                                            expand=True),
                                    favorite_btn,
                                ],
                                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                            ),
                            ft.Text(f"📅 happy时间：{row.get('day_range', '')} ",
                                    size=SEARCH_STYLES["result_text"]["detail_size"],
                                    color=SEARCH_STYLES["result_text"]["detail_color"]),
                            ft.Text(f"💰 类型：{row.get('budget_level', '')}",
                                    size=SEARCH_STYLES["result_text"]["detail_size"],
                                    color=SEARCH_STYLES["result_text"]["detail_color"]),
                            ft.Text(f"🏷️ 你是我的tags~：{row.get('tags', '')}",
                                    size=SEARCH_STYLES["result_text"]["detail_size"],
                                    color=SEARCH_STYLES["result_text"]["detail_color"]),
                            ft.Text(f"📝 大致路线："
                                    f"{row.get('route_details', '')}",
                                    size=SEARCH_STYLES["result_text"]["detail_size"],
                                    color=SEARCH_STYLES["result_text"]["detail_color"]),
                            ft.Text(f"🍽️ 恰饭恰饭："
                                    f"{row.get('dining', '')}",
                                    size=SEARCH_STYLES["result_text"]["detail_size"],
                                    color=SEARCH_STYLES["result_text"]["detail_color"]),
                            ft.Text(f"🏨 碎觉碎觉："
                                    f"{row.get('accommodation', '')}",
                                    size=SEARCH_STYLES["result_text"]["detail_size"],
                                    color=SEARCH_STYLES["result_text"]["detail_color"]),
                            ft.Text(f"💰 大致预算："
                                    f"{row.get('cost_estimation', '')}",
                                    size=SEARCH_STYLES["result_text"]["detail_size"],
                                    color=SEARCH_STYLES["result_text"]["detail_color"]),
                        ],
                        spacing=8,
                    ),
                    padding=CARD_STYLES["result_card"]["padding"],
                    bgcolor=CARD_STYLES["result_card"]["bgcolor"],
                    border_radius=CARD_STYLES["result_card"]["border_radius"],
                    shadow=CARD_STYLES["result_card"]["shadow"],
                )
            )
    else:
        results_container.controls.append(
            ft.Container(
                content=ft.Text("没有找到相关路线",
                                size=SEARCH_STYLES["empty_result"]["size"],
                                color=SEARCH_STYLES["empty_result"]["color"]),
                padding=SEARCH_STYLES["empty_result"]["padding"],
                bgcolor=SEARCH_STYLES["empty_result"]["bgcolor"],
                border_radius=SEARCH_STYLES["empty_result"]["border_radius"],
            )
        )

    content_card = ft.Container(
        expand=True,
        width=float('inf'),
        content=ft.Column(
            expand=True,
            width=float('inf'),
            scroll=ft.ScrollMode.AUTO,
            controls=[
                ft.Container(
                    expand=True,
                    width=float('inf'),
                    content=ft.Column(
                        scroll=ft.ScrollMode.AUTO,
                        controls=[
                            ft.Text("搜索结果",
                                size=SEARCH_STYLES["header"]["size"],
                                weight=SEARCH_STYLES["header"]["weight"],
                                color=SEARCH_STYLES["header"]["color"])],
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        alignment=ft.MainAxisAlignment.CENTER,
                        spacing=20,
                    ),
                    padding=ft.padding.all(10),
                ),
                ft.Container(
                    expand=True,
                    width=float('inf'),
                    content=ft.Column(
                        controls=[
                            search_info,
                            results_container],
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        alignment=ft.MainAxisAlignment.CENTER,
                        spacing=20
                    ),
                    padding=ft.padding.all(10)),
            ],
            spacing=0,
        ),
        padding=ft.padding.only(left=0, right=0, top=10, bottom=10),
        border_radius=PAGE_CONTAINER_STYLES["content_card"]["border_radius"],
    )

    return ft.Stack(
        expand=True,
        controls=[
            ft.Image(src=BACKGROUND_IMAGE_2,
                     width=PAGE_CONTAINER_STYLES["background_image"]["width"],
                     height=PAGE_CONTAINER_STYLES["background_image"]["height"],
                     fit=PAGE_CONTAINER_STYLES["background_image"]["fit"]),
            ft.Container(expand=True, width=float('inf'),
                         content=ft.Container(expand=True, width=float('inf'), content=content_card),
                         margin=ft.margin.all(PAGE_CONTAINER_STYLES["outer_margin"])),
        ]
    )