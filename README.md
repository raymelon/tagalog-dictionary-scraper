# Tagalog Dictionary Scraper :ledger: [![Tweet](https://img.shields.io/twitter/url/http/shields.io.svg?style=social)](https://twitter.com/intent/tweet?text=Check%20out%20Tagalog%20Dictionary%20Scraper!%20Ating%20pag-ibayuhin%20ang%20ating%20talahuluganan.%20%40github%20https://github.com/raymelon/tagalog-dictionary-scraper)

> **_Ating pag-ibayuhin ang ating talahuluganan!_**

Collects [Tagalog](http://tagaloglang.com/) words from [tagalog.pinoydictionary.com](http://tagalog.pinoydictionary.com/), a database of [Tagalog](http://tagaloglang.com/) words powered by Cyberspace.ph Web Hosting. This script uses a common web scraping technique known as HTML parsing.

**[42,723 words (as of Feb 19, 2023)](https://github.com/raymelon/tagalog-dictionary-scraper/blob/master/tagalog_dict.txt)**

![](https://reposs.herokuapp.com/?path=raymelon/tagalog-dictionary-scraper)
[![License: GPL v3](https://img.shields.io/badge/License-GPL%20v3-blue.svg)](http://www.gnu.org/licenses/gpl-3.0)
[![Build Status](https://travis-ci.org/raymelon/tagalog-dictionary-scraper.svg)](https://travis-ci.org/raymelon/tagalog-dictionary-scraper)
[![codecov](https://codecov.io/gh/raymelon/tagalog-dictionary-scraper/branch/master/graph/badge.svg)](https://codecov.io/gh/raymelon/tagalog-dictionary-scraper)

[![contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)]()

## How is it done? :muscle:

Each webpage is loaded and parsed, extracting the words enclosed in `<h2 class='word-entry'>` tag.

Included is [`tagalog.pinoydictionary.com`](http://tagalog.pinoydictionary.com/) `html` [snippet](https://github.com/raymelon/tagalog-dictionary-scraper/blob/master/tagalog.pinoydictionary.com%20html%20snippet.html) containing the source of
[`http://tagalog.pinoydictionary.com/list/a/`](http://tagalog.pinoydictionary.com/list/a/) to serve as point of reference on how dictionary words from the page are extracted.

**Disclaimer:**
I do not own the `html` code cited above, it is owned by [tagalog.pinoydictionary.com](http://tagalog.pinoydictionary.com/).

## How did the project started? :thought_balloon:

The main purpose of this project is for a [Scrabble ®](http://www.scrabble.com/) Tagalog dictionary database, but other uses may vary.

## Tools :pencil2:

- [Python3 v3.5+](https://www.python.org/) :snake:
- [beautifulsoup4 v4.5.1](https://www.crummy.com/software/BeautifulSoup/) :ramen: :package: for parsing html pages

```
  python -m pip install -U pip beautifulsoup4
```

- [requests-futures v1.0.0](https://github.com/ross/requests-futures) :zap: for request concurrency

```
  python -m pip install -U pip requests-futures
```

## Notes :pushpin:

- Run the scraper script [`collect_tagalog.py`](https://github.com/raymelon/tagalog-dictionary-scraper/blob/master/collect_tagalog.py)
- See the output of collected words at [`tagalog_dict.txt`](https://github.com/raymelon/tagalog-dictionary-scraper/blob/master/tagalog_dict.txt)
- Match [`max_workers`](https://github.com/raymelon/tagalog-dictionary-scraper/blob/master/collect_tagalog.py#L57) value with the CPU and network capacity of the environment. See the [comment](https://github.com/raymelon/tagalog-dictionary-scraper/blob/master/collect_tagalog.py#L41) for estimated values and expected download rates.

## License [![License: GPL v3](https://img.shields.io/badge/License-GPL%20v3-blue.svg)](http://www.gnu.org/licenses/gpl-3.0)

[GNU General Public License 3.0](https://www.gnu.org/licenses/gpl-3.0.en.html)
