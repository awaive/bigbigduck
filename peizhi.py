import logging
from logging.config import fileConfig

fileConfig(r'C:\Users\HUAWEI\py\logging.conf','encoding=‘utf-8’')
logger = logging.getLogger(r'C:\Users\HUAWEI\py\caishuzithinterup.py','encoding=‘utf-8’') # 同时输出到文件与控制台
# logger = logging.getLogger('debug') # 输出到控制台

logger.debug('test')