# GitHub Actions ワークフロー

このディレクトリには、Microsoft Build 2025 アップデート サンプルプロジェクトで使用するGitHub Actionsワークフローが含まれています。

## 📁 ディレクトリ構造

```
.github/
├── workflows/
│   ├── copilot-setup-steps.yml      # GitHub Copilotセットアップ用ワークフロー
│   ├── eval-single-agent-fail.yml   # エージェント評価（失敗ケース）
│   ├── eval-single-agent-success.yml # エージェント評価（成功ケース）
│   └── evals/                       # 評価スクリプト
├── README_ja.md                     # このファイル（日本語版）
└── README_en.md                     # 英語版README
```

## 🔧 ワークフロー説明

### 1. Copilot Setup Steps (`copilot-setup-steps.yml`)

**目的**: GitHub Copilotの環境セットアップを自動化

**トリガー**: 手動実行（`workflow_dispatch`）

**主な機能**:
- Ubuntu環境でのセットアップ手順実行
- リポジトリのチェックアウト
- 必要な権限設定（`contents: read`）

**使用方法**:
1. GitHubリポジトリの「Actions」タブにアクセス
2. "Copilot Setup Steps"ワークフローを選択
3. "Run workflow"ボタンをクリック

### 2. Agent Evaluation - Fail Case (`eval-single-agent-fail.yml`)

**目的**: AIエージェントの失敗シナリオでの評価テスト

**トリガー**: 手動実行（`workflow_dispatch`）

**主な機能**:
- Python 3.11環境のセットアップ
- Azure AI評価ライブラリのインストール
- 失敗ケースでのエージェント性能評価

**必要な環境変数**:
- `AZURE_OPENAI_ENDPOINT`
- `AZURE_OPENAI_RESPONSES_DEPLOYMENT_NAME`
- `AZURE_OPENAI_API_KEY`
- `AZURE_OPENAI_API_VERSION`
- `AZURE_SUBSCRIPTION_ID`

### 3. Agent Evaluation - Success Case (`eval-single-agent-success.yml`)

**目的**: AIエージェントの成功シナリオでの評価テスト

**トリガー**: 手動実行（`workflow_dispatch`）

**主な機能**:
- Python 3.11環境のセットアップ
- Azure AI評価ライブラリのインストール
- 成功ケースでのエージェント性能評価

**必要な環境変数**: 失敗ケースと同じ

## 🚀 セットアップ手順

### 1. 前提条件

- Azure OpenAIサービスのアクセス権
- Azure サブスクリプション
- 必要なシークレットの設定

### 2. シークレットの設定

GitHubリポジトリの設定で以下のシークレットを追加してください：

```
AZURE_OPENAI_ENDPOINT=<あなたのAzure OpenAI エンドポイント>
AZURE_OPENAI_RESPONSES_DEPLOYMENT_NAME=<デプロイメント名>
AZURE_OPENAI_API_KEY=<APIキー>
AZURE_OPENAI_API_VERSION=<APIバージョン>
AZURE_SUBSCRIPTION_ID=<サブスクリプションID>
```

### 3. ワークフローの実行

1. GitHubリポジトリにアクセス
2. 「Actions」タブを選択
3. 実行したいワークフローを選択
4. 「Run workflow」をクリック

## 📊 評価結果の確認

エージェント評価ワークフローの実行後、以下の方法で結果を確認できます：

1. **GitHub Actions ログ**: ワークフロー実行の詳細ログ
2. **評価メトリクス**: Azure AI Evaluationによる性能指標
3. **成功/失敗レポート**: 各テストケースの結果

## 🔍 トラブルシューティング

### よくある問題と解決方法

**問題**: ワークフローが失敗する
- **解決策**: シークレットが正しく設定されているか確認
- **解決策**: Azure OpenAIサービスが有効になっているか確認

**問題**: 評価スクリプトが見つからない
- **解決策**: `evals/`ディレクトリが存在するか確認
- **解決策**: 作業ディレクトリが正しく設定されているか確認

**問題**: Python依存関係のインストールエラー
- **解決策**: `requirements.txt`の依存関係を確認
- **解決策**: Pythonバージョンの互換性を確認

## 📝 カスタマイズ

### 新しいワークフローの追加

1. `.github/workflows/`ディレクトリに新しいYAMLファイルを作成
2. 適切なトリガーとジョブを定義
3. 必要に応じてシークレットを追加

### 既存ワークフローの変更

1. 対象のYAMLファイルを編集
2. テスト実行で動作確認
3. 本番環境での動作確認

## 🔗 関連リンク

- [GitHub Actions ドキュメント](https://docs.github.com/en/actions)
- [Azure AI Services](https://azure.microsoft.com/en-us/products/ai-services/)
- [Azure OpenAI Service](https://azure.microsoft.com/en-us/products/ai-services/openai-service/)
- [Microsoft Build 2025](https://mybuild.microsoft.com/)

## 📞 サポート

質問や問題がある場合は、GitHubのIssuesページでお気軽にお問い合わせください。
