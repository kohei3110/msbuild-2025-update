import asyncio
import time
from dotenv import load_dotenv
from semantic_kernel.agents import AzureResponsesAgent
from semantic_kernel.contents import (
    ChatMessageContent, 
    FunctionCallContent, 
    FunctionResultContent,
)

from skills.booking_skill import BookingPlugin
from skills.dining_skill import DiningPlugin
from skills.time_skill import TimePlugin
from skills.semantic_search_plugin import SemanticRoomSearchPlugin

load_dotenv()

intermediate_steps = []
_tool_call_timestamps = {}

async def handle_intermediate_steps(message: ChatMessageContent):
    intermediate_steps.append(message)
    
    for item in message.items:
        if isinstance(item, FunctionCallContent):
            print(f"\033[1;36m🛠️  ツール実行 → {item.name}\033[0m")
            print(f"   引数 → {item.arguments}")
            _tool_call_timestamps[item.name] = time.time()

        elif isinstance(item, FunctionResultContent):
            start_time = _tool_call_timestamps.get(item.name, None)
            duration = f"{(time.time() - start_time):.2f}s" if start_time else "N/A"
            print(f"\033[1;32m✅ ツール結果 {item.name} (実行時間: {duration})\033[0m")
            print(f"   → {item.result}")

async def main():
    client, model = AzureResponsesAgent.setup_resources()

    concierge_agent = AzureResponsesAgent(
        ai_model_id=model,
        client=client,
        name="ConciergeAgent",
        instructions="""
        あなたは高級ホテルのスマートコンシェルジュです。名前は「ロビーボーイ」です。

        あなたの仕事は以下の通りです：
        - 客室の予約
        - 空室状況の確認
        - 説明に合致する客室の検索（例：ロマンチック、エコフレンドリー、ワークスペース）

        セマンティック客室検索などのツールを使用する際は、以下を確認してください：
        - ユーザーのリクエストに本当に関連する客室のみを返す
        - 曖昧にマッチする客室は表示しない（例：「エコフレンドリー」の検索で「シングルルーム」を表示することを避ける）
        - 最も類似度が高い、またはキーワードに直接マッチする客室を優先する
        - 必要に応じて、なぜその客室を提案するかを説明する

        予約などのツールを使用する際は、まず空室状況を確認し、客室が利用可能な場合のみ予約を確定してください（同じステップで両方を行わない）。
        確定前に予約詳細（客室タイプ、1泊あたりの料金、日程、合計金額など）を要約する必要があります。

        フレンドリーで親切、かつ簡潔に対応してください。
        
        あなたは多言語を話しますが、デフォルトの言語は日本語です。
        ユーザーが他の言語で話す場合は、その言語に切り替えることができます。
        """,
        plugins=[
            BookingPlugin(),
            DiningPlugin(),
            SemanticRoomSearchPlugin(),
            TimePlugin(),
        ],
    )

    thread = None

    print("🛎️  スマートホスピタリティアシスタントへようこそ")
    print("下にメッセージを入力してください。終了するには'exit'または'終了'と入力してください。\n")

    while True:
        user_input = input("👤 ユーザー: ")
        if user_input.lower() in ["exit", "quit", "終了", "やめる"]:
            break

        async for response in concierge_agent.invoke(
            messages=user_input,
            thread=thread,
            on_intermediate_message=handle_intermediate_steps,
            stream=False,
        ):
            thread = response.thread
            print(f"# ConciergeAgent: {response.content}\n")

    await thread.delete() if thread else None
    print("👋 セッション終了")

if __name__ == "__main__":
    asyncio.run(main())