#!/usr/bin/env python
# encoding=utf8

import os
import sys
import json
import datetime
import logging
import logging.config


if __file__[-4:].lower() in ['.pyc', '.pyo']:
    _srcfile = __file__[:-4] + '.py'
else:
    _srcfile = __file__
_srcfile = os.path.normcase(_srcfile)


def setup_logger(filename=None, level=logging.INFO):
    FORMAT = '%(asctime)s %(thread)d %(levelname)s %(message)s'
    date_fmt = None
    filemode = 'w'
    if filename is None:
        filename = '%s.log' % sys.argv[0].rstrip('.py')
    os.environ['LOG_LEVEL'] = str(level)
    # CRITICAL > ERROR > WARNING > INFO > DEBUG > NOTSET
    logging.basicConfig(format=FORMAT, datefmt=date_fmt, level=level, filename=filename, filemode=filemode)


def set_debug(flag=True):
    if flag:
        os.environ['LOG_LEVEL_BKP'] = os.environ.get('LOG_LEVEL', str(logging.INFO))
        os.environ['LOG_LEVEL'] = str(logging.DEBUG)
        logging.basicConfig(level=logging.DEBUG)
    else:
        level = os.environ.get('LOG_LEVEL_BKP', str(logging.INFO))
        os.environ['LOG_LEVEL'] = str(level)
        logging.basicConfig(level=int(level))


def currentframe():
    """Return the frame object for the caller's stack frame."""
    try:
        raise Exception
    except:
        return sys.exc_info()[2].tb_frame.f_back


def findCaller():
    """
    Find the stack frame of the caller so that we can note the source
    file name, line number and function name.
    """
    f = currentframe()
    #On some versions of IronPython, currentframe() returns None if
    #IronPython isn't run with -X:Frames.
    if f is not None:
        f = f.f_back
    rv = "(unknown", 0, "(unknown)"
    while hasattr(f, "f_code"):
        co = f.f_code
        filename = os.path.normcase(co.co_filename)
        if filename == _srcfile:
            f = f.f_back
            continue
        rv = (co.co_filename, f.f_lineno, co.co_name)
        break
    return rv


def set_psn(psn):
    os.environ['PATIENT_SN'] = str(psn)


def add_header(msg):
    fn, ln, co = findCaller()
    psn = os.environ.get('PATIENT_SN', '')
    return '%s[line:%d] psn:%s, %s' % (os.path.basename(fn), ln, psn, msg)


def debug(msg, *args, **kwargs):
    if int(os.environ.get('LOG_LEVEL', logging.INFO)) <= logging.DEBUG:
        if os.environ.get('DUMP_JSON') == "1":
            args = [json.dumps(v, ensure_ascii=False) if type(v) in [list, dict] else v for v in args]
        logging.debug(add_header(msg), *args, **kwargs)


def info(msg, *args, **kwargs):
    if int(os.environ.get('LOG_LEVEL', logging.INFO)) <= logging.INFO:
        if os.environ.get('DUMP_JSON') == "1":
            args = [json.dumps(v, ensure_ascii=False) if type(v) in [list, dict] else v for v in args]
        logging.info(add_header(msg), *args, **kwargs)


def warning(msg, *args, **kwargs):
    if int(os.environ.get('LOG_LEVEL', logging.INFO)) <= logging.WARNING:
        if os.environ.get('DUMP_JSON') == "1":
            args = [json.dumps(v, ensure_ascii=False) if type(v) in [list, dict] else v for v in args]
        logging.warning(add_header(msg), *args, **kwargs)


def error(msg, *args, **kwargs):
    if int(os.environ.get('LOG_LEVEL', logging.INFO)) <= logging.ERROR:
        if os.environ.get('DUMP_JSON') == "1":
            args = [json.dumps(v, ensure_ascii=False) if type(v) in [list, dict] else v for v in args]
        logging.error(add_header(msg), *args, **kwargs)


def critical(msg, *args, **kwargs):
    if int(os.environ.get('LOG_LEVEL', logging.INFO)) <= logging.CRITICAL:
        if os.environ.get('DUMP_JSON') == "1":
            args = [json.dumps(v, ensure_ascii=False) if type(v) in [list, dict] else v for v in args]
        logging.critical(add_header(msg), *args, **kwargs)


def set_dump_json():
    os.environ['DUMP_JSON'] = "1"


# vim: set expandtab ts=4 sw=4 sts=4 tw=100:
