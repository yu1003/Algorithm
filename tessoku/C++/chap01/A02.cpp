#include <iostream>
using namespace std;

int N, X, A[109];
bool ans = false;

int main() {
    cin >> N >> X;
    for (int i = 1; i <= N; i++) cin >> A[i];

    for (int i = 1; i <= N; i++) {
        if (A[i] == X) ans = true;
    }
    
    if (ans == true) cout << "Yes" << endl;
    else cout << "No" << endl;

    return 0;
}