# SimplePush
get api for pushbullet

## setup
- install serverless
- deploy method
- add `PUSHBULLET_API_KEY` to method via AWS > Lambda > Code > env_vars
- add `AUTH_KEY` to AWS env_vars

## usage
get `/push?`

params:
- `type` - (optional, defaults to note) see [docs](https://pypi.python.org/pypi/pushbullet.py#pushing-things)
- `auth_key` - special auth key
- `header` - message header
- `body` - content
