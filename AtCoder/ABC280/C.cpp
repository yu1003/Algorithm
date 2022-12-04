#include <iostream>
using namespace std;

string S, T;
int m;

int main() {
    cin >> S;
    cin >> T;

    m = S.length();
    
    for (int i = 0; i < m; i++) {
        if (S[i] != T[i]) {
            cout << i + 1 << endl;
            return 0;
        }
    }
    
    cout << m + 1 << endl;

    return 0;
}