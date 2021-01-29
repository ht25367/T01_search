### 検索ツールサンプル
### たんじろう,ぎゆう,ねずこ,むざん,ぜんいつ
### これをベースに課題の内容を追記してください
import csv



# 検索ソースをCSVファイルから読み込む関数
def read_source():
	
	# Windows用のエンコード、改行コードで open
	with open("kimetu.csv",encoding = "utf_8",newline='') as source_csv:
		
		# date = source_csv.read()
		data = csv.reader( source_csv )
		header = next(data)
		
		
		# ！今回のcsvファイルが1行しかないため！？
		#  for文、回ってない様子。
		for header in data:
			print(header)
		print("「csv読み込み関数」から読み込んだリストを返します" )
		return header



# 渡されたリストを、CSVファイルに書き込む関数
def write_source(source):

	with open("kimetu.csv","w",encoding = "utf_8",newline='') as source_csv:
		# 開いたsource_csv に 受け取った source を書き込む
		writer = csv.writer(source_csv)
		writer.writerow( source )

	print( source )



### 検索ツール。
# 引数（検索する配列: list）
# 戻り値、入力名が見つかった return = ""
# 戻り値、入力名が見つからない return = 入力された名前
def search(source):
	word =input("鬼滅の登場人物の名前を入力してください >>> ")

	### ここに検索ロジックを書く
	for name in source:
		if word == name:
			print("{}が見つかりました".format(word))
			return ""

	# 入力された名前が見つからなかった時の処理
	print( "{}は見つかりませんでした。".format(word) )
	return word


## メインの処理
if __name__ == "__main__":
	
	# csvファイルを読み込む関数、戻り値（配列）をsource_list に入れる
	source_list = read_source()

	print("渡したリスト中から入力した名前を検索する関数を呼び出します")
	input_name = search( source_list )

	if input_name != "":
		# 入力された名前が見つからなかった場合、、、

		rst = input(input_name + "を登場人物リストに追加しますか？(y/n)：")
		if rst == "y":
			source_list.append( input_name )
			# csvファイルに書き込む関数を呼び出す
			write_source(source_list)
		else:
			# 入力されたy 以外の判定はとりあえずしない
			pass



