import sounddevice as sd
import numpy as np
from sound import recording_audio
from transform import speech_recognition

buttons = [
    ["⅟x", "(", ")", "AC", "CE"],
    ["±", "x!", "x²", "xⁿ", "%"],
    ["√x", "7", "8", "9", "÷"],
    ["π", "4", "5", "6", "×"],    ["Rand", "1", "2", "3", "－"],    ["000", "0", ".", "＝", "+"]
]

def find_button_position(value):
    for row_index, row in enumerate(buttons):
        if value in row:
            col_index = row.index(value)
            return row_index + 1, col_index + 1 

def push_button(page,Params):
    for Param in Params:
        row, col = find_button_position(Param)
        if row and col:
            css_selector = f"tr:nth-child({row}) > td:nth-child({col}) .char"
            button = page.locator(css_selector)
        button.click()

def test_calculator(Params, Result, setup_teardown):
    page = setup_teardown
    push_button(page, Params)

    if page.inner_text('#calculation span') == 'Error':
        actual_result = 'Error'
    else:
        actual_result = float(page.inner_text('#calculation span').replace(',', ''))

    expected_result = Result
    
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

def test_speech_recognition(setup_teardown):
    page = setup_teardown

    push_button(page, ["π","±"])

    speech_button = page.locator("div.sound svg.play")
    speech_button.click()
    recording_audio()
    excepted_result = speech_recognition()
    actual_result = float(page.inner_text('#calculation span').replace(',', ''))

    assert  actual_result == excepted_result





