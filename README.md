# Microsoft Build 2025 アップデート サンプル

このリポジトリは、Microsoft Build 2025で発表された最新のAI技術を活用したサンプルアプリケーションを提供します。Azure AI Agents、Semantic Kernel、Azure OpenAI Serviceを使用して、スマートホスピタリティ システムとマルチエージェント システムの実装例を紹介しています。

## 🌟 プロジェクト概要

### 主要コンポーネント

1. **Concierge Agent** (`concierge-agent/`)
   - Azure AI Agentsを使用したスマートホテルコンシェルジュ
   - 客室予約、空室確認、セマンティック検索機能
   - Cosmos DBとの統合によるデータ管理

2. **Jupyter Notebooks** (`notebook/`)
   - マルチエージェントシステムの実装例
   - Azure AI Agents品質評価の自動化
   - Connected Agentsパターンのデモンストレーション

## 🚀 特徴

### Concierge Agent
- **インテリジェントな対話**: 自然言語での客室予約とサービス提供
- **セマンティック検索**: 要求に最適な客室の提案
- **リアルタイム空室管理**: Cosmos DBでの在庫管理
- **多言語対応**: 日本語をデフォルトとした多言語コミュニケーション

### Multi-Agent Systems
- **協調処理**: 複数エージェントによる役割分担
- **リアルタイム検索**: Bing APIを使用した最新情報取得
- **構造化出力**: マークダウン形式での見やすいレポート生成
- **エージェント品質評価**: Azure AI Evaluationによる自動品質測定

## 🏗️ アーキテクチャ

### 技術スタック
- **Azure AI Foundry Agent Service**: エージェントのライフサイクル管理
- **Semantic Kernel**: AIアプリケーション開発フレームワーク
- **Azure OpenAI Service**: GPT-4o等の大規模言語モデル
- **Azure Cosmos DB**: NoSQLデータベース（客室・予約データ）
- **Azure AI Foundry**: エージェント管理とBing検索機能、品質の自動評価

### Concierge Agent アーキテクチャ
```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   User Input    │───▶│ Concierge Agent │───▶│   Azure OpenAI  │
└─────────────────┘    └─────────────────┘    └─────────────────┘
                                │
                                ▼
                       ┌─────────────────┐
                       │   Plugin Skills │
                       │                 │
                       │ • BookingPlugin │
                       │ • DiningPlugin  │
                       │ • SemanticSearch│
                       │ • TimePlugin    │
                       └─────────────────┘
                                │
                                ▼
                       ┌─────────────────┐
                       │   Cosmos DB     │
                       │                 │
                       │ • Room Data     │
                       │ • Booking Data  │
                       │ • Availability  │
                       └─────────────────┘
```

### Multi-Agent System アーキテクチャ
```
┌─────────────────┐    ┌─────────────────┐
│   User Query    │───▶│  Coordinator    │
└─────────────────┘    │     Agent       │
                       └─────────────────┘
                                │
                    ┌───────────┼───────────┐
                    ▼           ▼           ▼
            ┌──────────────┐ ┌──────────────┐ ┌──────────────┐
            │ Researcher   │ │    Writer    │ │  Other       │
            │    Agent     │ │    Agent     │ │  Agents      │
            └──────────────┘ └──────────────┘ └──────────────┘
                    │
                    ▼
            ┌──────────────┐
            │  Bing Search │
            │     API      │
            └──────────────┘
```

## 📋 前提条件

### Azure リソース
- Azure OpenAI Service（GPT-4o、埋め込みモデルのデプロイ）
- Azure AI Foundry Project
- Azure Cosmos DB アカウント
- Bing Search API（Azure AI Projects経由）

### 開発環境
- Python 3.8以上
- Visual Studio Code（推奨）
- Jupyter Notebook対応環境

## ⚙️ セットアップ

### 1. リポジトリのクローン
```bash
git clone <repository-url>
cd msbuild-2025-update
```

### 2. 仮想環境の作成とアクティベート
```bash
python -m venv .venv

# Windows
.venv\Scripts\activate

# macOS/Linux
source .venv/bin/activate
```

### 3. 依存関係のインストール
```bash
cd concierge-agent
pip install -r requirements.txt
```

### 4. 環境変数の設定
`concierge-agent/.env`ファイルを作成し、以下の設定を追加：

```env
# Azure OpenAI
AZURE_OPENAI_ENDPOINT=https://your-openai-resource.openai.azure.com/
AZURE_OPENAI_API_KEY=your-api-key
AZURE_OPENAI_API_VERSION=2024-10-01-preview
AGENT_MODEL_DEPLOYMENT_NAME=gpt-4o
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT=text-embedding-3-small

# Azure AI Projects
PROJECT_CONNECTION_STRING=your-project-connection-string
BING_CONNECTION_NAME=your-bing-connection-name

# Cosmos DB
COSMOS_ENDPOINT=https://your-cosmos-account.documents.azure.com:443/
COSMOS_KEY=your-cosmos-key
COSMOS_DB_NAME=hotel_db
COSMOS_CONTAINER_NAME=rooms
```

### 5. Cosmos DBの初期化
```bash
cd concierge-agent
python utils/seed_cosmosdb.py
```

## 🎯 使用方法

