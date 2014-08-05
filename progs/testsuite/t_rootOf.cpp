#define CORE_NO_AUTOMATIC_NAMESPACE
#ifdef CORE_LEVEL
#undef CORE_LEVEL
#define CORE_LEVEL 4
#endif

#include <CORE/CORE.h>
#include <CORE/poly/Poly.h>
#include <iostream>

int main()
{
   // Polynomial:-2 + 20t - 50t^2 + t^50
   // Roots : -1.09254, 0.2, 0.2, 1.07565

   CORE::BigRat c[51];
   c[0]= CORE::BigRat(-2);
   c[1]= CORE::BigRat(20);
   c[2]= CORE::BigRat(-50);
   c[50]= CORE::BigRat(1);
   for (int k=3;k<50;++k) c[k]=0;


   CORE::Polynomial<CORE::BigRat> poly(50, c);
   poly.contract();

   CORE::Sturm<CORE::BigRat> my_sturm(poly);

   int nb_roots=my_sturm.numberOfRoots(-1000, 1000);
   for (int k=1;k<=nb_roots;++k){
     CORE::BFInterval bfi_sturm = my_sturm.isolateRoot(k, -1000.5, 1000);
     std::cout << bfi_sturm.first << " " << bfi_sturm.second << std::endl;
     CORE::Expr res=CORE::rootOf(poly, bfi_sturm);
     std::cout <<  "Root "<< res << std::endl;
   }

   return 0;
}

