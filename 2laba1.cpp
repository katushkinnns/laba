#include <iostream>
#include <string>
#include <algorithm> 

using namespace std;

int main()
{
    setlocale(LC_ALL, "Russian");
    double s, x;
    bool incorrect_input = true;
    string Sx;

    cout << "Введите x: ";

    while (incorrect_input)
    {
        try
        {
            cin >> Sx;

            replace(Sx.begin(), Sx.end(), ',', '.');

            x = stod(Sx);

            if (x < 0)
            {
                cout << "Неверный ввод! x не может быть отрицательным. Пожалуйста, попробуйте еще раз!" << endl;
                continue;
            }

            incorrect_input = false;
        }
        catch (invalid_argument&)
        {
            cout << "Неверный ввод! Пожалуйста, введите корректное число." << endl;
        }
        catch (out_of_range&)
        {
            cout << "Неверный ввод! Число выходит за пределы допустимого диапазона." << endl;
        }
    }

    s = x * x - (0.5 * x * x);

    cout << "Площадь квадрата за вычетом площади вписанных в него треугольников: " << s << endl;

    return 0;
}

