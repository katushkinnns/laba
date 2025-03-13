#include <iostream>
#include <vector>
#include <cstdlib>
#include <ctime>

using namespace std;

int main() {
    setlocale(LC_ALL, "Russian");
    srand(time(0));

    int n;
    cout << "Введите размер массива: ";
    while (!(cin >> n) || n <= 0) {
        cin.clear();
        cin.ignore(10000, '\n');
        cout << "Ошибка! Введите положительное целое число: ";
    }

    vector<int> arr(n);

    cout << "Исходный массив: ";
    for (int i = 0; i < n; i++) {
        arr[i] = rand() % 51 - 20;
        cout << arr[i] << " ";
    }
    cout << endl;

    int minIndex = 0;
    for (int i = 1; i < n; i++) {
        if (arr[i] < arr[minIndex]) {
            minIndex = i;
        }
    }
    cout << "Номер минимального элемента: " << minIndex + 1 << endl;

    int lastZeroIndex = -1, sumAfterZero = 0;
    for (int i = n - 1; i >= 0; i--) {
        if (arr[i] == 0) {
            lastZeroIndex = i;
            break;
        }
    }

    if (lastZeroIndex != -1) {
        for (int i = lastZeroIndex + 1; i < n; i++) {
            sumAfterZero += arr[i];
        }
        cout << "Сумма элементов после последнего нуля: " << sumAfterZero << endl;
    }
    else {
        cout << "Сумма элементов после последнего нуля: 0" << endl;
    }

    vector<int> newArr;
    for (int i = 0; i < n; i++) {
        if (arr[i] <= 10) newArr.push_back(arr[i]);
    }
    for (int i = 0; i < n; i++) {
        if (arr[i] > 10) newArr.push_back(arr[i]);
    }

    cout << "Преобразованный массив: ";
    for (int num : newArr) {
        cout << num << " ";
    }
    cout << endl;

    return 0;
}
