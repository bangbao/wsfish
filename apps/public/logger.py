# coding: utf-8

import os
import stat
import logging

STAT_775 = stat.S_IRWXU + stat.S_IRWXG + stat.S_IROTH + stat.S_IXOTH


def get_logger(log_file, level=logging.DEBUG):
    """ 生成对应的日志对象
    Args:
        log_file: 日志文件
    Returns:
        logger: 日志对象
    """
    log_file = os.path.abspath(log_file)
    dirpath = os.path.dirname(log_file)
    if not os.path.exists(dirpath):
        os.makedirs(dirpath)
        os.chmod(dirpath, STAT_775)

    logger = logging.getLogger(log_file)

    if not logger.handlers:
        formatter = logging.Formatter('%(asctime)s %(message)s')
        hdlr = logging.FileHandler(log_file)
        hdlr.setFormatter(formatter)

        logger.addHandler(hdlr)
        logger.setLevel(level)

    return logger

