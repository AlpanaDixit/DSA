// #include <stdio.h>
// #include <stdlib.h>
// struct Array
// {
//     int *A;
//     int size;
//     int length;
// };

// void Display(struct Array arr)
// {
//     int i;
//     printf("\n Elements are \n");
//     for(i=0;i<arr.length;i++)
//         printf("%d ", arr.A[i]);
// }

// int main()
// {
//     struct Array arr;
//     int n,i;
//     printf("Enter size of an array");
//     scanf("%d", &arr.size);
//     arr.A=(int *)malloc(arr.size*sizeof(int));
//     arr.length=0;

//     printf("Enter number of numbers ");
//     scanf("%d", &n);

//     printf("Enter all Elemets\n");
//     for(i=0;i<n;i++)
//         scanf("%d", &arr.A[i]);
//     arr.length = n;

//     Display(arr);

//     return 0;
// }

#include <stdio.h>
#include <stdlib.h>

struct Array
{
    int *A;
    int size;
    int length;
};

void Display(struct Array arr)
{
    int i;
    printf("\n Elements are \n");
    for (i = 0; i < arr.length; i++)
        printf("%d ", arr.A[i]);
}

int main()
{
    struct Array arr;
    int n, i;
    printf("Enter number of numbers: ");
    scanf("%d", &n);

    arr.size = n;  // Allocate memory based on user-input n
    arr.A = (int *)malloc(arr.size * sizeof(int));

    if (arr.A == NULL)
    {
        printf("Memory allocation failed.\n");
        return 1; // Exit with an error code
    }

    arr.length = 0;

    printf("Enter all elements:\n");
    for (i = 0; i < n; i++)
        scanf("%d", &arr.A[i]);
    arr.length = n;

    Display(arr);

    // Don't forget to free the allocated memory when done
    free(arr.A);

    return 0;
}