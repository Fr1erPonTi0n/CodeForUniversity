import pytestqt
import pytest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../src'))

from app.addDataWin import AddDataWindow

class TestAddDataWindow:
    @pytest.fixture
    def window(self, qtbot):
        self.window = AddDataWindow()
        qtbot.addWidget(self.window)
        return self.window

    def test_sss(self, window):
        pass