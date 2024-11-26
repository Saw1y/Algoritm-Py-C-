// С утра шел дождь, и ничего не предвещало беды. Но к обеду выглянуло солнце, и в лагерь заглянула СЭС. Пройдя по всем домикам и корпусам, СЭС вынесла следующий вердикт: бельевые веревки в жилых домиках не удовлетворяют нормам СЭС. Как выяснилось, в каждом домике должно быть ровно по одной бельевой веревке, и все веревки должны иметь одинаковую длину. В лагере имеется N
//  бельевых веревок и K домиков. Чтобы лагерь не закрыли, требуется так нарезать данные веревки, чтобы среди получившихся веревочек было K
// одинаковой длины. Размер штрафа обратно пропорционален длине бельевых веревок, которые будут развешены в домиках. Поэтому начальство лагеря стремиться максимизировать длину этих веревочек.

// Входные данные
// В первой строке заданы два числа — N(1≤N≤10001) и K(1≤K≤10001). Далее в каждой из последующих N
// строк записано по одному числу — длине очередной бельевой веревки. Длина веревки задана в сантиметрах. Все длины лежат в интервале от 1сантиметра до 100 километров включительно.

// Выходные данные
// В выходной файл следует вывести одно целое число — максимальную длину веревочек, удовлетворяющую условию, в сантиметрах. В случае, если лагерь закроют, выведите 0.

#include <iostream>
#include <vector>
using namespace std;

bool good(double x, const vector<int>& arr, int k) {
    int cnt = 0;
    for (int ln : arr) 
    {
        cnt += static_cast<int>(ln / x);
    }
    return cnt >= k;
}

int main() {
    int n, k;
    cin >> n >> k;
    vector<int> arr(n);
    
    for (int i = 0; i < n; ++i) 
    {
        cin >> arr[i];
    }

    double left = 0; 
    double right = 1e7 + 1;
    double m;
    
    for (int i = 0; i < 100; ++i) {
        m = (left + right) / 2;
        if (good(m, arr, k)) 
        {
            left = m;
        } 
        else 
        {
            right = m;
        }
    }


    cout << static_cast<int> (left) << endl;
    return 0;
}
