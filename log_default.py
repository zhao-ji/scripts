import logging

from logging.handlers import SMTPHandler, TimedRotatingFileHandler
from logging.handlers import SysLogHandler, HTTPHandler
from logging import StreamHandler
from logging import Formatter

log = logging.getLogger("test")

formatter = Formatter(
    fmt=('%(asctime)s:%(created)f '
         '%(filename)s:%(module)s:%(funcName)s:%(lineno)d '
         '%(name)s:%(levelname)s '
         '%(process)d:%(processName)s '
         '%(thread)d:%(threadName)s '
         '%(message)s'),
    datefmt='%Y-%m-%d %H:%M:%S',
)

stream_handler = StreamHandler()
stream_handler.setFormatter(formatter)
log.addHandler(stream_handler)

timed_rotating_file_handler = TimedRotatingFileHandler(
    filename="hey.log", when="M", interval=1,
)
timed_rotating_file_handler.setFormatter(formatter)
log.addHandler(timed_rotating_file_handler)

smtp_handler = SMTPHandler(
    mailhost="smtp.qq.com",
    fromaddr="673326877@qq.com",
    toaddrs=["me@minganci.org", "BytesWarning+log@gmail.com"],
    subject="test-log-test",
    credentials=("673326877@qq.com", "guokr48657"),
)
smtp_handler.setFormatter(formatter)
log.addHandler(smtp_handler)

syslog_handler = SysLogHandler(
    address=("aliyun.chashuibiao.org", 514),
    facility="local0",
)
syslog_handler.setFormatter(formatter)
log.addHandler(syslog_handler)

http_handler = HTTPHandler(
    host="chashuibiao.org:8000",
    url="/",
    method="GET",
)
http_handler.setFormatter(formatter)
log.addHandler(http_handler)

log.warn("hello world")
