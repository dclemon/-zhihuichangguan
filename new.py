from selenium import webdriver
from selenium.webdriver.chrome.options import Options as Chrome_Options
from selenium.webdriver.firefox.options import Options as Firefox_Options
from env_check import *
from page_func import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import warnings
import jd_config
warnings.filterwarnings('ignore')


def sys_path(browser):
    path = 'driver'
    if browser == "chrome":
        if sys.platform.startswith('win'):
            return os.path.join(path, 'chromedriver.exe')
        elif sys.platform.startswith('linux'):
            return os.path.join(path, 'chromedriver.bin')
        else:
            raise Exception('不支持该系统')
    elif browser == "firefox":
        if sys.platform.startswith('win'):
            return os.path.join(path, 'geckodriver.exe')
        elif sys.platform.startswith('linux'):
            return os.path.join(path, 'geckodriver.bin')
        else:
            raise Exception('不支持该系统')
def login(browser,user_name,password):

    if browser == "chrome":
        chrome_options = Chrome_Options()
        #chrome_options.add_argument("--headless")
        global driver
        driver = webdriver.Chrome(
            options=chrome_options,
            executable_path=sys_path(browser="chrome"),
            service_args=['--ignore-ssl-errors=true', '--ssl-protocol=TLSv1'])
        print('chrome launched\n')
    elif browser == "firefox":
        firefox_options = Firefox_Options()
        firefox_options.add_argument("--headless")
        driver = webdriver.Firefox(
            options=firefox_options,
            executable_path=sys_path(browser="firefox"))
        print('firefox launched\n')
    else:
        raise Exception("不支持此类浏览器")
    print('门户登录中...')

    driver.get('https://ggtypt.njtech.edu.cn/venue-server/loginto')
    # driver.get(
    #    f'{iaaaUrl}?appID={appID}&appName={appName}&redirectUrl={redirectUrl}')

    time.sleep(1)
    driver.find_element_by_id('username').send_keys(user_name)
    WebDriverWait(driver, 10).until_not(
        EC.visibility_of_element_located((By.CLASS_NAME, "loading.ivu-spin.ivu-spin-large.ivu-spin-fix")))
    time.sleep(0.2)
    driver.find_element_by_id('password').send_keys(password)
    WebDriverWait(driver, 10).until_not(
        EC.visibility_of_element_located((By.CLASS_NAME, "loading.ivu-spin.ivu-spin-large.ivu-spin-fix")))
    time.sleep(0.2)
    driver.find_element_by_id('login').click()
    time.sleep(0.2)

    WebDriverWait(driver,
                  5).until(EC.visibility_of_element_located((By.CLASS_NAME, 'text-center')))
    print('门户登录成功')
    return '门户登录成功\n'
def go_to_venue(driver, locate, date):
    status = False
    while status == False:
        try:
            print("进入预约界面")
            driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[1]/div[2]/ul/div[1]/li[2]/span').click()
            driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[1]/div[2]/ul/div[1]/li[2]/span').click()
            time.sleep(0.1)

            print("点击场馆预约")
            driver.find_element_by_xpath(locate).click()
            #/html/body/div[1]/div/div[2]/div[3]/div/div[2]/div/div/div[2]/form/div[2]/div/div/label[7]

            driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[3]/div/div[2]/div/div/div[2]/form/div[1]/div/div/div[1]/div/div/input').click()

            print("点击日期框")
            # 这里由于与服务器有时差，容易造成错误
            str = '/html/body/div[1]/div/div[2]/div[3]/div/div[2]/div/div/div[2]/form/div[1]/div/div/div[2]/div/div/div/div[2]/div/span['+date+']/em'
            d = driver.find_element_by_xpath(str)

            d.click()

            print("点击日期")
            # /html/body/div[1]/div/div[2]/div[3]/div/div[2]/div/div/div[2]/form/div[2]/div/div/label[7]综合管
            # /html/body/div[1]/div/div[2]/div[3]/div/div[2]/div/div/div[2]/form/div[2]/div/div/label[6]足球场
            driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[3]/div/div[2]/div/div/div[2]/form/div[3]/div/div/label').click()

            print("点击羽毛球场")
            status = True
        except:
            print("出错了！可能未到服务器时间")
            status = False
            print("等待0.2S后重试")
            # /html/body/div[1]/div/div[1]/div/div[1]/div[2]/ul/div[1]/li[1]
            print("点击首页")
            driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[1]/div[2]/ul/div[1]/li[1]/span').click()
            driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[1]/div[2]/ul/div[1]/li[1]/span').click()
            time.sleep(0.2)
    return




    return status, log_str
