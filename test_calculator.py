from sound import recording_audio
from transform import speech_recognition    
import statistics
import numpy as np
import pytest
import pyautogui
import pyperclip
from push_buttons import push_button

def test_calculator(Params, Result, setup_teardown):
    page = setup_teardown
    push_button(page, Params)

    if page.inner_text('#calculation span') == 'Error':
        actual_result = 'Error'
    else:
        actual_result = float(page.inner_text('#calculation span').replace(',', ''))

    expected_result = Result

    page.pause()
    
    assert  actual_result == expected_result



def test_random_and_round(setup_teardown):
    page = setup_teardown
    push_button(page, ["Rand"])
    if float(page.inner_text('#calculation span')) > 0.5:
        excepted_result = 1
    else:
        excepted_result = 0
    
    Rnd_button = page.locator(".round.char", has_text="Rnd")
    Rnd_button.click()
    actual_result = int(page.inner_text('#calculation span'))

    assert  actual_result == excepted_result

def test_random_statistically(setup_teardown):
    page = setup_teardown

    samples = []
    
    for i in range(10000):
        push_button(page, ["Rand"])
        result = float(page.inner_text('#calculation span'))
        samples.append(result)
    

    mean = statistics.mean(samples) # Átlag (mean)
    median = statistics.median(samples) # Medián (median)
    stdev = statistics.stdev(samples) # Szórás (std deviation)

    expected_mean = 0.5
    expected_stdev = np.sqrt(1/12)



    assert abs(mean - expected_mean) < 0.01
    assert abs(median - expected_mean) < 0.01
    assert abs(stdev - expected_stdev) < 0.02


def font_size(page):
    style_attr = page.locator(".inputbox").get_attribute("style")
    font_size_part = style_attr.split(";")[0]
    font_size = font_size_part.replace("font-size:", "").replace("px", "").strip()
    return int(font_size)


def test_font_size_change(setup_teardown):
    page = setup_teardown

    range_slider = page.locator("#range")

    range_slider.press("ArrowRight")

    range_slider.press("ArrowLeft")
    expected_font_size_decrease_5 = 25
    actual_font_size_decrease_5 = font_size(page)

    range_slider.press("ArrowLeft")
    expected_font_size_decrease_10 = 20
    actual_font_size_decrease_10 = font_size(page)

    range_slider.press("ArrowLeft")
    expected_font_size_decrease_15 = 15
    actual_font_size_decrease_15 = font_size(page)

    range_slider.press("ArrowRight")
    expected_font_size_increase_5 = 20
    actual_font_size_increase_5 = font_size(page)

    range_slider.press("ArrowRight")
    expected_font_size_increase_10 = 25
    actual_font_size_increase_10 = font_size(page)

    range_slider.press("ArrowRight")
    expected_font_size_increase_15 = 30
    actual_font_size_increase_15 = font_size(page)

    assert actual_font_size_decrease_5 == expected_font_size_decrease_5
    assert actual_font_size_decrease_10 == expected_font_size_decrease_10
    assert actual_font_size_decrease_15 == expected_font_size_decrease_15
    assert actual_font_size_increase_5 == expected_font_size_increase_5
    assert actual_font_size_increase_10 == expected_font_size_increase_10
    assert actual_font_size_increase_15 == expected_font_size_increase_15

@pytest.mark.skip(reason="This testcase is maybe can not tested by automation")
def test_speech_recognition(setup_teardown):
    page = setup_teardown

    push_button(page, ["π","±"])

    speech_button = page.locator("div.sound svg.play")
    speech_button.click()
    recording_audio()
    excepted_result = speech_recognition()
    actual_result = float(page.inner_text('#calculation span').replace(',', ''))

    assert  actual_result == excepted_result

def test_from_clipboard_to_the_screen(setup_teardown):
    page = setup_teardown

    pyperclip.copy("-3.14")

    page.click('div.icon[onclick="paste()"]')

    page.wait_for_timeout(3000)

    pyautogui.press('p')
    print("p pressed")

    actual_result = float(page.inner_text('#calculation span').replace(',', ''))
    excepted_result = -3.14

    assert  actual_result == excepted_result

def test_answer(setup_teardown):
    page = setup_teardown

    push_button(page, ['1','0','×','1','1'])

    actual_result_step_one = float(page.inner_text(".resultbox #answer").replace('Ans = ', '').replace(',', ''))
    excepted_result__step_one = 110

    push_button(page, ['+','2'])

    actual_result_step_two = float(page.inner_text(".resultbox #answer").replace('Ans = ', '').replace(',', ''))
    excepted_result__step_two = 112

    push_button(page, ['－','8'])
    
    actual_result_step_three = float(page.inner_text(".resultbox #answer").replace('Ans = ', '').replace(',', ''))
    excepted_result__step_three = 104

    push_button(page, ['×','3'])
    
    actual_result_step_four = float(page.inner_text(".resultbox #answer").replace('Ans = ', '').replace(',', ''))
    excepted_result__step_four = 88

    push_button(page, ['÷','4'])

    actual_result_step_five = float(page.inner_text(".resultbox #answer").replace('Ans = ', '').replace(',', ''))
    excepted_result__step_five = 106

    push_button(page, ['AC','AC'])

    assert actual_result_step_one == excepted_result__step_one
    assert actual_result_step_two == excepted_result__step_two
    assert actual_result_step_three == excepted_result__step_three
    assert actual_result_step_four == excepted_result__step_four
    assert actual_result_step_five == excepted_result__step_five







