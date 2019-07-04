# tg-media-download
Ever wanted to download all media from a Telegram chat? Here's a simple way to do it.  

> This should've really been a gist. ¯\\_(ツ)_/¯  

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

## Prerequisites
- Python 3.5+

## Configuration
```shell
pip install -r requirements.txt
```
or (if you're using pipenv)
```shell
pipenv install
```
Also, make sure to set Telegram's `api_id` and `api_hash` in `main.py`. 
```python
api_id = 12345
api_hash = '0123456789abcdef0123456789abcdef'
```

> How to obtain [api_id](https://core.telegram.org/api/obtaining_api_id)?

## Usage
```shell
python main.py
```
or (if you're using pipenv)
```shell
pipenv run python main.py
```

## License
```
WWWWWW||WWWWWW
 W W W||W W W
      ||
    ( OO )__________
     /  |           \
    /o o|    MIT     \
    \___/||_||__||_|| *
         || ||  || ||
        _||_|| _||_||
       (__|__|(__|__|
```
Code and documentation are available according to the MIT License (see [LICENSE](LICENSE)).
