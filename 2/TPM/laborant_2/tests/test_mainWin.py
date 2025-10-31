import pytestqt
import pytest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../src'))

from app.mainWin import MainWindow

class TestMainWindow:
    @pytest.fixture
    def window(self, qtbot):
        self.window = MainWindow()
        qtbot.addWidget(self.window)
        return self.window

    def test_sss(self, window):
        pass