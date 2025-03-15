import sys
import requests
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QTextEdit, QLabel, QLineEdit

API_URL = "http://127.0.0.1:8000/generate"

class ElrondApp(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Совет Элронда - AI Оркестратор")
        self.setGeometry(100, 100, 400, 300)

        layout = QVBoxLayout()

        self.label = QLabel("Введите запрос:")
        layout.addWidget(self.label)

        self.input_field = QLineEdit(self)
        layout.addWidget(self.input_field)

        self.button = QPushButton("Отправить запрос")
        self.button.clicked.connect(self.send_request)
        layout.addWidget(self.button)

        self.result = QTextEdit(self)
        self.result.setReadOnly(True)
        layout.addWidget(self.result)

        self.setLayout(layout)

    def send_request(self):
        prompt = self.input_field.text()
        if not prompt:
            self.result.setText("Введите запрос!")
            return

        try:
            response = requests.post(API_URL, json={"prompt": prompt})
            data = response.json()
            self.result.setText(data.get("response", "Ошибка при генерации"))
        except Exception as e:
            self.result.setText(f"Ошибка соединения: {e}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ElrondApp()
    window.show()
    sys.exit(app.exec())
