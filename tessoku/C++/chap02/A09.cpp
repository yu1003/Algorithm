#include <iostream>
using namespace std;

int H, W, N;
int Z[1509][1509];
int A[100009], B[100009], C[100009], D[100009];

int main() {
    cin >> H >> W >> N;
    for (int i = 1; i <= N; i++) cin >> A[i] >> B[i] >> C[i] >> D[i];

    for (int i = 1; i <= H; i++) {
        for (int j = 1; j <= W; j++) Z[i][j] = 0;
    }

    for (int i = 1; i <= N; i++) {
        Z[A[i]][B[i]] += 1;
        Z[C[i] + 1][B[i]] -= 1;
        Z[A[i]][D[i] + 1] -= 1;
        Z[C[i] + 1][D[i] + 1] += 1;
    }

    for (int i = 1; i <= H; i++) {
        for (int j = 1; j <= W; j++) Z[i][j] += Z[i][j - 1];
    }
    for (int j = 1; j <= W; j++) {
        for (int i = 1; i <= H; i++) Z[i][j] += Z[i - 1][j];
    }

    for (int i = 1; i <= H; i++) {
        for (int j = 1; j <= W; j++) {
            if (j >= 2) cout << " ";
            cout << Z[i][j];
        }
        cout << endl;
    }

    return 0;
}