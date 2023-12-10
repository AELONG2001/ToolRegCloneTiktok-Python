import json
def setEnableStartButton(self):
    with open("configs_account.json", "r") as json_file:
      data = json.load(json_file)
    self.stop_button.setEnabled(False)
    self.start_button.setEnabled(True)

    if "darkmode" in data:
      if data["darkmode"]:
        self.start_button.setStyleSheet(
            "color:rgb(255, 252, 252); background-color:rgb(64, 170, 15)"
        )
        self.stop_button.setStyleSheet("color: #fff; background-color: #636e72;")
      else:
        self.start_button.setStyleSheet(
            "color:rgb(255, 252, 252); background-color:rgb(64, 170, 15)"
        )
        self.stop_button.setStyleSheet("color: #000; background-color: rgba(0, 0, 0, 0.2)")
    else:
        self.start_button.setStyleSheet(
            "color:rgb(255, 252, 252); background-color:rgb(64, 170, 15)"
        )
        self.stop_button.setStyleSheet("color: #000; background-color: rgba(0, 0, 0, 0.2)")