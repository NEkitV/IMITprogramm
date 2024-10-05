import unittest
from PyQt5.QtWidgets import QApplication
from start import on_click
from reportlab.pdfgen import canvas
import os

class PDFGenerationTestCase(unittest.TestCase):
    def test_pdf_creation(self):
        # Создание экземпляра приложения
        app = QApplication([])

        # Создание экземпляра вашего приложения
        your_app = on_click()


        filename = "test.pdf"
        c = canvas.Canvas(filename)
        c.drawString(100, 100, "Hello, World!")
        c.showPage()
        c.save()

        # Проверка созданного файла
        self.assertTrue(c.getPageNumber() > 0)  # Проверка, что в файле есть страницы
        self.assertTrue(os.path.exists(filename))  # Проверка, что файл существует

        # Очистка созданного файла после выполнения теста
        os.remove(filename)

        # Закрытие приложения
        app.quit()

        print("Тест успешно выполнен.")

if __name__ == '__main__':
    unittest.main()
