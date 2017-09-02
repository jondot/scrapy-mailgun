# Scrapy-mailgun: Mailgun integration for Scrapy

A [mailgun](https://mailgun.com) integration for scrapy.

## Quick Start

Install via `pip`:

```
$ pip install scrapy-mailgun
```

What's available right now is an `EmailReport` extension, that allows you to send a report once a spider is done through mailgun.

Configure:

```python
EXTENSIONS = {
    'scrapymailgun.extensions.EmailReport': True,
}

SM_DOMAIN = 'api.mailgun.net/v3/XXXXXXXXXXXXXXXX.mailgun.org'
SM_KEY = 'key-XXXXXXXXXXXXXXXXX'
SM_FROM = 'from-email@acme.org'
SM_TO = 'to-email@acme.org'  # comma sparated

SM_EMAIL_REPORT_TMPL_SUBJECT = 'Your spider [{{spider.name}}] is done: {{reason}}'
SM_EMAIL_REPORT_TMPL_BODY = 'job stats: {{ spider.crawler.stats._stats }}'
```

### Templates

Currently verbatim template strings are supported for flexible scraper configuration (you can change these remotely with no deploy).

As for template variables, what's available to you is your `spider` and `reason` instances directly. Do what ever you want with those in the templates. 


## Developers

Set up a development environment
```
$ pip install -r requirements.txt
```

### Development

* Dependencies: list them in `requirements.txt`

### Release

* Dependencies: list them in `setup.py` under `install_requires`:

```python
install_requires=['peppercorn'],
```

Then:

```
$ make dist && make release
```

# Contributing

Fork, implement, add tests, pull request, get my everlasting thanks and a respectable place here :).


### Thanks:

To all [Contributors](https://github.com/jondot/scrapy-mailgun/graphs/contributors) - you make this happen, thanks!


# Copyright

Copyright (c) 2017 [Dotan Nahum](http://gplus.to/dotan) [@jondot](http://twitter.com/jondot). See [LICENSE](LICENSE) for further details.
