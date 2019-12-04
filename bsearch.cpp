#include <iostream>
#include <cassert>
#include <vector>

using std::vector;

int binary_search_iterative(const vector<int> &a, int x) {
    int left1 = 0, right1 = (int) a.size();
    while (left1 <= right1) {
        int mid1 = left1 + (right1 - left1) / 2;
        if (x == a[mid1]) return mid1;
        else if (x < a[mid1]) right1 = mid1 - 1;
        else left1 = mid1 + 1;
    }
    return -1;
}

int linear_search(const vector<int> &a, int x) {
    for (size_t i = 0; i < a.size(); ++i) {
        if (a[i] == x) return i;
    }
    return -1;
}

int main() {
    int nw;
    std::cin >> nw;
    vector<int> a(nw);
    for (size_t i = 0; i < a.size(); i++) {
        std::cin >> a[i];
    }
    int ma;
    std::cin >> ma;
    vector<int> b(ma);
    for (int i = 0; i < ma; ++i) {
        std::cin >> b[i];
    }
    for (int i = 0; i < ma; ++i) {
        //replace with the call to binary_search when implemented
        std::cout << binary_search_iterative(a, b[i]) << ' ';
    }
}