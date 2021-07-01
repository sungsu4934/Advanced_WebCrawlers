import os
from datetime import datetime

def error_logging(basepath, library, element, error, log_type):

    """
    error_logging:
    save errors when something is wrong. It's different which type of data you collect
    """

    # Time when you get error
    error_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    datefolder = str(datetime.now().strftime('%Y-%m-%d'))

    # make file for save error log
    os.makedirs(f'{basepath.format(library)}/{datefolder}', exist_ok=True)

    if log_type == 'url':

        # url_crawler's error log
        error_msg = f"[{error_date}] == ({library}, {element}) Error \n >Error Message: {error} \n\n"
        filename = f'{library}_error_log({log_type}).txt'
        dstpath = f'{basepath.format(library)}/{datefolder}/{filename}'
        with open(dstpath, 'a') as wf:
            wf.write(error_msg)

    elif log_type == 'detail':

        # detail_craler's error log
        error_msg = f"[{error_date}] == URL NUMBER {element} Error \n >Message: {error} \n\n"
        filename = f'{library}_error_log({log_type}).txt'
        dstpath = f'{basepath.format(library)}/{datefolder}/{filename}'
        with open(dstpath, 'a') as wf:
            wf.write(error_msg)