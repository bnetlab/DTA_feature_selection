#include <fstream>
#include <sstream>
#include <iostream>
#include <vector>
using namespace std;
string infile = "AMD.csv";
int n;
vector <vector <int> > f;	
int main(int agrv, char ** argc)
{	
	infile = argc[1];
	ifstream fi(infile.c_str());
	string s;
	int x;
	while (getline(fi,s))
	{
		// cerr << s << endl;
		// cerr << s.length() << endl;
		f.push_back(vector<int>(0));
		for (int i = 0; i < s.length(); ++i)
		{
			// char c = s[i];
			// cerr << i << " " << s[i] << endl;
			if (s[i] == '0') f[n].push_back(0);
			if (s[i] == '1') f[n].push_back(1);
		}
		cerr << f[n].size() << endl;
		++n;
	}
	fi.close();
	for (auto i:f)
	{
		for (auto j:i)
			cout << j << " ";
		cout << endl;
	}
	return 0;
}