#include <iostream>
using namespace std;

int N, K;
int ans = 0;

int main() {
    cin >> N >> K;

    for (int x = 1; x <= N; x++) {
        for (int y = 1; y <= N; y++) {
            int z = K - x - y;
            if (z >= 1 && z <= N) ans += 1;
        }
    }
    cout << ans << endl;

    return 0;
}