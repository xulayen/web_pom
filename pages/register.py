from common.base import Base


class Registerpage (Base):
    ele_email = ("id", "id_email")
    ele_password = ("id", "id_password")
    ele_btn_register = ("id", "jsEmailRegBtn")

    def input_email(self, text):
        self.send(self.ele_email, text)

    def input_password(self, text):
        self.send(self.ele_password, text)

    def click_register(self):
        self.click(self.ele_btn_register)

    def  clear_nameloc(self):
        self.clear(self.ele_email)

    def clear_pasloc(self):
        self.clear(self.ele_password)
