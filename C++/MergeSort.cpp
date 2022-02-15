/* Student Name: Jacob Gowan Student NetID: jag1065
Student Name: Anthony Garcia, Perry Hervey, Cinthia Liu, Alonzo Reed
Programming language: C++
Compiler/IDE Used: Visual Studio
Program Description: An implementation of the merge sort algorithm done with c++
*/
#include <iostream>
using namespace std;

void merge(int numbers[], int const left, int const middle, int const right)
{
    int const arr1 = middle - left + 1;
    int const arr2 = right - middle;

    int* leftArray = new int[arr1],
        * rightArray = new int[arr2];

    for (int i = 0; i < arr1; i++)
        leftArray[i] = numbers[left + i];
    for (int j = 0; j < arr2; j++)
        rightArray[j] = numbers[middle + 1 + j];

    int arr1Index = 0,
        arr2Index = 0; 
    int mergedIndex = left; 

    while (arr1Index < arr1 && arr2Index < arr2) {
        if (leftArray[arr1Index] <= rightArray[arr2Index]) {
            numbers[mergedIndex] = leftArray[arr1Index];
            arr1Index++;
        }
        else {
            numbers[mergedIndex] = rightArray[arr2Index];
            arr2Index++;
        }
        mergedIndex++;
    }

    while (arr1Index < arr1) {
        numbers[mergedIndex] = leftArray[arr1Index];
        arr1Index++;
        mergedIndex++;
    }
    
    while (arr2Index < arr2) {
        numbers[mergedIndex] = rightArray[arr2Index];
        arr2Index++;
        mergedIndex++;
    }
}

void mergeSort(int numbers[], int const begin, int const end)
{
    if (begin >= end)
        return; 

    int middle = begin + (end - begin) / 2;
    mergeSort(numbers, begin, middle);
    mergeSort(numbers, middle + 1, end);
    merge(numbers, begin, middle, end);
}

void printArray(int numbers[], int size)
{
    for (auto i = 0; i < size; i++)
        cout << numbers[i] << " ";
    cout << endl;
}

int main()
{
    int numbers[] = {23, 17, 2, 9, 11, 27};
    int size = sizeof(numbers) / sizeof(numbers[0]);

    cout << "Unsorted array:" << endl;
    printArray(numbers, size);

    mergeSort(numbers, 0, size - 1);

    cout << "Sorted array:" << endl;
    printArray(numbers, size);
    return 0;
}