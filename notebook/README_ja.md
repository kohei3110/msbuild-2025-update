# Notebook Collection - Azure AI Agents実践ガイド

このディレクトリには、Microsoft Build 2025で発表されたAzure AI Agentsとマルチエージェントシステムに関する実践的なJupyter notebookが含まれています。

## 📚 ノートブック概要

### 🔍 evaluate-azure-ai-agent-quality.ipynb
**目的**: Azure AI Agentsの品質評価とパフォーマンス測定

**主な内容**:
- Azure AI Foundryプロジェクトクライアントの初期化
- Tourist Assistant エージェントの作成と設定
- エージェント評価メトリクスの実装
- 品質スコアリングシステム

**学習ポイント**:
- エージェント評価のベストプラクティス
- Azure AI Evaluationライブラリの使用方法
- 実世界でのエージェント性能測定手法

### 🔗 multi-agent-connected-agents.ipynb
**目的**: Connected Agentsを使用した複数エージェント連携システム

**主な内容**:
- Stock Price Agent（株価情報専門エージェント）の実装
- Main Agent（統合エージェント）の構築
- Connected Agent Toolによるエージェント間通信
- エージェント連携のデモンストレーション

**学習ポイント**:
- Connected Agentsアーキテクチャの理解
- エージェント間の責任分離設計
- モジュラーなAIシステムの構築

### 🧠 multi-agent-semantic-kernel.ipynb
**目的**: Semantic Kernelを使用したマルチエージェントシステム

**主な内容**:
- リサーチャーエージェント（Bing検索専門）
- ライターエージェント（レポート作成専門）
- コーディネーターエージェント（タスク振り分け）
- 協調型ワークフローの実装

**学習ポイント**:
- Semantic Kernelフレームワークの活用
- エージェント間の協調メカニズム
- 複雑なタスクの分解と分散処理

### 🛠️ user_functions.py
**目的**: エージェントが使用するカスタム関数の定義

**主な内容**:
- 現在時刻取得関数
- 天気情報取得関数（モック）
- その他のユーティリティ関数

## 📁 ディレクトリ構造

```
notebook/
├── evaluate-azure-ai-agent-quality.ipynb  # エージェント品質評価
├── multi-agent-connected-agents.ipynb     # Connected Agentsデモ
├── multi-agent-semantic-kernel.ipynb      # Semantic Kernelマルチエージェント
├── user_functions.py                      # カスタム関数定義
├── venv/                                  # Python仮想環境
├── __pycache__/                           # Pythonキャッシュ
├── README_ja.md                           # このファイル（日本語版）
└── README_en.md                           # 英語版README
```

## 🚀 セットアップ手順

### 1. 前提条件

- Python 3.8以上
- Jupyter Notebook または VS Code
- Azure AI Foundryプロジェクト
- Azure OpenAI Service アクセス権

### 2. 仮想環境の作成

```bash
cd notebook
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
```

### 3. 必要な依存関係のインストール

各ノートブックの最初のセルで、必要なパッケージがインストールされます：

```python
# 基本パッケージ
!pip install azure-ai-projects azure-identity azure-ai-evaluation
!pip install azure-ai-inference azure-ai-agents semantic-kernel
```

### 4. 環境変数の設定

`../concierge-agent/.env`ファイルに以下の環境変数を設定：

```bash
# Azure AI Foundry設定
PROJECT_CONNECTION_STRING=<プロジェクト接続文字列>
AGENT_MODEL_DEPLOYMENT_NAME=<モデルデプロイメント名>
PROJECT_NAME=<プロジェクト名>
RESOURCE_GROUP_NAME=<リソースグループ名>

# Azure OpenAI設定
AZURE_OPENAI_ENDPOINT=<OpenAIエンドポイント>
AZURE_OPENAI_API_KEY=<APIキー>
AZURE_OPENAI_API_VERSION=<APIバージョン>

# Azure基本設定
AZURE_SUBSCRIPTION_ID=<サブスクリプションID>

# Bing検索設定（Semantic Kernelノートブック用）
BING_CONNECTION_NAME=<Bing接続名>
```

