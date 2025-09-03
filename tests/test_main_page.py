import pytest
from pages.main_page import MainPage
from utils.data import MAIN_EXPECTED_ANSWERS
import allure

@pytest.mark.usefixtures("browser")
class TestMain:
    @pytest.mark.parametrize("question_index,expected_text", MAIN_EXPECTED_ANSWERS)
    @allure.story("Проверка текста ответов на вопросы")
    @allure.title("Тест вопроса с ожидаемым ответом")
    def test_main_questions_have_correct_answers(self, question_index, expected_text):
        main_page = MainPage(self.driver)
        
        with allure.step(f"Нажать на вопрос с индексом {question_index}"):
            main_page.click_question(question_index)
        
        with allure.step(f"Получить текст ответа для вопроса {question_index}"):
            actual_text = main_page.get_answer_text(question_index)
        
        with allure.step(f"Проверить, что текст ответа соответствует ожидаемому: {expected_text}"):
            assert actual_text == expected_text