#include <iostream>
using namespace std;

int D, N;
int L[100009], R[100009], A[100009], ans[100009];

int main() {
    cin >> D;
    cin >> N;
    for (int i = 1; i <= N; i++) cin >> L[i] >> R[i];

    for (int i = 1; i <= N; i++) {
        A[L[i]] += 1;
        A[R[i]+1] -= 1; 
    }

    for (int j = 1; j <= D; j++) {
        ans[j] = ans[j-1] + A[j];
        cout << ans[j] << endl;
    }

    return 0;
}