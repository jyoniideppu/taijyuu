import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['font.family'] = 'Yu Gothic'

# CSVファイルのパス
csv_path1 = "C:/Users/asupa/Downloads/vscodeyou/h.html/2023061.CSV"
csv_path2 = "C:/Users/asupa/Downloads/vscodeyou/h.html/2023070.CSV"

# CSVファイルの読み込み
df = pd.read_csv(csv_path1, encoding="shift-jis")
df2 = pd.read_csv(csv_path2, encoding="shift-jis")

# 2つのデータフレームを結合
combined_df = pd.concat([df, df2])

# 日付をx軸、体重をy軸としてデータポイントを線で結ぶ
plt.plot(combined_df['測定日'], combined_df['体重'], marker='o', linestyle='-', label='結合データ')

# グラフのタイトルと軸ラベル
plt.title("体重の推移")
plt.xlabel("測定日")
plt.ylabel("体重(kg)")

# 凡例を追加
plt.show()
