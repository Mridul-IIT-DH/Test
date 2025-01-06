#include <bits/stdc++.h>

using namespace std;


int solve(string s, string r, int i, int j, vector<string> z){

if(i>=s.length() || j >= r.length()) return;





}

int main(int argc, char* argv[]) {
    if(argc!=2) {
        cout <<" argument missing" ;
        return 1;
    }
    
    ifstream file(argv[1]);
    string str;
    file>>str;

    int n = str.length();
    string rstr;
    for(int i = n-1; i>=0; i--) {
        rstr+=str[i];
    }

    ofstream file2("output.txt");
    file2<<str<<endl;
    file2<<rstr<<endl;

    vector<vector<int>> dp(n+1, vector<int>(n+1, 0));

    for(int i=1;i<=n; i++){
        for(int j=1; j<=n;j++){
            if(str[i-1] == rstr[j-1]){
                dp[i][j] = 1 + dp[i-1][j-1]; 
            }else{
                dp[i][j] = max(dp[i-1][j],dp[i][j-1]);
            }
        }
    }
 file2 << dp[n-1][n-1] ;





}