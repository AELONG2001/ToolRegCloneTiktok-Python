def setEnableStartButton(self):
    self.stop_button.setEnabled(False)
    self.stop_button.setStyleSheet("background-color: rgba(0, 0, 0, 0.2)")
    self.start_button.setEnabled(True)
    self.start_button.setStyleSheet(
        "color:rgb(255, 252, 252); background-color:rgb(64, 170, 15)"
    )