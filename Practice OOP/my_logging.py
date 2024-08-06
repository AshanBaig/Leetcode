import logging
# logging.basicConfig(filename='f.log')
# logging.basicConfig(format='%(asctime)s-%(name)s -%(levelname)s-%(message)s',level=logging.DEBUG)

# l=logging.getLogger('Mylogger')
# l.warning('this is  warning')
# logging.warning('this is logging warning')
# l.debug('this is  warning 2')




# l=logging.getLogger('This')
# l.warning('his is a critiacal')
# logging.debug('this is a debug msg')
# logging.info('this is info msg')
# logging.critical('this is a critical msg')
# logging.warning('this is warning msg')
# logging.error('this is error msg',exc_info=True)
# logging.basicConfig(format='%(asctime)s- %(levelname)s - %(message)s', level=logging.INFO)


#Q3
# logging.basicConfig(filename='value1.log',format=' %(asctime)s - %(levelname)s - %(message)s ',level=logging.DEBUG)
# try:
#     num=int(input('Enter a value:'))
#     logging.info(num)
# except:
#     # logging.error('Error')
#     logging.exception('Erroee')

# Q4
# logging.basicConfig(format='%(levelname)s-  %(name)s -%(message)s',level=logging.DEBUG)
# logging.critical('this is crirtacal msg')
# l=logging.getLogger('custom msg')
# l.info('this is 2nd critcal msg')

#Q5
# logging.basicConfig(level=logging.DEBUG)
# l=logging.getLogger('My_logger')
# l.setLevel(logging.DEBUG)
# l.debug('hell')
# ch=logging.StreamHandler()  #Stramhandler stdout
# formatter=logging.Formatter('%(name)s-%(levelname)s-%(message)s')
# ch.setFormatter(formatter)
# # l.addHandler(ch)
# # l.info('This is debug')
# #Q6
# # l=logging.getLogger('My_logger_filing')
# # l.setLevel(logging.DEBUG)
# fh=logging.FileHandler('value2.log')
# formatter=logging.Formatter('-%(levelname)s-%(message)s')
# fh.setFormatter(formatter)
# l.addHandler(fh)
# l.addHandler(ch)
# l.info('this is info ch and fh new')