#include <iostream>
#include <fstream>
#include <vector>

#pragma GCC optimize("Ofast")

int main() {
    std::ios_base::sync_with_stdio(false);
    int MXNUM = 100000;

    std::vector<double> p;

    int tmp, sm = 0;
    while (std::cin >> tmp) {
        p.push_back(tmp);
        sm += tmp;
    }
    int n = p.size();

    std::vector<double> p_rev(n, 1);
    for (int i = 0; i < n; ++i)
        p[i] /= sm;

    double res = 0;
    for (int num = 0; num < MXNUM; ++num) {
        for (int i = 0; i < n; ++i) {
            p_rev[i] *= 1 - p[i];
            res += p[i] * p_rev[i];
        }
        if (num) std::cout << ' ';
        std::cout << res;
    }
    std::cout << '\n';
    return 0;
}