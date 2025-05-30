from typing import Annotated
from semantic_kernel.functions import kernel_function
from utils.cosmosdb_client import CosmosDBClient
from openai import AzureOpenAI
import os

class SemanticRoomSearchPlugin:
    def __init__(self):
        self.db = CosmosDBClient()
        self.openai = AzureOpenAI(
            api_key=os.getenv("AZURE_OPENAI_API_KEY"),
            api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
            azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
        )
        self.embedding_model = os.getenv("AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT")

    def embed_query(self, text: str) -> list[float]:
        return self.openai.embeddings.create(
            input=[text],
            model=self.embedding_model
        ).data[0].embedding    @kernel_function(description="セマンティック検索でホテルの客室を検索します。")
    def search_rooms_by_description(
        self,
        query: Annotated[str, "ユーザーが探している客室タイプの説明。"]
    ) -> Annotated[str, "リクエストにマッチする客室の短いリストを返します。"]:
        embedding = self.embed_query(query)

        sql_query = """
        SELECT TOP 3 r.roomType, r.description, r.price, r.available, r.date
        FROM rooms r
        ORDER BY VectorDistance(r.vectorDescription, @embedding)
        """

        results = self.db.container.query_items(
            query=sql_query,
            parameters=[
                {"name": "@embedding", "value": embedding}
            ],
            enable_cross_partition_query=True
        )        
        output = ""
        for item in results:
            output += (
                f"\n🏨 **{item['roomType'].capitalize()}**\n"
                f"📅 日付: {item['date']}\n"
                f"🛏 説明: {item['description']}\n"
                f"💵 料金: {item['price']}\n"
                f"🟢 空室数: {item['available']} 室\n"
            )

        return output or "申し訳ございませんが、お探しの条件に合う客室が見つかりませんでした。"