---
title: "19. Mathematical Methods for Classical Mechanics"
short_title: "Chapter 19"
label: ch-19-mathematical-methods-for-classical-mechanics
---


# 19. Mathematical Methods for Classical Mechanics

(ch-19)=

## 19.1: Introduction

Development of classical mechanics has involved a close and synergistic interweaving of physics and mathematics, that continues to play a key role in these fields. The concepts of scalar and vector fields play a pivotal role in describing the force fields and particle motion in both the Newtonian formulation of classical mechanics and electromagnetism. Thus it is imperative that you be familiar with the sophisticated mathematical formalism used to treat multivariate scalar and vector fields in classical mechanics. Ordinary and partial differential equations up to second order, as well as integration of algebraic and trigonometric functions play a major role in classical mechanics. It is assumed that you already have a working knowledge of differential and integral calculus in sufficient depth to handle this material. Computer codes, such as Mathematica, MatLab, and Maple, or symbolic calculators, can be used to obtain mathematical solutions for complicated cases.

The following 9 appendices provide brief summaries of matrix algebra, vector algebra, orthogonal coordinate systems, coordinate transformations, tensor algebra, multivariate calculus, vector differential plus integral calculus, Fourier analysis and time-sampled waveform analysis. The manipulation of scalar and vector fields is greatly facilitated by transforming to orthogonal curvilinear coordinate systems that match the symmetries of the problem. These appendices discuss how to account for the time dependence of the orthogonal unit vectors for curvilinear coordinate systems. It is assumed that, except for coordinate transformations and tensor algebra, you have been introduced to these topics in linear algebra and other physics courses, and thus the purpose of these appendices is to serve as a reference plus brief review.

## 19.2: Appendix - Matrix Algebra

### Matrices

Matrix algebra provides an elegant and powerful representation of multivariate operators, and coordinate transformations that feature prominently in classical mechanics. For example they play a pivotal role in finding the eigenvalues and eigenfunctions for coupled equations that occur in rigid-body rotation, and coupled oscillator systems. An understanding of the role of matrix mechanics in classical mechanics facilitates understanding of the equally important role played by matrix mechanics in quantal physics.

It is interesting that although determinants were used by physicists in the late $19^{th}$ century, and the concept of matrix algebra was developed by Arthur Cayley in England in 1855, many of these ideas were the work of Hamilton, and the discussion of matrix algebra was buried in a more general discussion of determinants. Matrix algebra was an esoteric branch of mathematics, little known by the physics community, until 1925 when Heisenberg proposed his innovative new quantum theory. The striking feature of this new theory was its representation of physical quantities by sets of time-dependent complex numbers and a peculiar multiplication rule. Max Born recognized that Heisenberg’s multiplication rule is just the standard “row times column” multiplication rule of matrix algebra; a topic that he had encountered as a young student in a mathematics course. In 1924 Richard Courant had just completed the first volume of the new text *Methods of Mathematical Physics* during which Pascual Jordan had served as his young assistant working on matrix manipulation. Fortuitously, Jordan and Born happened to share a carriage on a train to Hanover during which Jordan overheard Born talk about his problems trying to work with matrices. Jordan introduced himself to Born and offered to help. This led to publication, in September 1925, of the famous Born-Jordan paper[Bor25a] that gave the first rigorous formulation of matrix mechanics in physics. This was followed in November by the Born-Heisenberg-Jordan sequel[Bor25b] that established a logical consistent general method for solving matrix mechanics problems plus a connection between the mathematics of matrix mechanics and linear algebra. Matrix algebra developed into an important tool in mathematics and physics during World War 2 and now it is an integral part of undergraduate linear algebra courses.

Most applications of matrix algebra in this book are restricted to real, symmetric, square matrices. The size of a matrix is defined by the rank, which equals the row rank and column rank, i.e. the number of independent row vectors or column vectors in the square matrix. It is presumed that you have studied matrices in a linear algebra course. Thus the goal of this review is to list simple manipulation of symmetric matrices and matrix diagonalization that will be used in this course. You are referred to a linear algebra textbook if you need further details.

#### Matrix definition

A matrix is a rectangular array of numbers with $M$ rows and $N$ columns. The notation used for an element of a matrix is $A_{ij}$ where $i$ designates the row and $j$ designates the column of this matrix element in the matrix $\mathbf{A}$. Convention denotes a matrix $\mathbf{A}$ as

$$
\mathbf{A} \equiv \begin{pmatrix} A_{11} & A_{12} & \dots & A_{1(N−1)} & A_{1N} \\ A_{21} & A_{22} & .. & A_{2(N−1)} & A_{2N} \\ : & : & A_{ij} & : & : \\ A_{(M−1)1} & A_{(M−1)2} & .. & A_{(M−1)(N−1)} & A_{(M−1)N} \\ A_{M1} & A_{M2} & \dots & A_{M(N−1)} & A_{MN} \end{pmatrix} \label{A.1}
$$

Matrices can be square, $M = N$, or rectangular $M \neq N$. Matrices having only one row or column are called row or column vectors respectively, and need only a single subscript label. For example,

$$
\mathbf{A} = \begin{pmatrix} A_1 \\ A_2 \\ : \\ A_{M−1} \\ A_M \end{pmatrix} \label{A.2}
$$

#### Matrix manipulation

Matrices are defined to obey certain rules for matrix manipulation as given below.

1) Multiplication of a matrix by a scalar $\lambda$ simply multiplies each matrix element by $\lambda$.

$$
C_{ij} = \lambda A_{ij} \label{A.3}
$$

2) Addition of two matrices $\mathbf{A}$ and $\mathbf{B}$ having the same rank, i.e. the number of columns, is given by

$$
C_{ij} = A_{ij} + B_{ij} \label{A.4}
$$

3) Multiplication of a matrix $\mathbf{A}$ by a matrix $\mathbf{B}$ is defined only if the number of columns in $\mathbf{A}$ equals the number of rows in $\mathbf{B}$. The product matrix $\mathbf{C}$ is given by the **matrix product**

$$
\mathbf{C} = \mathbf{A} \cdot \mathbf{B} \label{A.5}
$$

$$
C_{ij} = [AB]_{ij} = \sum_k A_{ik}B_{kj} \label{A.6}
$$

For example, if both $\mathbf{A}$ and $\mathbf{B}$ are rank three symmetric matrices then

$$
\begin{align*} \mathbf{C} &= \mathbf{A} \cdot \mathbf{B} \\[4pt] &= \begin{pmatrix} A_{11} & A_{12} & A_{13} \\ A_{21} & A_{22} & A_{23} \\ A_{31} & A_{32} & A_{33} \end{pmatrix} \cdot \begin{pmatrix} B_{11} & B_{12} & B_{13} \\ B_{21} & B_{22} & B_{23} \\ B_{31} & B_{32} & B_{33} \end{pmatrix} \\[4pt] &= \begin{pmatrix} A_{11}B_{11} + A_{12}B_{21} + A_{13}B_{31} & A_{11}B_{12} + A_{12}B_{22} + A_{13}B_{32} & A_{11}B_{13} + A_{12}B_{23} + A_{13}B_{33} \\ A_{21}B_{11} + A_{22}B_{21} + A_{23}B_{31} & A_{21}B_{12} + A_{22}B_{22} + A_{23}B_{32} & A_{21}B_{13} + A_{22}B_{23} + A_{23}B_{33} \\ A_{31}B_{11} + A_{32}B_{21} + A_{33}B_{31} & A_{31}B_{12} + A_{32}B_{22} + A_{33}B_{32} & A_{31}B_{13} + A_{32}B_{23} + A_{33}B_{33} \end{pmatrix} \end{align*}
$$

In general, multiplication of matrices $\mathbf{A}$ and $\mathbf{B}$ is noncommutative, i.e.

$$
\mathbf{A} \cdot \mathbf{B} \neq \mathbf{B} \cdot \mathbf{A} \label{A.7}
$$

In the special case when $\mathbf{A} \cdot \mathbf{B} = \mathbf{B} \cdot \mathbf{A}$ then the matrices are said to commute.

#### Transposed matrix $\mathbf{A}^T$

The *transpose* of a matrix $\mathbf{A}$ will be denoted by $\mathbf{A}^T$ and is given by interchanging rows and columns, that is

$$
\left( A^T \right)_{ij} = A_{ji} \label{A.8}
$$

The transpose of a column vector is a row vector. Note that older texts use the symbol $\mathbf{\tilde{A}}$ for the transpose.

#### Identity (unity) matrix $\mathbb{I}$

The *identity (unity) matrix* $\mathbb{I}$ is diagonal with diagonal elements equal to 1, that is

$$
\mathbb{I}_{ij} = \delta_{ij} \label{A.9}
$$

where the Kronecker delta symbol is defined by

$$
\begin{align} \delta_{ik} & = 0 && \text{ if } i \neq k \label{A.10} \\ & = 1 && \text{ if } i = k \nonumber\end{align}
$$

#### Inverse matrix $\mathbf{A}^{−1}$

If a matrix is non-singular, that is, its determinant is non-zero, then it is possible to define an *inverse* matrix $\mathbf{A}^{−1}$. A square matrix has an inverse matrix for which the product

$$
\mathbf{A} \cdot \mathbf{A}^{−1} = \mathbb{I} \label{A.11}
$$

#### Orthogonal matrix

A matrix with *real elements* is *orthogonal* if

$$
\mathbf{A}^T = \mathbf{A}^{−1} \label{A.12}
$$

That is

$$
\sum_k \left( A^T \right)_{ik} A_{kj} = \sum_k A_{ki}A_{kj} = \delta_{ij} \label{A.13}
$$

#### Adjoint matrix $A^{\dagger}$

For a matrix with *complex elements*, the *adjoint* matrix, denoted by $A^{\dagger}$ is defined as the transpose of the complex conjugate

$$
\left( A^{\dagger}\right)_{ij} = A^{*}_{ji} \label{A.14}
$$

#### Hermitian matrix

The *Hermitian conjugate* of a complex matrix $\mathbf{H}$ is denoted as $\mathbf{H}^{\dagger}$ and is defined as

$$
\mathbf{H}^{\dagger} = \left( \mathbf{H}^T \right)^{*} = (\mathbf{H}^{*})^T \label{A.15}
$$

Therefore

$$
H^{\dagger}_{ij} = H^{*}_{ji} \label{A.16}
$$

A matrix is *Hermitian* if it is equal to its adjoint

$$
\mathbf{H}^{\dagger} = \mathbf{H} \label{A.17}
$$

that is

$$
H^{\dagger}_{ij} = H^{*}_{ji} = H_{ij} \label{A.18}
$$

A matrix that is both Hermitian and has real elements is a symmetric matrix since complex conjugation has no effect.

#### Unitary matrix

A matrix with *complex* elements is *unitary* if its inverse is equal to the adjoint matrix

$$
\mathbf{U}^{\dagger} = \mathbf{U}^{−1} \label{A.19}
$$

which is equivalent to

$$
\mathbf{U}^{\dagger}\mathbf{U} = \mathbb{I} \label{A.20}
$$

A unitary matrix with real elements is an orthogonal matrix as given in Equation \ref{A.12}.

#### Trace of a square matrix $Tr \mathbf{A}$

The *trace* of a square matrix, denoted by $Tr\mathbf{A}$, is defined as the sum of the diagonal matrix elements.

$$
Tr\mathbf{A} = \sum^N_{i=1} A_{ii} \label{A.21}
$$

#### Inner product of column vectors

##### Real vectors

The generalization of the scalar (dot) product in Euclidean space is called the **inner product**. Exploiting the rules of matrix multiplication requires taking the transpose of the first column vector to form a row vector which then is multiplied by the second column vector using the conventional rules for matrix multiplication. That is, for rank $N$ vectors

$$
[\mathbf{X}] \cdot [\mathbf{Y}] = \begin{pmatrix} X_1 \\ X_2 \\ : \\ X_N \end{pmatrix} \cdot \begin{pmatrix} Y_1 \\ Y_2 \\ : \\ Y_N \end{pmatrix} = [\mathbf{X}]^T [\mathbf{Y}] = \begin{pmatrix} X_1 & X_2 & .. & X_N \end{pmatrix} \begin{pmatrix} Y_1 \\ Y_2 \\ : \\ Y_N \end{pmatrix} = \sum^N_{i=1} X_iY_i \label{A.22}
$$

For rank $N = 3$ this inner product agrees with the conventional definition of the scalar product and gives a result that is a scalar. For the special case when $[\mathbf{A}] \cdot [\mathbf{B}]=0$ then the two matrices are called *orthogonal*. The magnitude squared of a column vector is given by the inner product

$$
[\mathbf{X}] \cdot [\mathbf{X}] = \sum^N_{i=1} (X_i)^2 \geq 0 \label{A.23}
$$

Note that this is only positive.

##### Complex vectors

For vectors having complex matrix elements the inner product is generalized to a form that is consistent with Equation \ref{A.22} when the column vector matrix elements are real.

$$
[\mathbf{X}]^{*} \cdot [\mathbf{Y}]=[\mathbf{X}]^{\dagger} [\mathbf{Y}] = \begin{pmatrix} X^{*}_1 & X^{*}_2 & .. & X^{*}_{N−1} & X^{*}_N \end{pmatrix} \begin{pmatrix} Y_1 \\ Y_2 \\ : \\ Y_{N−1} \\ Y_N \end{pmatrix} = \sum^N_{i=1} X^{*}_i Y_i \label{A.24}
$$

For the special case

$$
[\mathbf{X}]^{*} \cdot [\mathbf{X}]=[\mathbf{X}]^{\dagger} [\mathbf{X}] = \sum^N_{i=1} X^{*}_i X_i \geq 0 \label{A.25}
$$

### Determinants

#### Definition

The determinant of a square matrix with $N$ rows equals a single number derived using the matrix elements of the matrix. The determinant is denoted as $\det \mathbf{A}$ or $|\mathbf{A}|$ where

$$
|\mathbf{A}| = \sum^N_{j=1} \varepsilon (j_1, j_2, \dots .j_N )A_{1j_1}A_{2j_2} \dots A_{Nj_N} \label{A.26}
$$

where $\varepsilon (j_1, j_2, \dots .j_N )$ is the permutation index which is either even or odd depending on the number of permutations required to go from the normal order $(1, 2, 3, \dots N)$ to the sequence $(j_1j_2j_3\dots j_N )$.

For example for $N = 3$ the determinant is

$$
|\mathbf{A}| = A_{11}A_{22}A_{33} + A_{12}A_{23}A_{31} + A_{13}A_{21}A_{32} − A_{13}A_{22}A_{31} − A_{11}A_{23}A_{32} − A_{12}A_{21}A_{33} \label{A.27}
$$

#### Properties

1. The value of a determinant $|A| = 0$, if

all elements of a row (column) are zero.
all elements of a row (column) are identical with, or multiples of, the corresponding elements of another row (column).
2. The value of a determinant is unchanged if

rows and columns are interchanged.
a linear combination of any number of rows is added to any one row.
3. The value of a determinant changes sign if two rows, or any two columns, are interchanged.
4. Transposing a square matrix does not change its determinant. $\left|\mathbf{A}^T\right| = |\mathbf{A}|$
5. If any row (column) is multiplied by a constant factor then the value of the determinant is multiplied by the same factor.
6. The determinant of a diagonal matrix equals the product of the diagonal matrix elements. That is, when $A_{ij} = \lambda i\delta_{ij}$ then $|\mathbf{A}| = \lambda_1\lambda_2\lambda_3\dots \lambda_N$
7. The determinant of the identity (unity) matrix $|\mathbb{I}| = 1$.
8. The determinant of the null matrix, for which all matrix elements are zero, $|\mathbf{0}| = 0$
9. A *singular* matrix has a determinant equal to zero.
10. If each element of any row (column) appears as the sum (difference) of two or more quantities, then the determinant can be written as a sum (difference) of two or more determinants of the same order. For example for order $N = 2$, 
$$
\begin{vmatrix} A_{11} \pm B_{11} & A_{12} \pm B_{12} \\ A_{21} & A_{22} \end{vmatrix} = \begin{vmatrix} A_{11} & A_{12} \\ A_{21} & A_{22} \end{vmatrix} \pm \begin{vmatrix} B_{11} & B_{12} \\ A_{21} & A_{22} \end{vmatrix} \nonumber
$$

11. A determinant of a matrix product equals the product of the determinants. That is, if $\mathbf{C} = \mathbf{AB}$ then $|\mathbf{C}| = |\mathbf{A}| |\mathbf{B}|$

#### Cofactor of a square matrix

For a square matrix having $N$ rows the cofactor is obtained by removing the $i^{th}$ row and the $j^{th}$ column and then collapsing the remaining matrix elements into a square matrix with $N − 1$ rows while preserving the order of the matrix elements. This is called the complementary minor which is denoted as $A^{(ij)}$. The matrix elements of the cofactor square matrix $\mathbf{a}$ are obtained by multiplying the determinant of the $(ij)$ complementary minor by the phase factor $(−1)^{i+j}$. That is

$$
a_{ij} = (−1)^{i+j} \left| A^{(ij)} \right| \label{A.28}
$$

The cofactor matrix has the property that

$$
\sum^N_{k=1} A_{ik}a_{jk} = \delta_{ij} |\mathbf{A}| = \sum^N_{k=1} A_{ki}a_{kj} \label{A.29}
$$

Cofactors are used to expand the determinant of a square matrix in order to evaluate the determinant.

#### Inverse of a non-singular matrix

The $(i, j)$ matrix elements of the inverse matrix $\mathbf{A}^{−1}$ of a non-singular matrix $\mathbf{A}$ are given by the ratio of the cofactor $a_{ji}$ and the determinant $|\mathbf{A}|$, that is

$$
\mathbf{A}^{−1}_{ij} = \frac{1}{ |\mathbf{A}|} a_{ji} \label{A.30}
$$

Equations \ref{A.28} and \ref{A.29} can be used to evaluate the $i, j$ element of the matrix product $\left( \mathbf{A}^{−1}\mathbf{A}\right)$

$$
\left( \mathbf{A}^{−1}\mathbf{A}\right)_{ij} = \sum^N_{k=1} \mathbf{A}^{−1}_{ik} A_{kj} = \frac{1}{ |\mathbf{A}|} \sum^N_{k=1} a_{ji}A_{kj} = \frac{1}{ |\mathbf{A}|} \delta_{ji} |\mathbf{A}| = \delta_{ij} = \mathbb{I}_{ij} \label{A.31}
$$

This agrees with Equation \ref{A.11} that $\mathbf{A} \cdot \mathbf{A}^{−1} = \mathbb{I}$.

The inverse of rank 2 or 3 matrices is required frequently when determining the eigen-solutions for rigidbody rotation, or coupled oscillator, problems in classical mechanics as described in chapters $11$ and $12$. Therefore it is convenient to list explicitly the inverse matrices for both rank 2 and rank 3 matrices.

#### Inverse for rank 2 matrices:

$$
\mathbf{A}^{−1} = \begin{bmatrix} a & b \\ c & d \end{bmatrix}^{−1} = \frac{1}{ |\mathbf{A}|} \begin{bmatrix} d & −b \\ −c & a \end{bmatrix} = \frac{1}{ (a d − bc)} \begin{bmatrix} d & −b \\ −c & a \end{bmatrix} \label{A.32}
$$

where the determinant of $\mathbf{A}$ is written explicitly in Equation \ref{A.32}.

#### Inverse for rank 3 matrices:

$$
\mathbf{A}^{−1} =\begin{bmatrix} a & b & c \\ d & e & f \\ g & h & i \end{bmatrix}^{−1} = \frac{1}{ |\mathbf{A}|} \begin{bmatrix} A & B & C \\ D & E & F \\ G & H & I \end{bmatrix}^T = \frac{1}{ |\mathbf{A}|} \begin{bmatrix} A & D & G \\ B & E & H \\ C & F & I \end{bmatrix} \\ = \frac{1}{ a A + bB + cC} \begin{bmatrix} A = (ei − fh) & D = − (bi − ch) & G = (bf − ce) \\ B = − (di − fg) & E = (a i − cg) & H = − (a f − cd) \\ C = (dh − eg) & F = − (a h − bg) & I = (a e − bd) \end{bmatrix} \label{A.33}
$$

where the functions $A, B, C, D, E, F, G, H, I$, are equal to rank 2 determinants listed in Equation \ref{A.33}.

### Reduction of a matrix to diagonal form

Solving coupled linear equations can be reduced to diagonalization of a matrix. Consider the matrix $\mathbf{A}$ operating on the vector $\mathbf{X}$ to produce a vector $\mathbf{Y}$, that are expressed as components with respect to the unprimed coordinate frame, i.e.

$$
\mathbf{A} \cdot \mathbf{X} = \mathbf{Y} \label{A.34}
$$

Consider that the unitary real matrix $\mathbf{R}$ with rank $n$, rotates the $n$-dimensional un-primed coordinate frame into the primed coordinate frame such that $\mathbf{A}$, $\mathbf{X}$ and $\mathbf{Y}$ are transformed to $\mathbf{A}^{\prime}$, $\mathbf{X}^{\prime}$ and $\mathbf{Y}^{\prime}$ in the rotated primed coordinate frame. Then

$$
\mathbf{X}^{\prime} = \mathbf{R} \cdot \mathbf{X} \\ \mathbf{Y}^{\prime} = \mathbf{R} \cdot \mathbf{Y} \label{A.35}
$$

With respect to the primed coordinate frame Equation \ref{A.34} becomes

$$
\mathbf{R}\cdot(\mathbf{A} \cdot \mathbf{X}) = \mathbf{R} \cdot \mathbf{Y} \label{A.36}
$$

$$
\mathbf{R} \cdot \mathbf{A} \cdot \mathbf{R}^{−1} \cdot \mathbf{R} \cdot \mathbf{X} = \mathbf{R} \cdot \mathbf{Y} \label{A.37}
$$

$$
\mathbf{R} \cdot \mathbf{A} \cdot \mathbf{R}^{−1} \cdot \mathbf{X}^{\prime} = \mathbf{A}^{\prime} \cdot \mathbf{X}^{\prime} = \mathbf{Y}^{\prime} \label{A.38}
$$

using the fact that the identity matrix $\mathbf{I} = \mathbf{R} \cdot \mathbf{R}^{−1} = \mathbf{R} \cdot \mathbf{R}^T$ since the rotation matrix in $n$ dimensions is orthogonal.

Thus we have that the rotated matrix

$$
\mathbf{A}^{\prime} = \mathbf{R} \cdot \mathbf{A} \cdot \mathbf{R}^T \label{A.39}
$$

Let us assume that this transformed matrix is diagonal, then it can be written as the product of the unit matrix $\mathbb{I}$ and a vector of scalar numbers called the characteristic roots $\lambda$ as

$$
\mathbf{A}^{\prime} = \mathbf{R} \cdot \mathbf{A} \cdot \mathbf{R}^T = \lambda \mathbb{I} \label{A.40}
$$

using the fact that $\mathbf{R}^T= \mathbf{R}^{−1}$ then gives

$$
\mathbf{R}^T \cdot (\lambda \mathbb{I}) = \mathbf{A}^{\prime} \cdot \mathbf{R}^T \label{A.41}
$$

Let both sides of Equation \ref{A.41} act on $\mathbf{X}^{\prime}$ which gives

$$
\lambda \mathbb{I} \cdot \mathbf{X}^{\prime} = \mathbf{A}^{\prime} \cdot\mathbf{X}^{\prime} \label{A.42}
$$

or

$$
[ \lambda \mathbb{I}−\mathbf{A}^{\prime} ] \mathbf{X}^{\prime} = 0 \label{A.43}
$$

This represents a set of $n$ homogeneous linear algebraic equations in $n$ unknowns $\mathbf{X}^{\prime}$ where $\lambda$ is a set of characteristic roots, (eigenvalues) with corresponding eigenfunctions $\mathbf{X}^{\prime}$. Ignoring the trivial case of $\mathbf{X}^{\prime}$ being zero, then \ref{A.43} requires that the *secular determinant* of the bracket be zero, that is

$$
|\lambda \mathbb{I}−\mathbf{A}^{\prime}| = 0 \label{A.44}
$$

The determinant can be expanded and factored into the form

$$
(\lambda − \lambda_1) (\lambda − \lambda_2) (\lambda − \lambda_3)\dots .(\lambda − \lambda_n)=0 \label{A.45}
$$

where the $n$ eigenvalues are $\lambda = \lambda_1, \lambda_2, \dots \lambda_n$ of the matrix $\mathbf{A}^{\prime}$.

The eigenvectors $\mathbf{X}^{\prime}$ corresponding to each eigenvalue are determined by substituting a given eigenvalue $\lambda_i$ into the relation

$$
\mathbf{X}^{\prime T} \cdot \mathbf{A}^{\prime} \cdot \mathbf{X}^{\prime} = [\lambda_i \delta_{ij} ] \label{A.46}
$$

If all the eigenvalues are distinct, i.e. different, then this set of $n$ equations completely determines the ratio of the components of each eigenvector along the axes of the coordinate frame. However, when two or more eigenvalues are identical, then the reduction to a true diagonal form is not possible and one has the freedom to select an appropriate eigenvector that is orthogonal to the remaining axes.

In summary, the matrix can only be fully diagonalized if

(a) all the eigenvalues are distinct,

(b) the real matrix is symmetric,

(c) it is unitary.

A frequent application of matrices in classical mechanics is for solving a system of homogeneous linear equations of the form

$$
\begin{matrix} A_{11}x_1 & +A_{12}x_2 & \dots \dots & +A_{1n}x_n & = & 0 \\ A_{11}x_1 & +A_{12}x_2 & \dots \dots & +A_{1n}x_n & = & 0 \\ \dots .. & \dots \dots & \dots .. & \dots .. & = & \dots . \\ A_{n1}x_1 & +A_{n2}x_2 & \dots .. & +A_{nn}x_n & = & 0 \end{matrix} \label{A.47}
$$

Making the following definitions

$$
\mathbf{A} = \begin{pmatrix} A_{11} & A_{12} & \dots & A_{1n} \\ A_{21} & A_{22} & \dots & A_{2n} \\ \dots & \dots & \dots & \dots \\ A_{n1} & A_{n2} & \dots & A_{nn} \end{pmatrix} \label{A.48}
$$

$$
\mathbf{X} = \begin{pmatrix} x_1 \\ x_2 \\ \dots \\ x_n \end{pmatrix} \label{A.49}
$$

Then the set of linear equations can be written in a compact form using the matrices

$$
\mathbf{A} \cdot \mathbf{X} =0 \label{A.50}
$$

which can be solved using Equation \ref{A.43}. Ensure that you are able to diagonalize a matrices with rank 2 and 3. You can use Mathematica, Maple, MatLab, or other such mathematical computer programs to diagonalize larger matrices.

Example 19.1: Eigenvalues and eigenvectors of a real symmetric matrix

Consider the matrix

$$
\mathbf{A} = \begin{pmatrix} 0 & 1 & 0 \\ 1 & 0 & 0 \\ 0 & 0 & 0 \end{pmatrix}\nonumber
$$

The secular determinant is given by \ref{A.42}

$$
\begin{vmatrix} −\lambda & 1 & 0 \\ 1 & −\lambda & 0 \\ 0 & 0 & −\lambda \end{vmatrix} = 0 \nonumber
$$

This expands to

$$
−\lambda (\lambda + 1)(\lambda − 1) = 0 \nonumber
$$

Thus the three eigen values are $\lambda = −1, 0, 1$.

To find each eigenvectors we substitute the corresponding eigenvalue into Equation \ref{A.48}.

$$
\begin{pmatrix} −\lambda & 1 & 0 \\ 1 & −\lambda & 0 \\ 0 & 0 & −\lambda \end{pmatrix} \begin{pmatrix} x \\ y \\ z \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \\ 0 \end{pmatrix} \nonumber
$$

The eigenvalue $\lambda = −1$ yields $x + y = 0$ and $z = 0$. Thus the eigen vector is $r_1 = ( \frac{1}{\sqrt{2}}, \frac{-1}{\sqrt{2}}, 0)$. The eigenvalue $\lambda = 0$ yields $x = 0$ and $y = 0$. Thus the eigen vector is $r_2 = (0, 0, 1)$. The eigenvalue $\lambda = 1$ yields $−x + y = 0$ and $z = 0$. Thus the eigen vector is $r_3 = ( \frac{1}{\sqrt{2}}, \frac{1}{\sqrt{2}}, 0)$. The orthogonality of these three eigen vectors, which correspond to three distinct eigenvalues, can be verified.

