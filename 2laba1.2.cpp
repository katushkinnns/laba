#include <iostream>
#include <string>
#include <limits>

using namespace std;

string numberToWords(int num) {
    switch (num) {
    case -9: return "минус девять";
    case -8: return "минус восемь";
    case -7: return "минус семь";
    case -6: return "минус шесть";
    case -5: return "минус пять";
    case -4: return "минус четыре";
    case -3: return "минус три";
    case -2: return "минус два";
    case -1: return "минус один";
    case 0: return "ноль";
    case 1: return "один";
    case 2: return "два";
    case 3: return "три";
    case 4: return "четыре";
    case 5: return "пять";
    case 6: return "шесть";
    case 7: return "семь";
    case 8: return "восемь";
    case 9: return "девять";
    default: return ""; 
    }
}

bool isInteger(const string& str) {
    for (char c : str) {
        if (!isdigit(c) && c != '-' && c != '+') {
            return false;
        }
    }
    return true;
}

int main() {
    setlocale(LC_ALL, "Russian");
    string input;
    int C;

    while (true) {
        cout << "Введите целое число от -9 до 9: ";
        cin >> input;

        if (!isInteger(input)) {
            cout << "Ошибка ввода. Пожалуйста, введите целое число." << endl;
            continue;
        }

        C = stoi(input);

        if (C >= -9 && C <= 9) {
            cout << "Вы ввели: " << numberToWords(C) << endl;
            break; 
        }
        else {
            cout << "Число вне диапазона. Пожалуйста, попробуйте снова." << endl;
        }
    }

    return 0;
}
