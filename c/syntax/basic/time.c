#include<stdio.h>
//Convert time in s to H:M:S

int main(){
    int s,m,h;

    printf("Enter time in seconds: ");
    scanf("%d", &s);

    h = s/3600;
    s = s%3600;
    m = s/60;
    s = s%60;

    printf("Time- %d:%d:%d", h,m,s);
}