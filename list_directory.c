#include <stdio.h>
#include <stdlib.h>
#include <dirent.h>
int main(int argc, char* argv[]){
    DIR* dir;
    struct dirent *dirptr;
    if (argc < 2){
        printf("Usage: ./name_of_of <directory_name>\n");
        return EXIT_FAILURE;
    }
    dir = opendir(argv[1]);
    if (!dir){
        printf("Can't open %s directory\n", argv[1]);
        return EXIT_FAILURE;
    }
    while ((dirptr=readdir(dir)) != NULL){
        printf("%s\n", dirptr->d_name);
    }
    return EXIT_SUCCESS;
}
