
# 概要

通信量を継続的に記録するプログラムです。

Dockerのコンテナの中で動きます。

# 使い方

dockerをシステムに入れておいてください。

以下のコマンドを実行するたびにログの記録が始まります。（既存の記録されるファイルは上書きされます）

```
docker-compose up --build -d
```

# 備考

ログは新しく作られた./resultフォルダの中にspeed.tsvファイルとして書き出されます。

ファイルの中身は次の列を持つtsvファイルとなります。なお時間は、datetime.datetime.now()にてUTC形式で記録されます。

```
time download[Mbit/s] upload[Mbit/s]
```