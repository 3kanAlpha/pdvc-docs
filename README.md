# PDVC 学習の手順
研究に使ったコードのまとめ

## 学習に必要なもの
- 動画から抽出した特徴量
- 各動画データに対応するキャプションデータ

## データセットの作成手順

1. 元となる動画データを用意する。
2. PySceneDetectを使って、動画データを分割する。
    - `scenedetect --input [動画パス] detect-adaptive -m 10.0s list-scenes split-video`
    - この際に、シーンのリストをCSV出力しておく（`list-scenes`）
3. faster-whisperを使って動画音声の文字起こしをする
    - `caption/generate.py`
    - YouTube側の自動生成字幕は学習に使うには質が悪いため