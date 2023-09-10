# lambda-web-adapter-fastapi

を参考にfastapiをlambda-web-adapterで実装した。フロントエンドはfastapiでhtmlファイルをレスポンスする形にしている。CDNでReactで実装をしている。

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
- 使用するpythonのイメージは以下を使用しないとLambda上で動作しない

~~~Dockerfile
FROM public.ecr.aws/docker/library/python:3.8.12-slim-buster
~~~

- ローカルでDockerfileのデバックをする際は以下コマンドを使用すること 理由は[参考文献](https://zenn.dev/shake_sanma/articles/1c6475ba73da48)を参照

~~~Dockerfile
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
~~~

### requirements.txtについて

poetryで管理したパッケージを以下コマンドでrequirements.txtに出力できる。

~~~bash
poetry export -f requirements.txt --output requirements.txt
~~~

### 参考

- [Lambda Web Adapter でウェブアプリを (ほぼ) そのままサーバーレス化する](https://aws.amazon.com/jp/builders-flash/202301/lambda-web-adapter/?awsf.filter-name=*all)
- [aws-lambda-web-adapter](https://github.com/awslabs/aws-lambda-web-adapter/tree/main/examples/fastapi)
- [CDNの使い方](https://lightgauge.net/language/javascript/cdn-react-mui)