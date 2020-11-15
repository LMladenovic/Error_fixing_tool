#include <stdio.h>
#include <stdlib.h>

int zbir(int **P,int n){
  int i,j,be=0;
  for (i=0;i<n;i++){
   for (j=n-i;j<n;j++){
	    be+=P[i][j];
    }
  }
  return be;
}

int main(int argc, char *argv[]){
  FILE *in=NULL;
  int **P=NULL;
  int n;
  int i,j;
  if (argc==1){
    fprintf(stderr,"Premalo argumenata!\n");
    exit(EXIT_FAILURE);
  }
  if ((in=fopen(argv[1],"r"))==NULL){
    fprintf(stderr,"Greska prilikom otvaranja datoteke %s!\n", argv[1]);
    exit(EXIT_FAILURE);
  }

  //ALOCIRAMO MATRICU
  fscanf(in,"%d", &n);
  if(( P=malloc(n*sizeof(int*)))==NULL){
    fprintf(stderr,"Greska malloc()!\n");
    exit(EXIT_FAILURE);
  }
  for(i=0;i<n;i++)
    if ((P[i]=malloc(n*sizeof(int)))==NULL){
      fprintf(stderr,"Greska malloc()!\n");
      for (j=0;j<i;j++)
        free(P[j]);
      free(P);
      exit(EXIT_FAILURE);
    }

  //UCITAVAMO MATRICU
  for(i=0;i<n;i++)
    for(j=0;j<n;j++)
      fscanf(in,"%d ",&P[i][j]);

  for(i=0;i<n;i++){
    for(j=0;j<=n;j++)
      printf("%d ",P[i][j]);
    printf("\n");
  }



  printf ("Zbir elemenata ispod sporedne dijagonale je %d\n", zbir(P,n));

  //OSLOBADJAMO MATRICU
  for(i=0;i<n;i++)
    free(P[i]);
  free(P);
  fclose(in);
  return 0;
}
