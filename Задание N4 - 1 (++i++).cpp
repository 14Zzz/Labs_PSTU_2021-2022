//Делаем какие то обязательные штуки и помним, что тут "//", а не "#"
#include <iostream>
using namespace std;

int main()	// Обзначаем main функцию
{
	int c, i = 1; // обозначаем целочисленные переменные	
	c = ++i * i++;  // (1 + 1) * (1 + 1)
	cout << c;
}
