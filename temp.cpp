#include <iostream>
using namespace std;
int main() {

    
    int arr[] = {4,2,1,3,5};
    int n = 5; // size of the array

    // insertion sort
    for (int i = 1; i<n; i++) {
        int idx = i;
        while (idx >= 1 && arr[idx] < arr[idx-1]) {
            swap(arr[idx], arr[idx-1]);
            idx--;
        }
    }

    for (int i = 0 ; i<n; i++) cout << arr[i] << " ";
    cout << endl;
}