### Concierge Agent の実行
```bash
cd concierge-agent
python main.py
```

実行後、以下のような対話が可能です：
- 「今日空いているスイートルームはありますか？」
- 「ロマンチックな雰囲気の部屋を探しています」
- 「2025年6月10日にデラックスルームを予約したいです」

### Jupyter Notebooks の実行
```bash
cd notebook
jupyter notebook
```

利用可能なノートブック：
- `multi-agent-semantic-kernel.ipynb`: Semantic Kernelマルチエージェントシステム
- `multi-agent-connected-agents.ipynb`: Connected Agentsパターン
- `evaluate-azure-ai-agent-quality.ipynb`: エージェント品質評価

## 📁 プロジェクト構造

```
msbuild-2025-update/
│
├── README.md                           # このファイル
│
├── concierge-agent/                    # ホテルコンシェルジュエージェント
│   ├── main.py                         # メインアプリケーション
│   ├── generate_evaluation.py          # 評価データ生成
│   ├── requirements.txt                # Python依存関係
│   │
│   ├── skills/                         # エージェントスキル
│   │   ├── booking_skill.py            # 予約管理スキル
│   │   ├── dining_skill.py             # レストラン管理スキル
│   │   ├── semantic_search_plugin.py   # セマンティック検索スキル
│   │   └── time_skill.py               # 時間関連スキル
│   │
│   └── utils/                          # ユーティリティ
│       ├── cosmosdb_client.py          # Cosmos DBクライアント
│       └── seed_cosmosdb.py            # データベース初期化
│
└── notebook/                           # Jupyter ノートブック
    ├── multi-agent-semantic-kernel.ipynb      # マルチエージェント（Semantic Kernel）
    ├── multi-agent-connected-agents.ipynb     # マルチエージェント（Connected Agents）
    ├── evaluate-azure-ai-agent-quality.ipynb  # エージェント品質評価
    └── user_functions.py                      # ノートブック共通関数
```

## 🔧 主要な機能

### Concierge Agent の機能
1. **客室管理**
   - 空室状況の確認
   - 客室タイプ別の検索
   - 予約の確定と管理

2. **セマンティック検索**
   - 自然言語での客室検索
   - 要求に基づく最適な提案
   - 類似度によるランキング

3. **レストラン管理**
   - テーブル予約
   - メニュー情報提供

### Multi-Agent System の機能
1. **役割分担**
   - リサーチャー：情報収集
   - ライター：レポート作成
   - コーディネーター：タスク振り分け

2. **検索と分析**
   - Bing API経由のリアルタイム検索
   - 複数ソースからの情報統合
   - 構造化されたレポート生成

## 📊 評価とモニタリング

### Azure AI Evaluation
- **品質メトリクス**: 暴力性、有害性、関連性
- **自動評価**: 定期的なパフォーマンス測定
- **サンプリング設定**: カスタマイズ可能な評価範囲

### ログとトレーシング
- **関数呼び出し追跡**: 詳細な実行ログ
- **パフォーマンス測定**: 応答時間とスループット
- **エラーハンドリング**: 包括的なエラー処理

## 🔄 カスタマイズ

### 新しいスキルの追加
1. `concierge-agent/skills/`ディレクトリに新しいスキルファイルを作成
2. `@kernel_function`デコレーターを使用して関数を定義
3. `main.py`でスキルをエージェントに登録

### エージェントの設定変更
- `instructions`パラメーターでエージェントの役割を調整
- 新しいプラグインを追加してスキルを拡張
- カスタムモデルやデプロイメントの使用

## 🚨 注意事項

### API制限
- Bing Search APIの利用制限に注意
- Azure OpenAIのトークン制限を考慮
- Cosmos DBのRU消費量を監視

### セキュリティ
- 環境変数の適切な管理
- Azure Key Vaultの使用を推奨
- 本番環境では適切な認証・認可の実装

### パフォーマンス
- 大量検索時のレート制限対応
- キャッシュ機能の実装検討
- 並列処理の最適化

## 🤝 貢献

このプロジェクトへの貢献を歓迎します：

1. Issueの報告
2. 機能の提案
3. プルリクエストの送信
4. ドキュメントの改善

## 📚 関連リソース

### Microsoft公式ドキュメント
- [Azure AI Foundry Agent Service](https://learn.microsoft.com/ja-jp/azure/ai-services/agents/)
- [Semantic Kernel](https://learn.microsoft.com/semantic-kernel/)
- [Azure OpenAI Service](https://docs.microsoft.com/azure/ai-services/openai/)
- [Azure AI Foundry](https://docs.microsoft.com/azure/ai-studio/)

### Build 2025 関連
- [Microsoft Build 2025 セッション](https://build.microsoft.com/)
- [Connected Agents パターン](https://learn.microsoft.com/ja-jp/azure/ai-services/agents/how-to/connected-agents?pivots=python)

## 📝 ライセンス

このプロジェクトは MIT ライセンスの下で公開されています。詳細は [LICENSE](LICENSE) ファイルをご覧ください。

## ❓ サポート

質問やサポートが必要な場合：
- GitHubのIssueを作成
- Microsoft Tech Communityフォーラムを活用
- Azure サポートチームに連絡