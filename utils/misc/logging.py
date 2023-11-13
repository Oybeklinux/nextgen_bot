import logging

logging.basicConfig(filename='log_file.log',
                    filemode='a',
                    format=u'%(filename)s [LINE:%(lineno)d] #%(levelname)-8s [%(asctime)s]  %(message)s',
                    level=logging.WARNING,
                    # level=logging.DEBUG,
                    )
