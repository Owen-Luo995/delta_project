from behave import given, when, then
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@given('I input a title search data')
def step_impl(context):
    context.browser.get(context.base_url + '/')
    WebDriverWait(context.browser, 5).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'input[placeholder="Input the title of your search"]'))
    ).send_keys('test')


@when('I click the search button')
def step_impl(context):
    try:
        submit_button = WebDriverWait(context.browser, 5).until(  # 增加等待时间
            EC.element_to_be_clickable((By.NAME, "search"))
        )
        submit_button.click()
    except TimeoutException as e:
        print("Waiting for element to be clickable timed out: ", e)
        context.browser.save_screenshot("debug_screenshot.png")  # 保存屏幕截图，用于调试


@then('the search form should display the result')
def step_impl(context):
    try:
        message = WebDriverWait(context.browser, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, 'emptyresult'))
        )
        assert message is not None
    except TimeoutException:
        context.browser.save_screenshot('timeout_exception.png')  # 保存屏幕截图
        raise  # 抛出异常以便查看测试失败的原因
