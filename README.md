# Slack Invite Form

## 必要な環境

Python 3.x系が必要です。
pyenv 等を使って環境構築することをお勧めします。

pyenvの設定は[コチラ](http://qiita.com/la_luna_azul/items/3f64016feaad1722805c)を参考にして下さい

## 使い方

### config.jsonの準備
config.jsonを同一ディレクトリに準備して下さい。
中身は以下のようにして下さい。

```json:config.json
{
    "team_name": "フォーム画面に出したいチーム名",
    "domain": "slackドメイン名 (例) my-domain.slack.com",
    "token": "Admin権限を持ったユーザのSlack API Token"
}
```

### サーバの起動・終了

#### デバッグ時

```bash
<起動時>
$ pyenv activate your-virtualenv
$ python invite.py

<終了時>
ctrl + c
```

#### デーモン起動時 (通常はこちら)

```bash
<起動時>
$ pyenv activate your-virtualenv
$ ./control_process.sh start

<終了時>
$ pyenv activate your-virtualenv
$ ./control_process.sh stop
```

### 動作確認

* デフォルトでは5000番ポートで動作します
    http://your.domain:5000/slack-invite
* 起動ポートを変更したい場合は control_process.sh の PORT という変数を変更して下さい
