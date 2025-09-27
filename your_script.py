#!/usr/bin/env python3
"""
Text Analyzer Project for Lab #4.
A simple script to analyze text files.
"""

import sys
from collections import Counter


def read_file(file_path):
    """Reads content from a file and returns it as a string."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print(f"Ошибка: Файл '{file_path}' не найден.")
        sys.exit(1)
    except Exception as e:
        print(f"Произошла ошибка при чтении файла: {e}")
        sys.exit(1)


def analyze_text(text):
    """Analyzes the text and returns basic statistics."""
    stats = {}

    # Count characters (with and without spaces)
    stats['characters_with_spaces'] = len(text)
    stats['characters_without_spaces'] = len(text.replace(" ", ""))

    # Count words (simple split by whitespace)
    stats['words'] = len(text.split())

    # Count lines
    stats['lines'] = text.count('\n')  # Count newline characters

    # Count character frequency (optional)
    stats['character_frequency'] = Counter(text.lower())

    return stats


def print_stats(stats, show_frequency=False):
    """Prints the statistics in a readable format."""
    print("\n--- Результаты анализа текста ---")
    print(f"Количество символов (с пробелами): {stats['characters_with_spaces']}")
    print(f"Количество символов (без пробелов): {stats['characters_without_spaces']}")
    print(f"Количество слов: {stats['words']}")
    print(f"Количество строк: {stats['lines']}")

    if show_frequency:
        print("\n--- Частота символов (топ-10) ---")
        # Display top 10 most common characters, excluding spaces and newlines
        for char, count in stats['character_frequency'].most_common(15):
            if char not in (' ', '\n', '\t'):  # Filter out common whitespace
                print(f"'{char}': {count}")


def main():
    """Main function to run the text analyzer."""
    if len(sys.argv) < 2:
        print("Использование: python text_analyzer.py <путь_к_файлу> [--frequency]")
        print("   --frequency  Показать частоту символов")
        sys.exit(1)

    file_path = sys.argv[1]
    show_frequency = '--frequency' in sys.argv

    print(f"Анализируем файл: {file_path}")
    text = read_file(file_path)
    stats = analyze_text(text)
    print_stats(stats, show_frequency=show_frequency)


if __name__ == "__main__":
    main()