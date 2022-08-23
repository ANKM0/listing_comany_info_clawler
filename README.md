# ソースコードを公開するためのリポジトリ
https://gist.github.com/ANKM0/512ff5884492d7e14cc34f35efb610e0 用

## 自己紹介
関大商学部一年生<br> 
プログラムで効率化すること、問題を解決することが大好き

## 言語
Python3

## SNS
GitHub (https://github.com/ANKM0)

## 職歴
### 合同会社エクバタナ
2022 3月~現在<br>
アルバイトとして勤務<br>
クローラーに関わるプロジェクトに参加<br>

### 業務委託
2022 7月~現在<br>
建築関係の会社から案件を貰っている<br>
作業内容はホームページ移設など<br>

## 制作物
### 制作物一覧
・[クレジットカードの使用履歴をLineに送るシステム](#クレジットカードの使用履歴をLineに送るシステム)<br>
・[健康観察を自動入力するシステムとサイト](#健康観察を自動入力するシステムとサイト)<br>
・[会社情報を集めるクローラー](#会社情報を集めるクローラー)<br>
<br>
<br>
### クレジットカードの使用履歴をLineに送るシステム
#### <ソースコード>
https://github.com/ANKM0/showcase/blob/main/remote_mitsui_sumitomo_card/remote_mitsui_sumitomo_card.py
#### <設計資料>
![portfolio_ax1](https://user-images.githubusercontent.com/76755363/186085995-10cbab49-99be-4f08-8da2-35a33b8d3e3c.png)

#### <やりたかったこと>
クレジットカードの使用履歴をLineに通知して
確認しなくて良くする

#### <背景>
おばあちゃんが毎月クレジットカードの使用履歴を確認していたが<br>
サイトにたどり着くやり方がたまに分からなくなっていた<br>
<br>
そこで<br>
Lineに通知するシステムを作ればその手間が省けると思った<br>
#### <使った技術>
使用言語<br>
・Python<br>
フレームワーク<br>
・Selenium<br>
サーバー<br>
・Heroku<br>
その他<br>
・Git,GitHub,VSCode
#### <なぜそれを選んだか>
Python...使い慣れているため<br>
Selenium...動的な待機を実装したかったため<br>
　　(requests+bs4でやる方法をしらない)<br>
Heroku...簡易なシステムなので大掛かりなものを使いたくなかったから)<br>
<br>
<br>


### 健康観察を自動入力するシステムとサイト
#### <ソースコード>
https://github.com/ANKM0/showcase/tree/main/auto_kenkou_kansatu
#### <設計資料>
##### <全体>
![portfolio_ax2](https://user-images.githubusercontent.com/76755363/186117514-acec9b22-ccd5-4bcc-b9f7-d03ccf7beaa1.png)
##### <サイト>
![portfolio_ax3](https://user-images.githubusercontent.com/76755363/186117565-3a2016e5-808f-40c6-b781-430f496d21fd.png)


#### <やりたかったこと>
健康観察を自動入力するシステムを作る

#### <背景>
毎回　健康観察を入力するのが面倒だったので自動入力するシステムを作ろうと思った<br>
ついでに他の人が使えるようにサイトを作った

使用言語<br>
・Python<br>
フレームワーク<br>
・Django<br>
・Selenium<br>
DB<br>
・PostgreSQL<br>
サーバー<br>
・Heroku<br>
その他<br>
・Git,GitHub,VSCode
#### <なぜそれを選んだか>
Django...当時djangoを勉強中で<br>
 　　新しく学習する必要がなかったから<br>
Selenium...動的な待機を実装するため<br>
PostgreSQL...MySQLの設定が手間でherokuにあるDB(Heroku_Postgre)を使いたかったから<br>
Heroku...サーバーを管理する手間を減らすため
<br>
<br>

### 会社情報を集めるクローラー
#### <ソースコード>
https://github.com/ANKM0/showcase/tree/main/listing
#### <やりたかったこと>
会社情報をクローリングする
(複雑な技術を使わずに)
#### <背景>
指定されたURLから会社情報をクローリングする案件があったので
あまり時間をかけずにクローリングしたかった

#### <使った技術>
使用言語<br>
・Python<br>
ライブラリ<br>
・reauests,bs4,pandas<br>
その他<br>
・Git,GitHub,VSCode
#### <なぜそれを選んだか>
Python,reauests,bs4,pandas<br>
コーディングする時間をできるだけ短くするため

