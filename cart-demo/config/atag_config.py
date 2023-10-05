from Browser import Browser
from Browser.utils.data_types import SupportedBrowsers
import time
import numpy as np

class Atag_config(object):
    def __init__(self):
        self.test_env = None
        self.stepReached = [False, False, False]

        self.env_parameters = {
            'elements_file': 'config_elements.json',
            'actions_file': 'config_actions.json',
            'config_path': 'config/',
            'results_location': 'results/model2/',
            'passed_action_cost': -5.0,
            'failed_action_cost': -25.0,
            'stagnation_cost': -10.0
        }

        self.data_collection = {
            'collect_data': True,
            'elements_file': 'config_elements.json',
            'actions_file': 'config_actions.json',
            'temp_config_path': 'config/temp/',
            'click_actions': ['A', 'BUTTON'],
            'ignore_elements': ['DIV','P'],
            'type_actions': ['INPUT'],
            'type_word_list': ['test', 'test@test.fi']
        }

    def setup_env(self):
        self.test_env = Browser(timeout="10000 ms", retry_assertions_for="10 ms", strict=False)
        self.test_env.new_browser(headless=False, browser=SupportedBrowsers.chromium)
        self.test_env.new_context(acceptDownloads=True, viewport={"width": 700, "height": 500})
        return self.test_env
    
    def teardown_env(self):
        self.test_env.close_browser()
        self.stepReached = [False, False, False]

    def setup_test(self):
        page = 'http://localhost:3000/'
        self.test_env.set_browser_timeout("10 s")
        self.test_env.new_page(page)
        self.test_env.set_browser_timeout("700 ms")
        self.testStepReached = False

    def teardown_test(self):
        self.test_env.close_page()

    def env_ready(self):
        time.sleep(0.02)

    def state_rewards(self):
        reward = 0.0
        done = False

        """        xpath = "//*[starts-with(., 'Grand Total: $') and number(substring-after(., 'Grand Total: $ ')) > 5000]"
        if not self.stepReached[0] and "visible" in self.test_env.get_element_states(xpath):
            reward += 500.0
            self.stepReached[0] = True

        xpath = "//div[@class='CartPage_body__9xgUX']//*[contains(text(),'MusicMixer')]"
        if not self.stepReached[1] and "visible" in self.test_env.get_element_states(xpath):
            reward += 100.0
            self.stepReached[1] = True

        xpath = "//*[starts-with(., 'Grand Total: $') and number(substring-after(., 'Grand Total: $ ')) > 400]"
        if not self.stepReached[2] and "visible" in self.test_env.get_element_states(xpath):
            reward += 200.0
            self.stepReached[2] = True
        
        xpath = "//*[contains(text(),'Purchase Successful!')]"
        if "visible" in self.test_env.get_element_states(xpath):
            reward += 1000.0
            done = True"""

        return reward, done
