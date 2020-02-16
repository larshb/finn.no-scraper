Finn.no Scraper
===============

## Requirements

```bash
pip3 install -r requirements.txt
```

## Run

Modify [runner.py](runner.py) to configure crawler with debug options and arguments.

```bash
python3 runner.py
```

By default, the crawler dumps all lettings in location Oslo to `letting.json`.

## Notes

* `scrapyrt` can be used for hosted crawling, however this currently works bad 
  for passing arguments to the spider.