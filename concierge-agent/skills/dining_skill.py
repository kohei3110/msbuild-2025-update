from typing import Annotated
from semantic_kernel.functions import kernel_function

class DiningPlugin:
    """ダイニング関連のお問い合わせとテーブル予約を処理するプラグイン。"""

    @kernel_function(description="本日のダイニングスペシャルを提供します。")
    def get_specials(self) -> Annotated[str, "レストランのダイニングスペシャルを返します。"]:
        return """
        本日のスープ: クラムチャウダー
        本日のサラダ: コブサラダ
        本日のドリンク: チャイティー
        """

    @kernel_function(description="指定されたメニュー項目の価格を提供します。")
    def get_item_price(self, menu_item: Annotated[str, "メニュー項目名"]) -> Annotated[str, "メニュー項目の価格を返します。"]:
        return "$9.99"  # 必要に応じて動的価格設定で拡張可能

    @kernel_function(description="ホテルレストランでのテーブル予約をシミュレートします。")
    def reserve_table(self,
                      time: Annotated[str, "予約時間"],
                      party_size: Annotated[int, "人数"]) -> Annotated[str, "テーブル予約確認を返します。"]:
        return f"{party_size}名様のテーブルを{time}に予約いたしました。"