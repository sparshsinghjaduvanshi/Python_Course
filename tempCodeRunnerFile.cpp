#include<iostream>
using namespace std;

// Driver Code
int main()
{
	// Dimensions of the 2D array
	int row = 3, coloumn = 3, c = 0;

	// Declare a memory block of
	// size m*n
	int* arr = new int[row * coloumn];

	// Traverse the 2D array
	for (int i = 0; i < row; i++) {
		for (int j = 0; j < row; j++) {

			// Assign values to
			// the memory block
			if(i==j)
			{
			*(arr + i * row+ j) =1;
			}
			else
			*(arr + i * row+ j) =0;

		}
	}

	// Traverse the 2D array
	for (int i = 0; i < row; i++) {
		for (int j = 0; j < row; j++) {

			// Print values of the
			// memory block
			cout << *(arr + i * row + j)
				<< " ";
		}
		cout << endl;
	}

	//Delete the array created
	delete[] arr;

	return 0;
}
