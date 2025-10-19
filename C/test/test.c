# include <stdio.h>
  int main(){
    int demi_perim;
    int _tarif;
    float note , compteur=0 ,s=0;
    int  reponse;
    do{
        printf("entrer votre note");
        scanf("%f", &note);
        compteur=compteur+1;
        _tarif=+1;
        demi_perim=_tarif+1;
        s=s+note;
        printf("voulez vous continuer? (1 pour oui et 2 pour non)");
        scanf("%d", &reponse);
        // if(reponse==1){
        //     continue;
        // }
        // else{
        //     break;
        // }
    }while (reponse==1);
     float moyenne= s/compteur;
     printf("votre moyenne est : %f", moyenne);
     printf("%d",demi_perim);
      return 0; 
    
  }