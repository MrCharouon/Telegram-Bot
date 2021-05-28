
## How To Create Telegram Bot ?

I use [fandogh](https://www.fandogh.cloud/) platform

for install fandogh :

`pip install fandogh-cli`

`fandogh login`


## Config and push

`fandogh image init --name=fandoghibot`


If you received `Image created successfully`


`fandogh image publish --version v1`

Now if it is properly made and sent to the hazelnut it should be available in your hazelnut [dashboard](https://www.fandogh.cloud/)


deploy to fandogh :

`fandogh service deploy --version v1 --name fandoghibot`
