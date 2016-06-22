/* This is a c file to list all files and folders in a directory */

#include <stdio.h>
#include <stdlib.h>
#include <dirent.h>     /* dir header file for posix */
int main(int argc, char* argv[]){
    DIR* dir;
    struct dirent *dirptr;
    if (argc < 2){
        printf("Usage: ./name_of_of <directory_name>\n");
        return EXIT_FAILURE;
    }
    dir = opendir(argv[1]);     /* opens directory if it exists */
    if (!dir){
        printf("Can't open %s directory\n", argv[1]);
        return EXIT_FAILURE;            /* exit if directory does not exist */
    }
    while ((dirptr=readdir(dir)) != NULL){      /* read dir */
        printf("%s\n", dirptr->d_name);         /* write contents to stdout */
    }
    return EXIT_SUCCESS;
}
