/*
ID: gohit.y1
LANG: C++
TASK: milk
*/
#include<stdio.h>
#include<math.h>
#include<string.h>
FILE *fin = fopen("milk.in", "r");
FILE *fout = fopen("milk.out", "w");
int m, n;
int a[5000], b[5000];
void quicksort(int l, int r)
{
	int i = l, j = r, x = a[(l + r) / 2];
	while (i <= j)
	{
		while (i < r && a[i] < x) ++ i;
		while (l < j && a[j] > x) -- j;
		if (i <= j)
		{
			int temp = a[i];
			a[i] = a[j];
			a[j] = temp;
			temp = b[i];
			b[i ++] = b[j];
			b[j --] = temp;
		}
		if (i < r)	quicksort(i, r);
		if (l < j)	quicksort(l, j);
	}
}
int main()
{
	fscanf(fin, "%d", &m);
	fscanf(fin, "%d", &n);
	for (int i = 0; i < n; ++ i)
		fscanf(fin, "%d %d", a + i, b + i);
	quicksort(0, n - 1);
	int tot = 0;
	for (int i = 0; i < n; ++ i)
		if (m > b[i])
		{
			tot += a[i] * b[i];
			m -= b[i];
		} else
		{
			tot += a[i] * m;
			break;
		}
	fprintf(fout, "%d\n", tot);
	return 0;
}

