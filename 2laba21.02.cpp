//Задание 1

#include <iostream>
#include <ctime>
#include <cstdlib>

using namespace std;

int main() {
    setlocale(LC_ALL, "Russian");
    const int SIZE = 10;
    int A[SIZE], * ptr = A;

    srand(time(0)); 

    cout << "Массив: ";
    for (int i = 0; i < SIZE; i++) {
        *(ptr + i) = rand() % 20 - 10; 
        if (*(ptr + i) == 0) *(ptr + i) = 1; 
        cout << *(ptr + i) << " ";
    }
    cout << endl;

    int last = *(ptr + SIZE - 1), result = 0;

    for (int* p = ptr; p < ptr + SIZE - 1; p++) {
        if (*p < last) {
            result = *p;
            break;
        }
    }

    cout << "Первый элемент меньше " << last << ": " << result << endl;

    return 0;
}


//Задание 2

/*
#include <iostream>
#include <ctime>
#include <cstdlib>

using namespace std;

int main() {
    setlocale(LC_ALL, "Russian");
    const int SIZE = 10;
    double A[SIZE], * ptr = A;
    double sum = 0;

    srand(time(0)); 

    cout << "Исходный массив: ";
    for (int i = 0; i < SIZE; i++) {
        *(ptr + i) = (rand() % 200 - 100) / 10.0; 
        cout << *(ptr + i) << " ";
    }
    cout << endl;

    for (double* p = ptr; p < ptr + SIZE; p++) {
        if (*p > 0) sum += *p;
    }

    cout << "Сумма положительных элементов: " << sum << endl;

    return 0;
}
*/