# Concierge Agent - スマートホテルコンシェルジュ

Azure AI AgentsとSemantic Kernelを使用したスマートホテルコンシェルジュシステムです。「ロビーボーイ」という名前のAIエージェントが、客室予約、空室確認、セマンティック検索機能を提供します。

## 🏨 概要

このプロジェクトは、Microsoft Build 2025で発表されたAzure AI Agentsを活用したスマートホスピタリティシステムのデモンストレーションです。自然言語でホテルの各種サービスを利用できるインテリジェントなコンシェルジュエージェントを実装しています。

## ✨ 主な機能

### 🛏️ 客室管理
- **空室確認**: 指定された日付での客室の空室状況を確認
- **客室予約**: リアルタイムでの客室予約と在庫管理
- **セマンティック検索**: 自然言語での客室検索（例：「ロマンチック」「エコフレンドリー」「ワークスペース」）

### 🍽️ ダイニングサービス
- レストラン予約管理
- メニュー情報提供

### 🕐 時間関連サービス
- 現在時刻の確認
- 日付関連の処理

## 📁 プロジェクト構造

```
concierge-agent/
├── main.py                    # メインアプリケーション
├── generate_evaluation.py     # 評価用スクリプト
├── requirements.txt           # Python依存関係
├── .env.sample               # 環境変数テンプレート
├── skills/                   # スキルプラグイン
│   ├── __init__.py
│   ├── booking_skill.py      # 予約管理スキル
│   ├── dining_skill.py       # ダイニングスキル
│   ├── semantic_search_plugin.py # セマンティック検索
│   └── time_skill.py         # 時間関連スキル
├── utils/                    # ユーティリティ
│   ├── cosmosdb_client.py    # CosmosDB接続クライアント
│   └── seed_cosmosdb.py      # データベース初期化
├── README_ja.md              # このファイル（日本語版）
└── README_en.md              # 英語版README
```

## 🚀 セットアップ手順

### 1. 前提条件

- Python 3.8以上
- Azure OpenAI Service アクセス権
- Azure Cosmos DB アカウント
- Azure AI Foundry プロジェクト

### 2. 依存関係のインストール

```bash
pip install -r requirements.txt
```

### 3. 環境変数の設定

`.env.sample`を`.env`にコピーして、以下の値を設定してください：

```bash
# Azure OpenAI設定
AZURE_OPENAI_ENDPOINT=https://<リソース名>.openai.azure.com/
AZURE_OPENAI_RESPONSES_DEPLOYMENT_NAME=gpt-4.1
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT=text-embedding-3-small
AZURE_OPENAI_API_KEY=<APIキー>
AZURE_OPENAI_API_VERSION=2025-03-01-preview

# Azure Cosmos DB設定
COSMOS_ENDPOINT=https://<リソース名>.documents.azure.com:443/
COSMOS_KEY=<CosmosDBキー>
COSMOS_DB_NAME=hotel
COSMOS_CONTAINER_NAME=rooms

# Azure AI Foundry設定
AZURE_SUBSCRIPTION_ID=<サブスクリプションID>
RESOURCE_GROUP_NAME=<リソースグループ名>
```

### 4. データベースの初期化

```bash
python utils/seed_cosmosdb.py
```

### 5. アプリケーションの実行

```bash
python main.py
```

## 💬 使用方法

### 基本的な対話例

```
👤 ユーザー: 明日、スイートルームは空いていますか？

🛠️  ツール実行 → check_availability
   引数 → {"room_type": "suite", "date": "2025-06-19"}
✅ ツール結果 check_availability (実行時間: 0.34s)
   → 2025-06-19に2室のsuiteが空いています。料金: $500

# ConciergeAgent: 明日（2025年6月19日）は、スイートルームが2室空いております。
1泊の料金は$500となっております。ご予約をご希望でしたら、お申し付けください。
```

### セマンティック検索の例

