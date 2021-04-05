// problem one

#include <stdio.h> 
int main() 
{ 
    int A, B, C; 
  
    printf("Enter three numbers: "); 
    scanf("%d %d %d", &A, &B, &C); 
  
    if (A >= B && A >= C) 
        printf("%d is the largest number.", A); 
  
    else if (B >= A && B >= C) 
        printf("%d is the largest number.", B); 
  
    else
        printf("%d is the largest number.", C); 
  
    return 0; 
} 

















// problem two

#include <stdio.h>
 
int main()
{
    float celsius, fahrenheit;
 
    printf("Please Enter the temperature in Fahrenheit: \n");
    scanf("%f", &fahrenheit);
 
    // Convert the temperature from fahrenheit to celsius formula
    celsius = (fahrenheit - 32) * 5 / 9;

    printf("\n %.2f Fahrenheit = %.2f Celsius", fahrenheit, celsius);
 
    return 0;
}







// problem three

#include<stdio.h>

int main()
{
   int marks;
   
   printf("\nEnter The Marks Between 0 To 100:");
   
   printf("\nEnter The Mark: ");
   scanf("%d", &marks);
   
   if(marks>100)
   {
    printf("\nDon't Be Smart Enter your Marks Between Limit\n");
   }
   else
   {
   switch(marks/10)
   {
       case 10 :
       case 9 :

           printf("\n Your Grade is: A");
           break;
       case 8 :
           
           printf("\n Your Grade is: B" );
           break;
       case 7 :
           
           printf("\n Your Grade is: C" );
           break;
       case 6 :
           
           printf("\n Your Grade is: D" );
           break;
       case 5 :
            
           printf("\n Your Grade is: E" );
           break;
       
       default :
           
           printf("\n You Grade is: F or Fail\n");
   }
 }

   getch();
   return 0;
}






// problem 4 (first series)

// 1+2+3+4+5+6+.....+100

#include<stdio.h>
     
int main()
{
    int i ,sum;
    sum = 0;
    for (i=1; i<=100; i++)
        sum +=i;
    printf("Sum of the series is  %d", sum);
    getch();
     
    return 0;
}









// problem 4 (seond series)

// 2+4+6+....+100

#include<stdio.h>
int main()
{
    int i ,sum;
    sum = 0;
    for (i=2; i<=100; i+=2)
        if(i%2==0)
        sum +=i;
    printf("Sum of the series is  %d", sum);
    getch();


}










// problem 4 (third series)

// 5+10+15+20+.....+500
#include<stdio.h>
int main()
{
    int i ,sum;
    sum  = 0;
    for (i=5; i<=500; i+=5)
        if (i%5==0)
        sum += i;
    printf("Sum of the series is  %d", sum);
    getch();
}






