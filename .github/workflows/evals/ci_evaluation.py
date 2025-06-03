import os
import json
import sys
from azure.ai.evaluation import TaskAdherenceEvaluator, AzureOpenAIModelConfiguration
from pprint import pprint
from dotenv import load_dotenv

def main():
    """タスク遵守評価を実行し、結果に基づいてCIの成功/失敗を判定"""
    
    # 環境変数を読み込み
    load_dotenv('../.env')
    
    # Azure OpenAIの設定
    model_config = AzureOpenAIModelConfiguration(
        azure_endpoint=os.environ.get("AZURE_OPENAI_ENDPOINT"),
        azure_deployment=os.environ.get("AZURE_OPENAI_RESPONSES_DEPLOYMENT_NAME"),
        api_key=os.environ.get("AZURE_OPENAI_API_KEY"),
        api_version=os.environ.get("AZURE_OPENAI_API_VERSION"),
    )
    
    # ツール定義
    tool_definitions = [
        {
            "name": "BookingPlugin-check_availability",
            "description": "指定された日付で客室が利用可能かどうかを確認します。",
            "parameters": {
                "type": "object",
                "properties": {
                    "room_type": {
                        "type": "string",
                        "description": "客室タイプ。"
                    },
                    "date": {
                        "type": "string",
                        "description": "予約日（YYYY-MM-DD形式）。"
                    }
                }
            }
        },
        {
            "name": "BookingPlugin-confirm_booking",
            "description": "予約を確定し、客室数を減らします。",
            "parameters": {
                "type": "object",
                "properties": {
                    "room_type": {
                        "type": "string",
                        "description": "客室タイプ。"
                    },
                    "date": {
                        "type": "string",
                        "description": "予約日（YYYY-MM-DD形式）。"
                    },
                    "count": {
                        "type": "integer",
                        "description": "予約する客室数。"
                    }
                }
            }
        },
        {
            "name": "DiningPlugin-get_specials",
            "description": "本日のダイニングスペシャルを提供します。",
            "parameters": {
                "type": "object",
                "properties": {}
            }
        },
        {
            "name": "DiningPlugin-get_item_price",
            "description": "指定されたメニュー項目の価格を提供します。",
            "parameters": {
                "type": "object",
                "properties": {
                    "menu_item": {
                        "type": "string",
                        "description": "メニュー項目名。"
                    }
                }
            }
        },
        {
            "name": "DiningPlugin-reserve_table",
            "description": "ホテルレストランでのテーブル予約をシミュレートします。",
            "parameters": {
                "type": "object",
                "properties": {
                    "time": {
                        "type": "string",
                        "description": "予約時間（例：HH:MM）。"
                    },
                    "party_size": {
                        "type": "integer",
                        "description": "予約人数。"
                    }
                }
            }
        },
        {
            "name": "SemanticSearchPlugin-search_rooms_by_description",
            "description": "客室の説明に基づいてセマンティック検索でホテルの客室を検索します。",
            "parameters": {
                "type": "object",
                "properties": {
                    "query": {
                        "type": "string",
                        "description": "ユーザーが探している客室タイプの説明。"
                    }
                }
            }
        },
        {
            "name": "TimePlugin-get_today",
            "description": "今日の日付をYYYY-MM-DD形式で返します。",
            "parameters": {
                "type": "object",
                "properties": {}
            }
        },
        {
            "name": "TimePlugin-get_relative_date",
            "description": "日数のオフセットに基づいて相対的な日付を返します。",
            "parameters": {
                "type": "object",
                "properties": {
                    "days_offset": {
                        "type": "integer",
                        "description": "今日に追加する日数。"
                    }
                }
            }
        }
    ]
    
    file_path = "evaluation_dataset.jsonl"
    task_adherence_evaluator = TaskAdherenceEvaluator(model_config=model_config)
    
    failed_tests = []
    passed_tests = []
    total_tests = 0
    
    print("タスク遵守評価を開始...")
    print("=" * 60)
    
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            for line_num, line in enumerate(file, 1):
                line = line.strip()
                if not line:
                    continue
                
                total_tests += 1
                
                try:
                    record = json.loads(line)
                    query = record.get("query", "クエリが提供されていません")
                    response = record.get("response", "レスポンスが提供されていません")
                    
                    print(f"\n--- テスト {line_num} ---")
                    print(f"クエリ: {query}")
                    print(f"レスポンス: {response}")
                    
                    metric = task_adherence_evaluator(
                        query=query, 
                        response=response, 
                        tool_definitions=tool_definitions,
                    )
                    
                    print("\nタスク遵守結果:")
                    pprint(metric)
                    
                    # task_adherence_resultの値を確認
                    task_result = metric.get("task_adherence_result", "").lower()
                    
                    if task_result == "pass":
                        passed_tests.append(line_num)
                        print("✅ PASS")
                    elif task_result == "fail":
                        failed_tests.append({
                            "line": line_num,
                            "query": query,
                            "response": response,
                            "metric": metric
                        })
                        print("❌ FAIL")
                    else:
                        print(f"⚠️  不明な結果: {task_result}")
                        failed_tests.append({
                            "line": line_num,
                            "query": query,
                            "response": response,
                            "metric": metric,
                            "reason": f"不明な結果: {task_result}"
                        })
                    
                    print("-" * 47)
                    
                except json.JSONDecodeError as e:
                    print(f"❌ JSONデコードエラー (行 {line_num}): {e}")
                    failed_tests.append({
                        "line": line_num,
                        "reason": f"JSONデコードエラー: {e}"
                    })
                    
                except Exception as e:
                    print(f"❌ 評価エラー (行 {line_num}): {e}")
                    failed_tests.append({
                        "line": line_num,
                        "reason": f"評価エラー: {e}"
                    })
    
    except FileNotFoundError:
        print(f"❌ ファイルが見つかりません: {file_path}")
        sys.exit(1)
    
    except Exception as e:
        print(f"❌ 予期しないエラー: {e}")
        sys.exit(1)
    
    # 結果のサマリー
    print("\n" + "=" * 60)
    print("📊 評価結果サマリー")
    print("=" * 60)
    print(f"総テスト数: {total_tests}")
    print(f"成功: {len(passed_tests)}")
    print(f"失敗: {len(failed_tests)}")
    
    if failed_tests:
        print("\n❌ 失敗したテスト:")
        for failure in failed_tests:
            print(f"  - 行 {failure['line']}: {failure.get('reason', 'タスク遵守評価で失敗')}")
        
        print(f"\n💥 CI失敗: {len(failed_tests)}件のテストが失敗しました")
        sys.exit(1)
    else:
        print(f"\n✅ CI成功: すべてのテストが通過しました ({len(passed_tests)}/{total_tests})")
        sys.exit(0)

if __name__ == "__main__":
    main()