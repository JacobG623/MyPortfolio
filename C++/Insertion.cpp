/* Student Name: Jacob Gowan Student NetID: jag1065
Student Name: Anthony Garcia, Perry Hervey, Cinthia Liu, Alonzo Reed
Programming language: C++ 
Compiler/IDE Used: Visual Studio
Program Description: An implementation of the insertion sort algorithm done with c++
*/
#include <iostream>
using namespace std;

void insertionSort(int numbers[], int n)
{
    int i, key, j;
    for (i = 1; i < n; i++)
    {
        key = numbers[i];
        j = i - 1;

        while (j >= 0 && numbers[j] > key)
        {
            numbers[j + 1] = numbers[j];
            j = j - 1;
        }
        numbers[j + 1] = key;
    }
}

void printArray(int numbers[], int n)
{
    int i;
    for (i = 0; i < n; i++)
        cout << numbers[i] << " ";
    cout << endl;
}

int main()
{
    int numbers[] = {23, 17, 9, 2, 11, 27};
    int n = sizeof(numbers) / sizeof(numbers[0]);
    cout << "Unsorted Array:" << endl;
    printArray(numbers, n);
    cout << "Sorted Array:" << endl;
    insertionSort(numbers, n);
    printArray(numbers, n);

    return 0;
}