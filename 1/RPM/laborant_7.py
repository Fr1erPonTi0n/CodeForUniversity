from abc import ABC, abstractmethod
from typing import Any
import csv
import json


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
    
    csv_processor.load_data("data.csv")
    json_processor.load_data("data.json")
    
    csv_record_count = csv_processor.process_data()
    json_record_count = json_processor.process_data()
    
    print(f'Кол-во записей в CSV: {csv_record_count}')
    print(f'Кол-во записей в JSON: {json_record_count}')
    
    csv_processor.save_data('output_csv.txt')
    json_processor.save_data('output_json.txt')
