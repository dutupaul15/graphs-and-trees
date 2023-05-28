#include <stdio.h>
#include <stdlib.h>
#include <fcntl.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <unistd.h>
#include <string.h>
#include <sys/wait.h>
#include <time.h>
#include <signal.h>
#include <math.h>
#include <ctype.h>

#define READ_END 0
#define WRITE_END 1

int whereAmI; // 0 -> parent; 1 -> first child; 2 -> second child

int nrOfChars = 0;
int nrOfUniqueChars = 0;
int smallChars[26];
int distinctChars[26];

void handler(int sig)
{
    if (sig == SIGALRM)
    {
        if (whereAmI == 1)
        {
            kill(0, SIGUSR1);
            alarm(1);
        }
    }

    if (sig == SIGUSR1)
    {

        if (whereAmI == 2)
        {
            printf("Caractere mici citite: %d\n", nrCaractere);

            for (int i = 0; i < 26; i++)
            {

                if (!smallChars[i])
                    continue;

                printf("Litera '%c' apare de %d ori\n", 'a' + i, smallChars[i]);
                nrOfUniqueChars++;
            }
            printf("--------------------------\n");
        }
    }
}

int main()
{
    int pipeA[2];
    int pipeB[2];
    int pipeC[2];

    pid_t pid1;
    signal(SIGUSR1, handler);
    signal(SIGALRM, handler);

    pipe(pipeA);
    pipe(pipeB);
    pipe(pipeC);
    pid1 = fork();

    if (pid1 == 0)
    {
        char ch;
        whereAmI = 1;

        close(pipeA[1]);
        close(pipeB[0]);
        close(pipeC[0]);
        close(pipeC[1]);

        alarm(1);

        while (read(pipeA[0], &ch, 1))
        {
            if (ch >= 97 && ch <= 122)
            {
                write(pipeB[1], &ch, 1);
            }
        }

        close(pipeB[1]);
        close(pipeA[0]);
    }
    else
    {
        pid_t pid2 = fork();
        if (pid2 == 0)
        {
            whereAmI = 2;

            int fd;
            fd = creat("statistica.txt", 0777); // ToDO replace 0777

            dup2(fd, 1);

            close(pipeA[0]);
            close(pipeA[1]);
            close(pipeB[1]);
            close(pipeC[0]);

            char ch;
            int index;

            while (read(pipeB[0], &ch, 1))
            {

                index = ch - 97;
                smallChars[index]++;
                nrOfChars++;
            }
            close(pipeB[0]);

            write(pipeC[1], &nrOfUniqueChars, sizeof(nrOfUniqueChars));

            close(pipeC[1]);
            close(fd);
        }
        else
        {
            char ch;
            whereAmI = 0;

            int fd = open("data.txt", O_RDONLY);

            close(pipeA[0]);
            close(pipeB[0]);
            close(pipeB[1]);
            close(pipeC[1]);

            dup2(fd, 0);
            alarm(5);

            while (1)
            {
                ch = getchar();

                write(pipeA[1], &ch, 1);

                if (ch == EOF)
                {
                    printf("Am terminat de citit\n");
                    close(pipeA[1]);
                    break;
                }
            }

            int caractereDistincteDeLaCopil;

            read(pipeC[0], &caractereDistincteDeLaCopil, sizeof(caractereDistincteDeLaCopil));

            printf("Caractere distincte citite de la copil: %d\n", caractereDistincteDeLaCopil);

            close(pipeC[0]);
            close(fd);
        }
    }

    return 0;
}