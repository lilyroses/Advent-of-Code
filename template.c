/*
 * ADVENT OF CODE: 2019-01-1
 */

#include <stdio.h>
#include <stdlib.h>

int main(void) {

    const char *FILENAME = "input.txt";
    FILE *fp = fopen(FILENAME, "r");
    if (fp == NULL) {
        fprintf(stderr, "Error opening %s\n", FILENAME);
        return 1;
    }

    int floor = 0;
    int pos = 0;
    int c;
    
    
    while ((c = fgetc(fp)) != EOF) {
        pos++;

        if (c == '(') {
            floor++;
        } else if (c == ')') {
            floor--;
        }
    }

    printf("\n%i", floor);

    return 0;
}