## 19.3: Appendix - Vector algebra

### Linear operations

The important force fields in classical mechanics, namely, gravitation, electric, and magnetic, are vector fields that have a position-dependent magnitude and direction. Thus, it is useful to summarize the algebra of vector fields.

A vector $\mathbf{a}$ has both a magnitude $|a|$ and a direction defined by the *unit vector* $\mathbf{\hat{e}}_a$, that is, the vector can be written as a bold character $\mathbf{a}$ where

$$
\mathbf{a} =a \cdot \mathbf{\hat{e}}_a \label{B.1}
$$

where by convention the implied modulus sign is omitted. The hat symbol on the vector $\mathbf{\hat{e}}_a$ designates that this is a unit vector with modulus $|\mathbf{\hat{e}}_a| = 1$.

Vector force fields are assumed to be linear, and consequently they obey the principle of superposition, are commutative, associative, and distributive as illustrated below for three vectors $\mathbf{a}, \mathbf{b}, \mathbf{c}$ plus a scalar multiplier $\gamma$.

$$
\begin{align} \mathbf{a} \pm \mathbf{b} &= \pm \mathbf{b} + \mathbf{a} \label{B.2} \\[4pt] \mathbf{a}+ (\mathbf{b} + \mathbf{c}) &= (\mathbf{a} + \mathbf{b}) +\mathbf{c} \\[4pt] \gamma (\mathbf{a} + \mathbf{b}) &= \gamma \mathbf{a}+\gamma \mathbf{b} \end{align}
$$

The manipulation of vectors is greatly facilitated by use of components along an orthogonal coordinate system defined by three orthogonal unit vectors $(\mathbf{\hat{e}}_1,\mathbf{\hat{e}}_2,\mathbf{\hat{e}}_3)$. For example the cartesian coordinate system is defined by three unit vectors which, by convention, are called $(\mathbf{\hat{i}},\mathbf{\hat{j}}, \mathbf{\hat{k}})$.

### Scalar product

Multiplication of two vectors can produce a 9−component tensor that can be represented by a $3 \times 3$ matrix as discussed in appendix $19.5$. There are two special cases for vector multiplication that are important for vector algebra; the first is the scalar product, and the second is the vector product.

The *scalar product* of two vectors is defined to be

$$
\mathbf{a} \cdot \mathbf{b} = |a| |b| \cos \theta \label{B.3}
$$

where $\theta$ is the angle between the two vectors. It is a scalar and thus is independent of the orientation of the coordinate axis system. Note that the scalar product commutes, is distributive, and associative with a scalar multiplier, that is

$$
\mathbf{a} \cdot\mathbf{ b} = \mathbf{b} \cdot \mathbf{a} \label{B.4} \\ \mathbf{a}\cdot (\mathbf{b} + \mathbf{c}) = \mathbf{a} \cdot \mathbf{b} + \mathbf{a} \cdot \mathbf{c} \\ (\lambda \mathbf{a})\cdot \mathbf{b} = \lambda (\mathbf{b} \cdot \mathbf{a})
$$

Note that $\mathbf{a} \cdot \mathbf{a} = |a|^2$ and if $\mathbf{a}$ and $\mathbf{b}$ are perpendicular then $\cos \theta = 0$ and thus $\mathbf{a} \cdot \mathbf{b} =0$

If the three unit vectors $(\mathbf{\hat{e}}_1,\mathbf{\hat{e}}_2,\mathbf{\hat{e}}_3)$ form an orthonormal basis, that is, they are orthogonal unit vectors, then from equations \ref{B.3} and \ref{B.4}

$$
\mathbf{\hat{e}}_i \cdot \mathbf{\hat{e}}_k = \delta_{ik} \label{B.5}
$$

If $\mathbf{\hat{a}}$ is the unit vector for the vector $\mathbf{a}$ then the scalar product of a vector $\mathbf{a}$ with one of these unit vectors $\mathbf{\hat{e}}_n$ gives the cosine of the angle between the vector $\mathbf{a}$ and $\mathbf{\hat{e}}_n$, that is

$$
\mathbf{a} \cdot \mathbf{\hat{e}}_1 = |a|(\mathbf{\hat{a}} \cdot \mathbf{\hat{e}}_1) = |a| \cos \alpha \label{B.6} \\ \mathbf{a} \cdot \mathbf{\hat{e}}_2 = |a|(\mathbf{\hat{a}} \cdot \mathbf{\hat{e}}_2) = |a| \cos \beta \\ \mathbf{a} \cdot \mathbf{\hat{e}}_3 = |a|(\mathbf{\hat{a}} \cdot \mathbf{\hat{e}}_3) = |a| \cos \gamma
$$

where the cosines are called the direction cosines since they define the direction of the vector a with respect to each orthogonal basis unit vector. Moreover, $\mathbf{a} \cdot \mathbf{\hat{e}}_1 = |a| \mathbf{\hat{a}} \cdot \mathbf{\hat{e}}_1 = |a| \cos \alpha$ is the component of $\mathbf{a}$ along the $\mathbf{\hat{e}}_1$ axis. Thus the three components of the vector $\mathbf{a}$ is fully defined by the magnitude $|a|$ and the direction cosines, corresponding to the angles $\alpha, \beta, \gamma$. That is,

$$
a_1 = |a|(\mathbf{\hat{a}} \cdot \mathbf{\hat{e}}_1) = |a| \cos \alpha \label{B.7} \\ a_2 = |a|(\mathbf{\hat{a}} \cdot \mathbf{\hat{e}}_2) = |a| \cos \beta \\ a_3 = |a|(\mathbf{\hat{a}} \cdot \mathbf{\hat{e}}_3) = |a| \cos \gamma
$$

If the three unit vectors $(\mathbf{\hat{e}}_1,\mathbf{\hat{e}}_2,\mathbf{\hat{e}}_3)$ form an orthonormal basis then the vector is fully defined by

$$
\mathbf{a} = a_1\mathbf{\hat{e}}_1 + a_2\mathbf{\hat{e}}_2 + a_3\mathbf{\hat{e}}_3 \label{B.8}
$$

Consider two vectors

$$
\mathbf{a} = a_1\mathbf{\hat{e}}_1 + a_2\mathbf{\hat{e}}_2 + a_3\mathbf{\hat{e}}_3 \nonumber
$$

$$
\mathbf{b} = b_1\mathbf{\hat{e}}_1 + b_2\mathbf{\hat{e}}_2 + b_3\mathbf{\hat{e}}_3 \nonumber
$$

Then using \ref{B.5}

$$
\mathbf{a} \cdot \mathbf{b} =a_1b_1 + a_2b_2 + a_3b_3 = |a| |b| \cos \theta \label{B.9}
$$

where $\theta$ is the angle between the two vectors. In particular, since the direction cosine $\cos \alpha_a = \frac{ a_1}{ |a|}$, then Equation \ref{B.9} gives

$$
\cos \theta = \cos \alpha_a \cos \alpha_b + \cos \beta_a \cos \beta_b + \cos \gamma_a \cos \gamma_b \label{B.10}
$$

Note that when $\theta = 0$ then \ref{B.10} gives

$$
\cos^2 \alpha + \cos^2 \beta + \cos^2 \gamma = 1 \label{B.11}
$$

### Vector product

The vector product of two vectors is defined to be

$$
\mathbf{c} = \mathbf{a} \times \mathbf{b }= |a| |b| \sin \theta \mathbf{\hat{n}} \label{B.12}
$$

where $\theta$ is the angle between the vectors and $\mathbf{\hat{n}}$ is a unit vector perpendicular to the plane defined by $\mathbf{a}$ and $\mathbf{b}$ such that the unit vectors $\left( \mathbf{\hat{a}}, \mathbf{\hat{b}}, \mathbf{\hat{n}} \right)$ obey a right-handed screw rule. The vector product acts like a pseudovector which comprises a normal vector multiplied by a sign factor that depends on the handedness of the system as described in appendix $19.4.3$.

The components of $\mathbf{c}$ are defined by the relation

$$
c_i \equiv \sum_{jk} \varepsilon_{ijk}a_j b_k \label{B.13}
$$

where the (Levi-Civita) permutation symbol $\varepsilon_{ijk}$ has the following properties

$$
\begin{align} \varepsilon_{ijk} = 0 && \text{ if an index is equal to any another index} \nonumber\\ \varepsilon_{ijk} = +1 && \text{ if } i,j,k, \text{ form an even permutation of } 1, 2, 3 \label{B.14}\\ \varepsilon_{ijk} = −1 && \text{ if } i,j,k, \text{ form an odd permutation of }1, 2, 3 \nonumber \end{align}
$$

For example, if the three unit vectors $(\mathbf{\hat{e}}_1, \mathbf{\hat{e}}_2, \mathbf{\hat{e}}_3)$ form an orthonormal basis, then $\mathbf{\hat{e}}_i \equiv \sum_{jk} \varepsilon_{ijk}\mathbf{\hat{e}}_j\mathbf{\hat{e}}_k$, i.e.

$$
\begin{align} \mathbf{\hat{e}}_1 \times \mathbf{\hat{e}}_2 = \mathbf{\hat{e}}_3 && \mathbf{\hat{e}}_2 \times \mathbf{\hat{e}}_3 = \mathbf{\hat{e}}_1 && \mathbf{\hat{e}}_3 \times \mathbf{\hat{e}}_1 = \mathbf{\hat{e}}_2 \label{B.15}\\ \mathbf{\hat{e}}_2 \times \mathbf{\hat{e}}_1 = −\mathbf{\hat{e}}_3 && \mathbf{\hat{e}}_3 \times \mathbf{\hat{e}}_2 = −\mathbf{\hat{e}}_1 && \mathbf{\hat{e}}_1 \times \mathbf{\hat{e}}_3 = −\mathbf{\hat{e}}_2 \label{B.16}\\ \mathbf{\hat{e}}_1 \times \mathbf{\hat{e}}_1 = \mathbf{0} && \mathbf{\hat{e}}_2 \times \mathbf{\hat{e}}_2 = \mathbf{0} && \mathbf{\hat{e}}_3 \times \mathbf{\hat{e}}_0 = \mathbf{0} \label{B.17}\end{align}
$$

The vector product anticommutes in that

$$
\mathbf{a} \times \mathbf{b} = −\mathbf{b} \times \mathbf{a} \label{B.18}
$$

However, it is distributive and associative with a scalar multiplier

$$
\mathbf{a}\times (\mathbf{b} + \mathbf{c}) = \mathbf{a} \times \mathbf{b} + \mathbf{a} \times \mathbf{c} \label{B.19}
$$

$$
(\lambda \mathbf{a}) \times \mathbf{b} = \lambda (\mathbf{a} \times \mathbf{b}) \label{B.20}
$$

Note that when $\sin \theta = 0$ then $\mathbf{a} \times \mathbf{b} = 0$ and in particular, $\mathbf{a} \times \mathbf{a} = 0$.

Consider two vectors

$$
\mathbf{a} = a_1\mathbf{\hat{e}}_1 + a_2\mathbf{\hat{e}}_2 + a_3\mathbf{\hat{e}}_3 \nonumber
$$

$$
\mathbf{b} = b_1\mathbf{\hat{e}}_1 + b_2\mathbf{\hat{e}}_2 + b_3\mathbf{\hat{e}}_3 \nonumber
$$

Then using equations \ref{B.12} and \ref{B.15} − \ref{B.17}

$$
\mathbf{a} \times \mathbf{b} = |a| |b| \sin \theta = \begin{vmatrix} \mathbf{\hat{e}}_1 & \mathbf{\hat{e}}_2 & \mathbf{\hat{e}}_3 \\ a_1 & a_2 & a_3 \\ b_1 & b_2 & b_3 \end{vmatrix} = \mathbf{\hat{e}}_1 (a_2b_3 − a_3b_2) + \mathbf{\hat{e}}_2 (a_3b_1 − a_1b_3) + \mathbf{\hat{e}}_3 (a_1b_2 − a_2b_1) \nonumber
$$

where $\theta$ is the angle between the two vectors and the determinant is evaluated for the top row. Examples of vector products are torque $\mathbf{N} = \mathbf{r} \times \mathbf{F}$, angular momentum $\mathbf{L} = \mathbf{r} \times \mathbf{p}$, and the magnetic force $\mathbf{F}_B = q\mathbf{v} \times \mathbf{B}$.

### Triple products

The following scalar and vector triple products can be formed from the product of three vectors and are used frequently.

#### Scalar triple products

There are several permutations of scalar triple products of three vectors $[\mathbf{a},\mathbf{b}, \mathbf{c}]$ that are identical.

$$
\mathbf{a}\cdot (\mathbf{b} \times \mathbf{c}) = \mathbf{c}\cdot (\mathbf{a} \times \mathbf{b}) = \mathbf{b}\cdot (\mathbf{c} \times \mathbf{a})=(\mathbf{a} \times \mathbf{b}) \cdot \mathbf{c} = −\mathbf{a}\cdot (\mathbf{c} \times \mathbf{b}) \label{B.21}
$$

That is, the scalar product is invariant to cyclic permutations of the three vectors but changes sign for interchange of two vectors. The scalar product is unchanged by swapping the scalar $(dot)$ and vector $(cross)$.

Because of the symmetry the scalar triple product can be denoted as $[ \mathbf{ a}, \mathbf{b}, \mathbf{c}]$ and

$$
\begin{align} [\mathbf{a}, \mathbf{b}, \mathbf{c}] > 0 && \text{ if } [\mathbf{a}, \mathbf{b}, \mathbf{c}] \text{ is right-handed} \nonumber\\ [\mathbf{a}, \mathbf{b}, \mathbf{c}]=0 && \text{ if } [\mathbf{a}, \mathbf{b}, \mathbf{c}] \text{ is coplanar} \label{B.22} \\ [\mathbf{a}, \mathbf{b}, \mathbf{c}] < 0 && \text{ if } [\mathbf{a}, \mathbf{b}, \mathbf{c}] \text{ is left-handed} \nonumber\end{align}
$$

The scalar triple product can be written in terms of the components using a determinant

$$
[\mathbf{a}, \mathbf{b}, \mathbf{c}] = \begin{vmatrix} a_1 & a_2 & a_3 \\ b_1 & b_2 & b_3 \\ c_1 & c_2 & c_3 \end{vmatrix} \label{B.23}
$$

#### Vector triple product

The vector triple product $\mathbf{a}\times (\mathbf{b} \times \mathbf{c})$ is a vector. Since $(\mathbf{b} \times \mathbf{c})$ is perpendicular to the plane of $\mathbf{b}, \mathbf{c}$, then $\mathbf{a}\times (\mathbf{b} \times \mathbf{c})$ must lie in the plane containing $\mathbf{b}, \mathbf{c}$. Therefore the triple product can be expanded in terms of $\mathbf{b}, \mathbf{c}$, as given by the following identity

$$
\mathbf{a} \times (\mathbf{b} \times \mathbf{c})=(\mathbf{a} \cdot \mathbf{c}) \mathbf{b} − (\mathbf{a} \cdot \mathbf{ b}) \mathbf{c} \label{B.24}
$$

### Problems

1. Partition the following exercises among your collaborators. Once you have completed your problem, check with a classmate before writing it on the board. After you have verified that you have found the correct solution, write your answer in the space provided on the board, taking care to include the steps that you used to arrive at your solution. The following information is needed.

| $\mathbf{a} = 3\mathbf{i} + 2\mathbf{j} − 9\mathbf{k}$ | $\mathbf{b} = −2\mathbf{i} + 3\mathbf{k}$ | $\mathbf{c} = −2\mathbf{i} + \mathbf{j} − 6\mathbf{k}$ | $\mathbf{d} = \mathbf{i} + 9\mathbf{j} + 4\mathbf{k}$ |
| --- | --- | --- | --- |
| $\mathbf{E} = \begin{pmatrix} 2 & 7 & −4 \\ 3 & 1 & −2 \\ −2 & 0 & 5 \end{pmatrix}$ | $\mathbf{F} = \begin{pmatrix} 3 & 4 \\ 5 & 6 \end{pmatrix}$ | $\mathbf{G} = \begin{pmatrix} 2 & −4 \\ 7 & 1 \\ −1 & 1 \end{pmatrix}$ | $\mathbf{H} = \begin{pmatrix} −8 & −1 & −3 \\ −4 & 2 & −2 \\ −1 & 0 & 0 \end{pmatrix}$ |

Calculate each of the following

| 1. $\|\mathbf{a} − (\mathbf{b} + \mathbf{3c})\|$ | 7. $(\mathbf{EH})^T$ |
| --- | --- |
| 2. Component of $\mathbf{c}$ along $\mathbf{a}$ | 8. $\|\mathbf{HE}\|$ |
| 3. Angle between $\mathbf{c}$ and $\mathbf{d}$ | 9. $\mathbf{EHG}$ |
| 4. $(\mathbf{b} \times \mathbf{d}) \cdot \mathbf{a}$ | 10. $\mathbf{EG} − \mathbf{HG}$ |
| 5. $(\mathbf{b} \times \mathbf{d}) \times \mathbf{a}$ | 11. $\mathbf{EH} − \mathbf{H}^T \mathbf{E}^T$ |
| 6. $\mathbf{b}\times (\mathbf{d} \times \mathbf{a})$ | 12. $\mathbf{F}^{−1}$ |

2. For what values of $a$ are the vectors $\mathbf{A} = 2a\hat{i} − 2\hat{j} + a\hat{k}$ and $\mathbf{B} = a\hat{i} + 2a\hat{j}+ 2\hat{k}$ perpendicular?

3. Show that the triple scalar product $(A \times B) \cdot C$ can be written as

$$
(\mathbf{A} \times \mathbf{B}) \cdot \mathbf{C} = \begin{vmatrix} A_1 & A_2 & A_3 \\ B_1 & B_2 & B_3 \\ C_1 & C_2 & C_3 \end{vmatrix} \nonumber
$$

Show also that the product is unaffected by interchange of the scalar and vector product operations or by change in the order of $A, B, C$ as long as they are in cyclic order, that is

$$
(\mathbf{A} \times \mathbf{B}) \cdot \mathbf{C} = \mathbf{A} \cdot (\mathbf{B} \times \mathbf{C}) = \mathbf{B} \cdot (\mathbf{C} \times \mathbf{A}) =(\mathbf{C} \times \mathbf{A}) \cdot \mathbf{ B} \nonumber
$$

Therefore we may use the notation $ABC$ to denote the triple scalar product. Finally give a geometric interpretation of $ABC$ by computing the volume of the parallelepiped defined by the three vectors $\mathbf{A}, \mathbf{B}, \mathbf{C}$.

## 19.4: Appendix - Orthogonal Coordinate Systems

The methods of vector analysis provide a convenient representation of physical laws. However, the manipulation of scalar and vector fields is greatly facilitated by use of components with respect to an orthogonal coordinate system such as the following.

### Cartesian coordinates $(x, y, z)$

Cartesian coordinates (rectangular) provide the simplest orthogonal rectangular coordinate system. The unit vectors specifying the direction along the three orthogonal axes are taken to be $(\mathbf{\hat{i}},\mathbf{\hat{j}}, \mathbf{\hat{k}})$. In cartesian coordinates scalar and vector functions are written as

$$
\phi = \phi (x, y, z) \label{C.1}
$$

$$
\mathbf{r} = x\mathbf{\hat{i}}+y\mathbf{\hat{j}}+z\mathbf{\hat{k}} \label{C.2}
$$

Calculation of the time derivatives of the position vector is especially simple using cartesian coordinates because the unit vectors $(\mathbf{\hat{i}},\mathbf{\hat{j}}, \mathbf{\hat{k}})$ are constant and independent in time. That is;

$$
\frac{d\mathbf{\hat{i}}}{ dt} = \frac{d\mathbf{\hat{j}}}{ dt} = \frac{d\mathbf{\hat{k}}}{ dt} = 0 \nonumber
$$

Since the time derivatives of the unit vectors are all zero then the velocity $\mathbf{\dot{r}} = \frac{d\mathbf{r}}{ dt}$ reduces to the partial time derivatives of $x$, $y$, and $z$. That is,

$$
\mathbf{\dot{r}} = \dot{x} \mathbf{\hat{i}} + \dot{y} \mathbf{\hat{j}} + \dot{z} \mathbf{\hat{k}} \label{C.3}
$$

Similarly the acceleration is given by

$$
\mathbf{\ddot{r}} = \ddot{x} \mathbf{\hat{i}} + \ddot{y} \mathbf{\hat{j}} + \ddot{z} \mathbf{\hat{k}} \label{C.4}
$$

### Curvilinear coordinate systems

There are many examples in physics where the symmetry of the problem makes it more convenient to solve motion at a point $P(x, y, z)$ using non-cartesian curvilinear coordinate systems. For example, problems having spherical symmetry are most conveniently handled using a **spherical coordinate system** $(r, \theta , \phi )$ with the origin at the center of spherical symmetry. Such problems occur frequently in electrostatics and gravitation; e.g. solutions of the atom, or planetary systems. Note that a cartesian coordinate system still is required to define the origin plus the polar and azimuthal angles $\theta , \phi$. Using spherical coordinates for a spherically symmetry system allows the problem to be factored into a cyclic angular part, the solution which involves spherical harmonics that are common to all such spherically-symmetric problems, plus a one-dimensional radial part that contains the specifics of the particular spherically-symmetric potential. Similarly, for problems involving cylindrical symmetry, it is much more convenient to use a **cylindrical coordinate system** $(\rho , \phi , z)$. Again it is necessary to use a cartesian coordinate system to define the origin and angle $\phi$. Motion in a plane can be handled using two dimensional **polar coordinates.**

Curvilinear coordinate systems introduce a complication in that the *unit vectors are time dependent* in contrast to cartesian coordinate system where the unit vectors $(\mathbf{\hat{i}},\mathbf{\hat{j}}, \mathbf{\hat{k}})$ are independent and constant in time. The introduction of this time dependence warrants further discussion.

Each of the three axes $q_i$ in curvilinear coordinate systems can be expressed in cartesian coordinates $(x, y, z)$ as surfaces of constant $q_i$ given by the function

$$
q_i = f_i (x, y, z) \label{C.5}
$$

where $i = 1$, $2$, or $3$. An element of length $ds_i$ perpendicular to the surface $q_i$ is the distance between the surfaces $q_i$ and $q_i + dq_i$ which can be expressed as

$$
ds_i = h_idq_i \label{C.6}
$$

where $h_i$ is a function of $(q_1, q_2, q_3)$. In cartesian coordinates $h_1$, $h_2$, and $h_3$ are all unity. The unit-length vectors $\hat{q}_1$, $\hat{q}_2$, $\hat{q}_3$, are perpendicular to the respective $q_1$, $q_2$, $q_3$ surfaces, and are oriented to have increasing indices such that $\mathbf{\hat{q}}_1 \times \mathbf{\hat{q}}_2 = \mathbf{\hat{q}}_3$. The correspondence of the curvilinear coordinates, unit vectors, and transform coefficients to cartesian, polar, cylindrical and spherical coordinates is given in Table 19.1.

| Curvilinear | $q_1$ | $q_2$ | $q_3$ | $\mathbf{\hat{q}}_1$ | $\mathbf{\hat{q}}_2$ | $\mathbf{\hat{q}}_3$ | $h_1$ | $h_2$ | $h_3$ |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Cartesian | $x$ | $y$ | $z$ | $\hat{i}$ | $\hat{j}$ | $\mathbf{\hat{k}}$ | 1 | 1 | 1 |
| Polar | $r$ | $\theta$ |  | $\mathbf{\hat{r}}$ | $\boldsymbol{\hat{\theta}}$ |  | 1 | $r$ |  |
| Cylindrical | $\rho$ | $\varphi$ | $z$ | $\boldsymbol{\hat{\rho}}$ | $\boldsymbol{\hat{\varphi}}$ | $\mathbf{\hat{z}}$ | 1 | $\rho$ | 1 |
| Spherical | $r$ | $\theta$ | $\varphi$ | $\mathbf{\hat{r}}$ | $\boldsymbol{\hat{\theta}}$ | $\boldsymbol{\hat{\varphi}}$ | 1 | $r$ | $r\sin\theta$ |

The differential distance and volume elements are given by

$$
d\mathbf{s} = ds_1\mathbf{\hat{q}}_1 + ds_2\mathbf{\hat{q}}_2 + ds_3\mathbf{\hat{q}}_3 = h_1dq_1\mathbf{\hat{q}}_1 + h_2dq_2\mathbf{\hat{q}}_2 + h_3dq_3\mathbf{\hat{q}}_3 \label{C.7}
$$

$$
d \tau = ds_1ds_2ds_3 = h_1h_2h_3(dq_1dq_2dq_3) \label{C.8}
$$

These are evaluated below for polar, cylindrical, and spherical coordinates.

#### Two-dimensional polar coordinates $(r, \theta )$

The complication and implications of time-dependent unit vectors are best illustrated by considering twodimensional polar coordinates which is the simplest curvilinear coordinate system. Polar coordinates are a special case of cylindrical coordinates, when $z$ is held fixed, or a special case of spherical coordinate system, when $\phi$ is held fixed.

Consider the motion of a point $P$ as it moves along a curve $\mathbf{s}(t)$ such that in the time interval $dt$ it moves from $P^{(1)}$ to $P^{(2)}$ as shown in Figure 19.1. The two-dimensional polar coordinates have *unit vectors* $\mathbf{\hat{r}}, \boldsymbol{\hat{\theta}}$, which are orthogonal and change from $\mathbf{\hat{r}}_1, \boldsymbol{\hat{\theta}}_1$, to $\mathbf{\hat{r}}_2, \boldsymbol{\hat{\theta}}_2$, in the time $dt$. Note that for these polar coordinates the angle unit vector $\boldsymbol{\hat{\theta}}$ is taken to be *tangential* to the rotation since this is the direction of motion of a point on the circumference at radius $r$.

The net changes shown in figure of Table 19.2 are

$$
d\mathbf{\hat{r}} = \mathbf{\hat{r}}_2 − \mathbf{\hat{r}}_1 = d\mathbf{\hat{r}} = |\mathbf{\hat{r}}| d\theta \boldsymbol{\hat{\theta}} =d\theta \boldsymbol{\hat{\theta}} \label{C.9}
$$

since the unit vector $\mathbf{\hat{r}}$ is a constant with $|\mathbf{\hat{r}}| = 1$. Note that the infinitessimal $d\mathbf{\hat{r}}$ is perpendicular to the unit vector $\mathbf{\hat{r}}$, that is, $d\mathbf{\hat{r}}$ points in the tangential direction $\boldsymbol{\hat{\theta}}$.

Similarly, the infinitessimal

$$
d\boldsymbol{\hat{\theta}} = \boldsymbol{\hat{\theta}}_2 − \boldsymbol{\hat{\theta}}_1 = d\boldsymbol{\hat{\theta}} = −d\theta \mathbf{\hat{r}} \label{C.10}
$$

which is perpendicular to the tangential $\boldsymbol{\hat{\theta}}$ unit vector and therefore points in the direction $−\mathbf{\hat{r}}$. The minus sign causes $−d\theta \mathbf{\hat{r}}$ to be directed in the opposite direction to $\mathbf{\hat{r}}$.

The net distance element $d\mathbf{s}$ is given by

$$
d\mathbf{s} =dr\mathbf{\hat{r}} + rd\mathbf{\hat{r}} =dr\mathbf{\hat{r}} + rd\theta \boldsymbol{\hat{\theta}} \label{C.11}
$$

This agrees with the prediction obtained using Table 19.1.

The time derivatives of the unit vectors are given by equations \ref{C.9} and \ref{C.10} to be,

$$
\frac{d\mathbf{\hat{r}}}{ dt} = \frac{d\theta}{ dt} \boldsymbol{\hat{\theta}} \label{C.12}
$$

$$
\frac{d\boldsymbol{\hat{\theta}}}{ dt} = −\frac{d\theta}{ dt} \mathbf{\hat{r}} \label{C.13}
$$

