# Overview

PythonでTETRISを作成しました!  
stringのみで構成されたでテトリスが遊べます。  
フォントによっては体裁が崩れるので気を付けてください。  
得点計算やレベルアップ速度、落下速度はオリジナルですが動作は原作に近く作られています。

# How to Play

pythonファイルを実行すると以下のようなスタート画面が表示されます。  
![screenshot_TETRIS_title](https://github.com/takagiyuusuke/TETRIS-for-python/assets/142160956/a8f34050-eceb-47ef-acd7-b426737e0089)  
キーボードの上下ボタンでモードを選択できます。レベルごとに初期のレベル(落下速度)とレベル上昇速度が異なります。  
プレイ画面は以下のようになります。  
![screenshot_TETRIS_playing](https://github.com/takagiyuusuke/TETRIS-for-python/assets/142160956/357c1b57-c0d7-45a5-9b69-842b1c4d4540)  


操作：
- d→左移動　
- f→右移動
- j→左回転
- k→右回転
- space→下降(一番下まで落ちる)
- v→下降(1ブロック分)
- p→ポーズ(Enterで解除)
- h→ホールド


# はじめに

始めるにはkeyboardをインストールしてください。
```bash
pip install keyboard

python3 TETRIS.py
```
