# lambda-web-adapter-fastapi

[aws-lambda-web-adapter](https://github.com/awslabs/aws-lambda-web-adapter/tree/main/examples/fastapi)を参考にfastapiをlambda-web-adapterで実装した。フロントエンドはfastapiでhtmlファイルをレスポンスする形にしている。CDNでReactで実装をしている。

## Requirements

必須のソフトは以下である。

- Python 3.8.12
- Poetry (version 1.5.1)
- Docker version 20.10.11, build dea9396

## Deploy

~~~bash
poetry run sam build
poetry run sam deploy
~~~

## Note

### Dockerfile

- Portは8080にしないとLambda上で動作しない
- ローカルでDockerfileのデバックをする際は以下コマンドを使用すること 理由は[参考文献](https://zenn.dev/shake_sanma/articles/1c6475ba73da48)を参照

~~~bash
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
~~~

### requirements.txtについて

poetryで管理したパッケージを以下コマンドでrequirements.txtに出力できる。

~~~bash
poetry export -f requirements.txt --output requirements.txt
~~~
