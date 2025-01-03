#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#define m 128
#define n 256 
#define o 512 
double A[m][n], B[n][o], C[m][o];
int main(){
    for (int i = 0; i < m; i++){
	for (int j = 0; j < n; j++){
	    A[i][j] = (double) rand() / RAND_MAX; 
	}
    }
    for (int i = 0; i < n; i++){
	for (int j = 0; j < o; j++){
	    B[i][j] = (double) rand() / RAND_MAX; 
	}
    }
    clock_t start = clock();
    for (int i = 0; i < m; i++)
	for (int j = 0; j < o; j++)
	    for (int k = 0; k < n; k++)
		C[i][j] += A[i][k] * B[k][j];
    float seconds = (float) (clock() - start) / CLOCKS_PER_SEC;
    printf("%.4f\n", seconds);
