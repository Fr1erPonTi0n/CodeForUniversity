from abc import ABC, abstractmethod
from typing import Any
import csv
import json
import os


class DataProcessor(ABC):
    @abstractmethod
    def load_data(self, source: str) -> None:
        pass

    @abstractmethod
    def process_data(self) -> Any:
        pass

    @abstractmethod
    def save_data(self, destination: str) -> None:
        pass


class TXTProcessor(DataProcessor):
    def __init__(self):
        self.data = []

    def load_data(self, source: str) -> None:
        with open(source, 'r', encoding='utf-8') as file:
            self.data = file.readlines()

    def process_data(self) -> Any:
        return len(self.data)

    def save_data(self, destination: str) -> None:
        with open(destination, 'w', encoding='utf-8') as file:
            file.write(f'Кол-во записей: {len(self.data)}')


class CSVProcessor(DataProcessor):
    def __init__(self):
        self.data = []

    def load_data(self, source: str) -> None:
        with open(source, 'r', encoding='utf-8') as file:
            self.data = list(csv.reader(file))

    def process_data(self) -> Any:
        return len(self.data) - 1

    def save_data(self, destination: str) -> None:
        with open(destination, 'w', encoding='utf-8') as file:
            file.write(f'Кол-во записей: {len(self.data) - 1}')


class JSONProcessor(DataProcessor):
    def __init__(self):
        self.data = []

    def load_data(self, source: str) -> None:
        with open(source, 'r', encoding='utf-8') as file:
            self.data = json.load(file)

    def process_data(self) -> Any:
        if isinstance(self.data, list):
            return len(self.data)
        elif isinstance(self.data, dict):
            return len(self.data.keys())
        return 0

    def save_data(self, destination: str) -> None:
        with open(destination, 'w', encoding='utf-8') as file:
            file.write(f'Кол-во записей: {len(self.data)}')


if __name__ == '__main__':
    csv_processor = CSVProcessor()
    json_processor = JSONProcessor()

    project_dir = os.path.dirname(os.path.abspath(__file__))
    csv_path = os.path.join(project_dir, "data.csv")
    json_path = os.path.join(project_dir, "data.json")
    
    csv_processor.load_data(csv_path)
    json_processor.load_data(json_path)
    
    csv_record_count = csv_processor.process_data()
    json_record_count = json_processor.process_data()
    
    print(f'Кол-во записей в CSV: {csv_record_count}')
    print(f'Кол-во записей в JSON: {json_record_count}')
    
    output_csv_path = os.path.join(project_dir, "output_csv.txt")
    output_json_path = os.path.join(project_dir, "output_json.txt")

    csv_processor.save_data(output_csv_path)
    json_processor.save_data(output_json_path)
