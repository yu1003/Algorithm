#include <iostream>
using namespace std;

int H, W, ans = 0;
char S[19][19];

int main() {
    cin >> H >> W;
    for (int i = 1; i <= H; i++) cin >> S[i];

    for (int i = 1; i <= H; i++) {
        for (int j = 0; j < W; j++) {
            if (S[i][j] == '#') ans += 1;
        }
    }

    cout << ans << endl;

    return 0;
}