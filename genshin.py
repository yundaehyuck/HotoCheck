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

complete_text = wait.until(EC.presence_of_element_located((By.XPATH,"//div[contains(@class, 'components-common-common-dialog-__index_---title---')]"))).text

if complete_text == '출석체크 성공':

    print('출석체크 완료')

else:

    print('출석체크 실패')
