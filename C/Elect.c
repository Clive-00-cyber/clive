#include<stdio.h>
int main(){
    float A,B,C,D;
    printf("Enter the percentage (%) of scores of A,B,C and D\n");
    scanf("%f %f %f %f",&A,&B,&C,&D);
    if (A>50){
        printf("The candidate A is elected\n");
    }
    else if (A>12.5){
        if (A>B&&A>C&&A>D){
            printf("Going to Ballotage favorable\n");
        }
        else{
            printf("Going to Ballotage Defavorable\n");
        }  
    }
    else{
        printf("You are doom for \n Damn Brat");
    }
    return 0;
    
}