Note that *the time derivatives of unit vectors are perpendicular to the corresponding unit vector, and the unit vectors are coupled.*

Consider that the velocity $\mathbf{v}$ is expressed as

$$
\mathbf{v} = \frac{d\mathbf{r}}{ dt} = \frac{d}{ dt}(r\mathbf{\hat{r}}) = \frac{dr}{ dt}\mathbf{\hat{r}} + r \frac{d\mathbf{\hat{r}} }{dt} = \dot{r}\mathbf{\hat{r}} + r \dot{\theta} \boldsymbol{\hat{\theta}} \label{C.14}
$$

The velocity is resolved into a radial component $\dot{r}$ and an angular, transverse, component $r \dot{\theta}$.

Similarly the acceleration is given by

$$
\mathbf{a} = \frac{d\mathbf{v}}{ dt} = \frac{d\dot{r} }{dt} \mathbf{\hat{r}}+\dot{r} \frac{d\mathbf{\hat{r}}}{ dt} + \frac{dr}{ dt} \dot{\theta} \boldsymbol{\hat{\theta}}+ r \frac{d\dot{\theta} }{dt} \boldsymbol{\hat{\theta}}+r \dot{\theta} \frac{d\boldsymbol{\hat{\theta}}}{ dt} \\ = \left( \ddot{r}− r \dot{\theta}^2\right) \mathbf{\hat{r}} + \left( \ddot{r}\theta + 2\dot{r} \dot{\theta} \right) \boldsymbol{\hat{\theta}} \label{C.15}
$$

where the $r \dot{\theta}^2 \mathbf{\hat{r}}$ term is the effective centripetal acceleration while the $2\dot{r} \dot{\theta} \boldsymbol{\hat{\theta}}$ term is called the Coriolis term. For the case when $\dot{r} = \ddot{r} = 0$, then the first bracket in \ref{C.15} is the centripetal acceleration while the second bracket is the tangential acceleration.

This discussion has shown that in contrast to the time independence of the cartesian unit basis vectors, *the unit basis vectors for curvilinear coordinates are time dependent which leads to components of the velocity and acceleration involving coupled coordinates.*

| Coordinates | $r, \theta$ |
| --- | --- |
| Distance element | $d\mathbf{s} = dr\mathbf{\hat{r}} + rd\theta \boldsymbol{\hat{\theta}}$ |
| Area element | $da = r dr d\theta$ |
| Unit vectors | $\mathbf{\hat{r}} = \hat{i} \cos \theta + \hat{j} \sin \theta$
$\boldsymbol{\hat{\theta}} = -\hat{i} \sin \theta + \hat{j} \cos \theta$ |
| Time derivatives of unit vectors | $\frac{d\mathbf{\hat{r}}}{dt} = \dot{\theta} \boldsymbol{\hat{\theta}}$
$\frac{d\boldsymbol{\hat{\theta}}}{dt} = -\dot{\theta} \mathbf{\hat{r}}$ |
| Velocity | $\mathbf{v} = \dot{r}\mathbf{\hat{r}} + r\dot{\theta} \boldsymbol{\hat{\theta}}$ |
| Kinetic energy | $\frac{m}{2} \left(\dot{r}^2 + r^2 \dot{\theta}^2\right)$ |
| Acceleration | $\mathbf{a} = \left(\ddot{r} - r \dot{\theta}^2\right)\mathbf{\hat{r}} + \left(r\ddot{\theta} + 2\dot{r}\dot{\theta}\right) \boldsymbol{\hat{\theta}}$ |

:::{figure} ../images/lt-23015-c1.png
:alt: c1.PNG

$1$: Diagram for Table $2$.
:::

#### Cylindrical Coordinates $(\rho , \phi , z)$

The three-dimensional cylindrical coordinates $(\rho , \phi , z)$ are obtained by adding the motion along the symmetry axis $\mathbf{\hat{z}}$ to the case for polar coordinates. The unit basis vectors are shown in Table 19.3 where the angular unit vector $\boldsymbol{\hat{\phi}}$ is taken to be tangential corresponding to the direction a point on the circumference would move. The distance and volume elements, the cartesian coordinate components of the cylindrical unit basis vectors, and the unit vector time derivatives are shown in Table 19.3. The time dependence of the unit vectors is used to derive the acceleration. As for the two-dimensional polar coordinates, the $\boldsymbol{\hat{\rho}}$ and $\boldsymbol{\hat{\theta}}$ direction components of the acceleration for cylindrical coordinates are coupled functions of $\rho$, $\dot{\rho}$, $\ddot{\rho}$, $\dot{\phi}$, and $\ddot{\phi}$.

| Coordinates | $\rho, \phi, \theta$ |
| --- | --- |
| Distance element | $d\mathbf{s} = d \rho \boldsymbol{\hat{\rho}} + \rho d\phi \boldsymbol{\hat{\phi}} + dz\mathbf{\hat{z}}$ |
| Volume element | $dv = \rho d\rho d\phi dz$ |
| Unit vectors | $\boldsymbol{\hat{\rho}} = \hat{i} \cos \phi + \hat{j} \sin \phi$
$\boldsymbol{\hat{\phi}} = -\hat{i} \sin \phi + \hat{j} \cos \phi$
$\mathbf{\hat{z}} = \mathbf{\hat{k}}$ |
| Time derivatives of unit vectors | $\frac{d\boldsymbol{\hat{\rho}}}{dt} = \dot{\phi} \boldsymbol{\hat{\phi}}$
$\frac{d\boldsymbol{\hat{\phi}}}{dt} = -\dot{\phi} \boldsymbol{\hat{\rho}}$
$\frac{d\mathbf{\hat{z}}}{dt} = 0$ |
| Velocity | $\mathbf{v} = \dot{\rho} \boldsymbol{\hat{\rho}} + \rho \dot{\phi} \boldsymbol{\hat{\phi}} + \dot{z} \mathbf{\hat{z}}$ |
| Kinetic energy | $\frac{m}{2} \left(\dot{\rho}^2 + \rho^2 \dot{\phi}^2 + \dot{z}^2 \right)$ |
| Acceleration | $\mathbf{a} = \left(\ddot{\rho} - \rho \dot{\phi}^2\right)\boldsymbol{\hat{\rho}} + \left(\rho\ddot{\phi} + 2\dot{\rho}\dot{\phi}\right) \boldsymbol{\hat{\phi}} + \ddot{z}\mathbf{\hat{z}}$ |

:::{figure} ../images/lt-23016-c2.png
:alt: c2.PNG

$2$: Diagram for Table $3$.
:::

#### Spherical Coordinates $(r, \theta , \phi )$

The three dimensional spherical coordinates, can be treated the same way as for cylindrical coordinates. The unit basis vectors are shown in Table 19.4 where the angular unit vectors $\boldsymbol{\hat{\theta}}$ and $\boldsymbol{\hat{\phi}}$ are taken to be tangential corresponding to the direction a point on the circumference moves for a positive rotation angle.

| Coordinates | $r, \theta, \phi$ |
| --- | --- |
| Distance element | $ds = dr\mathbf{\hat{r}} + rd\theta \boldsymbol{\hat{\theta}} + r \sin \theta d \phi \boldsymbol{\hat{\phi}}$ |
| Volume element | $dv = r^2 \sin \theta drd\theta d\phi$ |
| Unit vectors | $\mathbf{\hat{r}} = \hat{i} \sin \theta \cos \phi + \hat{j} \sin \theta \cos \phi + \mathbf{\hat{k}} \cos \theta$
$\boldsymbol{\hat{\theta}} = \hat{i} \cos \theta \cos \phi + \hat{j} \cos \theta \sin \phi - \mathbf{\hat{k}} \sin \theta$
$\boldsymbol{\hat{\phi}} = -\hat{i} \sin \phi + \hat{j} \cos \phi$ |
| Time derivatives of unit vectors | $\frac{d\mathbf{\hat{r}}}{dt} = \boldsymbol{\hat{\theta}} \dot{\theta} + \boldsymbol{\hat{\phi}} \dot{\phi} \sin \theta$
$\frac{d\boldsymbol{\hat{\theta}}}{dt} = -\mathbf{\hat{r}} \dot{\theta} + \boldsymbol{\hat{\phi}} \dot{\phi} \cos \theta$
$\frac{d\boldsymbol{\hat{\phi}}}{dt} = -\mathbf{\hat{r}}\dot{\phi}\sin \theta - \boldsymbol{\hat{\theta}} \dot{\phi} \cos \theta$ |
| Velocity | $\mathbf{v} = \dot{r}\mathbf{\hat{r}} + r\dot{\theta} \boldsymbol{\hat{\theta}} + r \dot{\phi} \sin \theta \boldsymbol{\hat{\phi}}$ |
| Kinetic energy | $\frac{m}{2} \left(\dot{r}^2 + r^2 \dot{\theta}^2 + r^2\sin^2 \theta \dot{\phi}^2 \right)$ |
| Acceleration | $\mathbf{a} = \left(\ddot{r} - r \dot{\theta}^2 - r\dot{\phi}^2 \sin^2 \theta \right)\mathbf{\hat{r}} + \left(r\ddot{\theta} + 2\dot{r}\dot{\theta} - r\dot{\phi}^2 \sin \theta \cos \theta \right) \boldsymbol{\hat{\theta}} + \left(r \ddot{\phi} \sin \theta + 2\dot{r}\dot{\phi} \sin \theta + 2r\dot{\theta}\dot{\phi} \cos \theta \right) \boldsymbol{\hat{\phi}}$ |

:::{figure} ../images/lt-23017-c3.png
:alt: c3.PNG

$3$: Diagram for Table $4$.
:::

The distance and volume elements, the cartesian coordinate components of the spherical unit basis vectors, and the unit vector time derivatives are shown in the table given in Figure 19.3. The time dependence of the unit vectors is used to derive the acceleration. As for the case of cylindrical coordinates, the $\mathbf{\hat{r}}$, $\boldsymbol{\hat{\theta}}$, and $\boldsymbol{\hat{\phi}}$ components of the acceleration involve coupling of the coordinates and their time derivatives.

It is important to note that the angular unit vectors $\boldsymbol{\hat{\theta}}$ and $\boldsymbol{\hat{\phi}}$ are taken to be tangential to the circles of rotation. However, for discussion of angular velocity of angular momentum it is more convenient to use the axes of rotation defined by $\mathbf{\hat{r}} \times \boldsymbol{\hat{\theta}}$ and $\mathbf{\hat{r}} \times \boldsymbol{\hat{\phi}}$ for specifying the vector properties which is perpendicular to the unit vectors $\boldsymbol{\hat{\theta}}$ and $\boldsymbol{\hat{\phi}}$. Be careful not to confuse the unit vectors $\boldsymbol{\hat{\theta}}$ and $\boldsymbol{\hat{\phi}}$ with those used for the angular velocities $\dot{\theta}$ and $\dot{\phi}$.

### Frenet-Serret coordinates

The cartesian, polar, cylindrical, or spherical curvilinear coordinate systems, all are orthogonal coordinate systems that are fixed in space. There are situations where it is more convenient to use the Frenet-Serret coordinates which comprise an orthogonal coordinate system that is fixed to the particle that is moving along a continuous, differentiable, trajectory in three-dimensional Euclidean space. Let $s(t)$ represent a monotonically increasing arc-length along the trajectory of the particle motion as a function of time $t$. The Frenet-Serret coordinates, shown in Figure 19.4, are the three instantaneous orthogonal unit vectors $\mathbf{\hat{t}}$, $\mathbf{\hat{n}}$, and $\mathbf{\hat{b}}$ where the tangent unit vector $\mathbf{\hat{t}}$ is the instantaneous tangent to the curve, the normal unit vector $\mathbf{\hat{n}}$ is in the plane of curvature of the trajectory pointing towards the center of the instantaneous radius of curvature and is perpendicular to the tangent unit vector $\mathbf{\hat{t}}$, while the binormal unit vector is $\mathbf{\hat{b}} =\mathbf{\hat{t}} \times \mathbf{\hat{n}}$ which is the perpendicular to the plane of curvature and is mutually perpendicular to the other two Frenet-Serrat unit vectors. The Frenet-Serret unit vectors are defined by the relations

$$
\frac{d\mathbf{\hat{t}}}{ ds} = \kappa \mathbf{\hat{n}} \label{C.16}
$$

$$
\frac{d\mathbf{\hat{b}}}{ ds} = − \tau \mathbf{\hat{n}} \label{C.17}
$$

$$
\frac{d\mathbf{\hat{n}}}{ ds} = −\kappa \mathbf{\hat{t}}+ \tau \mathbf{\hat{b}} \label{C.18}
$$

The curvature $\kappa = \frac{1}{ \rho}$ where $\rho$ is the radius of curvature and $\tau$ is the torsion that can be either positive or negative. For increasing $s$, a non-zero curvature $\kappa$ implies that the triad of unit vectors rotate in a right-handed sense about $\mathbf{\hat{b}}$. If the torsion $\tau$ is positive (negative) the triad of unit vectors rotates in right (left) handed sense about $\mathbf{\hat{t}}$.

| Distance element | $d\mathbf{s}(t) = \mathbf{\hat{t}} \left\| \frac{d\mathbf{r}(t)}{dt} \right\| dt = \mathbf{\hat{t}} v(t) dt$ |
| --- | --- |
| Unit vectors | $\mathbf{\hat{t}}(t) = \frac{\mathbf{v}(t)}{ \left\| v(t) \right\|}$
$\mathbf{\hat{n}}(t) = \frac{d\mathbf{\hat{t}}/dt}{\left\| \mathbf{d\hat{t}}/dt \right\|}$
$\mathbf{\hat{b}} (t) = \mathbf{\hat{t}} \times \mathbf{\hat{n}}$ |
| Time derivatives of unit vectors | $\frac{d}{d t} \begin{pmatrix}

 \mathbf{\hat{t}} \\

 \mathbf{\hat{n}} \\

 \mathbf{\hat{b}}

 \end{pmatrix} =\|v\|\begin{pmatrix}

 0 & \kappa & 0 \\

 -\kappa & 0 & \tau \\

 0 & -\tau & 0

 \end{pmatrix} \begin{pmatrix}

 \mathbf{\hat{t}} \\

 \mathbf{\hat{n}} \\

 \mathbf{\hat{b}}

 \end{pmatrix}$ |
| Velocity | $\mathbf{v} (t) = \frac{d\mathbf{r}(t)}{dt}$ |
| Acceleration | $\mathbf{a}(t) = \frac{dv}{dt} \mathbf{\hat{t}} + \kappa v^2 \mathbf{\hat{n}}$ |

:::{figure} ../images/lt-23014-c4.png
:alt: c4.PNG

$4$: Diagram for Table $5$.
:::

The above equations also can be rewritten in the form using a new unit rotation vector $\boldsymbol{\omega}$ where

$$
\boldsymbol{\omega}= \tau \mathbf{\hat{t}}+\kappa \mathbf{\hat{b}} \label{C.19}
$$

Then equations \ref{C.16}−\ref{C.18} are transformed to

$$
\frac{d\mathbf{\hat{t}}}{ ds} = \boldsymbol{\omega} \times \mathbf{\hat{t}} \label{C.20}
$$

$$
\frac{d\mathbf{\hat{n}}}{ ds} = \boldsymbol{\omega} \times \mathbf{\hat{n}} \label{C.21}
$$

$$
\frac{d\mathbf{\hat{b}}}{ ds} = \boldsymbol{\omega} \times \mathbf{\hat{b}} \label{C.22}
$$

In general the Frenet-Serret unit vectors are time dependent. If the curvature $\kappa = 0$ then the curve is a straight line and $\mathbf{\hat{n}}$ and $\mathbf{\hat{b}}$ are not well defined. If the torsion is zero then the trajectory lies in a plane. Note that a helix has constant curvature and constant torsion.

The rate of change of a general vector field $\mathbf{E}$ along the trajectory can be written as

$$
\frac{d\mathbf{E}}{ds} = \left( \frac{dE_t}{ ds} \mathbf{\hat{t}} + \frac{dE_n }{ds} \mathbf{\hat{n}}+ \frac{dE_b }{ds} \mathbf{\hat{b}} \right) + \boldsymbol{\omega} \times \mathbf{E} \label{C.23}
$$

The Frenet-Serret coordinates are used in the life sciences to describe the motion of a moving organism in a viscous medium. The Frenet-Serret coordinates also have applications to General Relativity.

### Problems

1. The goal of this problem is to help you understand the origin of the equations that relate two different coordinate systems. Refer to diagrams for cylindrical and spherical coordinates as your teaching assistant explains how to arrive at expressions for $x_1$, $x_2$, and $x_3$ in terms of $\rho$, $\phi$, and $z$ and how to derive expressions for the velocity and acceleration vectors in cylindrical coordinates. Now try to relate spherical and rectangular coordinate systems. Your group should derive expressions relating the coordinates of the two systems, expressions relating the unit vectors and their time derivatives of the two systems, and finally, expressions for the velocity and acceleration in spherical coordinates.

## 19.5: Appendix - Coordinate transformations

Coordinate systems can be translated, or rotated with respect to each other as well as being subject to spatial inversion or time reversal. Scalars, vectors, and tensors are defined by their transformation properties under rotation, spatial inversion and time reversal, and thus such transformations play a pivotal role in physics.

### Translational transformations

Translational transformations are involved frequently for transforming between the center of mass and laboratory frames for reaction kinematics as well as when performing vector addition of central forces for the cases where the centers are displaced. Both the classical Galilean transformation or the relativistic Lorentz transformation are handled the same way. Consider two parallel orthonormal coordinate frames where the origin of $F^{\prime} (x^{\prime}, y^{\prime}, z^{\prime} )$ is displaced by a time dependent vector $\mathbf{a}(t)$ from the origin of frame $F (x, y, z)$. Then the Galilean transformation for a vector $\mathbf{r}$ in frame $\mathbf{F}$ to $\mathbf{r}^{\prime}$ in frame $F^{\prime}$ is given by

$$
\mathbf{r} (x^{\prime}, y^{\prime}, z^{\prime} ) = \mathbf{r} (x, y, z) +\mathbf{a}(t) \label{D.1}
$$

The velocities for a moving frame are given by the vector difference of the velocity in a stationary frame, and the velocity of the origin of the moving frame. Linear accelerations can be handled similarly.

### Rotational transformations

#### Rotation matrix

Rotational transformations of the coordinate system are used extensively in physics. The transformation properties of fields under rotation define the scalar and vector properties of fields, as well as rotational symmetry and conservation of angular momentum.

Rotation of the coordinate frame does not change the value of any scalar observable such as mass, temperature etc. That is, transformation of a scalar quantity is invariant under coordinate rotation from $x, y, z \rightarrow x^{\prime}, y^{\prime}, z^{\prime}$.

$$
\phi (x^{\prime} y^{\prime} z^{\prime} ) = \phi (xyz) \label{D.2}
$$

By contrast, the components of a vector along the coordinate axes change under rotation of the coordinate axes. This difference in transformation properties under rotation between a scalar and a vector is important and defines both scalars and a vectors.

Matrix mechanics, described in appendix $19.1$, provides the most convenient way to handle coordinate rotations. The transformation matrix, between coordinate systems having differing orientations is called the **rotation matrix**. This transforms the components of any vector with respect to one coordinate frame to the components with respect to a second coordinate frame rotated with respect to the first frame.

Assume a point $P$ has coordinates $(x_1, x_2, x_3)$ with respect to a certain coordinate system. Consider rotation to another coordinate frame for which the point $P$ has coordinates $(x^{\prime}_1, x^{\prime}_2, x^{\prime}_3)$ and assume that the origins of both frames coincide. Rotation of a frame does not change the vector, only the vector components of the unit basis states. Therefore

$$
\mathbf{x} = \mathbf{\hat{e}}^{\prime}_1 x^{\prime}_1 + \mathbf{\hat{e}}^{\prime}_2 x^{\prime}_2 + \mathbf{\hat{e}}^{\prime}_3x^{\prime}_3 = \mathbf{\hat{e}}_1x_1 + \mathbf{\hat{e}}_2x_2 + \mathbf{\hat{e}}_3x_3 \label{D.3}
$$

Note that if one designates that the unit vectors for the unprimed coordinate frame are $(\mathbf{\hat{e}}_1, \mathbf{\hat{e}}_2, \mathbf{\hat{e}}_3)$ and for the primed coordinate frame $(\mathbf{\hat{e}}^{\prime}_1, \mathbf{\hat{e}}^{\prime}_2, \mathbf{\hat{e}}^{\prime}_3)$, then taking the scalar product of Equation \ref{D.3} sequentially with each of the unit base vectors $(\mathbf{\hat{e}}^{\prime}_1, \mathbf{\hat{e}}^{\prime}_2, \mathbf{\hat{e}}^{\prime}_3)$ leads to the following three relations

$$
x^{\prime}_1 = (\mathbf{\hat{e}}^{\prime}_1 \cdot \mathbf{\hat{e}}_1)x_1 + (\mathbf{\hat{e}}^{\prime}_1 \cdot \mathbf{\hat{e}}_2)x_2 + (\mathbf{\hat{e}}^{\prime}_1 \cdot \mathbf{\hat{e}}_3)x_3 \label{D.4} \\ x^{\prime}_2 = (\mathbf{\hat{e}}^{\prime}_2 \cdot \mathbf{\hat{e}}_1)x_1 + (\mathbf{\hat{e}}^{\prime}_2 \cdot \mathbf{\hat{e}}_2)x_2 + (\mathbf{\hat{e}}^{\prime}_2 \cdot \mathbf{\hat{e}}_3)x_3 \\ x^{\prime}_3 = (\mathbf{\hat{e}}^{\prime}_3 \cdot \mathbf{\hat{e}}_1)x_1 + (\mathbf{\hat{e}}^{\prime}_3 \cdot \mathbf{\hat{e}}_2)x_2 + (\mathbf{\hat{e}}^{\prime}_3 \cdot \mathbf{\hat{e}}_3)x_3
$$

Note that the $(\mathbf{\hat{e}}^{\prime}_i \cdot \mathbf{\hat{e}}_j )$ are the direction cosines as defined by the scalar product of two unit vectors for axes $i, j$, that is, they are the cosine of the angle between the two unit vectors.

Equation \ref{D.4} can be written in matrix form as

$$
\mathbf{x}^{\prime} = \boldsymbol{\lambda} \cdot \mathbf{x} \label{D.5}
$$

where the “$\cdot$” means the *inner matrix product* of the rotation matrix $\boldsymbol{\lambda}$ and the vector $\mathbf{x}$ where

$$
\mathbf{x}^{\prime} \equiv \begin{pmatrix} x^{\prime}_1 \\ x^{\prime}_2 \\ x^{\prime}_3 \end{pmatrix} \quad \mathbf{x} \equiv \begin{pmatrix} x_1 \\ x_2 \\ x_3 \end{pmatrix} \quad \boldsymbol{\lambda} \equiv \begin{pmatrix} \mathbf{\hat{e}}^{\prime}_1 \cdot \mathbf{\hat{e}}_1 & \mathbf{\hat{e}}^{\prime}_1 \cdot \mathbf{\hat{e}}_2 & \mathbf{\hat{e}}^{\prime}_1 \cdot \mathbf{\hat{e}}_3 \\ \mathbf{\hat{e}}^{\prime}_2 \cdot \mathbf{\hat{e}}_1 & \mathbf{\hat{e}}^{\prime}_2 \cdot \mathbf{\hat{e}}_2 & \mathbf{\hat{e}}^{\prime}_2 \cdot \mathbf{\hat{e}}_3 \\ \mathbf{\hat{e}}^{\prime}_3 \cdot \mathbf{\hat{e}}_1 & \mathbf{\hat{e}}^{\prime}_3 \cdot \mathbf{\hat{e}}_2 & \mathbf{\hat{e}}^{\prime}_3 \cdot \mathbf{\hat{e}}_3 \end{pmatrix} \label{D.6}
$$

The inverse procedure is obtained by multiplying Equation \ref{D.3} successively by one of the unit basis vectors $(\mathbf{\hat{e}}_1, \mathbf{\hat{e}}_2, \mathbf{\hat{e}}_3)$ leading to three equations

$$
x_1 = (\mathbf{\hat{e}}_1 \cdot \mathbf{\hat{e}}^{\prime}_1) x^{\prime}_1 + (\mathbf{\hat{e}}_1 \cdot \mathbf{\hat{e}}^{\prime}_2) x^{\prime}_2 + (\mathbf{\hat{e}}_1 \cdot \mathbf{\hat{e}}^{\prime}_3) x^{\prime}_3 \label{D.7} \\ x_2 = (\mathbf{\hat{e}}_2 \cdot \mathbf{\hat{e}}^{\prime}_1)x^{\prime}_1 + (\mathbf{\hat{e}}_2 \cdot \mathbf{\hat{e}}^{\prime}_2)x^{\prime}_2 + (\mathbf{\hat{e}}_2 \cdot \mathbf{\hat{e}}^{\prime}_3)x^{\prime}_3 \\ x_3 = (\mathbf{\hat{e}}_3 \cdot \mathbf{\hat{e}}^{\prime}_1)x^{\prime}_1 + (\mathbf{\hat{e}}_3 \cdot \mathbf{\hat{e}}^{\prime}_2)x^{\prime}_2 + (\mathbf{\hat{e}}_3 \cdot \mathbf{\hat{e}}^{\prime}_3)x^{\prime}_3
$$

Equation \ref{D.7} can be written in matrix form as

$$
\mathbf{x} = \boldsymbol{\lambda}^T \cdot \mathbf{x}^{\prime} \label{D.8}
$$

where $\boldsymbol{\lambda}^T$ is the transpose of $\boldsymbol{\lambda}$.

Note that substituting Equation \ref{D.5} into Equation \ref{D.8} gives

$$
\mathbf{x} = \boldsymbol{\lambda}^T \cdot (\boldsymbol{\lambda} \cdot \mathbf{x}) = \left( \boldsymbol{\lambda}^T \cdot \boldsymbol{\lambda} \right) \cdot \mathbf{x} \label{D.9}
$$

Thus

$$
\left( \boldsymbol{\lambda}^T \cdot \boldsymbol{\lambda} \right) = \mathbb{I} \nonumber
$$

where $\mathbb{I}$ is the identity matrix. This implies that the rotation matrix $\boldsymbol{\lambda}$ is orthogonal with $\boldsymbol{\lambda}^T = \boldsymbol{\lambda}^{−1}$.

It is convenient to rename the elements of the rotation matrix to be

$$
\lambda_{ij} \equiv (\mathbf{\hat{e}}^{\prime}_i \cdot \mathbf{\hat{e}}_j ) \label{D.10}
$$

so that the rotation matrix is written more compactly as

$$
\boldsymbol{\lambda} \equiv \begin{pmatrix}\lambda_{11} & \lambda_{12} & \lambda_{13} \\ \lambda_{21} & \lambda_{22} & \lambda_{23} \\ \lambda_{31} & \lambda_{32} & \lambda_{33} \end{pmatrix} \nonumber
$$

and Equation \ref{D.4} becomes

$$
x^{\prime}_1 = \lambda_{11}x_1 + \lambda_{12}x_2 + \lambda_{13}x_3 \label{D.11} \\ x^{\prime}_2 = \lambda_{21}x_1 + \lambda_{22}x_2 + \lambda_{23}x_3 \\ x^{\prime}_3 = \lambda_{31}x_1 + \lambda_{32}x_2 + \lambda_{33}x_3
$$

Consider an arbitrary rotation through an angle $\theta$. Equations \ref{D.10} and \ref{D.11} can be used to relate six of the nine quantities $\lambda_{ij}$ in the rotation matrix, so only three of the quantities are independent. That is, because of Equation \ref{D.11} we have three equations which ensure that the transformation is unitary.

$$
\lambda^2_{i1} + \lambda^2_{i2} + \lambda^2_{i3} = 1 \label{D.12}
$$

Also requiring that the axes be orthogonal gives three equations

$$
\sum_j \lambda_{ij} \lambda_{kj} = 0, \quad i \neq k \label{D.13}
$$

These six relations can be expressed as

$$
\sum_j \lambda_{ij} \lambda_{kj} = \delta_{ik} \label{D.14}
$$

