!pip install pydub
import glob
import os
from google.colab import drive
from pydub import AudioSegment

# Google Driveをマウント
drive.mount('/content/drive')

# pydubをインポート
from pydub.silence import split_on_silence

# 入力ディレクトリと出力ディレクトリを指定
input_dir = '/content/drive/MyDrive/fin_movie1'
output_dir = '/content/drive/MyDrive/finrand/fin_movie1_5sec'

# 出力ディレクトリが存在しない場合は作成
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# 入力ディレクトリ内の音声ファイル（MP3）を取得
input_files = glob.glob(os.path.join(input_dir, '*.mp3'))

# 5秒ごとに音声を区切って保存
for input_file in input_files:
    # MP3ファイルを読み込みし、WAVに変換
    audio = AudioSegment.from_mp3(input_file)

    # 5秒ごとに区切る
    segment_duration = 5 * 1000  # 5秒をミリ秒に変換
    for i, start in enumerate(range(0, len(audio), segment_duration)):
        # 5秒ごとの部分音声を切り出し
        segment = audio[start:start + segment_duration]

        # 入力ファイルのファイル名から拡張子を取り除く
        file_name_without_extension = os.path.splitext(os.path.basename(input_file))[0]

        # 出力ファイル名をタイムコードにする
        output_file = os.path.join(output_dir, f'{file_name_without_extension}_{start / 1000}sec.wav')

        # 部分音声を保存
        segment.export(output_file, format="wav")

print("処理が完了しました。")