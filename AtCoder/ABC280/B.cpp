#include <iostream>
using namespace std;

int N;
int S[19], ans[19];

int main() {
    cin >> N;
    for (int i = 1; i <= N; i++) cin >> S[i];

    ans[1] = S[1];
    for (int i = 2; i <= N; i++) ans[i] = S[i] - S[i - 1];

    for (int i = 1; i <= N; i++) {
        if (i >= 2) cout << " ";
        cout << ans[i];
    }
    cout << endl;

    return 0;
}