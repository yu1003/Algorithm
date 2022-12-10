#include <iostream>
#include <string>
#include <regex>
using namespace std;

string S;

int main() {
    cin >> S;

    regex re("^[A-Z][1-9][0-9]{5}[A-Z]$");
    if (regex_match(S, re) == true) cout << "Yes" << endl;
    else cout << "No" << endl;

    return 0;
}