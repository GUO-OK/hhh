import os
import flet as ft
from flet import Colors
from dotenv import load_dotenv

load_dotenv()

DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY")
DEEPSEEK_BASE_URL = os.getenv("DEEPSEEK_BASE_URL", "https://api.deepseek.com")
DEEPSEEK_MODEL = os.getenv("DEEPSEEK_MODEL", "deepseek-chat")

if not DEEPSEEK_API_KEY:
    raise ValueError("请设置 DEEPSEEK_API_KEY 环境变量")

SYSTEM_PROMPT = """你是一名旅游方案计划师，请遵守以下几点：
1. 用中文回答，简洁清晰
2. 你需要根据用户需要推荐旅行方案
    方案包括：方案名称，适合人数，行程安排，预算范围
3.字数控制在1000字以内   
4.不要使用*号，每句话后加不同的表情，符合这句话的语境，不一定是面部表情，
5. 顾客是上帝，请保持专业友好的语气，不可生气"""

TEMPERATURE = 0.7
MAX_TOKENS = 2000
TOP_P = 0.9
USER_MESSAGE_COLOR = "BLUE_50"
AI_MESSAGE_COLOR = "GREY_100"
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
BACKGROUND_IMAGE_1 = "resource/img/1.png"
BACKGROUND_IMAGE_2 = "resource/img/2.png"
BACKGROUND_IMAGE_3 = "resource/img/3.png"
COLORS = {
    "primary": "#165DFF",
    "accent": "#FF7D00",
    "bg": "#E8F3FF",
    "white": "#FFFFFF",
    "black": "#000000",
    "grey_100": "#F5F5F5",
    "grey_600": "#757575",
    "OK":ft.Colors.BLUE_100
}

UI_STYLES = {
    "button": {
        "primary": {
            "bgcolor": COLORS["primary"],
            "color": COLORS["white"],
            "shape": ft.RoundedRectangleBorder(radius=25),
        },
        "accent": {
            "bgcolor": COLORS["accent"],
            "color": COLORS["white"],
            "shape": ft.RoundedRectangleBorder(radius=25),
        },
    },
    "dropdown": {
        "label_style": ft.TextStyle(color=COLORS["primary"], size=14),
        "width": 200,
        "border_color": COLORS["primary"],
        "focused_border_color": COLORS["accent"],
    },
    "text": {
        "title": {
            "size": 32,
            "weight": ft.FontWeight.BOLD,
            "color": COLORS["primary"],
        },
        "subtitle": {
            "size": 16,
            "color": COLORS["black"],
        },
        "body": {
            "size": 14,
            "color": COLORS["black"],
        },
    },
    "container": {
        "main": {
            "bgcolor": COLORS["grey_100"],
        },
        "card": {
            "bgcolor": COLORS["white"],
            "border_radius": 15,
            "shadow": ft.BoxShadow(
                spread_radius=1,
                blur_radius=10,
                color=Colors.BLACK12,
            ),
        },
    },
    "spacing": {
        "small": 10,
        "medium": 20,
        "large": 30,
    },
}

NAV_STYLES = {
    "footer": {
        "height": 60,
        "bgcolor": COLORS["OK"],
        "button_color": COLORS["primary"],
        "button_style": ft.TextStyle(color=COLORS["white"], size=14),
    }
}

WELCOME_STYLES = {
    "container": {
        "bgcolor": ft.Colors.WHITE,
        "expand": True,
    },
    "title": {
        "size": 40,
        "weight": ft.FontWeight.BOLD,
        "color": ft.Colors.BLACK87,
        "text_align": ft.TextAlign.CENTER,
    },
    "subtitle": {
        "size": 16,
        "color": ft.Colors.GREY_600,
        "text_align": ft.TextAlign.CENTER,
    },
    "skip_button": {
        "color": ft.Colors.WHITE,
        "bgcolor": ft.Colors.BLUE,
        "shape": ft.RoundedRectangleBorder(radius=8),
        "position": {"top": 20, "right": 20},
    },
    "auto_next_delay": 3,
}

TEXTFIELD_STYLES = {
    "width": 350,
    "bgcolor": "#FFFFFF",
    "color": COLORS["black"],
    "label_style": UI_STYLES["dropdown"]["label_style"],
    "border_color": UI_STYLES["dropdown"]["border_color"],
    "focused_border_color": UI_STYLES["dropdown"]["focused_border_color"],
}

CARD_STYLES = {
    "search_info": {
        "padding": 5,
        "bgcolor": ft.Colors.WHITE,
        "border_radius": 10,
        "shadow": ft.BoxShadow(spread_radius=1, blur_radius=5, color=ft.Colors.BLACK12),
        "margin_bottom": 20,
    },
    "result_card": {
        "padding": 5,
        "bgcolor": ft.Colors.WHITE,
        "border_radius": 15,
        "shadow": ft.BoxShadow(spread_radius=1, blur_radius=8, color=ft.Colors.BLACK12),
    },
    "user_card": {
        "padding": 5,
        "bgcolor": ft.Colors.WHITE,
        "border_radius": 15,
        "margin_bottom": 20,
        "shadow": ft.BoxShadow(spread_radius=1, blur_radius=10, color=ft.Colors.BLACK12),
    },
    "menu_card": {
        "bgcolor": ft.Colors.WHITE,
        "border_radius": 15,
        "shadow": ft.BoxShadow(spread_radius=1, blur_radius=10, color=ft.Colors.BLACK12),
    },
}

USER_STYLES = {
    "avatar": {
        "width": 80,
        "height": 80,
        "bgcolor": COLORS["accent"],
        "border_radius": 40,
        "text_size": 40,
        "text_color": ft.Colors.WHITE,
    },
    "username": {
        "size": 20,
        "weight": ft.FontWeight.BOLD,
        "color": COLORS["black"],
    },
    "menu_item": {
        "padding_vertical": 15,
        "padding_horizontal": 20,
        "text_size": 16,
        "text_color": COLORS["black"],
        "arrow_color": COLORS["grey_600"],
    },
    "logout_button": {
        "width": 200,
        "height": 45,
        "bgcolor": ft.Colors.RED_100,
        "color": ft.Colors.RED_700,
        "shape": ft.RoundedRectangleBorder(radius=25),
    },
    "section_title": {
        "size": 28,
        "weight": ft.FontWeight.BOLD,
        "color": COLORS["primary"],
    },
}

SEARCH_STYLES = {
    "result_text": {
        "title_size": 16,
        "title_weight": ft.FontWeight.BOLD,
        "title_color": COLORS["primary"],
        "detail_size": 14,
        "detail_color": COLORS["grey_600"],
    },
    "empty_result": {
        "size": 18,
        "color": COLORS["grey_600"],
        "padding": 50,
        "bgcolor": ft.Colors.WHITE,
        "border_radius": 15,
    },
    "header": {
        "size": 24,
        "weight": ft.FontWeight.BOLD,
        "color": COLORS["primary"],
    },
}

PAGE_CONTAINER_STYLES = {
    "content_card": {
        "padding": 1,
        "border_radius": 20,
    },
    "outer_margin": 20,
    "background_image": {
        "width": float('inf'),
        "height": float('inf'),
        "fit": "cover",
    },
}

AUTH_STYLES = {
    "error_text": {
        "color": ft.Colors.RED,
        "size": 12,
    },
}