The fact that the rotation matrix should have three independent quantities is due to the fact that all rotations can be expressed in terms of rotations about three orthogonal axes.

Example 19.1

Consider a point $P(x_1, x_2, x_3) = P(3, 4, 5)$ in the unprimed coordinate system. Consider the same point $P(x^{\prime}_1, x^{\prime}_2, x^{\prime}_3)$ in the primed coordinate system which has been rotated by an angle $60^{\circ}$ about the $x_1$ axis as shown. The direction cosines $\lambda_{i^{\prime}j} = \cos ( \theta_{i^{\prime}j} )$ can be determined from the figure to be the following

| $i^{\prime}$ | $j$ | $\theta_{i^{\prime}j}$ | $\lambda_{i^{\prime}j} = \cos (\theta_{i^{\prime}j})$ |
| --- | --- | --- | --- |
| 1 | 1 | 0 | 1 |
| 1 | 2 | 90 | 0 |
| 1 | 3 | 90 | 0 |
| 2 | 1 | 90 | 0 |
| 2 | 2 | 60 | 0.500 |
| 2 | 3 | 90-60 | 0.866 |
| 3 | 1 | 90 | 0 |
| 3 | 2 | 90+60 | -0.866 |
| 3 | 3 | 60 | 0.500 |

:::{figure} ../images/lt-23021-d1.png
:alt: d1.PNG

$1$
:::

Thus the rotation matrix is

$$
\lambda =\begin{pmatrix} 1. & 0 & 0 \\ 0 & 0.500 & 0.866 \\ 0 & −0.866 & 0.500 \end{pmatrix} \nonumber
$$

The transform point $P^{\prime} (x^{\prime}_1, x^{\prime}_2, x^{\prime}_3)$ therefore is given by

$$
\begin{pmatrix}x^{\prime}_1 \\ x^{\prime}_2 \\ x^{\prime}_3 \end{pmatrix} =\begin{pmatrix}1. & 0 & 0 \\ 0 & 0.500 & 0.866 \\ 0 & −0.866 & 0.500 \end{pmatrix} \cdot \begin{pmatrix} 3 \\ 4 \\ 5 \end{pmatrix} =\begin{pmatrix} 3 \\ 6.330 \\ −0.964 \end{pmatrix} \nonumber
$$

Note that the radial coordinate $r_P= r^{\prime}_P= \sqrt{50}$. That is, the rotational transformation is unitary and thus the magnitude of the vector is unchanged.

Example 19.2: Proof that a rotation matrix is orthogonal

Consider the rotation matrix

$$
\boldsymbol{\lambda} = \frac{1}{9} \begin{pmatrix} 4 & 7 & −4 \\ 1 & 4 & 8 \\ 8 & −4 & 1 \end{pmatrix} \nonumber
$$

The product

$$
\boldsymbol{\lambda}^T \cdot \boldsymbol{\lambda} = \frac{1}{ 81} \begin{pmatrix} 4 & 1 & 8 \\ 7 & 4 & −4 \\ −4 & 8 & 1 \end{pmatrix} \cdot \begin{pmatrix} 4 & 7 & −4 \\ 1 & 4 & 8 \\ 8 & −4 & 1 \end{pmatrix} = \frac{1}{ 81} \begin{pmatrix} 81 & 0 & 0 \\ 0 & 81 & 0 \\ 0 & 0 & 81 \end{pmatrix} = 1 \nonumber
$$

which implies that $\lambda$ is orthogonal.

#### Finite rotations

:::{figure} ../images/lt-23019-d2.png
:alt: d2.PNG

$2$: Order of two finite rotations for a parallelepiped.
:::

Consider two finite $90^{\circ}$ rotations $\lambda_{A}$ and $\lambda_{B}$ illustrated in Figure 19.2. The $\lambda_{A}$ rotation is $90^{\circ}$ around the $x_3$ axis in a right-handed direction as shown. In such a rotation the axes transform to $x^{\prime}_1 = x_2, x^{\prime}_2 = −x_1, x^{\prime}_3 = x_3$ and the rotation matrix is

$$
\boldsymbol{\lambda}_A =\begin{pmatrix} 0 & 1 & 0 \\ −1 & 0 & 0 \\ 0 & 0 & 1 \end{pmatrix} \label{D.15}
$$

The second rotation $\boldsymbol{\lambda}_B$ is a right-handed rotation about the $x^{\prime}_1$ axis which formerly was the $x_2$ axis. Then $x^{"}_1 = x^{\prime}_2, x^{"}_2 = −x^{\prime}_1, x^{"}_3 = x^{\prime}_3$ and the rotation matrix is

$$
\boldsymbol{\lambda}_B =\begin{pmatrix} 1 & 0 & 0 \\ 0 & 0 & 1 \\ 0 & −1 & 0 \end{pmatrix} \label{D.16}
$$

Consider the product of these two finite rotations which corresponds to a single rotation matrix $\boldsymbol{\lambda}_{AB}$

$$
\boldsymbol{\lambda}_{AB} = \boldsymbol{\lambda}_B \boldsymbol{\lambda}_A \label{D.17}
$$

That is:

$$
\boldsymbol{\lambda}_{AB} =\begin{pmatrix} 1 & 0 & 0 \\ 0 & 0 & 1 \\ 0 & −1 & 0 \end{pmatrix} \begin{pmatrix} 0 & 1 & 0 \\ −1 & 0 & 0 \\ 0 & 0 & 1 \end{pmatrix} = \begin{pmatrix} 0 & 1 & 0 \\ 0 & 0 & 1 \\ 1 & 0 & 0 \end{pmatrix} \label{D.18}
$$

Now consider that the order of these two rotations is reversed.

$$
\boldsymbol{\lambda}_{BA} = \boldsymbol{\lambda}_A \boldsymbol{\lambda}_B \label{D.19}
$$

That is:

$$
\boldsymbol{\lambda}_{BA} = \begin{pmatrix} 0 & 1 & 0 \\ −1 & 0 & 0 \\ 0 & 0 & 1 \end{pmatrix} \begin{pmatrix} 1 & 0 & 0 \\ 0 & 0 & 1 \\ 0 & −1 & 0 \end{pmatrix} = \begin{pmatrix} 0 & 0 & 1 \\ −1 & 0 & 0 \\ 0 & −1 & 0 \end{pmatrix} \neq \boldsymbol{\lambda}_{AB} \label{D.20}
$$

An entirely different orientation results as illustrated in Figure 19.2.

This behavior of finite rotations is a consequence of the fact that *finite rotations do not commute*, that is, reversing the order does not give the same answer. Thus, if we associate the vectors $\mathbf{A}$ and $\mathbf{B}$ with these rotations, then it implies that the vector product $\mathbf{AB} \neq \mathbf{BA}$. That is, for finite rotation matrices, the product does not behave like for true vectors since they do not commute.

#### Infinitessimal rotations

:::{figure} ../images/lt-23020-d3.png
:alt: d3.PNG

$3$: Infinitessimal rotation
:::

Infinitessimal rotations do not suffer from the noncommutation defect of finite rotations. If the position vector of a point changes from $\mathbf{r}$ to $\mathbf{r} + \delta \mathbf{r}$ then the geometrical situation is represented correctly by

$$
\delta \mathbf{r} = \delta \boldsymbol{\theta} \times \mathbf{r} \label{D.21}
$$

where $\delta \boldsymbol{\theta}$ is a quantity whose magnitude is equal to the infinitessimal rotation angle and which has a direction along the instantaneous axis of rotation as illustrated in Figure 19.3.

The infinitessimal angle $\delta \boldsymbol{\theta}$ is a vector which is shown by proving that two infinitessimal rotations $\delta \boldsymbol{\theta}_1$ and $\delta \boldsymbol{\theta}_2$ commute. The change in position vectors of the point are

$$
\delta \mathbf{r}_1 = \delta \boldsymbol{\theta}_1 \times \mathbf{r} \label{D.22}
$$

and

$$
\delta \mathbf{r}_2 = \delta \boldsymbol{\theta}_2 \times (\mathbf{r} + \delta \mathbf{r}_1) \label{D.23}
$$

Thus the final position vector for $\delta \boldsymbol{\theta}_1$ followed by $\delta \boldsymbol{\theta}_2$ is

$$
\mathbf{r} + \delta \mathbf{r}_1 + \delta \mathbf{r}_2 = \mathbf{r} + \delta \boldsymbol{\theta}_1 \times \mathbf{r} + \delta \boldsymbol{\theta}_2 \times ( \mathbf{r} + \delta \mathbf{r}_1) \label{D.24}
$$

Assuming that the second-order infinitessimals can be ignored gives

$$
\mathbf{r} + \delta \mathbf{r}_1 + \delta \mathbf{r}_2 = \mathbf{r} + \delta \boldsymbol{\theta}_1 \times \mathbf{}\mathbf{r} + \delta \boldsymbol{\theta}_2 \times \mathbf{r} \label{D.25}
$$

Consider now the inverse order of rotations.

$$
\mathbf{r} + \delta \mathbf{r}_2 + \delta \mathbf{r}_1 = \mathbf{r} + \delta \boldsymbol{\theta}_2 \times \mathbf{r} + \delta \boldsymbol{\theta}_1 \times (\mathbf{r} + \delta \mathbf{r}_2) \label{D.26}
$$

Again, neglecting the second-order infinitessimals gives

$$
\mathbf{r} + \delta \mathbf{r}_2 + \delta \mathbf{r}_1 = \mathbf{r} + \delta \boldsymbol{\theta}_2 \times \mathbf{r} + \delta \boldsymbol{\theta}_1 \times \mathbf{r} \label{D.27}
$$

Note that the products of these two infinitessimal rotations, \ref{D.25} and \ref{D.27} are identical. That is, assuming that second-order infinitessimals can be neglected, then the infinitessimal rotations commute, and thus $\delta \boldsymbol{\theta}_1$ and $\delta \boldsymbol{\theta}_2$ are correctly represented by vectors.

The fact that $\delta \boldsymbol{\theta}$ is a vector allows angular velocity to be represented by a vector. That is, angular velocity is the ratio of an infinitessimal rotation to an infinitessimal time.

$$
\boldsymbol{\omega} = \frac{\delta \boldsymbol{\theta}}{ \delta t } \label{D.28}
$$

Note that this implies that the velocity of the point can be expressed as

$$
\mathbf{v} = \frac{\delta \mathbf{r}}{ \delta t} = \frac{\delta \boldsymbol{\theta}}{ \delta t} \times \mathbf{r} = \boldsymbol{\omega} \times \mathbf{r} \label{D.29}
$$

#### Proper and improper rotations

The requirement that the coordinate axes be orthogonal, and that the transformation be unitary, leads to the relation between the components of the rotation matrix.

$$
\sum_j \lambda_{ij} \lambda_{kj} = \delta_{ik} \label{D.30}
$$

It was shown in equation $(19.1.12)$ that, for such an orthogonal matrix, the inverse matrix $\lambda^{−1}$ equals the transposed matrix $\lambda^T$

$$
\boldsymbol{\lambda}^{−1} = \boldsymbol{\lambda}^T \nonumber
$$

Inserting the orthogonality relation for the rotation matrix leads to the fact that the square of the determinant of the rotation matrix equals one,

$$
|\lambda |^2 = 1 \label{D.31}
$$

that is

$$
|\lambda | = \pm 1 \label{D.32}
$$

A **proper rotation** is the rotation of a normal vector and has

$$
|\lambda | = +1 \label{D.33}
$$

An **improper rotation** corresponds to

$$
|\lambda | = −1 \label{D.34}
$$

*An improper rotation implies a rotation plus a spatial reflection which cannot be achieved by any combination of only rotations.*

Consider the cross product of two vectors $\mathbf{c} = \mathbf{a} \times \mathbf{b}$. It can be shown that the cross product behaves under rotation as:

$$
c^{\prime}_i = |\lambda | \sum_j \lambda_{ij} c_j \label{D.35}
$$

For all proper rotations the determinant of $\lambda = +1$ and thus the cross product also acts like a proper vector under rotation. This is not true for improper rotations where $|\lambda | = −1$.

### Spatial inversion transformation

Spatial inversion, that is, mirror reflection, corresponds to reflection of all coordinate vectors, $\widehat{\mathbf{i}} = − \widehat{\mathbf{i}}$, $\widehat{\mathbf{j}} = − \widehat{\mathbf{j}}$, and $\widehat{\mathbf{k}} = − \widehat{\mathbf{k}}$. Such a transformation corresponds to the transformation matrix

$$
\boldsymbol{\lambda} =\begin{pmatrix} −1 & 0 & 0 \\ 0 & −1 & 0 \\ 0 & 0 & −1 \end{pmatrix} = −\begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{pmatrix} \label{D.36}
$$

:::{figure} ../images/lt-23018-d4.png
:alt: d4.PNG

$4$: Inversion of an object corresponds to reflection about the origin of all axes.
:::

Thus $|\lambda | = −1$, that is, it corresponds to an improper rotation. A spatial inversion for two vectors $\mathbf{A}(r)$ and $\mathbf{B}(r)$ correspond to

$$
\mathbf{A}(r) = −\mathbf{A}(-r) \label{D.37} \\ \mathbf{B}(r) = −\mathbf{B}(-r)
$$

That is, normal polar vectors change sign under spatial reflection. However, the cross product $\mathbf{C} = \mathbf{A} \times \mathbf{B}$ does not change sign under spatial inversion since the product of the two minus signs is positive. That is,

$$
\mathbf{C}(r)=+\mathbf{C}(-r) \label{D.38}
$$

Thus the cross product behaves differently from a polar vector. This improper behavior is characteristic of an **axial vector**, which also is called a **pseudovector**.

Examples of pseudovectors are angular momentum, spin, magnetic field etc. These pseudovectors are defined using the right-hand rule and thus have handedness. For a right-handed system

$$
\mathbf{C}_R = \mathbf{A} \times \mathbf{B} \label{D.39}
$$

Changing to a left-handed system leads to

$$
\mathbf{C}_L = \mathbf{B} \times \mathbf{A} = −\mathbf{A} \times \mathbf{B} \label{D.40}
$$

That is, handedness corresponds to a definite ordering of the cross product. Proper orthogonal transformations are said to preserve chirality (Greek for handedness) of a coordinate system.

An example of the use of the right-handed system is the usual definition of cartesian unit vectors,

$$
\widehat{\mathbf{i}} \times \widehat{\mathbf{j}} = \widehat{\mathbf{k}} \label{D.41}
$$

An obvious question to be asked, is the handedness of a coordinate system merely a mathematical curiosity or does it have some deep underlying significance? Consider the Lorentz force

$$
\mathbf{F} = q (\mathbf{E} + \mathbf{v} \times \mathbf{B}) \label{D.42}
$$

Since force and velocity are proper vectors then the magnetic $\mathbf{B}$ field must be a pseudo vector. Note that calculation of the $\mathbf{B}$ field occurs only in cross products such as,

$$
\boldsymbol{\nabla} \times \mathbf{B} = \mu \mathbf{j} \label{D.43}
$$

where the current density $\mathbf{j}$ is a proper vector. Another example is the Biot-Savart Law which expresses $\mathbf{B}$ as

$$
d\mathbf{B} = \frac{\mu_oI}{4\pi} \frac{ d\mathbf{l} \times \mathbf{r}}{r^2} \label{D.44}
$$

Thus even though $\mathbf{B}$ is a pseudo vector, the force $\mathbf{F}$ remains a proper vector. Thus if a left-handed coordinate definition of $\mathbf{B}_L = \frac{\mu_oI}{4\pi} \frac{ \mathbf{r} \times d\mathbf{l}}{r^2}$ is used in \ref{D.44}, and $\mathbf{F} = q (\mathbf{E} + \mathbf{B}_L \times \mathbf{v})$ in \ref{D.42}, then the same final physical result would be obtained.

It was long thought that the laws of physics were symmetric with respect to spatial inversion ( i.e. mirror reflection), meaning that the choice between a left-handed and right-handed representations (chirality) was arbitrary. This is true for gravitational, electromagnetic and the strong force, and is called the conservation of parity. The fourth fundamental force in nature, the weak force, violates parity and favours handedness. It turns out that right-handed ordinary matter is symmetrical with left-handed antimatter.

In addition to the two flavours of vectors, one has scalars and pseudoscalars defined by:

$$
\phi (r)=+\phi (−r) \label{D.45}
$$

$$
\phi (r) = −\phi (−r) \label{D.46}
$$

An example of a pseudoscalar is the scalar product $\mathbf{A} \cdot (\mathbf{B} \times \mathbf{C})$

### Time reversal transformation

The basic laws of classical mechanics are invariant to the sense of the direction of time. Under time reversal the vector $\mathbf{r}$ is unchanged while both momentum $\mathbf{p}$ and time $t$ change sign under time reversal, thus the time derivative $\mathbf{F} = \frac{d\mathbf{p}}{ dt}$ is invariant to time reversal; that is, the force is unchanged and Newton’s Laws $\mathbf{F} = \frac{d\mathbf{p}}{ dt}$ are invariant under time reversal. Since the force can be expressed as the gradient of a scalar potential for a conservative field, then the potential also remains unchanged. That is

$$
\frac{d\mathbf{p}}{ dt} = −\boldsymbol{\nabla} U(r) = \mathbf{F} \label{D.47}
$$

It is necessary to introduce tensor algebra, given in appendix $19.5$, prior to discussion of the transformation properties of observables which is the topic of appendix $19.5.5$.

### Exercises

1. Suppose the $x_2$-axis of a rectangular coordinate system is rotated by $30^{\circ}$ away from the $x_3$-axis around the $x_1$-axis.

(a) Find the corresponding transformation matrix. Try to do this by drawing a diagram instead of going to the book or the notes for a formula.

(b) Is this an orthogonal matrix? If so, show that it satisfies the main properties of an orthogonal matrix. If not, explain why it fails to be orthogonal.

(c) Does this matrix represent a proper or an improper rotation? How do you know?

2. When you were first introduced to vectors, you most likely were told that a scalar is a quantity that is defined by a magnitude, while a vector has both a magnitude and a direction. While this is certainly true, there is another, more sophisticated way to define a scalar quantity and a vector quantity: through their transformation properties. A scalar quantity transforms as $\phi^{\prime} = \phi$ while a vector quantity transforms as $A^{\prime}_i = \sum_j \lambda_{ij} A_j$. To show that the scalar product does indeed transform as a scalar, note that:

$$
\mathbf{A}^{\prime} \cdot \mathbf{B}^{\prime} = \sum_i A^{\prime}_i B^{\prime}_i = \sum_i \left( \sum_j \lambda_{ij} A_j \right) \left( \sum_k \lambda_{ik} B_k \right) = \sum_{j, k} \left( \sum_i \lambda_{ij} \lambda_{ik} \right) A_jB_k \\ = \sum_j \left( \sum_k \delta_{jk} A_j B_k \right) = \sum_j A_j B_j = \mathbf{A} \cdot \mathbf{B} \nonumber
$$

Now you will show that the vector product transforms as a vector. Begin by writing out what you are trying to show explicitly and show it to the teaching assistant. Once the teaching assistant has confirmed that you have the correct expression, try to prove it. The vector product is a bit more difficult to work with than the scalar product, so your teaching assistant is prepared to give you a hint if you get stuck.

3. Suppose you have two rectangular coordinate systems that share a common origin, but one system is rotated by an angle $\theta$ with respect to the other. To describe this rotation, you have made use of the rotation matrix $\lambda (\theta )$. (I’m changing the notation slightly to put the emphasis on the angle of rotation.)

(a) Verify that the product of two rotation matrices $\lambda (\theta_1)\lambda (\theta_2)$ is in itself a rotation matrix.

(b) In abstract algebra, a group $G$ is defined as a set of elements $g$ together with a binary operation $*$ acting on that set such that four properties are satisfied:

i. (Closure) For any two elements $g_i$ and $g_j$ in the group $G$, the product of the elements, $g_i * g_j$ is also in the group $G$.

ii. (Associativity) For any three elements $g_i, g_j , g_k$ of the group $G$, $(g_i * g_j ) * g_k = g_i * (g_j * g_k)$.

iii. (Existence of Identity) The group $G$ contains an identity element $e$ such that $g * e = e * g = g$ for all $g \in G$.

iv. (Existence of Inverses) For each element $g \in G$, there exists an inverse element $g^{−1} \in G$ such that $g * g^{−1} = g^{−1} * g = e$.

Show that if the product $*$ denotes the product of two matrices, then the set of rotation matrices together with $*$ forms a group. This group is known as the special orthogonal group in two dimensions, also known as $SO(2)$.

(c) Is this group commutative? In abstract algebra, a commutative group is called an abelian group.

4. When you look in a mirror the image of you appears left-to-right reversed, that is, the image of your left ear appears to be the right ear of the image and vise versa. Explain why the image is left-right reversed rather than up-down reversed or reversed about some other axis; i.e. explain what breaks the symmetry that leads to these properties of the mirror image.

5. Find the transformation matrix that rotates the axis $x_3$ of a rectangular coordinate system $45^{\circ}$ toward $x_1$ around the $x_2$ axis.

6. For simplicity, take $\lambda$ to be a two-dimensional transformation matrix. Show by direct expansion that $|\boldsymbol{\lambda}|^2 = 1$.

## 19.6: Appendix - Tensor Algebra

### Tensors

Mathematically scalars and vectors are the first two members of a hierarchy of entities, called **tensors**, that behave under coordinate transformations as described in appendix $19.4$. The use of the tensor notation provides a compact and elegant way to handle transformations in physics.

A scalar is a rank 0 tensor with one component, that is invariant under change of the coordinate system.

$$
\phi (x^{\prime} y^{\prime} z^{\prime} ) = \phi (xyz) \label{E.1}
$$

A vector is a rank 1 tensor which has three components, that transform under rotation according to matrix relation

$$
\mathbf{x}^{\prime} = \boldsymbol{\lambda} \cdot \mathbf{x} \label{E.2}
$$

where $\boldsymbol{\lambda}$ is the rotation matrix. Equation \ref{E.2} can be written in the suffix form as

$$
x^{\prime}_i = \sum^3_{j=1} \lambda_{ij} x_j \label{E.3}
$$

The above definitions of scalars and vectors can be subsumed into a class of entities called tensors of rank $n$ that have $3^n$ components. A scalar is a tensor of rank $r = 0$, with only $3^0 = 1$ component, whereas a vector has rank $r = 1$, that is, the vector $\mathbf{x}$ has one suffix $i$ and $3^1 = 3$ components.

A second-order tensor $T_{ij}$ has rank $r = 2$ with two suffixes, that is, it has $3^2 = 9$ components that transform under rotation as

$$
T^{\prime}_{ij} = \sum^3_{k=1} \sum^3_{l=1} \lambda_{ik}\lambda_{jl}T_{kl} \label{E.4}
$$

For second-order tensors, the transformation formula given by Equation \ref{E.4} can be written more compactly using matrices. Thus the second-order tensor can be written as a $3 \times 3$ matrix

$$
\mathbf{T} \equiv \begin{pmatrix} T_{11} & T_{12} & T_{13} \\ T_{21} & T_{22} & T_{23} \\ T_{31} & T_{32} & T_{33} \end{pmatrix} \label{E.5}
$$

The rotational transformation given in Equation \ref{E.4} can be written in the form

$$
T^{\prime}_{ij} = \sum^3_{l=1} \left( \sum^3_{k=1} \lambda_{ik}T_{kl}\right) \lambda_{jl} = \sum^3_{l=1} \left( \sum^3_{k=1} \lambda_{ik}T_{kl}\right) \lambda^T_{lj} \label{E.6}
$$

where $\lambda^T_{lj}$ are the matrix elements of the transposed matrix $\boldsymbol{\lambda}^T$. The summations in \ref{E.6} can be expressed in both the tensor and conventional matrix form as the matrix product

$$
\mathbf{T}^{\prime} = \boldsymbol{\lambda} \cdot \mathbf{T} \cdot \boldsymbol{\lambda}^T \label{E.7}
$$

Equation \ref{E.7} defines the rotational properties of a spherical tensor.

### Tensor products

#### Tensor outer product

Tensor products feature prominently when using tensors to represent transformations. A second-order tensor $\mathbf{T}$ can be formed by using the **tensor product**, also called **outer product**, of two vectors $\mathbf{a}$ and $\mathbf{b}$ which, written in suffix form, is

$$
\mathbf{T} \equiv \mathbf{a} \otimes \mathbf{b} = \begin{pmatrix} a_1b_1 & a_1b_2 & a_1b_3 \\ a_2b_1 & a_2b_2 & a_2b_3 \\ a_3b_1 & a_3b_2 & a_3b_3 \end{pmatrix} \label{E.8}
$$

In component form the matrix elements of this matrix are given by

$$
T_{ij} = a_ib_j \label{E.9}
$$

This second-order **tensor product** has a rank $r = 2$, that is, it equals the sum of the ranks of the two vectors. Equation \ref{E.8} is called a *dyad* since it was derived by taking the dyadic product of two vectors. In general, multiplication, or division, of two vectors leads to second-order tensors. Note that this second-order tensor product completes the triad of tensors possible taking the product of two vectors. That is, the scalar product $\mathbf{a} \cdot \mathbf{b}$, has rank $r = 0$, the vector product $\mathbf{a} \times \mathbf{b}$, rank $r = 1$ and the tensor product $\mathbf{a} \otimes \mathbf{b}$ has rank<sup>1</sup> $r = 2$.

Higher-order tensors can be created by taking more complicated tensor products. For example, a rank-3 tensor can be created by taking the tensor outer product of the rank-2 tensor $T_{ij}$ and a vector $c_k$ which, for a dyadic tensor, can be written as the tensor product of three vectors. That is,

$$
T_{ijk} = T_{ij} c_k = a_ib_j c_k \label{E.10}
$$

In summary, the rank of the tensor product equals the sum of the ranks of the tensors included in the tensor product.

#### Tensor Inner Product

The lowest rank tensor product, which is called the **inner product**, is obtained by taking the tensor product of two tensors for the special case where one index is repeated, and taking the sum over this repeated index. Summing over this repeated index, which is called **contraction**, removes the two indices for which the index is repeated, resulting in a tensor that has rank $r$ equal to the sum of the ranks minus 2 for one contraction. That is, the product tensor has rank $r = r_1 + r_2 − 2$.

The simplest example is the inner product of two vectors which has rank $r =1+1 − 2=0$, that is, it is the scalar product that equals the trace of the inner product matrix, and this inner product is commutative.

An especially important case is the inner product of a rank-2 dyad $\mathbf{a} \otimes \mathbf{b}$, given by Equation \ref{E.8}, with a vector $\mathbf{c}$, that is, the inner product $\mathbf{T} = \mathbf{a} \otimes \mathbf{b} \cdot \mathbf{c}$. Written in component form, the inner product is

$$
\sum^3_i a_ib_ic_j = \left( \sum^3_i a_ib_i \right) c_j = (\mathbf{a} \cdot \mathbf{b}) c_j \label{E.11}
$$

The scalar product $\mathbf{a} \cdot \mathbf{b}$ is a scalar number, and thus the inner-product tensor is the vector $\mathbf{c}$ renormalized by the magnitude of the scalar product $\mathbf{a} \cdot \mathbf{b}$. That is, it has a rank $r = 2+1−2=1$. Thus the inner product of this rank-2 tensor with a vector gives a vector. The inner product of a rank-2 tensor with a rank-1 tensor is used in this book for handling the rotation matrix, the inertia tensor for rigid-body rotation, and for the stress and the strain tensors used to describe elasticity in solids.

Example 19.1: Displacement gradient tensor

The displacement gradient tensor provides an example of the use of the matrix representation to manipulate tensors. Let $\boldsymbol{\phi}(x_1, x_2, x_3)$ be a vector field expressed in a cartesian basis. The definition of the gradient $G = \boldsymbol{\nabla}\boldsymbol{\phi}$ gives that

$$
d\boldsymbol{\phi} = \mathbf{G} \cdot d\mathbf{x} \nonumber
$$

Calculating the components of $d\boldsymbol{\phi}$ in terms of $\mathbf{x}$ gives

$$
d\phi_1 = \dfrac{\partial \phi_1}{\partial x_1} dx_1 + \dfrac{\partial \phi_1}{ \partial x_2} dx_2 + \dfrac{\partial \phi_1}{ \partial x_3} dx_3 \nonumber
$$

$$
d\phi_2 = \dfrac{\partial \phi_2}{ \partial x_1} dx_1 + \dfrac{\partial \phi_2}{ \partial x_2} dx_2 + \dfrac{\partial \phi_2}{ \partial x_3} dx_3 \nonumber
$$

$$
d\phi_3 = \dfrac{\partial \phi_3}{ \partial x_1} dx_1 + \dfrac{\partial \phi_3}{ \partial x_2} dx_2 + \dfrac{\partial \phi_3}{ \partial x_3} dx_3 \nonumber
$$

Using index notation this can be written as

$$
d\phi_i = \dfrac{\partial \phi_i}{ \partial x_j} dx_j \nonumber
$$

The second-rank gradient tensor $\mathbf{G}$ can be represented in the matrix form as

$$
\mathbf{G} = \begin{vmatrix} \dfrac{\partial \phi_1}{ \partial x_1} & \dfrac{\partial \phi_1}{ \partial x_2} & \dfrac{\partial \phi_1}{ \partial x_3} \\ \dfrac{\partial \phi_2}{ \partial x_1} & \dfrac{\partial \phi_2}{ \partial x_2} & \dfrac{\partial \phi_2}{ \partial x_3} \\ \dfrac{\partial \phi_3}{ \partial x_1} & \dfrac{\partial \phi_3}{ \partial x_2} & \dfrac{\partial \phi_3}{ \partial x_3} \end{vmatrix} \nonumber
$$

Then the vector $\boldsymbol{\phi}$ can be expressed compactly as the inner product of $\mathbf{G}$ and $\mathbf{x}$, that is

$$
d\boldsymbol{\phi} = \mathbf{G} \cdot d\mathbf{x} \nonumber
$$

### Tensor Properties

In principle one must distinguish between a $3\times 3$ square matrix, and the tensor component representations of a rank-2 tensor. However, as illustrated by the previous discussion, for orthogonal transformations, the tensor components of the second rank tensor transform identically with the matrix components. Thus functionally, the matrix formulation and tensor representations are identical. As a consequence, all the terminology and operations used in matrix mechanics are equally applicable to the tensor representation.

The tensor representation of the rotation matrix provides the simplest example of the equivalence of the matrix and tensor representations of transformations. Appendix $19.4.2$ showed that the unitary rotation matrix $\boldsymbol{\lambda}$, acting on a vector $\mathbf{x}$ transforms it to the vector $\mathbf{x}^{\prime}$ that is rotated with respect to $\mathbf{x}$. That is, the transformation is

$$
\mathbf{x}^{\prime} = \boldsymbol{\lambda} \cdot \mathbf{x} \label{D5}
$$

where

$$
\mathbf{x}^{\prime} \equiv \begin{pmatrix} x^{\prime}_1 \\ x^{\prime}_2 \\ x^{\prime}_3 \end{pmatrix} \quad \mathbf{x} \equiv \begin{pmatrix} x_1 \\ x_2 \\ x_3 \end{pmatrix} \quad \boldsymbol{\lambda} \equiv \begin{pmatrix} \mathbf{\hat{e}}^{\prime}_1 \cdot \mathbf{\hat{e}}_1 & \mathbf{\hat{e}}^{\prime}_1 \cdot \mathbf{\hat{e}}_2 & \mathbf{\hat{e}}^{\prime}_1 \cdot \mathbf{\hat{e}}_3 \\ \mathbf{\hat{e}}^{\prime}_2 \cdot \mathbf{\hat{e}}_1 & \mathbf{\hat{e}}^{\prime}_2 \cdot \mathbf{\hat{e}}_2 & \mathbf{\hat{e}}^{\prime}_2 \cdot \mathbf{\hat{e}}_3 \\ \mathbf{\hat{e}}^{\prime}_3 \cdot \mathbf{\hat{e}}_1 & \mathbf{\hat{e}}^{\prime}_3 \cdot \mathbf{\hat{e}}_2 & \mathbf{\hat{e}}^{\prime}_3 \cdot \mathbf{\hat{e}}_3 \end{pmatrix} \label{D6}
$$

Appendix $19.4.2$ showed that the rotation matrix $\boldsymbol{\lambda}$ requires 9 components to fully specify the transformation from the initial 3-component vector $\mathbf{x}$ to the rotated vector $\mathbf{x}^{\prime}$. The rotation tensor is a dyad as well as being unitary and dimensionless. Note that Equation \ref{D5} is an example of the inner product of a rank−2 rotation tensor acting on a vector leading to a another vector that is rotated with respect to the first vector.

In general, rank-2 tensors have dimensions and are not unitary. For example, the angular velocity vector $\boldsymbol{\omega}$ and the angular momentum vector $\mathbf{L}$ are related by the inner product of the inertia tensor $\{\mathbf{I}\}$ and $\boldsymbol{\omega}$. That is

$$
\mathbf{L} =\{\mathbf{I}\} \cdot \boldsymbol{\omega} \label{11.6}
$$

The inertia tensor has dimensions of $mass \times length^2$ and relates two very different vector observables. The stress tensor and the strain tensor, discussed in chapter $15$, provide another example of second-order tensors that are used to transform one vector observable to another vector observable analogous to the case of the rotation matrix or the inertia tensor.

Note that pseudo-tensors can be used to make a rotational transformation plus a change in the sign. That is, they lead to a parity inversion.

The tensor notation is used extensively in physics since it provides a powerful, elegant, and compact representation for describing transformations.

### Contravariant and covariant tensors

In general the configuration space used to specify a dynamical system is not a Euclidean space in that there may not be a system of coordinates for which the distance between any two neighboring points can be represented by the sum of the squares of the coordinate differentials. For example, a set of cartesian coordinate does not exist for the two-dimension motion of a single particle constrained to the curved surface of a fixed sphere. Such curved spaces need to be represented in terms of Riemannian geometry rather than Euclidean geometry. Curved configuration spaces occur in some branches of physics such as Einstein’s General Theory of Relativity.

Tensors have transformation properties that can be either contravariant or covariant. Consider a set of generalized coordinates $q^{\prime}$ that are a function of the coordinates $q$. Then infinitessimal changes $dq^m$ will lead to infinitessimal changes $dq^{\prime n}$ where

$$
dq^{\prime n} = \sum_m \dfrac{\partial q^{\prime n}}{ \partial q^m } dq^m \label{E.12}
$$

**Contravariant** components of a tensor transform according to the relation

$$
\lambda^{\prime n} = \sum_m \dfrac{\partial q^{\prime n}}{ \partial q^m} \lambda^m \label{E.13}
$$

Equation \ref{E.13} relates the contravariant components in the unprimed and primed frames.

Derivatives of a scalar function $\phi$, such as

$$
\lambda^{\prime}_n = \dfrac{\partial \phi}{ \partial q^n} = \sum_m \dfrac{\partial \phi}{ \partial q^m} \dfrac{ \partial q^m}{ \partial q^n} = \sum_m \dfrac{\partial q^m }{\partial q^n} \lambda^m \label{E.14}
$$

That is, **covariant** components of the tensor transform according to the relation

$$
\lambda^{\prime}_n = \sum_m \dfrac{\partial q^m}{ \partial q^n} \lambda^m \label{E.15}
$$

It is important to differentiate between contravariant and covariant vectors. The superscript/subscript convention for distinguishing between these two flavours of tensors is given in table 19.1

| $x^{\mu}$ | denotes a contravariant vector |
| --- | --- |
| $x_{\nu}$ | denotes a covariant vector |

In linear algebra one can map from one coordinate system to another as illustrated in appendix $19.4$. That is, the tensor $\mathbf{x}$ can be expressed as components with respect to either the unprimed or primed coordinate frames

$$
\mathbf{x} = \mathbf{\hat{e}}^{\prime}_1x^{\prime}_1 + \mathbf{\hat{e}}^{\prime}_2x^{\prime}_2 + \mathbf{\hat{e}}^{\prime}_3x^{\prime}_3 = \mathbf{\hat{e}}_1x_1 + \mathbf{\hat{e}}_2x_2 + \mathbf{\hat{e}}_3x_3 \label{E.16}
$$

For a $n$−dimensional manifold the unit basis column vectors $\mathbf{\hat{e}}$ transform according to the transformation matrix $\boldsymbol{\lambda}$

$$
\mathbf{\hat{e}}^{\prime} = \boldsymbol{\lambda} \cdot \mathbf{\hat{e}} \label{E.17}
$$

Since the tensor $\mathbf{x}$ is independent of the coordinate basis, the components of $\mathbf{x}$ must have the opposite transform

$$
\mathbf{x}^{\prime} = \left( \boldsymbol{\lambda}^{−1}\right)^T \cdot \mathbf{x} \label{E.18}
$$

This normal vector $\mathbf{x}$ is called a “contravariant vector” because it transforms contrary to the basis column vector transformation.

The inverse of Equation \ref{E.18} gives that the column vector element

$$
x_{\mu} = \sum_{\nu} \boldsymbol{\lambda}_{\mu \nu} x^{\prime}_{\nu} \label{E.19}
$$

Consider the case of a gradient with respect to the coordinate $\mathbf{x}$ in both the unprimed and primed bases. Using the chain rule for the partial derivative then the component of the gradient in the primed frame can be expanded as

$$
(\nabla f)^{\prime}_{\mu} = \dfrac{\partial f}{\partial x^{\prime}_{\mu}} = \sum_{\nu} \dfrac{ \partial f}{ \partial x_{\nu}} \dfrac{ \partial x_{\nu}} { \partial x^{\prime}_{ \mu}} = \sum_{\nu} \dfrac{ \partial f}{ \partial x_{\nu}} \boldsymbol{\lambda}_{\nu \mu} \delta_{\mu \nu} = \lambda_{\mu \mu} \dfrac{ \partial f}{ \partial x_{\mu}} \label{E.20}
$$

That is, the gradient transforms as

$$
\boldsymbol{\nabla}^{\prime} f = \boldsymbol{\lambda} \cdot \boldsymbol{\nabla}f \label{E.21}
$$

That is, *a gradient transforms as a covariant vector, like the unit vectors, whereas a vector*$x$*is contravariant under transformation.*

Normally the basis is orthonormal, $\left( \boldsymbol{\lambda}^{−1}\right)^T = \boldsymbol{\lambda}$, and thus there is no difference between contravariant and covariant vectors. However, for curved coordinate systems, such as non-Euclidean geometry in the General Theory of Relativity, the covariant and contravariant vectors behave differently.

The Einstein convention is extended to apply to matrices by writing the elements of the matrix $\mathbf{A}$ as $A^{\mu}_{\nu}$ while the elements of the transposed matrix $\mathbf{A}^{−1}$ are written as $A_{\mu}^{\nu}$. The matrix product for $\mathbf{A}$ with a contravariant vector $\mathbf{X}$ is written as

$$
X^{\prime \mu} = \sum_{\nu} A^{\mu}_{\nu} X^{\nu} \label{E.22}
$$

where the summation over $\nu$ effectively cancels the identical superscript and subscript $\nu$.

Similarly a covariant vector, such as a gradient, is written as,

$$
\left( \boldsymbol{\nabla}^{\prime} f \right)_{\mu} = \sum_{\nu} \left( A^{−1} \right)^{T \nu}_{ \mu} (\boldsymbol{\nabla}f)_{\nu} = \sum_{\nu} \left( A^{-1}\right)^{\nu}_{ \mu} (\boldsymbol{\nabla}f)_{\nu} \label{E.23}
$$

Again the summation cancels the $\nu$ superscript and subscript. The Kronecker delta symbol is written as

$$
\sum_{\nu} \delta^{\mu}_{\nu} X^{\nu} = X^{\mu} \label{E.24}
$$

### Generalized inner product

The generalized definition of an *inner product* is

$$
S = \sum_{\mu \nu} g_{\mu \nu} X^{\mu} Y^{\nu} \label{E.25}
$$

where $g_{\mu \nu}$ is a unitary matrix called a covariant metric. The covariant metric transforms a contravariant to a covariant tensor. For example the matrix element of a covariant tensor $X_{\nu}$ can be written as

$$
X_{\nu} = \sum_{\mu} g_{\mu \nu} X^{\mu} \label{E.26}
$$

By association of the *covariant metric* with either of the vectors in the inner product gives

$$
S = \sum_{\mu \nu} g_{\mu \nu} X^{\mu} Y^{\nu} = \sum_{\nu} X_{\nu} Y^{\nu} = \sum_{\mu} X^{\mu} Y_{\mu} \label{E.27}
$$

Similarly it can be defined in terms of an *orthogonal contravariant metric* $g^{\mu \nu}$ where

$$
S = \sum_{\mu \nu} g^{\mu \nu} X_{\mu} Y_{\nu} \label{E.28}
$$

Then

$$
X^{\nu} = \sum_{\mu} g^{\mu \nu} X_{\mu} \label{E.29}
$$

Association of the contravariant metric with one of the vectors in the inner product gives the inner product

$$
S = \sum_{\mu \nu} g^{\mu \nu} X_{\mu} Y_{\nu} = \sum_{\nu} X^{\nu} Y_{\nu} = \sum_{\mu} X_{\mu} Y^{\mu} \label{E.30}
$$

For most situations in this book the metric $g_{\mu \nu}$ is diagonal and unitary.

### Transformation Properties of Observables

In physics, observables can be represented by spherical tensors which specify the angular momentum and parity characteristics of the observable, and the tensor rank is independent of the time dependence. The transformation properties of these tensors, coupled with their time-reversal invariance, specify the fundamental characteristics of the observables.

Table 19.2 summarizes the transformation properties under rotation, spatial inversion and time reversal for observables encountered in classical mechanics and electrodynamics. Note that observables can be scalar, vector, pseudovector, or second-order tensors, under rotation, and even or odd under either space inversion or time inversion. For example, in classical mechanics the inertia tensor $\mathbf{I}$ relates the angular velocity vector $\boldsymbol{\omega}$ to the angular momentum vector $\mathbf{L }$ by taking the inner product $\mathbf{L} = \mathbf{I} \cdot \boldsymbol{\omega}$. In general $\mathbf{I}$ is not diagonal and thus the angular momentum is not parallel to the angular velocity $\boldsymbol{\omega}$. A similar example in electrodynamics is the dielectric tensor $\mathbf{K}$ which relates the displacement field $\mathbf{D}$ to the electric field $\mathbf{E}$ by $\mathbf{D} = \mathbf{K} \cdot \mathbf{E}$. For anisotropic crystal media $\mathbf{K}$ is not diagonal leading to the electric field vectors $\mathbf{E}$ and $\mathbf{D}$ not being parallel.

As discussed in chapter $7$, Noether’s Theorem states that symmetries of the transformation properties lead to important conservation laws. The behavior of classical systems under rotation relates to the conservation of angular momentum, the behavior under spatial inversion relates to parity conservation, and time-reversal invariance relates to conservation of energy. That is, conservative forces conserve energy and are time-reversal invariant.

| Physical Observable |  | Rotation (Tensor rank) | Space inversion | Time reversal | Name |
| --- | --- | --- | --- | --- | --- |
| *1) Classical Mechanics* |  |  |  |  |  |
| Mass density | $\rho$ | 0 | Even | Even | Scalar |
| Kinetic energy | $p^2/2m$ | 0 | Even | Even | Scalar |
| Potential energy | $U(r)$ | 0 | Even | Even | Scalar |
| Lagrangian | $L$ | 0 | Even | Even | Scalar |
| Hamiltonian | $H$ | 0 | Even | Even | Scalar |
| Gravitational potential | $\phi$ | 0 | Even | Even | Scalar |
| Coordinate | $\mathbf{r}$ | 1 | Odd | Even | Vector |
| Velocity | $\mathbf{v}$ | 1 | Odd | Odd | Vector |
| Momentum | $\mathbf{p}$ | 1 | Odd | Odd | Vector |
| Angular momentum | $\mathbf{L} = \mathbf{r} \times \mathbf{p}$ | 1 | Even | Odd | Pseudovector |
| Force | $\mathbf{F}$ | 1 | Odd | Even | Vector |
| Torque | $\mathbf{N} = \mathbf{r} \times \mathbf{F}$ | 1 | Even | Even | Pseudovector |
| Gravitational field | $\mathbf{g}$ | 1 | Odd | Even | Vector |
| Inertia tensor | $\mathbf{I}$ | 2 | Even | Even | Tensor |
| Elasticity stress tensor | $\mathbf{T}_{ik}$ | 2 | Even | Even | Tensor |
|  |  |  |  |  |  |
| *2) Electromagnetism* |  |  |  |  |  |
| Charge density | $\rho$ | 0 | Even | Even | Scalar |
| Current density | $\mathbf{j}$ | 1 | Odd | Odd | Vector |
| Electric field | $\mathbf{E}$ | 1 | Odd | Even | Vector |
| Polarization | $\mathbf{P}$ | 1 | Odd | Even | Vector |
| Displacement | $\mathbf{D}$ | 1 | Odd | Even | Vector |
| Magnetic $B$ field | $\mathbf{B}$ | 1 | Even | Odd | Pseudovector |
| Magnetization | $\mathbf{M}$ | 1 | Even | Odd | Pseudovector |
| Magnetic $H$ field | $\mathbf{H}$ | 1 | Even | Odd | Pseudovector |
| Poynting vector | $\mathbf{S} = \mathbf{E} \times \mathbf{H}$ | 1 | Odd | Odd | Vector |
| Dielectric tensor | $\mathbf{K}$ | 2 | Even | Even | Tensor |
| Maxwell stress tensor | $\mathbf{T}_{ik}$ | 2 | Even | Even | Tensor |