def book(driver):
    print("查找空闲场地")
    log_str = "查找空闲场地\n"
    time.sleep(0.1)
    for i in range(8):
        n = i+2
        b = "/html/body/div[1]/div/div[2]/div[3]/div/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div/div/div/table/tbody/tr[2]/td[" + str(n) +"]/div"
        b2 = "/html/body/div[1]/div/div[2]/div[3]/div/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div/div/div/table/tbody/tr[3]/td[" + str(n) +"]/div"
        a = driver.find_element_by_xpath(b)
        a2 = driver.find_element_by_xpath(b2)
        print(a.get_attribute('class'))
        if "free" in a.get_attribute('class') and "free" in a2.get_attribute('class'):
            print("查找到空余位置，开始预约")
            driver.find_element_by_xpath(b).click()
            driver.find_element_by_xpath(b2).click()
            log_str += "找到空闲场地，场地编号为%d\n"
            print("点击同意")
            log_str = "点击同意\n"
            driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[3]/div/div[2]/div/div/div[2]/div[3]/label/span/input").click()
            print("点击同意成功\n")
            log_str += "点击同意成功\n"
            print("确定预约")
            log_str = "确定预约\n"
            driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[3]/div/div[2]/div/div/div[2]/div[4]/div/button').click()
            print("确定预约成功")
            log_str += "确定预约成功\n"
            status = True
            break
        else:
            status = False

            print("今天没有空闲位置了！")
    return status, log_str, None, None, None
def submit_order(driver,phonenumber):
    print("提交订单")
    time.sleep(0.1)
    input_box = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[3]/div/div[2]/div/div/div[2]/form/div/div[4]/div/div/div/div/input')
    input_box.clear()
    input_box.send_keys(phonenumber)
    log_str = "输入手机号\n"
    time.sleep(0.1)
    driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[3]/div/div[2]/div/div/div[2]/form/div/div[2]/div/div/label[1]/span[1]/input').click()
    driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[3]/div/div[2]/div/div/div[2]/form/div/div[2]/div/div/label[2]/span[1]/input').click()
    print("选择同伴")
    driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[3]/div/div[2]/div/div/div[2]/div/div/button').click()
    print("提交订单成功")
    log_str += "提交订单成功\n"
    print("付款（校园卡）")
    log_str = "付款（校园卡）\n"
    driver.switch_to.window(driver.window_handles[-1])
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div/div[2]/div[3]/div/div[2]/div/div/div[3]/div[5]/div[2]/button')))
    driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[3]/div/div[2]/div/div/div[3]/div[5]/div[2]/button').click()
    print("付款成功")
    log_str += "付款成功\n"
    return log_str

def main():
    yuyue_time = jd_config.read_ini('config', 'yuyue_time', 'config.ini')
    username = jd_config.read_ini('config', 'username', 'config.ini')
    password = jd_config.read_ini('config', 'password', 'config.ini')
    locate = jd_config.read_ini('config', 'locate', 'config.ini')
    date = jd_config.read_ini('config', 'date', 'config.ini')
    phone = jd_config.read_ini('config', 'phone', 'config.ini')
    login("chrome",username,password)
    #可以提前登录以后挂机
    #提取三秒预约
    #预约平台可预约3天内开放时段的体育场馆，每天8点放票。

    timeArray = time.strptime(str(yuyue_time), "%Y-%m-%d %H:%M:%S")
    yuyue_time = int(time.mktime(timeArray)) * 1000

    print(yuyue_time)


    while True:
        a = int(time.time() * 1000)
        if a >= int(yuyue_time):
            print('开始预约')
            go_to_venue(driver, locate, date)
            book(driver)
            submit_order(driver, phone)
            y = int(time.time() * 1000)
            print("本次预约用时："+str(y-a))
            break
        else:
            print('未到预约时间，等待1s')
            time.sleep(1)


    return
if __name__ == '__main__':
    main()
