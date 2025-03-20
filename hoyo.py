from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 웹 드라이버 실행 (Chrome 기준)

# Chrome 옵션 설정
chrome_options = Options()
chrome_options.add_argument("--headless")  # GUI 없이 실행

driver = webdriver.Chrome()
driver.get("https://act.hoyolab.com/ys/event/signin-sea-v3/index.html?act_id=e202102251931481&hyl_auth_required=true&hyl_presentation_style=fullscreen&utm_source=hoyolab&utm_medium=tools&lang=ko-kr&bbs_theme=light&bbs_theme_device=1")  # 원하는 웹사이트 URL

wait = WebDriverWait(driver, 10)  # 최대 10초 대기

# 닫기 버튼 클릭
button = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(@class, 'guide-close')]")))
button.click()

# 로그인 창 불러오기
button = wait.until(EC.element_to_be_clickable((By.XPATH, "//img[contains(@class, 'mhy-hoyolab-account-block__avatar-icon')]")))
button.click()

# 2. 입력 필드 찾기 (XPath 사용)
        
# change the control to signin page
#iframe = driver.find_element(By.XPATH,"/html/body/div[2]/div/div[1]")
driver.switch_to.frame(0)

id = wait.until(
    EC.presence_of_element_located((By.XPATH, "//input[@name='username' and @type='text']"))
)
#id.click()

# # 4. 아이디 입력
id.send_keys("your id")  # 여기에 아이디 입력

# 비밀번호 입력
password_input = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@name='password' and @type='password']")))
password_input.send_keys("your password")

# 로그인 버튼 클릭
login_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit' and contains(@class, 'el-button--primary')]/span[text()='로그인']")))
login_button.click()

# 로그인 후, 기본(원래) 프레임으로 돌아가기
driver.switch_to.default_content()

# "더보기" 버튼 클릭
more_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='더보기']")))
more_button.click()

# 현재 출석일수 가져오기
count_element = wait.until(EC.presence_of_element_located((By.XPATH, "//span[@class='sign-num']")))
count = int(count_element.text)

target = count + 1

xpath = f"//div[contains(@class, 'components-home-assets-__sign-content-test_---item-day---1C_BmH') and contains(text(), '{target}일째')]"

sign_button = wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
sign_button.click()

print('출석체크 완료')

driver.quit()

###########################################################

# 웹 드라이버 실행 (Chrome 기준)

from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://act.hoyolab.com/bbs/event/signin/hkrpg/e202303301540311.html?act_id=e202303301540311&hyl_auth_required=true&hyl_presentation_style=fullscreen&utm_source=hoyolab&utm_medium=tools&utm_campaign=checkin&utm_id=6&lang=ko-kr&bbs_theme=light&bbs_theme_device=1")  # 원하는 웹사이트 URL

time.sleep(2)

# XPath를 사용하여 버튼 요소 찾기
button = driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[1]")

# 버튼 클릭
button.click()

time.sleep(1)

# XPath를 사용하여 버튼 요소 찾기
button = driver.find_element(By.XPATH, "/html/body/div/div[1]/div/div/div/div[2]/div[1]/img")

# 버튼 클릭
button.click()

time.sleep(2)

# 2. 입력 필드 찾기 (XPath 사용)
        
# change the control to signin page
#iframe = driver.find_element(By.XPATH,"/html/body/div[2]/div/div[1]")
driver.switch_to.frame(0)

id = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div[1]/form/div[3]/div[1]/input")

# 3. 클릭
id.click()

# 4. 아이디 입력
id.send_keys("your_id")  # 여기에 아이디 입력

password = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div[1]/form/div[4]/div[1]/input")

# 3. 클릭
password.click()

# 4. 아이디 입력
password.send_keys("your_password")  # 여기에 아이디 입력
time.sleep(1)

login = driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div[2]/div[1]/form/button")

login.click()

time.sleep(2)

driver.switch_to.default_content()

count = driver.find_element(By.XPATH,"/html/body/div/div[2]/div[1]/div[4]/div/div[1]/div[1]/p[1]/span").text

count = int(count)

target = count + 1

button = driver.find_element(By.XPATH,"/html/body/div/div[2]/div[1]/div[4]/div/div[2]/div[2]/img")
button.click()
time.sleep(2)

xpath = f'/html/body/div/div[2]/div[1]/div[4]/div/div[2]/div[1]/div[{target}]'

button = driver.find_element(By.XPATH,xpath)
button.click()

time.sleep(2)

driver.find_element(By.XPATH,'/html/body/div[3]/div[2]/div[2]/div').click()

driver.quit()