<sup>1</sup>The common convention is to denote the scalar product as $\mathbf{a} \cdot \mathbf{b}$, the vector product as $\mathbf{a} \times \mathbf{b}$, and tensor product as $\mathbf{a} \otimes \mathbf{b}$.

<sup>2</sup>Based on table 6.1 in *"Classical Electrodynamics"* $2^{nd}$ edition, by J.D. Jackson [Jac75]

## 19.7: Appendix - Aspects of Multivariate Calculus

Multivariate calculus provides the framework for handling systems having many variables associated with each of several bodies. It is assumed that the reader has studied linear differential equations plus multivariate calculus and thus has been exposed to the calculus used in classical mechanics. Chapter $5$ of this book introduced variational calculus which covers several important aspects of multivariate calculus such as Euler’s variational calculus and Lagrange multipliers. This appendix provides a brief review of a selection of other aspects of multivariate calculus that feature prominently in classical mechanics.

### Partial Differentiation

The extension of the derivative to multivariate calculus involves use of [partial derivatives](https://math.libretexts.org/Bookshelves/Calculus/Book%3A_Calculus_(OpenStax)/14%3A_Differentiation_of_Functions_of_Several_Variables/14.3%3A_Partial_Derivatives). The partial derivative with respect to the variable $x_i$ of a multivariate function $f(x_1, x_2,...., x_N )$ involves taking the normal one-variable derivative with respect to $x_i$ assuming that the other $N − 1$ variables are held constant. That is,

$$
\dfrac{\partial f\left(x_{1}, x_{2}, \ldots x_{N}\right)}{\partial x_{i}}=\lim _{h_{i} \rightarrow 0}\left[\dfrac{f\left(x_{1}, x_{2}, \ldots x_{i-1},\left(x_{i}+h_{i}\right), \ldots x_{N}\right)-f\left(x_{1}, x_{2}, \ldots, x_{N}\right)}{h_{i}}\right] \label{F.1}
$$

where it will be assumed that the function $f(x)$ is a continuously-differentiable function to $n^{th}$ order, then all partial derivatives of that order or less are independent of the order in which they are performed. That is,

$$
\dfrac{\partial^2 f(x)}{\partial x_i \partial x_j} = \dfrac{\partial^2 f(x)}{\partial x_j \partial x_i} \label{F.2}
$$

The chain rule for partial differentiation gives that

$$
\dfrac{\partial f (y_1, y_2, ...., y_N )}{ \partial y_j} = \sum^N_{k=1} \dfrac{\partial f(x)}{ \partial x_k} \dfrac{\partial x_k (y)}{\partial y_j} \label{F.3}
$$

The total differential of a multivariate function $f(x)$ is

$$
df = \sum^N_{k=1} \dfrac{\partial f(x)}{ \partial x_k} dx_k \label{F.4}
$$

This can be extended to higher-order derivatives using the operator formalism

$$
d^{n} f(x)=\left(d x_{1} \dfrac{\partial}{\partial x_{1}}+\ldots+d x_{N} \dfrac{\partial}{\partial x_{N}}\right)^{n} f(x)=\sum d x_{j_{1}} \ldots d x_{j_{n}} \dfrac{\partial^{n} f(x)}{\partial x_{j_{1}} \ldots \partial x_{j_{n}}} \label{F.5}
$$

### Linear Operators

The linear operator notation provides a powerful, elegant, and compact way to express, and apply, the equations of multivariate calculus; it is used extensively in mathematics and physics. The linear operators typically comprise partial derivatives that act on scalar, vector, or tensor fields. Table 19.1 lists a few elementary examples of the use of linear operators in this textbook. The first four linear operators involve the widely used del operator $\boldsymbol{\nabla}$ to generate the gradient, divergence and curl as described in appendices $19.7$ and $19.8$. The fifth and sixth linear operators act on the Lagrangian in Lagrangian mechanics applications. The final two linear operators act on the wavefunction for wave mechanics.

| Name | Partial derivative | Field | Action |
| --- | --- | --- | --- |
| Gradient | $\boldsymbol{\nabla} \equiv \hat{i} \dfrac{\partial}{ \partial x} + \hat{j} \dfrac{\partial}{ \partial y} + \mathbf{\hat{k}} \dfrac{\partial}{ \partial z}$ | Scalar potential $V$ | $\mathbf{E} = \boldsymbol{\nabla}V$ |
| Divergence | $\boldsymbol{\nabla} \cdot \equiv \left( \hat{i} \dfrac{\partial}{ \partial x} + \hat{j} \dfrac{\partial}{ \partial y} + \mathbf{\hat{k}} \dfrac{\partial}{ \partial z} \right) \cdot$ | Vector field $\mathbf{E}$ | $\boldsymbol{\nabla} \cdot \mathbf{E}$ |
| Curl | $\boldsymbol{\nabla} \times \equiv \left( \hat{i} \dfrac{\partial}{ \partial x} + \hat{j} \dfrac{\partial}{ \partial y} + \mathbf{\hat{k}} \dfrac{\partial}{ \partial z} \right) \times$ | Vector field $\mathbf{E}$ | $\boldsymbol{\nabla} \times \mathbf{E}$ |
| Laplacian | $\nabla^2 = \boldsymbol{\nabla} \cdot \boldsymbol{\nabla} \equiv \dfrac{\partial^2}{ \partial x^2} + \dfrac{\partial^2}{ \partial y^2} + \dfrac{\partial^2}{ \partial z^2}$ | Scalar potential $V$ | $\nabla^2V$ |
| Euler-Lagrange | $\Lambda_j \equiv \dfrac{d}{dt} \dfrac{\partial}{ \partial \dot{q}_j} − \dfrac{\partial}{ \partial q_j}$ | Scalar Lagrangian $L$ | $\Lambda L = 0$ |
| Canonical momentum | $p_j \equiv \dfrac{\partial}{ \partial \dot{q}_j}$ | Scalar Lagrangian $L$ | $p_j \equiv \dfrac{\partial L}{ \partial \dot{q}_j}$ |
| Canonical momentum | $p_j \equiv \dfrac{\hbar}{ i} \dfrac{\partial}{ \partial \dot{q}_j}$ | Wavefunction $\Psi$ | $p_j\Psi \equiv \dfrac{\hbar}{ i} \dfrac{\partial \Psi}{ \partial \dot{q}_j}$ |
| Hamiltonian | $H = i\hbar \dfrac{ \partial }{ \partial t}$ | Wavefunction $\Psi$ | $H\Psi = i\hbar \dfrac{ \partial \Psi}{ \partial t} = E\Psi$ |

There are three ways of expressing operations such as addition, multiplication, transposition or inversion of operations that are completely equivalent because they all are based on the same principles of linear algebra. For example, a transformation $\mathbf{O}$ acting on a vector $\mathbf{A}$ can produce the vector $\mathbf{B}$. The simplest way to express this transformation is in terms of components

$$
B_i = \sum^3_{j=1} O_{ij}A_j \label{F.6}
$$

Another way is to use matrix mechanics where the $3 \times 3$ matrix $(\mathbf{O})$ transforms the column vector $(\mathbf{A})$ to the column vector $(\mathbf{B})$, that is,

$$
(\mathbf{B})=(\mathbf{O}) (\mathbf{A}) \label{F.7}
$$

The third approach is to assume an operator $\mathbf{O}$ acts on the vector $\mathbf{A}$

$$
\mathbf{B} = \mathbf{OA} \label{F.8}
$$

In classical mechanics, and quantum mechanics, these three equivalent approaches are used and exploited extensively and interchangeably. In particular the rules of matrix manipulation, that are given in appendix $19.1$, are synonymous, and equivalent to, those that apply for operator manipulation. If the operator is complex then the operator properties are summarized as follows.

The generalization of the transpose for complex operators is the *Hermitian conjugate* $O^{\dagger}$

$$
O^{\dagger}_{ij} = O^*_{ji} \label{F.9}
$$

Note also that

$$
\mathbf{O}^{\dagger} = (O^*)^T = (O^T )^* \label{F.10}
$$

The generalization of a symmetric matrix is *Hermitian*, that is, $O$ is equal to its Hermitian conjugate

$$
O^{\dagger}_{ij} = O^*_{ji} = O_{ij} \label{F.11}
$$

For a real matrix the complex conjugation has no effect so the matrix is real and symmetric.

The generalization of orthogonal is *unitary* for which the operator is unitary if it is non-singular and

$$
O^{−1} = O^{\dagger} \label{F.12}
$$

which implies

$$
OO^{\dagger} = U = O^{\dagger}O \label{F.13}
$$

### Transformation Jacobian

The Jacobian determinant, which is usually called the [Jacobian](https://math.libretexts.org/Bookshelves/Calculus/Supplemental_Modules_(Calculus)/Vector_Calculus/3%3A_Multiple_Integrals/3.8%3A_Jacobians), is used extensively in mechanics for both rotational and translational coordinate transformations. The Jacobian determinant is defined as being the ratio of the $n$-dimensional volume element $dx_1dx_2...dx_n$ in one coordinate system, to the volume element $dy_1dy_2...dy_n$ in the second coordinate system. That is

$$
J\left(y_{1} y_{2} \ldots y_{n}\right) \equiv \dfrac{\partial x_{1} \partial x_{2} \ldots \partial x_{n}}{\partial y_{1} \partial y_{2} \ldots \partial y_{n}}=\begin{vmatrix}

\dfrac{\partial x_{1}}{\partial y_{1}} & \dfrac{\partial x_{1}}{\partial y_{2}} & \ldots & \dfrac{\partial x_{1}}{\partial y_{n}} \\ \dfrac{\partial x_{2}}{\partial y_{1}} & \dfrac{\partial x_{2}}{\partial y_{2}} & \cdots & \dfrac{\partial x_{2}}{\partial y_{n}} \\ \vdots & \vdots & \vdots & \vdots \\ \dfrac{\partial x_{n}}{\partial y_{1}} & \dfrac{\partial x_{n}}{\partial y_{2}} & \ldots & \dfrac{\partial x_{n}}{\partial y_{n}} \end{vmatrix} \label{F.14}
$$

#### Transformation of integrals

Consider a coordinate transformation for the integral of the function $f(x_1, x_2, ..x_n)$ to the integral of a function $g(y_1, y_2, ...y_n)$ where $y_i = h (x_1, x_2, ...x_n)$. The coordinate transformation of the integral equation can be expressed in terms of the Jacobian $J(y_1y_2...y_n)$

$$
\begin{align} \label{F.15} \int f\left(x_{1}, x_{2}, \ldots x_{n}\right) d x_{1} d x_{2} \ldots d x_{n} &=\int g\left(y_{1}, y_{2}, \ldots y_{n}\right) d y_{1} d y_{2} \ldots d y_{n}=\\ \int f\left(x_{1}, x_{2}, \ldots x_{n}\right) \dfrac{\partial x_{1} \partial x_{2} \ldots \partial x_{n}}{\partial y_{1} \partial y_{2} \ldots \partial y_{n}} d y_{1} d y_{2} \ldots d y_{n} &=\int f\left(y_{1}, y_{2}, . . y_{n}\right) J\left(y_{1}, y_{2}, \ldots y_{n}\right) d y_{1} d y_{2} \ldots d y_{n} \nonumber \end{align}
$$

#### Transformation of differential equations

The differential cross sections for scattering can be defined either by the number of a definite kind of particle/per event, going into the volume element in momentum space $dp_1dp_2dp_3$, or by the number going into the solid angle element having momentum between $p$ and $p + dp$. That is, the first definition can be written as a differential equation

$$
\dfrac{\partial^3S(p_1, p_2, p_3)}{ \partial p_1\partial p_2\partial p_3 } dp_1dp_2dp_3 = \dfrac{\partial^3 S (p_1(p\theta \phi ), p_2(p\theta \phi ), p_3(p\theta \phi )) }{\partial p_1\partial p_2\partial p_3 } \dfrac{\partial (p_1, p_2, p_3) }{\partial (p, \theta , \phi )} dpd\theta d\phi \label{F.16}
$$

As shown in table $19.3.4$, $dp_1dp_2dp_3 = p^2 \sin \theta dpd\theta d\phi$, that is, the Jacobian equals $p^2 \sin \theta$. Thus Equation \ref{F.16} can be written as

$$
\dfrac{\partial^3S(p_1, p_2, p_3)}{ \partial p_1\partial p_2\partial p_3} dp_1dp_2dp_3 = \left[\dfrac{ \partial^3S }{\partial p_1\partial p_2\partial p_3} p^2 \right] (\sin \theta dpd\theta d\phi ) = \dfrac{\partial^2 \sigma (p, \theta , \phi )}{ \partial p\partial \Omega} dpd\Omega \label{F.17}
$$

The differential cross section is defined by

$$
\dfrac{\partial^2\sigma (p, \theta , \phi )}{ \partial p\partial \Omega} \equiv \dfrac{\partial^3S}{ \partial p_1\partial p_2\partial p_3} p^2 \label{F.18}
$$

where the $p^2$ factor is absorbed into the cross section and the solid angle term is factored out

#### Properties of the Jacobian

In classical mechanics the Jacobian often is extended from 3 dimensions to $n$-dimensional transformations. The Jacobian is unity for unitary transformations such as rotations and linear translations which implies that the volume element is preserved. It will be shown that this also is true for a certain class of transformations in classical mechanics that are called canonical transformations. The Jacobian transforms the local density to be correct for any scale transformations such as transforming linear dimensions from centimeters to inches.

Example 19.1: Jacobian for transform from cartesian to spherical coordinates

Consider the transform in the three-dimensional integral $\int (x_1, x_2, x_3)dx_1dx_2dx_3$ under transformation from cartesian coordinates $(x_1, x_2, x_3)$ to spherical coordinates $(r, \theta , \phi )$. The transformation is governed by the geometric relations $x_1 = r \sin \theta \cos \phi , x_2 = r \sin \theta \sin \phi , x_3 = r \cos \theta$. For this transformation the Jacobian determinant equals

$$
J(r, \theta, \phi)= \begin{vmatrix} \sin \theta \cos \phi & r \cos \theta \cos \phi & -r \sin \theta \sin \phi \\ \sin \theta \sin \phi & r \cos \theta \sin \phi & r \sin \theta \cos \phi \\ \cos \theta & -r \sin \theta & 0 \end{vmatrix} = r^{2} \sin \theta \nonumber
$$

Thus the three-dimensional volume integral transforms to

$$
\int f(x_1, x_2, x_3)dx_1dx_2dx_3 = \int f(r, \theta , \phi ) J (r, \theta , \phi ) drd\theta d\phi = \int f(r, \theta , \phi )r^2 \sin \theta drd\theta d\phi \nonumber
$$

which is the well-known volume integral in spherical coordinates.

### Legendre transformation

Hamiltonian mechanics can be derived directly from Lagrange mechanics by considering the Legendre transformation between the conjugate variables $(\mathbf{q}, \mathbf{\dot{q}}, t)$ and $(\mathbf{q}, \mathbf{p}, t)$. Such a derivation is of considerable importance in that it shows that Hamiltonian mechanics is based on the same variational principles as those used to derive Lagrangian mechanics; that is d’Alembert’s Principle or Hamilton’s Principle. The general problem of converting Lagrange’s equations into the Hamiltonian form hinges on the inversion of equation $(8.1.3)$ that defines the generalized momentum $\mathbf{p}$. This inversion is simplified by the fact that $(8.1.3)$ is the first partial derivative of the Lagrangian $L(\mathbf{q}, \mathbf{\dot{q}}, t)$ which is a scalar function.

Consider transformations between two functions $F(\mathbf{u}, \mathbf{w})$ and $G(\mathbf{v}, \mathbf{w})$ where $\mathbf{u}$ and $\mathbf{v}$ are the active variables related by the functional form

$$
\mathbf{v} = \boldsymbol{\nabla}_{\mathbf{u}} F(\mathbf{u}, \mathbf{w}) \label{F.19}
$$

and where $\mathbf{w}$ designates passive variables and $\boldsymbol{\nabla}_{\mathbf{u}}F(\mathbf{u}, \mathbf{w})$ is the first-order derivative of $F(\mathbf{u}, \mathbf{w})$, i.e. the gradient, with respect to the components of the vector $\mathbf{u}$. The Legendre transform states that the inverse formula can always be written in the form

$$
\mathbf{u} = \boldsymbol{\nabla}_{\mathbf{v}}G(\mathbf{v}, \mathbf{w}) \label{F.20}
$$

where the function $G(\mathbf{v}, \mathbf{w})$ is related to $F(\mathbf{u}, \mathbf{w})$ by the symmetric relation

$$
G(\mathbf{v}, \mathbf{w}) + F(\mathbf{u}, \mathbf{w}) = \mathbf{u} \cdot \mathbf{v} \label{F.21}
$$

and where the scalar product $\mathbf{u} \cdot \mathbf{ v} = \sum^N_{i = 1} u_iv_i$.

Furthermore the derivatives with respect to all the passive variables $\{w_i\}$ are related by

$$
\boldsymbol{\nabla}_{\mathbf{w}}F(\mathbf{u}, \mathbf{w}) = −\boldsymbol{\nabla}_{\mathbf{w}} G(\mathbf{v}, \mathbf{w}) \label{F.22}
$$

The relationship between the functions $F(\mathbf{u}, \mathbf{w})$ and $G(\mathbf{v}, \mathbf{w})$ is symmetrical and each is said to be the Legendre transform of the other.

### Exercises

1. Below you will find a set of integrals. Your teaching assistant will divide you into groups and each group will be assigned one integral to work on. Once your group has solved the integral, write the solution on the board in the space provided by the teaching assistant.

(a) $\int^{2\pi}_0 \int^{\pi/4}_{0} \int^{\cos \theta}_0 r^2 \sin \theta dr d\theta d \phi$

(b) $\int (\dfrac{\mathbf{\dot{r}}}{r} - \dfrac{\mathbf{r}\dot{r}}{r^2}) dt$

(c) $\int_S \mathbf{A} \cdot d\mathbf{a}$ where $\mathbf{A} = x\hat{i} + y\hat{j} + z\mathbf{\hat{k}}$ and $S$ is the sphere $x^2 + y^2 + z^2 = 9$.

(d) $\int_S ( \boldsymbol{\nabla} \times \mathbf{A}) \cdot d\mathbf{a}$ where $\mathbf{A} = y\hat{i} + z\hat{j} + x\mathbf{\hat{k}}$ and $S$ is the surface defined by the paraboloid $z = 1−x^2 − y^2$, where $z \geq 0$.

## 19.8: Appendix - Vector Differential Calculus

This appendix reviews vector differential calculus which is used extensively in both classical mechanics and electromagnetism.

### Scalar differential operators

#### Scalar field

Differential operators like time $\left( \frac{d}{dt} \right)$ do not change the rotational properties of scalars or proper vectors. A scalar operator $\frac{d}{ds}$ acting on a scalar field $\phi (xyz)$, in a rotated coordinated frame $\phi^{\prime} (x^{\prime} y^{\prime} z^{\prime} )$ is unchanged.

$$
\frac{d\phi^{\prime}}{ds} = \frac{d\phi}{ds} \label{G.1}
$$

#### Vector field

Similarly for a proper vector field

$$
\frac{dA^{\prime}_i}{ ds} = \sum_j \lambda_{ij} \frac{dA_j}{ds} \label{G.2}
$$

That is, differentiation of scalar or vector fields with respect to a scalar operator does not change the rotational behavior. In particular, the scalar differentials of vectors continue to obey the rules of ordinary proper vectors. The scalar operator $\frac{\partial}{ \partial t}$ is used for calculation of velocity or acceleration.

### Vector differential operators in cartesian coordinates

Vector differential operators, such as the gradient operator, are important in physics. The action of vector operators differ along different orthogonal axes.

#### Scalar field

Consider a continuous, single-valued scalar function $\phi (x_i, x_j, x_k)$. Since

$$
\phi^{\prime} = \phi \label{G.3}
$$

then the partial differential with respect to one component $x_i$ of the vector $\mathbf{x}^{\prime}$ gives

$$
\frac{\partial \phi^{\prime}}{ \partial x^{\prime}_i} = \sum_j \frac{\partial \phi}{ \partial x_j} \frac{\partial x_j}{\partial x^{\prime}_i} \label{G.4}
$$

The inverse rotation gives that

$$
x_j= \sum_k \lambda_{kj}x^{\prime}_k \label{G.5}
$$

Therefore

$$
\frac{\partial x_j}{\partial x^{\prime}_i } = \sum_k \lambda_{kj} \frac{\partial x^{\prime}_k }{\partial x^{\prime}_i } = \sum_k \lambda_{kj} \delta_{ik} = \lambda_{ij} \label{G.6}
$$

Thus

$$
\frac{\partial \phi^{\prime}}{ \partial x^{\prime}_i} = \sum_j \lambda_{ij}\frac{ \partial \phi}{ \partial x_j} \label{G.7}
$$

That is the vector derivative acting of a scalar field transforms like a proper vector.

Define the gradient, or $\boldsymbol{\nabla}$ operator, as

$$
\boldsymbol{\nabla} \equiv \sum_i \widehat{\mathbf{e}_i} \frac{\partial}{ \partial x_i} \label{G.8}
$$

where $\widehat{\mathbf{e}_i}$ is the unit vector along the $x_i$ axis. In cartesian coordinates, the del vector operator is,

$$
\boldsymbol{\nabla} \equiv \widehat{\mathbf{i}} \frac{\partial}{ \partial x} + \widehat{\mathbf{j}} \frac{\partial}{ \partial y} + \widehat{\mathbf{k}} \frac{\partial }{ \partial z} \label{G.9}
$$

The gradient was applied to the gravitational and electrostatic potential to derive the corresponding field. For example, for electrostatics it was shown that the gradient of the scalar electrostatic potential field $V$ can be written in cartesian coordinates as

$$
\mathbf{E} = −\boldsymbol{\nabla}V \label{G.10}
$$

Note that the gradient of a scalar field produces a vector field. You are familiar with this if you are a skier in that the gravitational force pulls you down the line of steepest descent for the ski slope.

#### Vector field

Another possible operation for the del operator is the scalar product with a vector. Using the definition of a scalar product in cartesian coordinates gives

$$
\boldsymbol{\nabla} \cdot \mathbf{A}=\widehat{\mathbf{i}} \cdot \widehat{\mathbf{i}} \frac{\partial A_{x}}{\partial x}+\widehat{\mathbf{j}} \cdot \widehat{\mathbf{j}} \frac{\partial A_{y}}{\partial y}+\widehat{\mathbf{k}} \cdot \widehat{\mathbf{k}} \frac{\partial A_{z}}{\partial z}=\frac{\partial A_{x}}{\partial x}+\frac{\partial A_{y}}{\partial y}+\frac{\partial A_{z}}{\partial z} \label{G.11}
$$

This scalar derivative of a vector field is called the divergence. Note that the scalar product produces a scalar field which is invariant to rotation of the coordinate axes.

The vector product of the del operator with another vector, is called the curl which is used extensively in physics. It can be written in the determinant form

$$
\boldsymbol{\nabla} \times \mathbf{A} = \begin{vmatrix} \widehat{\mathbf{i}} & \widehat{\mathbf{j}} & \widehat{\mathbf{k}} \\ \frac{\partial}{ \partial x} & \frac{\partial}{ \partial y} & \frac{\partial}{ \partial z} \\ A_x & A_y & A_z \end{vmatrix} \label{G.12}
$$

By contrast to the scalar product, both the gradient of a scalar field, and the vector product, are vector fields for which the components along the coordinate axes transform in a specific manner, such as to keep the length of the vector constant, as the coordinate frame is rotated. The gradient, scalar and vector products with the $\boldsymbol{\nabla}$ operator are the first order derivatives of fields that occur most frequently in physics.

Second derivatives of fields also are used. Let us consider some possible combinations of the product of two del operators.

##### 1) $\boldsymbol{\nabla} \cdot (\boldsymbol{\nabla}V ) = \nabla^2V$

The scalar product of two del operators is a scalar under rotation. Evaluating the scalar product in cartesian coordinates gives

$$
\left( \widehat{\mathbf{i}} \frac{\partial}{ \partial x} + \widehat{\mathbf{j}} \frac{\partial}{ \partial y} + \widehat{\mathbf{k}} \frac{\partial}{ \partial z} \right) \cdot \left( \widehat{\mathbf{i}} \frac{\partial V}{ \partial x} + \widehat{\mathbf{j}} \frac{\partial V}{ \partial y} + \widehat{\mathbf{k}} \frac{\partial V}{ \partial z} \right) = \frac{\partial^2 V}{ \partial x^2} + \frac{\partial^2V}{ \partial y^2} + \frac{\partial^2V}{ \partial z^2} \label{G.13}
$$

This also can be obtained without confusion by writing this product as;

$$
\boldsymbol{\nabla} \cdot (\boldsymbol{\nabla}V ) = \boldsymbol{\nabla} \cdot \boldsymbol{\nabla}V = (\boldsymbol{\nabla} \cdot \boldsymbol{\nabla}) V \label{G.14}
$$

where the scalar product of the del operator is a scalar, called the Laplacian $\nabla^2$, given by

$$
\boldsymbol{\nabla} \cdot \boldsymbol{\nabla} = \nabla^2 \equiv \frac{\partial^2}{ \partial x^2} + \frac{\partial^2}{ \partial y^2} + \frac{\partial^2}{ \partial z^2} \label{G.15}
$$

The Laplacian operator is encountered frequently in physics.

##### 2) $\boldsymbol{\nabla}\times (\boldsymbol{\nabla}V )=0$

Note that the vector product of two identical vectors

$$
\mathbf{A} \times \mathbf{A} = 0 \label{G.16}
$$

Therefore

$$
\boldsymbol{\nabla}\times (\boldsymbol{\nabla}V )=0 \label{G.17}
$$

This can be confirmed by evaluating the separate components along each axis.

##### 3) $\boldsymbol{\nabla} \cdot (\boldsymbol{\nabla} \times \mathbf{A})=0$

This is zero because the cross-product is perpendicular to $\boldsymbol{\nabla} \times \mathbf{A}$ and thus the dot product is zero.

##### 4) $\boldsymbol{\nabla}\times (\boldsymbol{\nabla} \times \mathbf{A}) = \boldsymbol{\nabla} \cdot (\boldsymbol{\nabla} \cdot \mathbf{A}) − \nabla^2\mathbf{A}$

The identity

$$
\mathbf{A} \times (\mathbf{B} \times \mathbf{C}) = \mathbf{B} (\mathbf{A} \cdot \mathbf{C}) − (\mathbf{A} \cdot \mathbf{B}) \mathbf{C} \label{G.18}
$$

can be used to give

$$
\boldsymbol{\nabla}\times (\boldsymbol{\nabla} \times \mathbf{A}) = \boldsymbol{\nabla} \cdot (\boldsymbol{\nabla} \cdot \mathbf{A}) − \nabla^2\mathbf{A} \label{G.19}
$$

since $\boldsymbol{\nabla} \cdot \boldsymbol{\nabla} = \nabla^2$.

There are pitfalls in the discussion of second derivatives in that it is assumed that both del operators operate on the same variable, otherwise the results are different.

### Vector differential operators in curvilinear coordinates

As discussed in Appendix $19.3$ there are many situations where the symmetries make it more convenient to use orthogonal curvilinear coordinate systems rather than cartesian coordinates. Thus it is necessary to extend vector derivatives from cartesian to curvilinear coordinates. Table $19.3.1$ can be used for expressing vector derivatives in curvilinear coordinate systems.

#### Gradient

The gradient in curvilinear coordinates is

$$
\boldsymbol{\nabla}f = \frac{1}{h_1} \frac{\partial f}{ \partial q_1} \mathbf{\hat{q}}_1 + \frac{1}{h_2} \frac{\partial f}{ \partial q_2} \mathbf{\hat{q}}_2 + \frac{1}{h_3} \frac{\partial f}{ \partial q_3} \mathbf{\hat{q}}_3 \label{G.20}
$$

where the coefficients $h_i$ are listed in table $19.3.1$. For cylindrical coordinates this becomes

$$
\boldsymbol{\nabla}f = \frac{\partial f}{ \partial \rho} \boldsymbol{\hat{\rho}} + \frac{1}{ \rho} \frac{\partial f}{ \partial \varphi } \boldsymbol{\hat{\varphi}} + \frac{\partial f}{ \partial z} \mathbf{\hat{z}} \label{G.21}
$$

In spherical coordinates

$$
\boldsymbol{\nabla}f = \frac{\partial f}{ \partial r} \mathbf{\hat{r}} + \frac{1}{ r} \frac{\partial f}{ \partial \theta} \boldsymbol{\hat{\theta}} + \frac{1}{ r \sin \theta} \frac{\partial f}{ \partial \varphi} \boldsymbol{\hat{\varphi}} \label{G.22}
$$

#### Divergence

The divergence can be expressed as

$$
\boldsymbol{\nabla} \cdot \mathbf{A} = \frac{1}{h_1h_2h_3} \left[ \frac{\partial}{ \partial q_1} (A_1h_2h_3) + \frac{\partial}{ \partial q_2 } (A_2h_3h_1) + \frac{\partial}{ \partial q_3} (A_3h_1h_2) \right] \label{G.23}
$$

In cylindrical coordinates the divergence is

$$
\boldsymbol{\nabla} \cdot \mathbf{A} = \frac{1}{\rho} \frac{\partial}{ \partial \rho} (\rho A_{\rho}) + \frac{1}{\rho} \frac{\partial A_{\varphi}}{ \partial \varphi} + \frac{\partial A_z}{ \partial z} = \frac{A_{\rho}}{ \rho} + \frac{\partial A_{\rho}}{ \partial \rho} + \frac{1}{\rho} \frac{\partial A_{\varphi}}{ \partial \varphi} + \frac{\partial A_z}{ \partial z} \label{G.24}
$$

In spherical coordinates the divergence is

$$
\boldsymbol{\nabla} \cdot \mathbf{A} = \frac{1}{ r^2 \sin \theta} \left[ \frac{\partial}{ \partial r} \left( A_r r^2 \sin \theta \right) + \frac{\partial}{ \partial \theta} (A_{\theta} r \sin \theta ) + \frac{\partial}{ \partial \varphi} (A_{\varphi} r) \right] \label{G.25}
$$

#### Curl

$$
\boldsymbol{\nabla} \times \mathbf{A}= \frac{1}{h_{1} h_{2} h_{3}} \begin{vmatrix} h_{1} \mathbf{\hat{q}}_{1} & h_{2} \mathbf{\hat{q}}_{2} & h_{3} \mathbf{\hat{q}}_{3} \\

\frac{\partial}{\partial q_{1}} & \frac{\partial}{\partial q_{2}} & \frac{\partial}{\partial q_{3}} \\ h_{1} A_{1} & h_{2} A_{2} & h_{3} A_{3} \end{vmatrix} \label{G.26}
$$

In cylindrical coordinates the curl is

$$
\boldsymbol{\nabla} \times \mathbf{A}=\frac{1}{\rho} \begin{vmatrix}

\boldsymbol{\hat{\rho}} & \rho \boldsymbol{\hat{\varphi}} & \mathbf{\hat{z}} \\

\frac{\partial}{\partial \rho} & \frac{\partial}{\partial \varphi} & \frac{\partial}{\partial z} \\

A_{\rho} & \rho A_{\varphi} & A_{z} \end{vmatrix} \label{G.27}
$$

In spherical coordinates the curl is

$$
\boldsymbol{\nabla} \times \mathbf{A}=\frac{1}{r^{2} \sin \theta}\begin{vmatrix}

\mathbf{\hat{r}} & r \boldsymbol{\hat{\theta}} & r \sin \theta \boldsymbol{\hat{\varphi}} \\

\frac{\partial}{\partial r} & \frac{\partial}{\partial \theta} & \frac{\partial}{\partial \varphi} \\

A_{r} & r \rho A_{\theta} & r \sin \theta A_{\varphi} \end{vmatrix} \label{G.28}
$$

#### Laplacian

Taking the divergence of the gradient of a scalar gives

$$
\nabla^2f = \boldsymbol{\nabla} \cdot \boldsymbol{\nabla}f = \frac{1}{h_1h_2h_3} \left[ \frac{\partial}{ \partial q_1} \left(\frac{h_2h_3 }{h_1} \frac{\partial f}{ \partial q_1} \right) + \frac{\partial}{ \partial q_2} \left(\frac{h_3h_1}{h_2} \frac{\partial f}{ \partial q_2} \right) + \frac{\partial}{ \partial q_3} \left(\frac{h_1h_2 }{h_3} \frac{\partial f}{ \partial q_3} \right)\right] \label{G.29}
$$

The Laplacian of a scalar function $f$ in cylindrical coordinates is

$$
\nabla^2f = \frac{1}{\rho} \frac{\partial}{ \partial \rho} \left( \rho \frac{\partial f}{ \partial \rho} \right) + \frac{1}{ \rho^2} \frac{\partial^2f}{ \partial \varphi^2} + \frac{\partial^2f}{ \partial z^2} \label{G.30}
$$

The Laplacian of a scalar function $f$ in spherical coordinates is

$$
\nabla^2f = \frac{1}{ r^2} \frac{\partial}{ \partial r} \left( r^2 \frac{\partial f}{ \partial r} \right) + \frac{1}{ r^2 \sin \theta} \frac{\partial}{ \partial \theta} \left( \sin \theta \frac{\partial f}{ \partial \theta} \right) + \frac{1}{ r^2 \sin \theta } \frac{ \partial^2f}{ \partial \varphi^2} \label{G.31}
$$

The gradient, divergence, curl and Laplacian are used extensively in curvilinear coordinate systems when dealing with vector fields in Newtonian mechanics, electromagnetism, and fluid flow.

## 19.9: Appendix - Vector Integral Calculus

Field equations, such as for electromagnetic and gravitational fields, require both line integrals, and surface integrals, of vector fields to evaluate potential, flux and circulation. These require use of the gradient, the Divergence Theorem and Stokes Theorem which are discussed in the following sections.

### Line integral of the gradient of a scalar field

The change $\Delta V$ in a scalar field for an infinitessimal step $d\mathbf{l}$ along a path can be written as

$$
\Delta V = (\boldsymbol{\nabla}V ) \cdot d\mathbf{l} \label{H.1}
$$

since the gradient of $V$, that is, $\boldsymbol{\nabla}V$, is the rate of change of $V$ with $d\mathbf{l}$. Discussions of gravitational and electrostatic potential show that the line integral between points $a$ and $b$ is given in terms of the del operator by

$$
V_b − V_a = \int^b_a (\boldsymbol{\nabla}V ) \cdot d\mathbf{l} \label{H.2}
$$

This relates the difference in values of a scalar field at two points to the line integral of the dot product of the gradient with the element of the line integral.

### Divergence Theorem

#### Flux of a vector field for Gaussian surface

:::{figure} ../images/lt-23023-h1.png
:alt: h1.PNG

$1$: A volume V enclosed by a closed surface S is cut into two pieces at the surface $S_{ab}$. This gives V$_1$ enclosed by S$_1$ and V$_1$ enclosed by S$_2$.
:::

Consider the flux $\Phi$ of a vector field $\mathbf{F}$ for a closed surface, usually called a **Gaussian surface**, $S$ shown in Figure 19.1.

$$
\Phi = \oint_S \mathbf{F} \cdot d\mathbf{S} \label{H.3}
$$

If the enclosed volume is cut in to two pieces enclosed by surfaces $S_1 = S_a + S_{ab}$ and $S_2 = S_b + S_{ab}$. The flux through the surface $S_{ab}$ common to both $S_1$ and $S_2$ are equal and in the same direction. Then the net flux through the sum of $S_1$ and $S_2$ is given by

$$
\oint_{S_1} \mathbf{F} \cdot d\mathbf{S} + \oint_{S_2} \mathbf{F} \cdot d\mathbf{S} = \oint_S \mathbf{F} \cdot d\mathbf{S} \label{H.4}
$$

since the contributions of the common surface $S_{ab}$ cancel in that the flux out of $S_1$ is equal and opposite to the flux into $S_2$ over the surface $S_{ab}$. That is, independent of how many times the volume enclosed by $S$ is subdivided, the net flux for the sum of all the Gaussian surfaces enclosing these subdivisions of the volume, still equals $\oint_S \mathbf{F} \cdot d\mathbf{S}$.

Consider that the volume enclosed by $S$ is subdivided into $N$ subdivisions where $N \rightarrow \infty$, then even though $\oint_{S_i} \mathbf{F} \cdot d\mathbf{S} \rightarrow 0$ as $N \rightarrow \infty$, the sum over surfaces of all the infinitessimal volumes remains unchanged

$$
\Phi = \oint_S \mathbf{F} \cdot d\mathbf{S} = \sum^{N \rightarrow \infty}_i \oint_{S_i} \mathbf{F} \cdot d\mathbf{S} \label{H.5}
$$

Thus we can take the limit of a sum of an infinite number of infinitessimal volumes as is needed to obtain a differential form. The surface integral for each infinitessimal volume will equal zero which is not useful, that is $\oint_{S_i} \mathbf{F} \cdot d\mathbf{S} \rightarrow 0$ as $N \rightarrow \infty$. However, the flux per unit volume has a finite value as $N \rightarrow \infty$. This ratio is called the *divergence* of the vector field;

$$
div \mathbf{F} = Lim_{\Delta \tau_i \rightarrow 0} \frac{\oint_{S_i} \mathbf{F} \cdot d\mathbf{S}}{ \Delta \tau_i} \label{H.6}
$$

where $\Delta \tau_i$ is the infinitessimal volume enclosed by surface $S_i$. The divergence of the vector field is a scalar quantity.

Thus the sum of flux over all infinitessimal subdivisions of the volume enclosed by a closed surface $S$ equals

$$
\Phi = \oint_S \mathbf{F} \cdot d\mathbf{S} = \sum^{N \rightarrow \infty}_i \frac{\oint_{S_i} \mathbf{F} \cdot d\mathbf{S}}{ \Delta \tau_i} \Delta \tau_i = \sum^{N \rightarrow \infty}_i div \mathbf{F}\Delta \tau_i \label{H.7}
$$

In the limit $N \rightarrow \infty$, $\Delta \tau_i \rightarrow 0$, this becomes the integral;

$$
\Phi = \oint_S \mathbf{F} \cdot d\mathbf{S} = \int_{Enclosed \ volume} div \mathbf{F} d\tau \label{H.8}
$$

This is called the [*Divergence Theorem*](https://math.libretexts.org/Bookshelves/Calculus/Book%3A_Calculus_(Guichard)/16%3A_Vector_Calculus/16.09%3A_The_Divergence_Theorem) or Gauss’s Theorem. To avoid confusion with Gauss’s law in electrostatics, it will be referred to as the Divergence theorem.

#### Divergence in Cartesian Coordinates

:::{figure} ../images/lt-23024-h2.png
:alt: h2.PNG

$2$: Computation of flux out of an infinitessimal rectangular box, $\Delta x$, $\Delta y$, $\Delta z$.
:::

Consider the special case of an infinitessimal rectangular box, size $\Delta x, \Delta y, \Delta z$ shown in Figure 19.2. Consider the net flux for the $z$ component $F_z$ *entering* the surface $\Delta x\Delta y$ at location $(x, y, z)$.

$$
\Delta \Phi ^{in}_z = \left( F_z + \frac{\Delta x}{ 2} \frac{\partial F_z}{ \partial x} + \frac{\Delta y}{ 2} \frac{\partial F_z }{\partial y} \right) \Delta x\Delta y \label{H.9}
$$

The net flux of the $z$ component *out* of the surface at $z + \Delta z$ is

$$
\Delta \Phi ^{out}_z = \left( F_z + \Delta z \frac{\partial F_z}{ \partial z} + \frac{\Delta x}{2} \frac{\partial F_z}{ \partial x} + \frac{\Delta y}{ 2} \frac{\partial F_z}{ \partial y} \right) \Delta x\Delta y \label{H.10}
$$

Thus the net flux out of the box due to the z component of F is

$$
\Delta \Phi _z = \Delta \Phi ^{out}_z − \Delta \Phi ^{in}_z = \frac{\partial F_z}{ \partial z} \Delta x\Delta y\Delta z \label{H.11}
$$

Adding the similar $x$ and $y$ components for $\Delta \Phi$ gives

$$
\Delta \Phi = \left(\frac{\partial F_x}{ \partial x} + \frac{\partial F_y }{\partial y} + \frac{\partial F_z }{\partial z} \right) \Delta x\Delta y\Delta z \label{H.12}
$$

This gives that the divergence of the vector field $\mathbf{F}$ is

$$
div \mathbf{F} = Lim_{\Delta \tau_i \rightarrow 0} \frac{\oint_{S_i} \mathbf{F} \cdot d\mathbf{S}}{ \Delta \tau_i} = \left(\frac{\partial F_x }{\partial x} + \frac{\partial F_y}{ \partial y} + \frac{\partial F_z}{ \partial z} \right) \label{H.13}
$$

since $\Delta \tau = \Delta x\Delta y\Delta z$. But the right hand side of the equation equals the scalar product $\boldsymbol{\nabla} \cdot \mathbf{F}$, that is,

$$
div \mathbf{F} = \boldsymbol{\nabla} \cdot \mathbf{F} \label{H.14}
$$

The divergence is a scalar quantity. The physical meaning of the divergence is that it gives the net flux per unit volume flowing out of an infinitessimal volume. A positive divergence corresponds to a net outflow of flux from the infinitessimal volume at any location while a negative divergence implies a net inflow of flux to this infinitessimal volume.

It was shown that for an infinitessimal rectangular box

$$
\Delta \Phi = \left(\frac{\partial F_x }{\partial x} + \frac{\partial F_y}{ \partial y} + \frac{\partial F_z}{ \partial z} \right) \Delta x\Delta y\Delta z = \boldsymbol{\nabla} \cdot \mathbf{F}\Delta \tau \label{H.15}
$$

Integrating over the finite volume enclosed by the surface $S$ gives

$$
\Phi = \oint_S \mathbf{F} \cdot d\mathbf{S} = \int\limits_{Enclosed \\ volume} \boldsymbol{\nabla} \cdot \mathbf{F} d \tau \label{H.16}
$$

This is another way of expressing the Divergence theorem

$$
\Phi = \oint_S \mathbf{F} \cdot d\mathbf{S} = \int\limits_{Enclosed \\ volume} div \mathbf{F} d \tau \label{H.17}
$$

The divergence theorem, developed by Gauss, is of considerable importance, it relates the surface integral of a vector field, that is, the outgoing flux, to a volume integral of $\boldsymbol{\nabla} \cdot \mathbf{F}$ over the enclosed volume.

Example 19.1: Maxwell's Flux Equations

As an example of the usefulness of this relation, consider the Gauss’s law for the flux in Maxwell’s equations.

Gauss’ Law for the electric field

$$
\Phi _E = \oint_{Closed \ surface} E \cdot dS = \frac{1}{ \varepsilon_0} \int_{enclosed \ volume} \rho d\tau \nonumber
$$

But the divergence relation gives that

$$
\Phi _E = \oint_S \mathbf{E} \cdot d\mathbf{S} = \int_{Enclosed \ volume} \boldsymbol{\nabla} \cdot \mathbf{E} d \tau \nonumber
$$

Combining these gives

$$
\oint_{Closed \ surface} \mathbf{E} \cdot d\mathbf{S} = \int_{Enclosed \ volume} \boldsymbol{\nabla} \cdot \mathbf{E} d \tau = \frac{1}{ \varepsilon_0} \int_{enclosed \ volume} \rho d \tau \nonumber
$$

This is true independent of the shape of the surface or enclosed volume, leading to the differential form of Maxwell’s first law, that is Gauss’s law for the electric field.

$$
\boldsymbol{\nabla} \cdot E = \frac{\rho}{ \varepsilon_0} \nonumber
$$

The differential form of Gauss’s law relates $\boldsymbol{\nabla} \cdot \mathbf{E}$ to the charge density $\rho$ at that same location. This is much easier to evaluate than a surface and volume integral required using the integral form of Gauss’s law.

Gauss’s law for magnetism

$$
\Phi _B = \oint_{Closed \ surface} \mathbf{B} \cdot d\mathbf{S} = 0 \nonumber
$$

Using the divergence theorem gives that

$$
\Phi _B = \oint_{Closed \ surface} \mathbf{B} \cdot d\mathbf{S} = \int_{Enclosed \ volume} \boldsymbol{\nabla} \cdot \mathbf{B} d \tau = 0 \nonumber
$$

This is true independent of the shape of the Gaussian surface leading to the differential form of Gauss’s law for $\mathbf{B}$

$$
\boldsymbol{\nabla} \cdot \mathbf{B} = 0 \nonumber
$$

That is, the local value of the divergence of $\mathbf{B}$ is zero everywhere.

Example 19.2: Buoyancy forces in fluids

Buoyancy in fluids provides an example of the use of flux in physics. Consider a fluid of density $\rho (z)$ in a gravitational field $\bar{g}(z) = −g(z)\hat{z}$ where the $z$ axis points in the opposite direction to the gravitational force. Pressure equals force per unit area and is a scalar quantity. For a conservative fluid system, in static equilibrium, the net work done per unit area for an infinitessimal displacement $d r$ is zero. The net pressure force per unit area is the difference $P(r+ d r)−P(r) = \nabla P \cdot d r$ while the net change in gravitational potential energy is $\rho (z)\bar{g}(z) \cdot d r$. Thus energy conservation gives

$$
[\boldsymbol{\nabla}P + \rho (z)\bar{\mathbf{g}}(\mathbf{z})] \cdot d \mathbf{r} =0 \nonumber
$$

which can be expanded as

$$
\frac{d P}{ d z} = −\rho (z)g(z) \label{19-A} \\ \frac{d P}{ d x} = \frac{d P}{ d y} = 0 \tag{A}
$$

Integrating the net forces normal to the surface over any closed surface enclosing an empty volume, inside the fluid, gives a net buoyancy force on this volume that simplifies using the Divergence theorem

$$
\oint \mathbf{F} \cdot d\mathbf{S}= \oint P d\hat{\mathbf{S}} \cdot d\mathbf{S} = \oint P d S = \int_{Enclosed \ vol} \left( \frac{d P}{ d x} + \frac{d P}{ d y} + \frac{d P}{ d z} \right) d \tau \nonumber
$$

Using equations \ref{19-A} leads to the net buoyancy force

$$
\oint \mathbf{F} \cdot d\mathbf{S}= \int_{Enclosed \ vol} \frac{d P}{ d z} d \tau = − \int_{Enclosed \ vol} \rho (z)g(z) d \tau \nonumber
$$

The right hand side of this equation equals minus the weight of the displaced fluid. That is, the buoyancy force equals the weight of the fluid displaced by the empty volume. Note that this proof applies both to compressible fluids, where the density depends on pressure, as well as to incompressible fluids where the density is constant. It also applies to situations where local gravity $g$ is position dependent. If an object of mass $M$ is completely submerged then the net force on the object is $Mg − \int_{Enclosed \ vol} \rho (z)g(z) d \tau$. If the object floats on the surface of a fluid then the buoyancy force must be calculated separately for the volume under the fluid surface and the upper volume above the fluid surface. The buoyancy due to displaced air usually is negligible since the density of air is about $10^{−3}$ times that of fluids such as water.

### Stokes Theorem

#### The curl

Maxwell’s laws relate the circulation of the field around a closed loop to the rate of change of flux through the surface bounded by the closed loop. It is possible to write these integral equations in a differential form as follows.

Consider the line integral around a closed loop $C$ shown in Figure 19.3.

If this area is subdivided into two areas enclosed by loops $C_1$ and $C_2$, then the sum of the line integrals is the same

$$
\oint_C \mathbf{F} \cdot d\mathbf{l} = \oint_{C_1} \mathbf{F} \cdot d\mathbf{l} + \oint_{C_2} \mathbf{F} \cdot d\mathbf{l} \label{H.18}
$$

because the contributions along the common boundary cancel since they are taken in opposite directions if $C_1$ and $C_2$ both are taken in the same direction. Note that the line integral, and corresponding enclosed area,

are vector quantities related by the right-hand rule and this must be taken into account when subdividing the area. Thus the area can be subdivided into an infinite number of pieces for which

$$
\oint_C \mathbf{F} \cdot d\mathbf{l} = \sum^{N \rightarrow \infty}_i \oint_{C_i} \mathbf{F} \cdot d\mathbf{l} = \sum^{N \rightarrow \infty}_i \frac{\oint_{C_i} \mathbf{F} \cdot d\mathbf{l}}{ \Delta \mathbf{S}_i \cdot \widehat{\mathbf{n}} } \Delta \mathbf{S}_i \cdot \widehat{\mathbf{n}} \label{H.19}
$$

where $\Delta \mathbf{S}_i$ is the infinitessimal area bounded by the closed sub-loop $C_i$ and $\Delta \mathbf{S}_i \cdot \widehat{\mathbf{n}}$ is the normal component of this area pointing along the $\widehat{\mathbf{n}}$ direction which is the direction along which the line integral points.

:::{figure} ../images/lt-23025-h3.png
:alt: h3.PNG

$3$: The circulation around a path is equal to the sum of the circulations around subareas made by subdividing the area.
:::

The component of the curl of the vector function along the direction $\widehat{\mathbf{n}}$ is defined to be

$$
(curl \mathbf{F}) \cdot \widehat{\mathbf{n}} \equiv Lim_{\Delta S\rightarrow 0} \sum^{N \rightarrow \infty}_i \frac{\oint_{C_i} \mathbf{F} \cdot d\mathbf{l}}{ \Delta \mathbf{S}_i \cdot \widehat{\mathbf{n}} } \label{H.20}
$$

Thus the line integral can be written as

$$
\oint_C \mathbf{F} \cdot d\mathbf{l} = \sum^{N \rightarrow \infty}_i \frac{\oint_{C_i} \mathbf{F} \cdot d\mathbf{l}}{ \Delta \mathbf{S}_i \cdot \widehat{\mathbf{n}}} \Delta \mathbf{S}_i \cdot \widehat{\mathbf{n}} \label{H.21} \\ = \int [(curl \mathbf{F}) \cdot \widehat{\mathbf{n}}] d\mathbf{S}_i \cdot \widehat{\mathbf{n}}
$$

The product $\widehat{\mathbf{n}} \cdot \widehat{\mathbf{n}} = 1$, that is, this is true independent of the direction of the infinitessimal loop. Thus the above relation leads to *Stokes Theorem*

$$
\oint_C \mathbf{F} \cdot d\mathbf{l} = \int_{Area \ bounded \ by \ C} (curl \mathbf{F}) \cdot d\mathbf{S} \label{H.22}
$$

This relates the line integral to a surface integral over a surface bounded by the loop.

#### Curl in cartesian coordinates

Consider the infinitessimal rectangle $\Delta x\Delta y$ pointing in the $\widehat{\mathbf{k}}$ direction shown in Figure 19.4.

:::{figure} ../images/lt-23022-h4.png
:alt: h4.PNG

$4$: Circulation around an infinitessimal rectangle $\Delta x\Delta y$ in the z direction.
:::

The line integral, taken in a right-handed way around $\widehat{\mathbf{k}}$ gives

$$
\oint_C \mathbf{F} \cdot d\mathbf{l} = F_x\Delta x + \left( F_y + \frac{\partial F_y}{ \partial x} \Delta x \right) − \left( F_x + \frac{\partial F_x}{ \partial y} \Delta y \right) − F_y\Delta y = \left( \frac{\partial F_y }{\partial x} − \frac{\partial F_x }{\partial y} \right) \Delta x\Delta y \label{H.23}
$$

Thus since $\Delta x\Delta y = \Delta \mathbf{S}_z$ the $z$ component of the curl is given by

$$
(curl \mathbf{F}) \cdot \widehat{\mathbf{k}} = \frac{\oint_{C_i} \mathbf{F} \cdot d\mathbf{l}}{ \Delta \mathbf{S}_i \cdot \widehat{\mathbf{n}}} = \left(\frac{\partial F_y}{ \partial x} − \frac{\partial F_x}{ \partial y} \right) \label{H.24}
$$

The same argument for the component of the curl in the $y$ direction is given by

$$
(curl \mathbf{F}) \cdot\widehat{\mathbf{j}}= \left(\frac{\partial F_x }{\partial z} − \frac{\partial F_z}{ \partial x} \right) \label{H.25}
$$

Similarly the same argument for the component of the curl in the $x$ direction is given by

$$
(curl \mathbf{F}) \cdot\widehat{\mathbf{i}}= \left(\frac{\partial F_z }{\partial y} − \frac{\partial F_y }{\partial z} \right) \label{H.26}
$$

Thus combining the three components of the curl gives

$$
curl \mathbf{F} = \left(\frac{\partial F_z}{ \partial y} − \frac{\partial F_y }{\partial z} \right)\widehat{\mathbf{i}}+ \left(\frac{\partial F_x}{ \partial z} − \frac{\partial F_z}{ \partial x} \right) \widehat{\mathbf{j}} + \left(\frac{\partial F_y }{\partial x} − \frac{\partial F_x }{\partial y} \right) \widehat{\mathbf{k}} \label{H.27}
$$

Note that cross-product of the del operator with the vector $\mathbf{F}$ is

$$
\boldsymbol{\nabla} \times \mathbf{F} = \begin{vmatrix} \widehat{\mathbf{i}} & \widehat{\mathbf{j}} & \widehat{\mathbf{k}} \\ \frac{\partial}{ \partial x} & \frac{\partial}{ \partial y} & \frac{\partial}{ \partial z} \\ F_x & F_y & F_z \end{vmatrix} \label{H.28}
$$

which is identical to the right hand side of the relation for the curl in cartesian coordinates. That is;

$$
\boldsymbol{\nabla} \times \mathbf{F} = curl \overrightarrow{\mathbf{F}} \label{H.29}
$$

Therefore *Stokes Theorem* can be rewritten as

$$
\oint_C \mathbf{F} \cdot d\mathbf{l} = \int_{Area \ bounded \ by \ C} (curl \mathbf{F}) \cdot d\mathbf{S} = \int_{Area \ bounded \ by \ C} (\boldsymbol{\nabla} \times F) \cdot d\mathbf{S} \label{H.30}
$$

The physics meaning of the curl is that it is the circulation, or rotation, for an infinitessimal loop at any location. The word curl is German for rotation.

Example 19.3: Maxwell's circulation equations

As an example of the use of the curl, consider Faraday’s Law

$$
\int_{Closed \ loop \ C} \mathbf{E} \cdot d\mathbf{l} = − \int_{surface \ bounded \ by \ C} \frac{\partial \mathbf{B}}{ \partial t} \cdot \partial \mathbf{S} \nonumber
$$

Using Stokes Theorem gives

$$
\oint_C \mathbf{E} \cdot d\mathbf{l} = \int_{Surface \ bounded \ by \ C} (\boldsymbol{\nabla} \times \mathbf{E}) \cdot d\mathbf{S} \nonumber
$$

These two relations are independent of the shape of the closed loop, thus we obtain Faraday’s Law in the differential form

$$
(\boldsymbol{\nabla} \times \mathbf{E}) = −\frac{\partial \mathbf{B}}{ \partial t} \nonumber
$$

A differential form of the Ampère-Maxwell law also can be obtained from

$$
\int_{Closed \ loop \ C} \mathbf{B} \cdot d\mathbf{l} = \mu_0 \int_{Bounded \ by \ C} (\mathbf{j} + \varepsilon_0 \frac{\partial \mathbf{E}}{ \partial t} ) \cdot d\mathbf{S} \nonumber
$$

Using Stokes Theorem

$$
\oint_C \mathbf{B} \cdot d\mathbf{l} = \int_{Surface \ bounded \ by \ C} (\boldsymbol{\nabla} \times \mathbf{B}) \cdot d\mathbf{S} \nonumber
$$

Again this is independent of the shape of the loop and thus we obtain Ampère-Maxwell law in differential form

$$
\boldsymbol{\nabla} \times \mathbf{B} = \mu_0 \mathbf{j} + \mu_0\varepsilon_0 \frac{\partial \mathbf{E}}{ \partial t} \nonumber
$$

The differential forms of Maxwell’s circulation relations are easier to apply than the integral equations because the differential form relates the curl to the time derivatives at the same specific location.

### Potential formulations of curl-free and divergence-free fields

Interesting consequences result from the Divergence theorem and Stokes Theorem for vector fields that are either curl-free or divergence-free. In particular two theorems result from the second derivatives of a vector field.

#### Theorem 1 - Curl-free (irrotational) fields:

For curl-free fields

$$
\boldsymbol{\nabla} \times \mathbf{F} = 0 \label{H.31}
$$

everywhere. This is automatically obeyed if the vector field is expressed as the gradient of a scalar field

$$
\mathbf{F} = \boldsymbol{\nabla}\phi \label{H.32}
$$

since

$$
\boldsymbol{\nabla}\times (\boldsymbol{\nabla}\phi)=0 \label{H.33}
$$

That is, any curl-free vector field can be expressed in terms of the gradient of a scalar field.

The scalar field $\phi$ is not unique, that is, any constant $\alpha$ can be added to $\phi$ since $\boldsymbol{\nabla}\alpha = 0$, that is, the addition of the constant $\alpha$ does not change the gradient. This independence to addition of a number to the scalar potential is called a gauge invariance discussed in chapter $13.2$, for which

$$
\mathbf{F} = \boldsymbol{\nabla}\phi^{\prime} = \boldsymbol{\nabla} (\phi + \alpha ) = \boldsymbol{\nabla}\phi \label{H.34}
$$

That is, this gauge-invariant transformation does not change the observable $\mathbf{F}$. The electrostatic field $\mathbf{E}$ and the gravitation field $\mathbf{g}$ are examples of irrotational fields that can be expressed as the gradient of scalar potentials.

#### Theorem 2 - Divergence-free (solenoidal) fields:

For divergence-free fields

$$
\boldsymbol{\nabla} \cdot \mathbf{F} = 0 \label{H.35}
$$

everywhere. This is automatically obeyed if the field $\mathbf{F}$ is expressed in terms of the curl of a vector field $\mathbf{G}$ such that

$$
\mathbf{F} = \boldsymbol{\nabla} \times \mathbf{G} \label{H.36}
$$

since $\boldsymbol{\nabla} \cdot \boldsymbol{\nabla} \times \mathbf{G} = \mathbf{0}$. That is, any divergence-free vector field can be written as the curl of a related vector field.

As discussed in chapter $13.2$, the vector potential $\mathbf{G}$ is not unique in that a gauge transformation can be made by adding the gradient of any scalar field, that is, the gauge transformation $\mathbf{G^{\prime}} = \mathbf{G} + \boldsymbol{\nabla}\boldsymbol{\varphi}$ gives

$$
\mathbf{F} = \boldsymbol{\nabla} \times \mathbf{G^{\prime}} = \boldsymbol{\nabla}\times (\mathbf{G} + \boldsymbol{\nabla}\boldsymbol{\varphi}) = \boldsymbol{\nabla} \times \mathbf{G}. \label{H.37}
$$

This gauge invariance for transformation to the vector potential $\mathbf{G^{\prime}}$ does not change the observable vector field $\mathbf{F}$. The magnetic field $\mathbf{B}$ is an example of a solenoidal field that can be expressed in terms of the curl of a vector potential $\mathbf{A}$.

Example 19.4: Electromagnetic fields

Electromagnetic interactions are encountered frequently in classical mechanics so it is useful to discuss the use of potential formulations of electrodynamics.

For electrostatics, Maxwell’s equations give that

$$
\boldsymbol{\nabla} \times \mathbf{E} = 0 \nonumber
$$

Therefore theorem 1 states that it is possible to express this static electric field as the gradient of the scalar electric potential $V$, where

$$
\mathbf{E} = −\boldsymbol{\nabla}V \nonumber
$$

For electrodynamics, Maxwell’s equations give that

$$
(\boldsymbol{\nabla} \times \mathbf{E}) + \frac{\partial \mathbf{B}}{ \partial t} = 0 \nonumber
$$

Assume that the magnetic field can be expressed in the terms of the vector potential $\mathbf{B} = \boldsymbol{\nabla} \times \mathbf{A}$, then the above equation becomes

$$
\boldsymbol{\nabla} \times (\mathbf{E} + \frac{\partial \mathbf{A}}{ \partial t} )=0 \nonumber
$$

Theorem 1 gives that this curl-less field can be expressed as the gradient of a scalar field, here taken to be the electric potential $V$.

$$
(\mathbf{E} + \frac{\partial \mathbf{A}}{ \partial t} ) == −\boldsymbol{\nabla}V \nonumber
$$

that is

$$
\mathbf{E} = −(\boldsymbol{\nabla}V + \frac{\partial \mathbf{A}}{ \partial t} ) \nonumber
$$

Gauss’ law states that

$$
\boldsymbol{\nabla}\cdot \mathbf{E} = \frac{\rho}{ \varepsilon_0} \nonumber
$$

which can be rewritten as

$$
\boldsymbol{\nabla}\cdot \mathbf{E} = −\boldsymbol{\nabla}^2V − \frac{\partial (\boldsymbol{\nabla} \cdot \mathbf{A}) }{\partial t} = \frac{\rho}{ \varepsilon_0} \label{X} \tag{X}
$$

Similarly insertion of the vector potential $\mathbf{A}$ in Ampère’s Law gives

$$
\boldsymbol{\nabla} \times \mathbf{B} = \boldsymbol{\nabla} \times (\boldsymbol{\nabla} \times \mathbf{A})=\mu_0 \mathbf{j} + \mu_0 \varepsilon_0 \frac{\partial\mathbf{ E }}{\partial t} = \mu_0 \mathbf{j} −\mu_0\varepsilon_0\boldsymbol{\nabla} \left(\frac{\partial V}{ \partial t} \right) − \mu_0\varepsilon_0 \left(\frac{\partial^2\mathbf{A}}{ \partial t^2} \right) \nonumber
$$

Using the vector identity $\boldsymbol{\nabla} \times (\boldsymbol{\nabla} \times \mathbf{A}) = \boldsymbol{\nabla} (\boldsymbol{\nabla} \cdot \mathbf{A}) − \boldsymbol{\nabla}^2 A$ allows the above equation to be rewritten as

$$
\left(\nabla^2\mathbf{A}−\mu_0\varepsilon_0 \left(\frac{\partial^2\mathbf{A}}{ \partial t^2} \right)\right) − \boldsymbol{\nabla} \left( \boldsymbol{\nabla} \cdot \mathbf{A}+\mu_0\varepsilon_0 \left(\frac{\partial V }{\partial t} \right)\right) = −\mu_0 \mathbf{j} \tag{Y} \label{Y}
$$

The use of the scalar potential $V$ and vector potential $\mathbf{A}$ leads to two coupled equations \ref{X} and \ref{Y}. These coupled equations can be transformed into two uncoupled equations by exploiting the freedom to make a gauge transformation for the vector potential such that the middle brackets in both equations \ref{X} and \ref{Y} are zero. That is, choosing the Lorentz gauge

$$
\boldsymbol{\nabla} \cdot \mathbf{A} = −\mu_0\varepsilon_0 \left(\frac{\partial V}{ \partial t} \right) \nonumber
$$

simplifies equations \ref{X} and \ref{Y} to be

$$
\boldsymbol{\nabla}^2V −\mu_0\varepsilon_0 \frac{\partial^2V}{ \partial t^2} = − \frac{\rho}{ \varepsilon_0} \nonumber
$$

$$
\boldsymbol{\nabla}^2\mathbf{A}−\mu_0\varepsilon_0 \left(\frac{\partial^2\mathbf{A}}{ \partial t^2} \right) = −\mu_0 \mathbf{j} \nonumber
$$

The virtue of using the Lorentz gauge, rather than the Coulomb gauge $\boldsymbol{\nabla} \cdot \mathbf{A} = 0$, is that it separates the equations for the scalar and vector potentials. Moreover, these two equations are the wave equations for these two potential fields corresponding to a velocity $c = \frac{1}{ \sqrt{\mu_0\varepsilon_0 }}$. This example illustrates the power of using the concept of potentials in describing vector fields.

## 19.10: Appendix - Waveform analysis

### Harmonic Waveform Decomposition

Any linear system that is subject to a time-dependent forcing function $F( t)$, can be expressed as a linear superposition of frequency-dependent solutions of the individual harmonic decomposition $a(\omega )$ of the forcing function. Similarly, any linear system subject to a spatially-dependent forcing function $F(x)$ can be expressed as a linear superposition of the wavenumber-dependent solutions of the individual harmonic decomposition $a(k_x)$ of the forcing function. Fourier analysis provides the mathematical procedure for the transformation between the periodic waveforms and the harmonic content, that is, $F( t) \Leftrightarrow a(\omega )$, or $F(x) \Leftrightarrow a(k_x)$. Fourier’s theorem states that any arbitrary forcing function $F( t)$ can be decomposed into a sum of harmonic terms. For example for a time-dependent periodic forcing function the decomposition can be a cosine series of the form

$$
F( t) = \sum^{\infty}_{n=1} \alpha_n \cos(n\omega_0 t + \phi_n) \label{I.1}
$$

where $\omega_0$ is the lowest (fundamental) frequency solution. For an aperiodic function a cosine decomposition can be of the form

$$
F( t) = \int^{\infty}_0 \alpha (\omega ) \cos(\omega t + \phi (\omega ))d\omega \label{I.2}
$$

Either of the complementary functions $F( t) \Leftrightarrow a(\omega )$, or $F(x) \Leftrightarrow a(k_x)$ are equivalent representations of the harmonic content that can be used to describe signals and waves. The following two sections give an introduction to Fourier analysis.

#### Periodic systems and the Fourier series

Discrete solutions occur for systems when periodic boundary conditions exist. The response of periodic systems can be described in either the time versus angular frequency domains, or equivalently, the spatial coordinate $x$ versus the corresponding wave number $k_x$. For periodic systems this decomposition leads to the Fourier series where a generalized phase coordinate $\phi$ can be used to represent either the time or spatial coordinates, that is, with $\phi = \omega_0 t$ or $\phi = k_xx$ respectively. The Fourier series relates the two representations of the discrete wave solutions for such periodic systems.

Fourier’s theorem states that for a general periodic system any arbitrary forcing function $F(\phi)$ can be decomposed into a sum of sinusoidal or cosinusoidal terms. The summation can be represented by three equivalent series expansions given below, where $\phi = \omega_0 t$ or $\phi = \mathbf{k}_0\cdot \mathbf{r}$, and where $\omega_0, \mathbf{k}_0$ are the fundamental angular frequency and fundamental wave number respectively.

$$
f (\phi) = \frac{a_0}{2} + \sum^{\infty}_{n=1} [a_n \cos (n\phi) + b_n \sin (n\phi)] \label{I.3}
$$

$$
f (\phi) = \frac{a_0}{2} + \sum^{\infty}_{n=0} c_n \cos (n\phi + \varphi_n) \label{I.4}
$$

$$
f (\phi) = \frac{a_0}{2} + \sum^{\infty}_{n=0} d_n \sin (n\phi + \theta_n) \label{I.5}
$$

where $n$ is an integer, and $\varphi_n, \theta_n$ are phase shifts fit to the initial conditions.

The normal modes of a discrete system form a complete set of solutions that satisfy the following orthogonality relation

$$
\int^{2\pi}_0 f_n (\phi) f_m (\phi) d\phi = c_n \delta_{mn} \label{I.6}
$$

where $\delta_{mn}$ is the Kronecker delta symbol defined in equation $(9.2.10)$. Orthogonality can be used to determine the coefficients for equations \ref{I.3} to be

$$
a_0 = \frac{1}{ \pi} \int^{+\pi}_{ −\pi} f (\phi) d\phi \label{I.7}
$$

$$
a_n = \frac{1}{ \pi} \int^{+\pi}_{ −\pi} f (\phi) \cos (n\phi) d\phi \label{I.8}
$$

$$
b_n = \frac{1}{ \pi} \int^{+\pi}_{ −\pi} f (\phi) \sin (n\phi) d\phi \label{I.9}
$$

Similarly the coefficients for \ref{I.4} and \ref{I.5} are related to the above coefficients by

$$
c^2_n = d^2_n = a^2_n + b^2_n \nonumber
$$

Instead of the simple trigonometric form used in equations (\ref{I.3} − \ref{I.5}) the cosine and sine functions can be expanded into the exponential form where

$$
\cos \phi = \frac{1}{ 2} ( e^{i\phi} + e^{-i\phi}) \label{I.10} \\ \sin \phi = \frac{−i}{ 2} ( e^{i\phi} − e^{-i\phi})
$$

then Equation \ref{I.3} becomes

$$
f (\phi) = \sum^{\infty}_{ n=−\infty} g_n e^{in\phi} \label{I.11}
$$

where $n$ is any integer and, from the orthogonality, the Fourier coefficients are given by

$$
g_n = \frac{1}{ 2\pi} \int^{+\pi}_{ −\pi} f (\phi) e^{n\phi} d\phi \label{I.12}
$$

These coefficients are related to the cosine plus sine series amplitudes by

$$
g_n = \frac{1}{ 2} (a_n − ib_n) \tag{when $n$ is positive}
$$

$$
g_n = \frac{1}{ 2} (a_n + ib_n) \tag{when $n$ is negative}
$$

These results show that the coefficients of the exponential series are in general *complex*, and that they occur in conjugate pairs (that is, the imaginary part of a coefficient $a_n$ is equal but opposite in sign to that for the coefficient $a_{−n}$). Although the introduction of complex coefficients may appear unusual, it should be remembered that the real part of a pair of coefficients denotes the magnitude of the cosine wave of the relevant frequency, and that the imaginary part denotes the magnitude of the sine wave. If a particular pair of coefficients $a_n$ and $a_{−n}$ are real, then the component at the frequency $n\omega_0$ is simply a cosine; if $a_n$ and $a_{−n}$ are purely imaginary, the component is just a sine; and if, as is the general case, $a_n$ and $a_{−n}$ are complex, both cosine and a sine terms are present.

The use of the exponential form of the Fourier series gives rise to the notion of ‘negative frequency’. Of course, $f ( t) = a_n \cos \omega_n t$ is a wave of a single frequency $\omega_n = n\omega_0$ radians/second, and may be represented by a single line of height $a_n$ in a normal spectral diagram. However, using the exponential form of the Fourier series results in both positive and negative $\omega$ components.

The coexistence of both negative and positive angular frequencies $\pm \omega$ can be understood by consideration of the Argand diagram where the real component is plotted along the $x$-axis and the imaginary component along the $y$-axis. The function $g_ne^{+i\omega t}$ represents a vector of length $g_n$ that rotates with an angular velocity $\omega$ in a positive direction, that is counterclockwise, whereas, $g_ne^{−i\omega t}$ represents the vector rotating in a negative direction, that is clockwise. Thus the sum of the two rotating vectors, according to equations \ref{I.3}, leads to cancellation of the opposite components on the imaginary $y$ axis and addition of the two $g_n \cos \omega t$ real components on the $x$ axis. Subtraction leads to cancellation of the real $x$ components and addition of the imaginary $y$ axis components.

#### Aperiodic systems and the Fourier Transform

The Fourier transform (also called the Fourier integral) does for the non-repetitive signal waveform what the Fourier series does for the repetitive signal. It was shown that the line spectrum of a recurrent periodic pulse waveform is modified as the pulse duration decreases, assuming the period of the waveform (and hence its fundamental component) remains unchanged. Suppose now that the duration of the pulses remain fixed but the separation between them increases, giving rise to an increasing period. In the limit, only a single rectangular pulse remains, its neighbors having moved away on either side towards $\pm \infty$. In this case, the fundamental frequency $\omega_0$ tends towards zero and the harmonics become extremely closely spaced and of vanishingly small amplitudes, that is, the system approximates a continuous spectrum.

Mathematically, this situation may be expressed by modifications to the exponential form of the Fourier series already derived. Let the phase factor $\phi = \omega_0 t$ in Equation \ref{I.11} then

$$
g_n = \frac{\omega_0 }{2\pi} \int^{+\pi}_{ −\pi} f ( t) e^{n\omega_0 t} d t = \frac{1}{ \tau} \int^{\frac{\tau }{2}}_{ − \frac{\tau}{ 2}} f ( t) e^{n\omega_0 t} d t \label{I.13}
$$

where $\tau$ is the period of the periodic force. Let $G (\omega ) = \tau g_n$, $\omega = n\omega_0$, and take the limit for $\tau \rightarrow \infty$, then Equation \ref{I.12} can be written as

$$
G (\omega ) = \int^{+\infty}_{ −\infty} f ( t) e^{\omega t}d t \label{I.14}
$$

Similarly making the same limit for $\tau \rightarrow \infty$ then $\omega_0 = \frac{2\pi}{ \tau} \rightarrow d\omega$ and Equation \ref{I.11} becomes

$$
f ( t) = \sum^{\infty}_{ n=−\infty} \frac{G (\omega )}{ \tau} e^{in\omega_0 t} = \sum^{\infty}_{ n=−\infty} G (\omega ) \frac{\omega_0 }{2\pi} e^{i\omega t} = \frac{1}{ 2\pi} \int^{ +\infty}_{ −\infty} G (\omega ) e^{i\omega t} d\omega \label{I.15}
$$

Equation \ref{I.15} shows how a non-repetitive time-domain wave form is related to its continuous spectrum. These are known as Fourier integrals or Fourier transforms. They are of central importance for signal processing. For convenience the transforms often are written in the operator formalism using the $\mathcal{F}$ symbol in the form

$$
f ( t) = \frac{1}{ 2\pi } \int^{ +\infty}_{ −\infty} G (\omega ) e^{i\omega t} d\omega \equiv \mathcal{F}^{−1} \left[ \frac{1}{ 2\pi} G(\omega ) \right] \label{I.16}
$$

$$
G (\omega ) = \int^{ +\infty}_{ −\infty} f ( t) e^{−i\omega t} d t \equiv \mathcal{F}f( t) \label{I.17}
$$

It is very important to grasp the significance of these two equations. The first tells us that the Fourier transform of the waveform $f( t)$ is continuously distributed in the frequency range between $\omega = \pm \infty$, whereas the second shows how, in effect, the waveform may be synthesized from an infinite set of exponential functions of the form $e^{\pm i\omega t}$, each weighted by the relevant value of $G(\omega )$. It is crucial to realize that this transformation can go either way equally, that is, from $G(\omega )$ to $f ( t)$ or vice versa.<sup>1</sup>

Example 19.1: Fourier transform of a single isolated square pulse

Consider a single isolated square pulse of width $\tau$ that is described by the rectangular function $\prod$ defined as

$$
\prod( t) = \begin{cases} 1 & | t|< \frac{\tau}{ 2} \\ 0 & | t| > \frac{\tau}{2} \end{cases}\nonumber
$$

That is, assume that the amplitude of the pulse is unity between $−\frac{\tau }{2} \leq t \leq \frac{\tau }{2}$. Then the Fourier transform

$$
G (\omega ) = \int^{+\tau}_{ −\tau} 1.e^{−i\omega t} d t = \tau \left(\frac{\sin \frac{\omega \tau}{ 2}}{ \frac{\omega \tau}{ 2 }}\right) \nonumber
$$

which is an unnormalized $sinc(\omega \tau )$ function. Note that the width of the pulse $\Delta t = \pm \frac{\tau }{2}$ leads to a frequency envelope that has the first zeros at $\Delta\omega = \pm \frac{\pi}{ \tau}$. Thus the product of these widths $\Delta t \cdot \Delta\omega = \pm \pi$ which is independent of the width of the pulse, that is $\Delta\omega = \frac{\pi}{ \Delta t}$ which is an example of the uncertainty principle which is applicable to all forms of wave motion.

Example 19.2: Fourier transform of the Dirac delta function

The Dirac delta function, $\delta ( t − t^{\prime} )$, is a pulse of extremely short duration and unit area at $t = t^{\prime}$ and is zero at all other times. That is,

$$
1 = \int^{ +\infty}_{ −\infty} \delta ( t − t^{\prime} ) d t \nonumber
$$

The Dirac function, which is sometimes referred to as the impulse function, has many important applications to physics and signal processing. For example, a shell shot from a gun is given a mechanical impulse imparting a certain momentum to the shell in a very short time. Other things being equal, one is interested only in the impulse imparted to the shell, that is, the time integral of the force accelerating the shell in the gun, rather than the details of the time dependence of the force. Since the force acts for a very short time the Dirac delta function can be employed in such problems.

As described in section $3.11$ and **appendix J**, the Dirac delta function is employed in signal processing when signals are sampled for short time intervals. The Fourier transform of the delta function is needed for discussion of sampling of signals

$$
G (\omega ) = \int^{ +\infty}_{ −\infty} \delta ( t − t^{\prime} ) e^{−i\omega t} d t = e^{−i\omega t^{\prime}} \nonumber
$$

Since $e^{−i\omega t}$ essentially is constant over the infinitesimal time duration of the $\delta ( t − t^{\prime} )$ function, and the time integral of the $\delta$ function is unity, thus the term $e^{−i\omega t}$ has unit magnitude for any value of $\omega$ and has a phase shift of $−\omega ( t − t^{\prime} )$ radians. For $t^{\prime} = 0$ the phase shift is zero and thus the Fourier transform of a Dirac $\delta ( t)$ function is $G(\omega )=1$. That is, this is a uniform white spectrum for all values of $\omega$.

### Time-sampled waveform analysis

An alternative approach for unloosing periodic signals, that is complementary to the Fourier analysis harmonic decomposition, is time-sampled (discrete-sample) waveform analysis where the signal amplitude is measured repetitively at regular time intervals in a time-ordered sequence, that is, a sequence of samples of the instantaneous delta-function amplitudes is recorded. Typically an amplitude-to-digital converter is used to digitize the amplitude for each measured sample and the digital numbers are recorded; this process is called **digital signal processing**.

The general principles are best explained by first considering the response of a linear system to a step function impulse, followed by a square impulse, and leading to the response of a $\delta$-function impulsive driving force.

:::{figure} ../images/lt-23026-i1.png
:alt: i1.PNG

$1$: Response of a underdamped linear oscillator with $\omega = 10$, and $\Gamma = 2$ to the following impulsive force. (a) Step function force $F = 0$ for $t < 0$ and $F = m$ for $t > 0$. (b) Square-wave force where $F = m$ for $0 < t<\tau$ for $\tau = 3$, and $F = 0$ at other times. (c) Delta-function impulse $P = 1$.
:::

#### Delta-function impulse response

Consider the damped oscillator equation

$$
\ddot{x} + \Gamma \dot{x} + \omega^2_0x = \frac{F ( t)}{ m} \label{I.18}
$$

and assume that a step function is applied at time $t = 0$. That is;

$$
\begin{align} \frac{F ( t)}{ m} = 0 && t < 0 && \frac{F ( t)}{ m } = a && t> 0 \label{I.19} \end{align}
$$

where $a$ is a constant. The initial conditions are that $x(0) = \dot{x}(0) = 0$.

The transient or complementary solution is the solution of the linearly-damped harmonic oscillator

$$
\ddot{x} + \Gamma \dot{x} + \omega^2_0x = 0 \label{I.20}
$$

This is independent of the driving force and the solution is given in the chapter $3.5$ discussion of the linearly-damped harmonic oscillator.

The particular, steady-state, solution is easy to obtain just by inspection since the force is a constant, that is, the particular solution is

$$
\begin{aligned} x_S = \frac{a}{ \omega^2_0} && t > 0 && x_S = 0 && t < 0 \end{aligned}
$$

Taking the sum of the transient and particular solutions, using the initial conditions, gives the final solution to be

$$
x( t) = \frac{a}{ \omega^2_0} \left[ 1 − e^{− \frac{\Gamma}{2} t} \cos \omega_1 t − \frac{\Gamma e^{− \frac{\Gamma}{2} t}}{ 2\omega_1} \sin \omega_1 t \right] \label{I.21}
$$

where $\omega_1 \equiv \sqrt{ \omega^2_0 − ( \frac{\Gamma}{2} )^2}$. This functional form is shown in Figure 19.1a. Note that the amplitude of the transient response equals $−a$ at $t = 0$ to cancel the particular solution when it jumps to $+a$. The oscillatory behavior then is just that of the transient response.

A square impulse can be generated by the superposition of two opposite-sign stepfunctions separated by a time $\tau$ as shown in Figure 19.1b.

The square impulse can be taken to the limit where the width $\tau$ is negligibly small relative to the response times of the system. It can be shown that letting $\tau \rightarrow 0$, but keeping the magnitude of the total impulse $P = a\tau$ finite for the impulse at time $t_0$, leads to the solution for the $\delta$-function impulse occurring at $t_0$

$$
x( t) = \frac{P}{ \omega_1} e^{− \frac{\Gamma}{2} ( t− t_0)} \sin \omega_1 ( t − t_0) \quad t> t_0 \label{I.22}
$$

This response to a delta function impulse is shown in Figure 19.1c for the case where $t_0 = 0$. An example is the response when the hammer strikes a piano string at $t = 0$.

:::{figure} ../images/lt-23029-i2.png
:alt: i2.PNG

$2$: Decomposition of the function $x( t) = 2 \sin ( t)+ \sin (5 t)+ \frac{1}{ 3} \sin (15 t)+ \frac{1}{ 5} \sin (25 t)$ into a time-ordered sequence of $\delta$-function samples.
:::

#### Green’s function waveform decomposition

The response of the linearly-damped linear oscillator to an delta function impulse, that has been expressed above, can be used to exploit the powerful Green’s technique for decomposition of any general forcing function. That is, if the driven system is linear, then the principle of superposition is applicable and allowing expression of the inhomogeneous part of the differential equation as the sum of individual delta functions. That is;

$$
\ddot{x} + \Gamma \dot{x} + \omega^2_0 x = \sum^{\infty}_{ n=−\infty} \frac{F_n ( t)}{ m} = \sum^{\infty}_{ n=−\infty} I_n ( t) \label{I.23}
$$

As illustrated in Figure 19.2 discrete-time waveform analysis involves repeatedly sampling the instantaneous amplitude in a regular and repetitive sequence of $\delta$-function impulses. Since the superposition principle applies for this linear system then the waveform can be described by a sum of an ordered series of deltafunction impulses where $t^{\prime}$ is the time of an impulse. Integrating over all the $\delta$-function responses that have occurred at time $t^{\prime}$, that is prior to the time of interest $t$, leads to

$$
x ( t) = \int^t_{ −\infty} \frac{F ( t^{\prime} )}{ m\omega_1} e^{− \frac{\Gamma}{2} ( t− t^{\prime} )} \sin \omega_1 ( t − t^{\prime} ) d t^{\prime} \quad t \geq t^{\prime} \label{I.24}
$$

The Green’s function $G ( t − t^{\prime} )$ is defined by

$$
G( t − t^{\prime} ) = \frac{1}{ m\omega_1} e^{− \frac{\Gamma}{2} ( t− t^{\prime} )} \sin \omega_1 ( t − t^{\prime} ) \quad t \geq t^{\prime} \label{I.25} \\ = 0 \quad t< t^{\prime}
$$

Superposition allows the summed response of the system to be written in an integral form

$$
x( t) = \int^t_{ −\infty} F( t^{\prime} )G( t − t^{\prime} )d t^{\prime} \label{I.26}
$$

which gives the final time dependence of the forced system. This repetitive time-sampling approach avoids the need of using Fourier analysis. Note that the Green’s function $G ( t − t^{\prime} )$ includes implicitly the frequency of the free undamped linear oscillator $\omega_0$, the free damped linear oscillator $\omega_1 \equiv \sqrt{\omega^2_0 − ( \frac{\Gamma}{2} )^2}$, as well as the damping coefficient $\Gamma$. Access to the combination of fast microcomputers coupled to fast digital sampling techniques has made digital signal sampling the pre-eminent technique for signal recording of audio, video, and detector signal processing.

<sup>1</sup>The only asymmetry in the Fourier transform relations comes from the $2\pi$ factor originating from the fact that by convention physicists use the angular frequency $\omega = 2\pi\nu$ rather than the frequency $\nu$. In order to restore symmetry many papers use the factor $\frac{1}{\sqrt{ 2\pi}}$ in both relations rather than using the $\frac{1}{ 2\pi}$ factor in Equation \ref{I.16} and unity in Equation \ref{I.17}.

## 19.11: Bibliography

### [1] SELECTION OF TEXTBOOKS ON CLASSICAL MECHANICS

[Ar78] V. I. Arnold, *“Mathematical methods of Classical Mechanics”*, $2^{nd}$ edition, Springer-Verlag (1978)

This textbook provides an elegant and advanced exposition of classical mechanics expressed in the language of differential topology.

[Co50] H.C. Corben and P. Stehle, *“Classical Mechanics”*, John Wiley (1950)

This classic textbook covers the material at the same level and comparable scope as the present textbook.

[Fo05] G. R. Fowles, G. L. Cassiday, *“Analytical Mechanics”*. Thomson Brookes/Cole, Belmont, (2005)

An elementary undergraduate text that emphasizes computer simulations.

[Go50] H. Goldstein, *“Classical Mechanics”*, Addison-Wesley, Reading (1950)

This has remained the gold standard graduate textbook in classical mechanics since 1950. Goldstein’s book is the best graduate-level reference to supplement the present textbook. The lack of worked examples is an impediment to using Goldstein for undergraduate courses. The $3^{rd}$ edition, published by Goldstein, Poole, and Safko (2002), uses the symplectic notation that makes the book less friendly to undergraduates. The Cline book adopts the nomenclature used by Goldstein to provide a consistent presentation of the material.

[Gr06] R. D. Gregory, *“Classical Mechanics”*, Cambridge University Press

This outstanding, and original, introduction to analytical mechanics was written by a mathematician. It is ideal for the undergraduate, but the breadth of the material covered is limited.

[Gr10] W. Greiner, *“Classical Mechanics, Systems of particles and Hamiltonian Dynamics”*, $2^{nd}$ edition, Springer (2010). This excellent modern graduate textbook is similar in scope and approach to the present text. Greiner includes many interesting worked examples, as well as a reproduction of the Struckmeier[Str08] presentation of the extended Lagrangian and Hamiltonian mechanics formalism of Lanczos[La49].

[Jo98] J. V. José and E. J. Saletan, *“Classical Dynamics, A Contemporary Approach”*, Cambridge University Press (1998)

This modern advanced graduate-level textbook emphasizes configuration manifolds and tangent bundles which makes it unsuitable for use by most undergraduate students.

[Jo05] O. D. Johns, *“Analytical Mechanics for Relativity and Quantum Mechanics”*, $2^{nd}$ edition, Oxford University Press (2005). Excellent modern graduate text that emphasizes the Lanczos[La49] parametric approach to Special Relativity. The Johns and Cline textbooks were developed independently but are similar in scope and approach. For consistency, the name “generalized energy”, which was introduced by Johns, has been adopted in the Cline textbook.

[Ki85] T.W.B. Kibble, F.H. Berkshire. *“Classical Mechanics, (5th edition)”*, Imperial College Press, London, 2004. Based on the textbook written by Kibble that was published in 1966 by McGrawHill. The 4th and 5th editions were published jointly by Kibble and Berkshire. This excellent and well-established textbook addresses the same undergraduate student audience as the present textbook. This book covers the variational principles and applications with minimal discussion of the philosophical implications of the variational approach.

[La10] O.L. De Lange and J. Pierrus, *"Solved Problems in Classical Mechanics"*, Oxford University Press, 2010. Presents both numerical and analytical solution of problems in classical mechanics.

[La49] C. Lanczos, *“The Variational Principles of Mechanics”*, University of Toronto Press, Toronto, (1949)

An outstanding graduate textbook that has been one of the founding pillars of the field since 1949. It gives an excellent introduction to the philosophical aspects of the variational approach to classical mechanics, and introduces the extended formulations of Lagrangian and Hamiltonian mechanics that are applicable to relativistic mechanics.

[La60] L. D. Landau, E. M. Lifshitz, *“Mechanics”*, Volume 1 of a *Course in Theoretical Physics*, Pergamon Press (1960)

An outstanding, succinct, description of analytical mechanics that is devoid of any superfluous text. This Course in Theoretical Physics is a masterpiece of scientific writing and is an essential component of any physics library. The compactness and lack of examples makes this textbook less suitable for most undergraduate students.

[Li94] Yung-Kuo Lim, *“Problems and Solutions on Mechanics”* (1994)

This compendium of 408 solved problems, which are taken from graduate qualifying examinations in physics at several U.S. universities, provides an invaluable resource that complements this textbook for study of Lagrangian and Hamiltonian mechanics.

[Ma65] J. B. Marion, *“Classical Dynamics of Particles and Systems”*, Academic Press, New York, (1965)

This excellent undergraduate text played a major role in introducing analytical mechanics to the undergraduate curriculum. It has an outstanding collection of challenging problems. The $5^{th}$ edition has been published by S. T. Thornton and J. B. Marion, Thomson, Belmont, (2004).

[Me70] L. Meirovitch, *“Methods of Analytical Dynamics”*, McGraw-Hill New York, (1970)

An advanced engineering textbook that emphasizes solving practical problems, rather than the underlying theory.

[Mu08] H. J. W. Müller-Kirsten, *“Classical Mechanics and Relativity”*, World Scientific, Singapore, (2008)

This modern graduate-level textbook emphasizes relativistic mechanics making it an excellent complement to the present textbook.

[Pe82] I. Percival and D. Richards, *“Introduction to Dynamics”* Cambridge University Press, London, (1982)

Provides a clear presentation of Lagrangian and Hamiltonian mechanics, including canonical transformations, Hamilton-Jacobi theory, and action-angle variables.

[Sy60] J.L. Synge, *“Principles of Classical Mechanics and Field Theory”*, Volume III/I of *“Handbuck der Physik”* Springer-Verlag, Berlin (1960).

A classic graduate-level presentation of analytical mechanics.

[Th04] S.T. Thornton, and J. B. Marion, *"Classical Dynamics of Particles and Systems"*, $5^{th}$ edition. Brooks/Cole-Thomson Learning, New York, (2004)

Thornton has expanded the outstanding collection of challenging problems in this popular classical mechanics book.

### [2] GENERAL REFERENCES

[Bak96] L. Baker, J.P. Gollub, *Chaotic Dynamics*, $2^{nd}$ edition, 1996 (Cambridge University Press)

[Bat31] H. Bateman, *Phys. Rev.* **38** (1931) 815

[Bau31] P.S. Bauer, *Proc. Natl. Acad. Sci.* **17** (1931) 311

[Bor25a] M. Born and P. Jordan, *Zur Quantenmechanik*, Zeitschrift für Physik, 34, (1925) 858-888.

[Bor25b] M. Born, W. Heisenberg, and P. Jordan, *Zur Quantenmechanik II*, Zeitschrift für Physik, 35, (1925), 557-615,

[Boy08] R. W. Boyd, *Nonlinear Optics*, $3^{rd}$ edition, 2008 (Academic Press, NY)

[Bri14] L. Brillouin, Ann. Physik **44**(1914)

[Bri60] L. Brillouin, Wave Propagation and Group Velocity, 1960 (Academic Press, New York)

[Cay1857] A. Cayley, Proc. Roy. Soc. London **8** (1857) 506

[Cei10] J.L. Cie´sli´nski, T. Nikiciuk, J. Phys. A:Math. Theor. **43** (2010) 175205

[Cio07] Ciocci and Langerock, *Regular and Chaotic Dynamics*, **12** (2007) 602

[Cli71] D. Cline, Proc. Orsay Coll. on Intermediate Nuclei, Ed. Foucher, Perrin, Veneroni, 4 (1971).

[Cli72] D. Cline and C. Flaum, Proc. of the Int. Conf. on Nuclear Structure Studies Using Electron Scattering, Sendai, Ed. Shoa, Ui, 61 (1972).

[Cli86] D. Cline, Ann. Rev. Nucl. Part. Sci. 36, (1986) 683.

[Coh77] R.J. Cohen, Amer. J. of Phys. **45** (1977) 12

[Cra65] F.S. Crawford, *Berkeley Physics Course 3; Waves*, 1970 (Mc Graw Hill, New York)

[Cum07] D. Cumin, C.P. Unsworth, Physica D 226 (2007) 181

[Dav58] A. S. Davydov and G. F. Filippov. Nuclear Physics, 8 (1958) 237

[Dek75] H. Dekker, Z. Physik, **B21** (1975) 295

[Dep67] A. Deprit, American J. of Phys **35**, no.5 424 (1967)

[Dir30] P.A.M. Dirac, *Quantum Mechanics*, Oxford University Press, (1930).

[Dou41] D. Douglas, Trans. Am. Math. Soc. **50** (1941) 71

[Fey84] R.P. Feynman, R.B. Leighton, M. Sands, The Feynman Lectures, (Addison-Wesley, Reading, MA,1984) Vol. 2, p17.5

[Fro80] C. Frohlich, Scientific American, **242** (1980) 154

[Gal13] C. R. Galley, Physical Review Letters, **11** (2013) 174301

[Gal14] C. R. Galley, D. Tsang, L.C. Stein, arXiv:1412.3082v1 [math-phys] 9 Dec 2014

[Har03] James B. Hartle, *Gravity: An Introduction to Einstein’s General Relativity* (Addison Wesley, 2003)

[Jac75] J.D. Jackson, *Classical Electrodynamics*, $2^{nd}$ edition , (Wiley, 1975)

[Kur75] International Symposium on Math. Problems in Theoretical Physics, Lecture Notes in Physics, Vol39 Springer, NY (1975)

[Mus08a] Z.E. Musielak, J. Phys. A. Math. Theor. **41** (2008) 055205

[Mus08b] Z.E. Musielak, D. Rouy, L.D. Swift, Chaos, Solitons, Fractals **38** (2008) 894

[Ray1881] J.W. Strutt, $3^{rd}$ Baron Rayleigh, Proc. London Math. Soc., s1-4 (1), (1881) 357

[Ray1887] J.W. Strutt, $3^{rd}$ Baron Rayleigh, *The Theory of Sound*, 1887 (Macmillan, London)

[Rou1860] E.J. Routh, *Treatise on the dynamics of a system of rigid bodies*, MacMillan (1860)

[Sim98] M. Simon, D. Cline, K. Vetter, et al, Unpublished

[Sta05] T. Stachowiak and T. Okada, Chaos, Solitons, and Fractals, **29** (2006) 417.

[Str00] S.H. Strogatz, Physica **D43** (2000) 1

[Str05] J. Struckmeier, J. Phys. A: Math; Gen. **38** (2005) 1257

[Str08] J. Struckmeier, Int. J. of Mod. Phys. **E18** (2008) 79

[Vir15] E.G. Virga, Phys, Rev. **E91** (2015) 013203

[Win67] A.T. Winfree, J. Theoretical Biology **16** (1967) 15
