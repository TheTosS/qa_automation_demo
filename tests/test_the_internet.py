# Пример: проверка заголовка страницы
def test_title(driver):
    driver.get('https://the-internet.herokuapp.com/login')
    assert "The Internet" in driver.title
