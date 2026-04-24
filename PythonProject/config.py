import flet as ft

# DeepSeek API 配置
DEEPSEEK_API_KEY = 
DEEPSEEK_BASE_URL = "https://api.deepseek.com"
DEEPSEEK_MODEL = "deepseek-chat"

# 系统提示词（定义 AI 的说话格式）
SYSTEM_PROMPT = """你是一名旅游方案计划师，请遵守以下格式：
1. 用中文回答，简洁清晰
2. 你需要根据用户需要推荐旅行方案
    方案包括：方案名称，适合人群，行程安排，预算范围
3.字数控制在500字以内   
4.不要使用*号，尽可能使用一些表情
4. 保持专业友好的语气"""

# API 参数
TEMPERATURE = 0.7
MAX_TOKENS = 2000
TOP_P = 0.9

# UI 配置
USER_MESSAGE_COLOR = "BLUE_50"
AI_MESSAGE_COLOR = "GREY_100"
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

from flet import Colors

BACKGROUND_IMAGE = "resource/img/1.png"


COLORS = {
    "primary": "#165DFF",
    "accent": "#FF7D00",
    "bg": "#E8F3FF",
    "white": "#FFFFFF",
    "black": "#000000",
    "grey_100": "#F5F5F5",
    "grey_600": "#757575",
}

# UI 样式配置
UI_STYLES = {
    # 按钮样式
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
    # 下拉框样式（只支持 Flet 0.83.0 的参数）
    "dropdown": {
        "label_style": ft.TextStyle(color=COLORS["primary"], size=14),
        "width": 200,
        "border_color": COLORS["primary"],
        "focused_border_color": COLORS["accent"],
    },
    # 文本样式
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
    # 容器样式
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
    # 间距配置
    "spacing": {
        "small": 10,
        "medium": 20,
        "large": 30,
    },
}
