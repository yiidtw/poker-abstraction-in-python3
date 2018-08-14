from datetime import datetime
import sys

def logger(log_type, msg):
    try:
        print(' %s %s %s' % (log_type, datetime.now().strftime("%Y-%m-%d %H:%M:%S"),  msg))
    except:
        print(' ERROR logging' + sys.exec_info()[0])
        raise
