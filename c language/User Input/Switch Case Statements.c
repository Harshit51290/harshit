// switch ( integer expression )
// {  
// case {value 1} :  
// do this ;
 
// case {value 2} :  
//  do this ;  
 
// case {value 3} :  
// do this ;  
 
// default :  
// do this ;
//  }



#include <stdio.h>
 
int main()
{
    int i = 2;
 
    switch (i)
    {
    case 1:
        printf("Statement 1");
        break;
 
    case 2:
        printf("Statement 2");
        break;
 
    case 3:
        printf("Statement 3");
        break;
 
    default:
        printf("No valid i to switch to.");
        break;
    }
    return 0;
}
