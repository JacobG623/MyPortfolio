(ISORT)
//int isort (int *begin, int *end) {
//  int *i = begin ;
//  int *j ;
//  int x ;
//  while(i<end) {
//    x = *i ;
//    j = i-1 ;
//    ** NOTE semantics here! the && operator will prevent the execution
//    ** of the *j>x part of the expression, this is not just  a logical
//    ** operation! 
//    while(j>=begin && *j>x) {
//      *(j+1) = *j ;
//      j=j-1 ;
//    }
//	  *(j+1) = x
//    i=i+1 ;
//  }
//  return end-begin ;
// }

$pushFrame 2 3
= ISORT.begin 0
= ISORT.end 1
= ISORT.i 0
= ISORT.j 1
= ISORT.x 2

//*i=begin
$getArgument ISORT.begin
$setLocal ISORT.i

//while(i<end)
(loop1)
$getLocal ISORT.i
$pushD
$getArgument ISORT.end
$pushD
$lt
$popAD
@loop1exit
D;JEQ

//x=*i
$getLocal ISORT.i
$pushD
$getPTR
$popAD
$setLocal ISORT.x

//j=i-1
$getLocal ISORT.i
D=D-1
$setLocal ISORT.j

//while(j>=begin)
(loop2)
$getLocal ISORT.j
$pushD
$getArgument ISORT.begin
$pushD
$gt
$popAD
@loop2right
D+1;JEQ
$getLocal ISORT.j
$pushD
$getArgument ISORT.begin
$pushD
$eq
$popAD
@loop2exit
D;JEQ

(loop2right)
//while(*j>x)
$getLocal ISORT.j
$pushD
$getPTR
$getLocal ISORT.x
$pushD
$gt
$popAD
@loop2exit
D;JEQ

//*(j+1) = *j
$getLocal ISORT.j
$pushD
$getPTR
$getLocal ISORT.j
D=D+1
$pushD
$setPTR

//j=j-1
$getLocal ISORT.j
D=D-1
$setLocal ISORT.j
@loop2
0;JMP

(loop2exit)
//*(j+1) = x
$getLocal ISORT.x
$pushD
$getLocal ISORT.j
D=D+1
$pushD
$setPTR

//i=i+1
$getLocal ISORT.i
D=D+1
$setLocal ISORT.i
@loop1
0;JMP

(loop1exit)
//return end-begin
$getArgument ISORT.end
$pushD
$getArgument ISORT.begin
$pushD
$sub
$popAD
$setArgument 0
$popFrame 2 3
$return