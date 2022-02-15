#include <iostream>
using namespace std;

int main(){

    string s; getline(cin, s);

    for(int i = 1; i <= 25; i++){
        for(int j = 0; j < s.size(); j++){
            if(isalpha(s[j])){
                s[j] -= 1;
                if(s[j] == 64) s[j] = 'Z';
            }
        }
        cout << "-" << i << ": " << s << endl;
    }
    for(int i = 1; i <= 25; i++){
        for(int j = 0; j < s.size(); j++){
            if(isalpha(s[j])){
                s[j] += 1;
                if(s[j] == 'Z' + 1) s[j] = 'A';
            }
        }
        cout << i << ": " << s << endl;
    }

}