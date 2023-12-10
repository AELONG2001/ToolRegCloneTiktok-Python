import json
def setDisableStartButton(self):
   with open("configs_account.json", "r") as json_file:
      data = json.load(json_file)
   self.start_button.setEnabled(False)
   self.stop_button.setEnabled(True)

   if "darkmode" in data:
      if data["darkmode"]:
         self.start_button.setStyleSheet("color: #fff; background-color: #636e72;")
         self.stop_button.setStyleSheet(
            "color:rgb(255, 252, 252);\n" "background-color:rgb(255, 0, 0)"
         )
      else:
         self.start_button.setStyleSheet("color: #000; background-color: rgba(0, 0, 0, 0.2)")
         self.stop_button.setStyleSheet(
            "color:rgb(255, 252, 252);\n" "background-color:rgb(255, 0, 0)"
         )
   else:
      self.start_button.setStyleSheet("color: #000; background-color: rgba(0, 0, 0, 0.2)")
      self.stop_button.setStyleSheet(
         "color:rgb(255, 252, 252);\n" "background-color:rgb(255, 0, 0)"
      )
   