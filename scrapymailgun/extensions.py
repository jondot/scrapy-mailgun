from scrapy import signals
import requests
import logging
from jinja2 import Template

logger = logging.getLogger(__name__)


class EmailReport(object):
    @classmethod
    def from_crawler(cls, crawler):
        ext = cls()
        crawler.signals.connect(
            ext.spider_closed, signal=signals.spider_closed)
        return ext

    def spider_closed(self, spider, reason):
        stats = spider.crawler.stats._stats
        settings = spider.crawler.settings
        subject = Template(
            settings.get("SM_EMAIL_REPORT_TMPL_SUBJECT",
                         "Set your subject in settings.py"))
        body = Template(
            settings.get("SM_EMAIL_REPORT_TMPL_BODY",
                         "Set your body in settings.py"))

        logger.debug("Sending email report")
        requests.post(
            "https://%s/messages" % (settings["SM_DOMAIN"]),
            auth=("api", settings["SM_KEY"]),
            data={
                "from": settings.get("SM_FROM", "Your Scrapy Spider"),
                "to": settings["SM_TO"],
                "subject": subject.render(spider=spider, reason=reason),
                "text": body.render(spider=spider, reason=reason)
            })
