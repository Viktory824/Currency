import csv
import os

import pytest
from run_driver import DriverActions


@pytest.yield_fixture(scope='session', autouse=True)
def driver_manager():
    driver = DriverActions()
    driver.set_up()
    # BasePage.init_driver(driver)
    yield driver
    driver.tear_down()