```
👤 ユーザー: ロマンチックな雰囲気の部屋を探しています

🛠️  ツール実行 → semantic_room_search
   引数 → {"query": "ロマンチック"}
✅ ツール結果 semantic_room_search (実行時間: 0.52s)
   → ハネムーンスイート - バルコニー付きの豪華なスイート、シャンパンサービス付き

# ConciergeAgent: ロマンチックな雰囲気をお求めでしたら、「ハネムーンスイート」をお勧めいたします。
バルコニー付きの豪華なスイートで、特別なシャンパンサービスもご用意しております。
空室状況をお調べいたしましょうか？
```

## 🔧 スキル詳細

### BookingPlugin
- `check_availability()`: 空室状況の確認
- `confirm_booking()`: 予約の確定

### DiningPlugin
- レストラン関連サービス（実装可能）

### SemanticRoomSearchPlugin
- `semantic_room_search()`: 自然言語での客室検索

### TimePlugin
- `get_current_time()`: 現在時刻の取得

## 📊 評価システム

`generate_evaluation.py`を使用してエージェントの性能評価を実行できます：

```bash
python generate_evaluation.py
```

### 評価メトリクス
- **応答精度**: 質問に対する回答の正確性
- **ツール使用効率**: 適切なスキルの選択と実行
- **応答時間**: レスポンス速度の測定
- **ユーザー体験**: 会話の自然さと有用性

## 🛠️ カスタマイズ

### 新しいスキルの追加

1. `skills/`ディレクトリに新しいプラグインファイルを作成
2. `@kernel_function`デコレータを使用して関数を定義
3. `main.py`でエージェントにプラグインを追加

例：
```python
from semantic_kernel.functions import kernel_function

class NewPlugin:
    @kernel_function(description="新機能の説明")
    def new_function(self, param: str) -> str:
        return f"処理結果: {param}"
```

### データベーススキーマの変更

`utils/cosmosdb_client.py`と`utils/seed_cosmosdb.py`を編集してデータ構造をカスタマイズできます。

## 🔍 トラブルシューティング

### よくある問題と解決方法

**問題**: Azure OpenAI接続エラー
- **解決策**: `.env`ファイルの設定値を確認
- **解決策**: Azure OpenAIサービスが有効になっているか確認

**問題**: Cosmos DB接続エラー
- **解決策**: Cosmos DBアカウントのアクセス許可を確認
- **解決策**: ネットワーク設定とファイアウォール規則を確認

**問題**: スキルが実行されない
- **解決策**: エージェントの`instructions`を確認
- **解決策**: 関数の`description`が適切に設定されているか確認

**問題**: セマンティック検索の精度が低い
- **解決策**: 埋め込みモデルの設定を確認
- **解決策**: 検索クエリの改善

## 📚 技術スタック

- **Azure AI Agents**: エージェントフレームワーク
- **Semantic Kernel**: AIオーケストレーション
- **Azure OpenAI Service**: 言語モデルと埋め込み
- **Azure Cosmos DB**: NoSQLデータベース
- **Python**: プログラミング言語
- **FastAPI**: Web APIフレームワーク（オプション）

## 🔗 関連リンク

- [Azure AI Agents ドキュメント](https://docs.microsoft.com/azure/ai-services/agents/)
- [Semantic Kernel ドキュメント](https://learn.microsoft.com/semantic-kernel/)
- [Azure OpenAI Service](https://azure.microsoft.com/products/ai-services/openai-service/)
- [Azure Cosmos DB](https://azure.microsoft.com/products/cosmos-db/)
- [Microsoft Build 2025](https://mybuild.microsoft.com/)

## 📄 ライセンス

このプロジェクトはMITライセンスの下で公開されています。

## 🤝 貢献

プルリクエストやイシューの報告を歓迎しています。貢献する前に、コーディング規約とプロジェクトガイドラインをご確認ください。

## 📞 サポート

質問や問題がある場合は、GitHubのIssuesページでお気軽にお問い合わせください。
