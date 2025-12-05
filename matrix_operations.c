#include <stdio.h>

int main() {
    int r = 3, c = 3;
    int a[3][3] = {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}};
    int b[3][3] = {{9, 8, 7}, {6, 5, 4}, {3, 2, 1}};
    int result[3][3];

    printf("--- Matrix Multiplication in C ---\n");

    // Multiplication Logic
    for (int i = 0; i < r; i++) {
        for (int j = 0; j < c; j++) {
            result[i][j] = 0;
            for (int k = 0; k < c; k++) {
                result[i][j] += a[i][k] * b[k][j];
            }
        }
    }

    // Displaying Result
    printf("Resultant Matrix:\n");
    for (int i = 0; i < r; i++) {
        for (int j = 0; j < c; j++) {
            printf("%d\t", result[i][j]);
        }
        printf("\n");
    }

    return 0;
}