## 💡 使用方法

### ノートブックの実行順序

1. **初心者向け**: `evaluate-azure-ai-agent-quality.ipynb`
   - 単一エージェントの基本概念を学習
   - エージェント評価手法の理解

2. **中級者向け**: `multi-agent-connected-agents.ipynb`
   - エージェント間通信の実装
   - Connected Agentsアーキテクチャの体験

3. **上級者向け**: `multi-agent-semantic-kernel.ipynb`
   - 複雑なマルチエージェントシステム
   - Semantic Kernelの高度な活用

### 実行方法

```bash
# Jupyter Notebookで開く
jupyter notebook

# または VS Codeで開く
code .
```

## 🔧 主要機能

### エージェント評価機能
- **品質メトリクス**: 応答精度、関連性、完全性の測定
- **パフォーマンス分析**: 実行時間とリソース使用量の監視
- **A/Bテスト**: 複数のエージェント設定の比較

### Connected Agents機能
- **エージェント連携**: 専門エージェント間の協調動作
- **ツール統合**: エージェントを他のエージェントのツールとして使用
- **動的ルーティング**: クエリ内容に基づく適切なエージェント選択

### Semantic Kernel機能
- **プラン実行**: 複雑なタスクの自動分解と実行
- **プラグイン管理**: 再利用可能な機能モジュール
- **メモリ管理**: 会話履歴と状態の永続化

## 📊 評価メトリクス

### 品質評価
- **正確性**: 提供された情報の事実確認
- **関連性**: クエリに対する回答の適切性
- **完全性**: 必要な情報の網羅性
- **一貫性**: 複数回答間の整合性

### パフォーマンス評価
- **応答時間**: エージェントの応答速度
- **スループット**: 単位時間あたりの処理量
- **リソース効率**: CPU/メモリ使用量の最適化
- **エラー率**: 失敗したリクエストの割合

## 🔍 トラブルシューティング

### よくある問題と解決方法

**問題**: Azure AI Foundryプロジェクトに接続できない
- **解決策**: `PROJECT_CONNECTION_STRING`の設定を確認
- **解決策**: Azure CLI認証の状態を確認（`az login`）

**問題**: モデルデプロイメントが見つからない
- **解決策**: Azure AI Foundryポータルでデプロイメント名を確認
- **解決策**: モデルが正常にデプロイされているか確認

**問題**: パッケージインストールエラー
- **解決策**: 仮想環境が有効になっているか確認
- **解決策**: Python バージョンの互換性を確認

**問題**: Connected Agentsの通信エラー
- **解決策**: エージェント間の権限設定を確認
- **解決策**: ネットワーク接続とファイアウォール設定を確認

## 🎯 学習目標

### 基礎レベル
- Azure AI Agentsの基本概念理解
- 単一エージェントの作成と設定
- 基本的なツール統合

### 中級レベル
- Connected Agentsアーキテクチャの実装
- エージェント評価システムの構築
- 複数エージェント間の協調設計

### 上級レベル
- Semantic Kernelを使用した高度なマルチエージェントシステム
- カスタムプラグインの開発
- 本格的なAIアプリケーションの設計

## 🔗 関連リンク

- [Azure AI Agents ドキュメント](https://docs.microsoft.com/azure/ai-services/agents/)
- [Semantic Kernel ドキュメント](https://learn.microsoft.com/semantic-kernel/)
- [Azure AI Foundry](https://ai.azure.com/)
- [Azure OpenAI Service](https://azure.microsoft.com/products/ai-services/openai-service/)
- [Microsoft Build 2025](https://mybuild.microsoft.com/)

## 📄 ライセンス

このプロジェクトはMITライセンスの下で公開されています。

## 🤝 貢献

ノートブックの改善や新しい例の追加など、プルリクエストを歓迎しています。貢献前にコーディング規約をご確認ください。

## 📞 サポート

質問や問題がある場合は、GitHubのIssuesページでお気軽にお問い合わせください。
