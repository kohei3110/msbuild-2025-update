from typing import Annotated
from semantic_kernel.functions import kernel_function
from utils.cosmosdb_client import CosmosDBClient

class BookingPlugin:
    def __init__(self):
        self.db = CosmosDBClient()    
    
    @kernel_function(description="指定された日付で客室が利用可能かどうかを確認します。")
    def check_availability(
        self,
        room_type: Annotated[str, "客室タイプ"],
        date: Annotated[str, "予約日"]
    ) -> Annotated[str, "空室情報"]:
        room_type = room_type.lower()
        
        room = self.db.get_room_availability(room_type, date)
        if room and room["available"] > 0:
            return f"{date}に{room['available']}室の{room_type}が空いています。料金: {room['price']}"
        return f"申し訳ございませんが、{date}に{room_type}の空室はございません。"

    @kernel_function(description="予約を確定し、客室数を減らします。")
    def confirm_booking(
        self,
        room_type: Annotated[str, "客室タイプ"],
        date: Annotated[str, "予約日"],
        count: Annotated[int, "予約する客室数"]
    ) -> Annotated[str, "確認メッセージ"]:
        room_type = room_type.lower()
        room = self.db.get_room_availability(room_type, date)
        if not room:
            return f"{date}に{room_type}の客室が見つかりませんでした。"
        if room["available"] < count:
            return f"{date}に{room_type}は{room['available']}室のみ空いています。"
        updated = self.db.update_room_count(room_type, date, count)
        return f"✅ {date}に{count}室の{room_type}を{room['price']}で予約確定いたしました。"