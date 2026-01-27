import sys 
import csv
from PyQt6.QtWidgets import \
    (QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QHBoxLayout, 
     QLabel, QComboBox, QTableWidget, QFileDialog, QMessageBox, QTableWidgetItem)
from PyQt6.QtGui import \
    (QColor, QFont)



class MainWin(QMainWindow):
    def __init__(self):
        super().__init__()

        self.data = []
        self.filtered_data = []
        self.schools = set()
        self.classes = set()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Результат олимпиады: фильтрация')

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        layout = QVBoxLayout(central_widget)

        load_layout = QHBoxLayout()
        self.load_btn = QPushButton("Загрузить CSV файл")
        self.load_btn.clicked.connect(self.upload_data)
        load_layout.addWidget(self.load_btn)
        layout.addLayout(load_layout)
        
        filter_layout = QHBoxLayout()
        
        filter_layout.addWidget(QLabel("Школа:"))
        self.school_combo = QComboBox()
        self.school_combo.addItem("Все школы")
        self.school_combo.currentTextChanged.connect(self.apply_filters)
        filter_layout.addWidget(self.school_combo)
        
        filter_layout.addWidget(QLabel("Класс:"))
        self.class_combo = QComboBox()
        self.class_combo.addItem("Все классы")
        self.class_combo.currentTextChanged.connect(self.apply_filters)
        filter_layout.addWidget(self.class_combo)
        
        self.reset_btn = QPushButton("Сбросить фильтры")
        self.reset_btn.clicked.connect(self.reset_filters)
        filter_layout.addWidget(self.reset_btn)
        
        filter_layout.addStretch()
        layout.addLayout(filter_layout)
        
        self.table = QTableWidget()
        self.table.setColumnCount(3)
        self.table.setHorizontalHeaderLabels(["Логин", "ФИО", "Суммарный балл"])
        
    
        layout.addWidget(self.table)

    def upload_data(self, file_csv):
        filename, _ = QFileDialog.getOpenFileName(
            self, "Выберите CSV файл с результатами", "", "CSV Files (*.csv)")
        
        if filename:
            try:
                self.load_data_from_csv(filename)
                self.apply_filters()
                self.statusBar().showMessage(f"Файл загружен: {filename}")
            except Exception as e:
                QMessageBox.critical(self, "Ошибка", f"Не удалось загрузить файл: {str(e)}")
        
    def load_data_from_csv(self, filename):
        self.data.clear()
        self.schools.clear()
        self.classes.clear()
        
        with open(filename, 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            
            headers = next(reader)
            
            for row_num, row in enumerate(reader):
                if len(row) < 8:
                    continue
                    
                try:
                    place = row[0].strip()
                    user_name = row[1].strip()
                    login = row[2].strip()
                    score_str = row[7].strip()
                    
                    score = int(score_str) if score_str.isdigit() else 0
                    
                    login_parts = login.split('-')
                    if len(login_parts) >= 5:
                        school = login_parts[3]
                        class_num = login_parts[4]
                    else:
                        school = "unknown"
                        class_num = "unknown"
                    
                    self.data.append({
                        'place': place,
                        'user_name': user_name,
                        'login': login,
                        'school': school,
                        'class': class_num,
                        'score': score
                    })
                    
                    self.schools.add(school)
                    self.classes.add(class_num)
                    
                except (ValueError, IndexError) as e:
                    print(f"Ошибка в строке {row_num + 2}: {row} - {e}")
                    continue
        
        self.update_filters()

    def update_filters(self):
        current_school = self.school_combo.currentText()
        self.school_combo.clear()
        self.school_combo.addItem("Все школы")
        self.school_combo.addItems(sorted(self.schools))
        
        if current_school in self.schools:
            self.school_combo.setCurrentText(current_school)
        
        current_class = self.class_combo.currentText()
        self.class_combo.clear()
        self.class_combo.addItem("Все классы")
        self.class_combo.addItems(sorted(self.classes))

    def update_filters(self):
        current_school = self.school_combo.currentText()
        self.school_combo.clear()
        self.school_combo.addItem("Все школы")
        self.school_combo.addItems(sorted(self.schools))
        
        if current_school in self.schools:
            self.school_combo.setCurrentText(current_school)
        
        current_class = self.class_combo.currentText()
        self.class_combo.clear()
        self.class_combo.addItem("Все классы")
        self.class_combo.addItems(sorted(self.classes))
        
        if current_class in self.classes:
            self.class_combo.setCurrentText(current_class)
    
    def apply_filters(self):
        selected_school = self.school_combo.currentText()
        selected_class = self.class_combo.currentText()
        
        self.filtered_data = self.data.copy()
        
        if selected_school != "Все школы":
            self.filtered_data = [row for row in self.filtered_data if row['school'] == selected_school]
        
        if selected_class != "Все классы":
            self.filtered_data = [row for row in self.filtered_data if row['class'] == selected_class]
        
        self.filtered_data.sort(key=lambda x: x['score'], reverse=True)
        self.calculate_places()
        self.display_data()
    
    def calculate_places(self):
        if not self.filtered_data:
            return
            
        current_place = 1
        current_score = self.filtered_data[0]['score']
        
        for i, participant in enumerate(self.filtered_data):
            if participant['score'] < current_score:
                current_place = i + 1
                current_score = participant['score']
            participant['filtered_place'] = current_place
    
    def display_data(self):
        self.table.setRowCount(len(self.filtered_data))
        
        self.table.clearContents()
        
        first_place_score = None
        second_place_score = None
        third_place_score = None
        
        if self.filtered_data:
            unique_scores = sorted(set(p['score'] for p in self.filtered_data), reverse=True)
            if len(unique_scores) > 0:
                first_place_score = unique_scores[0]
            if len(unique_scores) > 1:
                second_place_score = unique_scores[1]
            if len(unique_scores) > 2:
                third_place_score = unique_scores[2]
        
        for row, participant in enumerate(self.filtered_data):
            login_item = QTableWidgetItem(participant['login'])
            login_item.setFlags(login_item.flags())
            
            name_item = QTableWidgetItem(participant['user_name'])
            name_item.setFlags(name_item.flags())
            
            score_item = QTableWidgetItem(str(participant['score']))
            score_item.setFlags(score_item.flags())
            
            self.table.setItem(row, 0, login_item)
            self.table.setItem(row, 1, name_item)
            self.table.setItem(row, 2, score_item)
            
            if participant['score'] == first_place_score:
                self.highlight_row(row, QColor(255, 215, 0))
            elif participant['score'] == second_place_score:
                self.highlight_row(row, QColor(192, 192, 192))
            elif participant['score'] == third_place_score:
                self.highlight_row(row, QColor(205, 127, 50))
    
    def highlight_row(self, row, color):
        for col in range(self.table.columnCount()):
            item = self.table.item(row, col)
            if item:
                item.setBackground(color)
                font = QFont()
                font.setBold(True)
                item.setFont(font)

    def reset_filters(self):
        self.school_combo.setCurrentIndex(0)
        self.class_combo.setCurrentIndex(0)


def main():
    app = QApplication(sys.argv)
    window = MainWin()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()