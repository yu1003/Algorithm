#include <iostream>
using namespace std;

long long N, T;
long long A[100009], B[100009];

int main() {
    cin >> N >> T;
    for (int i = 1; i <= N; i++) cin >> A[i];
    
    B[1] = A[1]; 
    for (int i = 2; i <= N; i++) B[i] = A[i] + B[i - 1];
    
    long long W = T % B[N];

    for (int i = 1; i <= N; i++) {
        if (B[i] > W) {
            cout << i;
            cout << " ";
            cout << W - B[i - 1] << endl;
            return 0;
        };
    }

    return 0;
}