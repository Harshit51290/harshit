// #include <stdio.h>
 
// int main()
// {
//     int i = 0;
//     while (1)
//     {
//         if (i > 5)
//         {
//             break;
//         }
//         printf("%d ", i);
//         i++;
//     }
 
//     return 0;
// }









#include <stdio.h>
 
int main()
{
    for (int i = 0; i <= 10; i++)
    {
        if (i < 6)
        {
            continue;
        }
        printf("%d ", i);
    }
    return 0;
}
