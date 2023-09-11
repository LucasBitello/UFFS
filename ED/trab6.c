#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>

int nroDDD(){
    int ddd, isEcontrou;
    int vetDDD[8] = {
        61, 71, 11, 21, 32, 19, 27, 31
    };
    char* vetCidade[8] = {
        "Brasilia", "Salvador", "Sao Paulo", "Rio de Janeiro",
        "Juiz de Fora", "Campinas", "Vitoria", "Belo Horizonte" 
    };

    scanf("%d", &ddd);

    isEcontrou = 0;
    for(int i = 0; i < 8; i++){
        if(ddd == vetDDD[i]){
            isEcontrou = 1;
            printf("%s\n", vetCidade[i]);
            break;
        }
    }

    if(!isEcontrou){
        printf("DDD nao cadastrado\n");
    }

    return 0;
}

int preenchimentoVetorII(){
    int a, b;
    int vet[1000];

    scanf("%d", &a);

    b = 0;
    for(int i = 0; i < 1000; i++){
        vet[i] = b;
        printf("N[%d] = %d\n", i, b);
        b++;
        if(b == a){
            b = 0;
        }
    } 
}

int areaCirculo(){
    double raio, pi, area;

    pi = 3.14159;
    scanf("%lf", &raio);

    area = pi * (raio * raio);
    printf("A=%.4lf\n", area);
}

int prefacio(){
    int a, b, q, r, sobraA, rSobraA, valResul;

    scanf("%d %d", &a, &b);

    if(a >= 0){
        q = a / b;
        r = a % b;
    }else{
        int modb = b < 0 ? ~b + 1 : b;

        for(r = 0; r < modb; r++){
            sobraA = a - r;
            if(sobraA % b == 0){
                break;
            }
        }

        q = sobraA / b;
    }

    printf("%d %d\n", q, r);

    return 0;
}

int preenchimentoVetorI(){
    int valInit;
    int vet[10];

    scanf("%d", &valInit);

    vet[0] = valInit;
    printf("N[0] = %d\n", valInit);

    for(int i = 1; i < 10; i++){
        vet[i] = vet[i-1]*2;

        printf("N[%d] = %d\n", i, vet[i]);
    }
}

int fibonacci(){
    int qtdeNro;
    
    scanf("%d", &qtdeNro);

    int vetFibbo[qtdeNro];

    for(int i = 0; i < qtdeNro; i++){
        if(i >= 2){
            vetFibbo[i] = vetFibbo[i-1] + vetFibbo[i-2];

            printf((i == qtdeNro - 1) ? " %d\n":" %d", vetFibbo[i]);
        } else{
            vetFibbo[i] = i/1;

            printf(vetFibbo[i] == 0 ? "%d" : " %d", vetFibbo[i]);
        }
    }
}

int calculoSimples(){
    int c1, c2, q1, q2; 
    double v1, v2, r1, r2;

    scanf("%d %d %lf", &c1, &q1, &v1);
    scanf("%d %d %lf", &c2, &q2, &v2);

    r1 = q1 * v1;
    r2 = q2 * v2;

    printf("VALOR A PAGAR: R$ %.2lf\n", r1 + r2);
}

int basico(){
    int a, b, x;

    scanf("%d", &a);
    scanf("%d", &b);

    x = a + b;

    printf("X = %d\n", x);
}


int floresFlorenca() {
    char inputUser[1049];
    char firstCaracter[1];
    int isIguais = 1;
    
    while (fgets(inputUser, 1049, stdin) != NULL)
    {
        isIguais = 1;
        firstCaracter[0] = inputUser[0];

        if(firstCaracter[0] == '*'){
            break;
        }

        for(int i = 0; i < 1049; i++){
            if(inputUser[i] == ' ' && tolower(inputUser[i+1]) != tolower(firstCaracter[0])){
                isIguais = 0;
            }else if (inputUser[i] == '\0')
            {
                break;
            }
            
        }

        printf(isIguais ? "Y\n" : "N\n");
    }
}