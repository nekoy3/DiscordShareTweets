# DiscordShareTweets
ついーとをdiscordのチャンネルに共有してくれるbot。  
こちらの記事を参考に開発中→ https://qiita.com/uS_aito/items/9076334b1731004434f6
  
# 概要
このbotは、あらかじめサーバーに追加して、Twitterユーザーをコマンドで登録することで、その人のツイートをDiscordのチャンネル内に更新されるたびにTweetのリンクを共有するbotです。  
  
# つかいかた
### １，BotをServerに追加する
こちらのリンク→ [ 未公開 ] をクリックすることで、自身がbotを追加できる権限を所持するサーバーを選択して、botを追加する事が出来ます。  
  
### ２，通知するチャンネル内でコマンドを打つ
***/set_user (TwitterユーザーID)」***  
そのユーザーの最新のツイートを最初に共有し、それ以降ツイートが更新されるたびに設定したチャンネルにツイートのリンクを共有するようになります。  
負荷防止のため、1ユーザー5チャンネルまでの登録が可能。申請すればより多くの登録が可能(予定)  
  
***/reset_user***  
そのチャンネルに登録された情報を削除します。チャンネルにsetされた状態からsetすることは出来ません。  
  
### sp，set_userコマンド時の引数
set_userコマンド実行時に引数としてより細かな情報を与える事が出来ます。  
「media:(true:false)」trueにすると画像や動画データを含むツイートのみ共有します。falseにするとテキストツイートのみ共有します。  
「word:(string)」文字列を与えると、その文字列を含むツイートのみ共有します。  
以降、要望やアイデアによって追加予定  

# メモ(個人用)
コマンドプロンプトで ```python -m venv venv``` で仮想環境を構築し、pipでパッケージをプロジェクト別に導入する事が出来る。(https://qiita.com/fiftystorm36/items/b2fd47cf32c7694adc2e)  
仮想環境内で動作するには ```.\venv\Scripts\activate```  
終了する場合 ```deactivate```  
パッケージ確認 ```pip freeze```
パッケージインストール ```pip install パッケージ名```
requirements.txtへパッケージ一覧を出力する ```pip freeze > requirements.txt```
requirements.txtから一括でパッケージをインストールする ```pip install -r requirements.txt```

masterブランチをもとに、各機能追加中の各ブランチがあり、開発とテストが終わったらmasterブランチにmargeしていく使い方をする。  
masterブランチに書きかけコードが存在しないようにし、行き詰ったときにmasterブランチでスタート地点に戻れるようにする。  

py-cordは2.0.0b7を使用(requirements.txt)
bot追加用リンクにapplications.commandsスコープを追加しないとslash_commandが使えない。

データベースファイル名は任意(config.iniで設定)テーブル名はtweet_shareで固定