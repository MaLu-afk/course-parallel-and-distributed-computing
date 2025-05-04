#include <iostream>
#include <vector>
using namespace std;

// Función para imprimir una matriz representada como vector 1D
void printMatrix(const vector<int>& matrix, int rows, int cols) {
    for (int i = 0; i < rows; ++i) {
        for (int j = 0; j < cols; ++j)
            cout << matrix[i * cols + j] << "\t";
        cout << "\n";
    }
}

int main() {
    // Creamos una matriz de 2 filas y 3 columnas
    vector<int> matrix = {
        1, 2, 3,
        4, 5, 6
    };

    int rows = 2;
    int cols = 3;

    cout << "Matriz 2x3:\n";
    printMatrix(matrix, rows, cols);

    return 0;
}
