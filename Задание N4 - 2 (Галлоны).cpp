//������ ����� �� ������������ ����� � ������, ��� ��� "//", � �� "#", � � ����� ';'
#include <iostream>
using namespace std;

int main()	// ��������� main �������
{
	float g;
	setlocale(LC_ALL, "Rus");	// ��� �� ������ �� �������
	cout << "������� ����� ��������: "; // �����
	cin >> g;	//���� ����� �������
	cout << "����� ������ ����� " << g / 7.481;
}