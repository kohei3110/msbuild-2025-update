from datetime import datetime, timedelta
from semantic_kernel.functions import kernel_function
from typing import Annotated

class TimePlugin:
    """現在の日付や相対的な日付を取得するユーティリティスキル。"""

    @kernel_function(description="今日の日付をYYYY-MM-DD形式で返します。")
    def get_today(self) -> Annotated[str, "YYYY-MM-DD形式でフォーマットされた現在の日付。"]:
        return datetime.now().strftime("%Y-%m-%d")

    @kernel_function(description="日数のオフセットに基づいて相対的な日付を返します。")
    def get_relative_date(self, days_offset: Annotated[int, "今日に追加する日数。"]) -> Annotated[str, "今日からオフセットされた日付をYYYY-MM-DD形式で。"]:
        return (datetime.now() + timedelta(days=days_offset)).strftime("%Y-%m-%d")