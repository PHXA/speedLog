
# 概要

speedtest-cliとPythonを利用して通信量を継続的に記録するプログラムです。

Dockerのコンテナの中で動きます。

# 変数

m.py内のDURATION_SECを変更してもらうと収集する期間が変わります。

初期値として10分に設定してあります。

# 使い方

dockerとdocker-composeをシステムに入れておいてください。

以下のコマンドを実行するたびにログの記録が始まります。

```
docker-compose up --build -d
```

# 備考

ログは新しく作られた./resultフォルダの中にspeed:{tag}.tsvファイルとして書き出されます。

tagは0から始まる整数をとります。最大のtagを持つ既存のファイルがある場合はに1が加算されたtagが付与されて複製されます。そしてそれに対して追記されます。

ファイルの中身は次の列を持つtsvファイルとなります。
時間はdatetime.datetime.now()にてUTC形式で記録されます。

```
time download[Mbit/s] upload[Mbit/s]
```
