import sys
from jd_seckill.jd_spider_requests import JdSeckill
from jd_seckill.jd_login import JDLogin


if __name__ == '__main__':
    jd_login = JDLogin()
    jd_login.login_by_qrcode()
    jd_seckill = JdSeckill()
    jd_seckill.reserve()
    jd_seckill.seckill_by_proc_pool()

