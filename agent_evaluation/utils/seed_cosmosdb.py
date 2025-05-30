import os
import random
import json
from azure.cosmos import CosmosClient, PartitionKey, exceptions
from openai import AzureOpenAI
from dotenv import load_dotenv

# 環境変数をロード
load_dotenv()

# Azure OpenAI クライアントを初期化
openai_client = AzureOpenAI(
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT")
)

def generate_embeddings(text):
    """Azure OpenAIを使用して指定されたテキストの埋め込みを生成します。"""
    response = openai_client.embeddings.create(
        input=[text],
        model=os.getenv("AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT")
    )
    return response.data[0].embedding

# Cosmos DB クライアントを初期化
cosmos_client = CosmosClient(os.getenv("COSMOS_ENDPOINT"), os.getenv("COSMOS_KEY"))

# データベースとコンテナー名
database_name = os.getenv("COSMOS_DB_NAME")
container_name = os.getenv("COSMOS_CONTAINER_NAME")
partition_key_path = "/roomType"
vector_dimensions = 1536  # text-3-embedding-small 出力次元

# データベースを作成（または取得）
database = cosmos_client.create_database_if_not_exists(database_name)

# ベクトル埋め込みポリシーを定義
vector_embedding_policy = {
    "vectorEmbeddings": [
        {
            "path": "/vectorDescription",
            "dataType": "float32",
            "dimensions": vector_dimensions,
            "distanceFunction": "cosine"
        }
    ]
}

# インデックスポリシーを定義
indexing_policy = {
    "includedPaths": [
        {
            "path": "/*"
        }
    ],
    "excludedPaths": [
        {
            "path": "/\"_etag\"/?",
            "path": "/vectorDescription/*"
        }
    ],
    "vectorIndexes": [
        {
            "path": "/vectorDescription",
            "type": "quantizedFlat"
        }
    ]
}


# 指定されたポリシーでコンテナーを作成（または取得）
try:
    container = database.create_container(
        id=container_name,
        partition_key=PartitionKey(path=partition_key_path),
        indexing_policy=indexing_policy,
        vector_embedding_policy=vector_embedding_policy,
    )
    print(f"コンテナー '{container_name}' が正常に作成されました。")
except exceptions.CosmosResourceExistsError:
    container = database.get_container_client(container_name)
    print(f"コンテナー '{container_name}' は既に存在します。")

# 挿入する客室レコード
rooms = [
    {
        "roomType": "suite",
        "date": "2025-04-12",
        "available": 2,
        "price": "$250",
        "description": "キングサイズベッド、オーシャンビュー、エレガントな装飾を備えた広々とした豪華なスイートルーム。ロマンチックな休暇に最適です。"
    },
    {
        "roomType": "double",
        "date": "2025-04-12",
        "available": 4,
        "price": "$150",
        "description": "モダンなデザインのデスクスペース付きの快適なダブルルーム。ビジネス旅行者やファミリーに理想的です。"
    },
    {
        "roomType": "single",
        "date": "2025-04-12",
        "available": 5,
        "price": "$120",
        "description": "一人旅に最適な居心地の良いシングルルーム。読書コーナー、コンパクトなワークスペース、中庭の眺めが含まれます。"
    },
    {
        "roomType": "loft",
        "date": "2025-04-12",
        "available": 3,
        "price": "$300",
        "description": "インダストリアルな雰囲気、むき出しのレンガ、フルキッチンを備えたスタイリッシュなオープンプランロフト。クリエイティブな隠れ家に最適です。"
    },
    {
        "roomType": "penthouse",
        "date": "2025-04-12",
        "available": 1,
        "price": "$500",
        "description": "スカイラインビュー、プライベートバルコニー、ジャグジー、VIPアメニティ付きのプレミアムペントハウススイート。"
    },
    {
        "roomType": "family",
        "date": "2025-04-12",
        "available": 3,
        "price": "$200",
        "description": "クイーンベッド2台、子供向けの装飾、小さなプレイエリアを備えた大きなファミリースイート。"
    },
    {
        "roomType": "garden",
        "date": "2025-04-12",
        "available": 2,
        "price": "$180",
        "description": "パティオアクセス、自然光、読書やヨガに最適なリラックスした雰囲気の静かなガーデンビュールーム。"
    },
    {
        "roomType": "executive",
        "date": "2025-04-12",
        "available": 2,
        "price": "$220",
        "description": "プライベートオフィススペース、人間工学に基づいた椅子、エスプレッソマシン、通話用防音設備を備えたエグゼクティブスイート。"
    },
    {
        "roomType": "accessible",
        "date": "2025-04-12",
        "available": 2,
        "price": "$140",
        "description": "ウォークインシャワー、手すり、移動のための追加フロアスペースを備えた車椅子対応ルーム。"
    },
    {
        "roomType": "eco",
        "date": "2025-04-12",
        "available": 2,
        "price": "$160",
        "description": "リサイクル素材、ゼロウェイストアメニティ、緑の屋上庭園の眺めを備えたエコフレンドリールーム。"
    }
]

# ベクトル埋め込みを含む客室レコードを挿入
for room in rooms:
    room_id = f"{room['roomType']}_{random.randint(1, 1000)}"
    vector_description = generate_embeddings(room["description"])
    room_record = {
        "id": room_id,
        "roomType": room["roomType"],
        "date": room["date"],
        "available": room["available"],
        "price": room["price"],
        "description": room["description"],
        "vectorDescription": vector_description
    }
    try:
        container.create_item(body=room_record)
        print(f"客室レコードを挿入しました: {room_id}")
    except exceptions.CosmosHttpResponseError as e:
        print(f"客室レコード {room_id} の挿入に失敗しました: {e.message}")

print("すべての客室レコードが処理されました。")