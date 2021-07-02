######################################
#Crated By Yahya Rhiba, 2021         #
#linkedin.com/in/yahya-rhiba/        #
#Channel Youtube : ROBUINO - YR      #
######################################

import time
# This function is used for doing delay en Second
def delay(second):
    star = time.time()
    while True:
        end = time.time()-star
        if end > second:
            return "Time End"
