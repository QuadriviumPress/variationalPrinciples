---
title: "16. Analytical Formulations for Continuous Systems"
short_title: "Chapter 16"
label: ch-16-analytical-formulations-for-continuous-systems
---


# 16. Analytical Formulations for Continuous Systems

(ch-16)=

## 16.1: Introduction

Lagrangian and Hamiltonian mechanics have been used to determine the equations of motion for discrete systems having a finite number of discrete variables $q_i$ where $1 \leq i \leq n$. There are important classes of systems where it is more convenient to treat the system as being continuous. For example, the interatomic spacing in solids is a few $10^{−10}m$ which is negligible compared with the size of typical macroscopic, three-dimensional solid objects. As a consequence, for wavelengths much greater than the atomic spacing in solids, it is useful to treat macroscopic crystalline lattice systems as continuous three-dimensional uniform solids, rather than as three-dimensional discrete lattice chains. Fluid and gas dynamics are other examples of continuous mechanical systems. Another important class of continuous systems involves the theory of fields, such as electromagnetic fields. Lagrangian and Hamiltonian mechanics of the continua extend classical mechanics into the advanced topic of field theory. This chapter goes beyond the scope of a typical undergraduate classical mechanics course in order to provide a brief glimpse of how Lagrangian and Hamiltonian mechanics can underlie advanced and important aspects of the mechanics of the continua, including field theory.

## 16.2: The Continuous Uniform Linear Chain

The Lagrangian for the discrete lattice chain, for longitudinal modes, is given by equation $(14.10.3)$ to be

$$
L = \frac{1}{2} \sum^{n+1}_{j=1} \left( m\dot{q}^2_j - \kappa (q_{j-1} - q_j)^2\right)\label{16.1}
$$

where the $n$ masses are attached in series to $n+1$ identical springs of length $d$ and spring constant $\kappa$. Assume that the spring has a uniform cross-section area $A$ and length $d$. Then each spring volume element $\Delta \tau = Ad$ has a mass $m$, that is, the volume mass density $\rho = \frac{m }{\Delta \tau}$ or $m = \rho \Delta \tau$. Chapter $16.5$ will show that the spring constant $\kappa = \frac{EA}{ d}$ where $E$ is Young’s modulus, $A$ is the cross sectional area of the chain element, and $d$ is the length of the element. Then the spring constant can be written as $\kappa = \frac{E\Delta \tau }{ d^2}$. Therefore Equation \ref{16.1} can be expressed as a sum over volume elements $\Delta \tau = Ad$

$$
L = \frac{1}{2} \sum^{n+1}_{j=1} \left( \rho \dot{q}^2_j − E \left(\frac{q_{j-1} -q_j}{d} \right)^2 \right) \Delta \tau \label{16.2}
$$

In the limit that $n \rightarrow \infty$ and the spacing $d = dx \rightarrow 0$, then the summation in Equation \ref{16.2} can be written as a volume integral where $x = jd$ is the distance along the linear chain and the volume element $\boldsymbol{\Delta} \boldsymbol{\tau} \rightarrow \mathcal{0}$. Then the Lagrangian can be written as the integral over the volume element $d\tau$ rather than a summation over $\Delta \tau$. That is,

$$
L = \frac{1}{ 2} \int \left( \rho \dot{q}^2 − E \left(\frac{dq(x, t)}{ dx }\right)^2 \right) d\tau\label{16.3}
$$

The discrete-chain coordinate $q(t)$ is assumed to be a continuous function $q(x, t)$ for the uniform chain. Thus the integral form of the Lagrangian can be expressed as

$$
L = \frac{1}{2} \int \left( \rho \dot{q}^2 − E \left( \frac{dq(x, t) }{dx } \right)^2 \right) d\tau = \int \mathfrak{L}d\tau \label{16.4}
$$

where the function $\mathfrak{L}$ is called the **Lagrangian density** defined by

$$
\mathfrak{L} \equiv \frac{1}{2} \left( \rho \dot{q}^2 − E \left(\frac{dq(x, t) }{dx }\right)^2 \right) \label{16.5}
$$

The variable $x$ in the Lagrangian density is not a generalized coordinate; it only serves the role of a continuous index played previously by the index $j$. For the discrete case, each value of $j$ defined a different generalized coordinate $q_i$. Now for each value of $x$ there is a continuous function $q(x, t)$ which is a function of both position and time.

Lagrange’s equations of motion applied to the continuous Lagrangian in Equation \ref{16.4} gives

$$
\rho \frac{ d^2q}{ dt^2} − E \frac{d^2q}{ dx^2} = 0 \label{16.6}
$$

This is the familiar wave equation in one dimension for a longitudinal wave on the continuous chain with a phase velocity

$$
v_{phase} = \sqrt{\frac{E}{ \rho}} \label{16.7}
$$

The continuous linear chain also can exhibit transverse modes which have a Lagrangian density were the Young’s modulus $E$ is replaced by the tension $\tau$ in the chain, and $\rho$ is replaced by the linear mass density $\mu$ of the chain, leading to a phase velocity for a transverse wave $v_{phase} = \sqrt{\frac{\tau}{\mu}}$.

## 16.3: The Lagrangian density formulation for continuous systems

### One spatial dimension

In general the Lagrangian density can be a function of $q, \nabla q, \frac{dq}{dt} , x, y, z$, and $t$. It is of interest that Hamilton’s principle leads to a set of partial differential equations of motion, based on the Lagrangian density, that are analogous to the Lagrange equations of motion for discrete systems. When deriving the Lagrangian equations of motion in terms of the Lagrangian density using Hamilton’s principle, the notation is simplified if the system is limited to one spatial coordinate $x$. In addition, it is convenient to use the compact notation where the spatial derivative is written $q^{\prime} \equiv \frac{dq}{dx}$ and the time derivative is $\dot{q} \equiv \frac{dq}{dt}$, and the one-dimensional Lagrangian density is assumed to be a function $\mathfrak{L}(q, q^{\prime} , \dot{q}, x, t )$. The appearance of the derivative $q^{\prime} \equiv \frac{dq}{dx}$ as an argument of the Lagrange density is a consequence of the continuous dependence of $q$ on $x$. In principle, higher-order derivatives could occur but they do not arise in most problems of physical interest.

Assuming that the one spatial dimension is $x$, then Hamilton’s principle of least action can be expressed in terms of the Lagrangian density as

$$
\delta S = \delta \int^{t_2}_{t_1} L(q, \dot{q},t )dt = \delta \int^{t_2}_{t_1} \int^{x_2}_{x_1} \mathfrak{L}(q, q^{\prime} , \dot{q}, x, t )dxdt \label{16.8}
$$

Following the same approach used in chapter $5.2$, it is assumed that the stationary path for the action integral is described by the function $q(x, t)$. Define a neighboring function using a parametric representation $q(x, t; \epsilon )$ such that when $\epsilon = 0$, the extremum function $q = q(x, t)$ yields the stationary action integral $S$.

Assume that an infinitessimal fraction $\epsilon$ of a neighboring function $\eta (x, t)$ is added to the extremum path $q(x, t)$. That is, assume

$$
q(x, t; \epsilon ) = q(x, t) + \epsilon \eta (x, t) \label{16.9}
$$

$$
q^{\prime} (x, t; \epsilon ) \equiv \frac{dq(x, t; \epsilon ) }{dx} = \frac{dq(x, t)}{ dx} + \epsilon \frac{d\eta (x, t)}{ dx} = q^{\prime} (x, t) + \epsilon \eta^{\prime} (x, t) \label{16.10}
$$

$$
\dot{q}(x, t; \epsilon ) \equiv \frac{dq(x, t; \epsilon ) }{dt} = \frac{dq(x, t) }{dt} + \epsilon \frac{ d\eta (x, t)}{ dt} = \dot{q}(x, t) + \epsilon \dot{\eta}(x, t) \label{16.11}
$$

where it is assumed that both the extremum function $q(x, t)$ and the auxiliary function $\eta (x, t)$ are well behaved functions of $x$ and $t$, with continuous first derivatives, and that $\eta (x, t)=0$ at $(x_1, t_1)$ and $(x_2, t_2)$ because, for all possible paths, the function $q(x, t; \epsilon )$ must be identical with $q(x, t)$ at the end points of the path, i.e. $\eta (x_1, t_1) = \eta (x_2, t_2)=0$.

A parametric family of curves $S(\epsilon )$, as a function of the admixture coefficient $\epsilon$, is described by the function

$$
S(\epsilon ) = \int^{t_2}_{t_1} \int^{x_2}_{x_1} \mathfrak{L}(q(x, t; \epsilon ), q^{\prime} (x, t; \epsilon ), \dot{q}(x, t; \epsilon ), x, t)dxdt \label{16.12}
$$

Then Hamilton’s principle requires that the action integral be a stationary function value for $\epsilon = 0$, that is, $S(\epsilon )$ is independent of $\epsilon$ which is satisfied if

$$
\frac{\partial S(\epsilon ) }{\partial \epsilon} = \int^{t_2}_{t_1} \int^{x_2}_{x_1}\left( \frac{\partial \mathfrak{L}}{\partial q} \frac{\partial q }{\partial \epsilon } + \frac{\partial \mathfrak{L}}{\partial \dot{q} } \frac{\partial \dot{q} }{\partial \epsilon} + \frac{\partial \mathfrak{L}}{\partial q^{\prime}} \frac{\partial q^{\prime}}{ \partial \epsilon} \right) dxdt = 0 \label{16.13}
$$

Equations \ref{16.9}, \ref{16.10},and \ref{16.11} give the partial differentials

$$
\frac{\partial q}{ \partial \epsilon} = \eta (x, t) \label{16.14}
$$

$$
\frac{\partial q^{\prime}}{ \partial \epsilon} = \eta^{\prime} (x, t) \label{16.15}
$$

$$
\frac{\partial \dot{q} }{\partial \epsilon} = \dot{\eta}(x, t) \label{16.16}
$$

Integration by parts in both the $x$ and $t$ terms in Equation \ref{16.13}, plus using the fact that $\eta (x_1, t_1) = \eta (x_2, t_2)=0$ at both end points, yields

$$
\int^{t_2}_{t_1} \frac{\partial \mathfrak{L}}{\partial \dot{q}} \frac{\partial \dot{q} }{\partial \epsilon} dt = − \int^{t_2}_{t_1} \frac{\partial}{\partial t }\left( \frac{\partial \mathfrak{L}}{\partial \dot{q} } \right) \frac{\partial q }{\partial \epsilon} dt \label{16.17}
$$

$$
\int^{x_2}_{x_1} \frac{\partial \mathfrak{L}}{\partial q^{\prime} } \frac{\partial q^{\prime}}{ \partial \epsilon } dx = − \int^{x_2}_{x_1} \frac{\partial}{\partial x}\left( \frac{\partial \mathfrak{L}}{\partial q^{\prime} } \right) \frac{\partial q}{ \partial \epsilon} dx \label{16.18}
$$

Therefore Hamilton’s principle, Equation \ref{16.13} becomes

$$
\frac{\partial S(\epsilon )}{ \partial \epsilon } = \int^{t_2}_{t_1} \int^{x_2}_{x_1} \left[ \frac{\partial \mathfrak{L}}{\partial q} − \frac{\partial}{\partial t}\left( \frac{\partial \mathfrak{L}}{\partial \dot{q}} \right) − \frac{\partial}{\partial x}\left( \frac{\partial \mathfrak{L}}{\partial q^{\prime}} \right) \right] \eta (x, t)dxdt = 0 \label{16.19}
$$

Since the auxiliary function $\eta (x, t)$ is arbitrary, then the integrand term in the square brackets of Equation \ref{16.19} must equal zero. That is,

$$
\frac{\partial}{\partial t}\left( \frac{\partial \mathfrak{L}}{\partial \dot{q}} \right) + \frac{\partial}{\partial x}\left( \frac{\partial \mathfrak{L}}{\partial q^{\prime}} \right) − \frac{\partial \mathfrak{L}}{\partial q} = 0 \label{16.20}
$$

Equation \ref{16.20} gives the equations of motion in terms of the Lagrangian density that has been derived based on Hamilton’s principle.

### Three spatial dimensions

Equation $(16.2.4)$ expresses the Lagrangian as an integral of the Lagrangian density over a single continuous index $q(x, t)$ where the Lagrangian density is a function $\mathfrak{L}(q, \frac{dq}{dt} , \frac{dq}{dx} , x, t)$. The derivation of the Lagrangian equations of motion in terms of the Lagrangian density for three spatial dimensions involves the straightforward addition of the $y$, and $z$ coordinates. That is, in three dimensions the vector displacement is expressed by the vector $\mathbf{q} (x, y, z, t)$ and the Lagrangian density is related to the Lagrangian by integration over three dimensions. That is, they are related by the equation

$$
L = \int \mathfrak{L}(\mathbf{q}, \frac{d\mathbf{q} }{dt }, \boldsymbol{\nabla} \cdot \mathbf{q}, x, y, z, t)d\tau \label{16.21}
$$

where, in cartesian coordinates, the volume element $d\tau = dxdydz$. The Lagrangian density is a function $\mathfrak{L}(\mathbf{q}, \frac{d\mathbf{q}}{ dt} , \boldsymbol{\nabla} \cdot \mathbf{q}, x, y, z, t)$ where the one field quantity $q(x, t)$ has been extended to a spatial vector $\mathbf{q} (x, y, z, t)$ and the spatial derivatives $q^{\prime}$ have been transformed into $\boldsymbol{\nabla} \cdot \mathbf{q}$. Applying the method used for the one-dimensional spatial system, to the three-dimensional system, leads to the following set of equations of motion

$$
\frac{\partial}{\partial t }\left(\frac{ \partial \mathfrak{L}}{\frac{ \partial \mathbf{q} }{\partial t}} \right) + \frac{\partial}{\partial x} \left(\frac{ \partial \mathfrak{L}}{\frac{ \partial \mathbf{q} }{\partial x}} \right) + \frac{\partial}{\partial y} \left(\frac{ \partial \mathfrak{L}}{\frac{ \partial \mathbf{q} }{\partial y}} \right) + \frac{\partial}{\partial z} \left(\frac{ \partial \mathfrak{L}}{\frac{ \partial \mathbf{q} }{\partial z}} \right) − \frac{\partial \mathfrak{L}} {\partial \mathbf{q}} = 0 \label{16.22}
$$

where the $x, y, z$ spatial derivatives have been written explicitly for clarity.

Note that the equations of motion, Equation \ref{16.22}, treat the spatial and time coordinates symmetrically. This symmetry between space and time is unchanged by multiplying the spatial and time coordinate by arbitrary numerical factors. This suggests the possibility of introducing a four-dimensional coordinate system

$$
\phi_u \equiv \{x, y, z, \alpha t\}\nonumber
$$

where the parameter $\alpha$ is freely chosen. Using this 4-dimensional formalism allows Equation \ref{16.22} to be written more compactly as

$$
\sum^4_{\mu} \frac{ \partial }{ \partial \phi_u} \left( \frac{\partial \mathfrak{L}}{ \frac{\partial \mathbf{q} }{\partial \phi_u }} \right) − \frac{\partial \mathfrak{L} }{\partial \mathbf{q}} = 0 \label{16.23}
$$

As discussed in chapter $17$, relativistic mechanics treats time and space symmetrically, that is, a four-dimensional vector $\mathbf{q} (x, y, z, t)$ can be used that treats time and the three spatial dimensions symmetrically and equally. This four-dimensional space-time formulation allows the first four terms in Equation \ref{16.22} to be condensed into a single term which illustrates the symmetry underlying Equation \ref{16.23}. If the Lagrangian density is Lorentz invariant, and if $\alpha = ic$, then Equation \ref{16.23} is covariant. Thus the Lagrangian density formulation is ideally suited to the development of relativistically covariant descriptions of fields.

## 16.4: The Hamiltonian density formulation for continuous systems

Chapter $16.3$ illustrated, in general terms, how field theory can be expressed in a Lagrangian formulation via use of the Lagrange density. It is equally possible to obtain a Hamiltonian formulation for continuous systems analogous to that obtained for discrete systems. As summarized in chapter $8$, the Hamiltonian and Hamilton’s canonical equations of motion are related directly to the Lagrangian by use of a Legendre transformation. The Hamiltonian is defined as being

$$
H\equiv \sum_i \left( \dot{q}_i \frac{\partial L}{ \partial \dot{q}_i} \right) − L \label{16.24}
$$

The generalized momentum is defined to be

$$
p_i \equiv \frac{\partial L}{ \partial \dot{q}_i} \label{16.25}
$$

Equation \ref{16.25} allows the Hamiltonian \ref{16.24} to be written in terms of the conjugate momenta as

$$
H (q_i, p_i, t) = \sum_i p_i\dot{q}_i − L(q_i, \dot{q}_i, t) = \sum_i (p_i\dot{q}_i − L_i(q_i, \dot{q}_i, t)) \label{16.26}
$$

where the Lagrangian has been partitioned into the terms for each of the individual coordinates, that is, $L (q_i, \dot{q}_i, t) = \sum_i L_i(q_i, \dot{q}_i, t)$.

In the limit that the coordinates $q, p$ are continuous, then the summation in Equation \ref{16.26} can be transformed into a volume integral over the Lagrangian density $\mathfrak{L}$. In addition, a momentum density can be represented by the vector field $\boldsymbol{\pi}$ where

$$
\boldsymbol{\pi} \equiv \frac{\partial \mathfrak{L}}{ \partial \mathbf{\dot{q}}} \label{16.27}
$$

Then the obvious definition of the Hamiltonian density $\mathfrak{H}$ is

$$
H = \int \mathfrak{H}d\tau = \int (\boldsymbol{\pi} \cdot \mathbf{\dot{q}}−\mathfrak{L}) d\tau \label{16.28}
$$

where the Hamiltonian density is defined to be

$$
\mathfrak{H} =\boldsymbol{\pi} \cdot \mathbf{\dot{q}}−\mathfrak{L} \label{16.29}
$$

Unfortunately the Hamiltonian density formulation does not treat space and time symmetrically making it more difficult to develop relativistically covariant descriptions of fields. Hamilton’s principle can be used to derive the Hamilton equations of motion in terms of the Hamiltonian density analogous to the approach used to derive the Lagrangian density equations of motion. As described in Classical Mechanics $2^{nd}$ edition by Goldstein, the resultant Hamilton equations of motion for one dimension are

$$
\frac{\partial \mathfrak{H}}{ \partial \pi }= \dot{q} \label{16.30}
$$

$$
\frac{\partial \mathfrak{H}}{ \partial q} − \frac{d}{dx} \frac{\partial \mathfrak{H}}{ \partial q^{\prime}} = −\dot{\pi} \label{16.31}
$$

$$
\frac{\partial \mathfrak{H}}{ \partial t} = −\frac{\partial \mathfrak{L}}{ \partial t} \label{16.32}
$$

Note that Equation \ref{16.31} differs from that for discontinuous systems.

## 16.5: Linear Elastic Solids

Elasticity is a property of matter where the atomic forces in matter act to restore the shape of a solid when distorted due to the application of external forces. A perfectly elastic material returns to its original shape if the external force producing the deformation is removed. Materials are elastic when the external forces do not exceed the elastic limit. Above the elastic limit, solids can exhibit plastic flow and concomitant heat dissipation. Such non-elastic behavior in solids occurs when they are subject to strong external forces.

The discussion of linear systems, in chapters $3$ and $14$, focussed on one dimensional systems, such as the linear chain, where the transverse rigidity of the chain was ignored. An extension of the one-dimensional linear chain to two-dimensional membranes, such as a drum skin, is straightforward if the membrane is thin enough so that the rigidity of the membrane can be ignored. Elasticity for three-dimensional solids requires accounting for the strong elastic forces exerted against any change in shape in addition to elastic forces opposing change in volume. The stiffness of solids to changes in shape, or volume, is best represented using the concepts of stress and strain.

Forces in matter can be divided into two classes;

1. body forces, such as gravity, which act on each volume element, and
2. surface forces which are the forces that act on both sides of any infinitessimal surface element inside the solid.

Surface forces can have components along the normal to the infinitessimal surface, as well as shear components in the plane of the surface element. Typically solids are elastic to both normal and shear components of the surface forces whereas shear forces in liquids and gases lead to fluid flow plus viscous forces due to energy dissipation. As described below, the forces acting on an infinitessimal surface element are best expressed in terms of the stress tensor, while the relative distortion of the shape, or volume, of the body are best expressed in terms of the strain tensor. The moduli of elasticity relate the ratio of the corresponding stress and strain tensors. The moduli of elasticity are constant in linear elastic solids and thus the stress is proportional to the strain providing that the strains do not exceed the elastic limit.

### Stress tensor

Consider an infinitessimal surface area $d\mathbf{A}$ of an arbitrary closed volume element $dV$ inside the medium. The surface area element is defined as a vector $d\mathbf{A} = \mathbf{\hat{n}} dA$ where $\mathbf{\hat{n}}$ is the outward normal to the closed surface that encloses the volume element. Assume that $d\mathbf{F}$ is the force element exerted by the outside on the material inside the volume element. The stress tensor $\mathbf{T}$ is defined as the ratio of $d\mathbf{F}$ and $d\mathbf{A}$ where the force vector $d\mathbf{F}$ is given by the inner product of the stress tensor $\mathbf{T}$ and the surface element vector $d\mathbf{A}$. That is,

$$
d\mathbf{F} = \mathbf{T}\cdot d\mathbf{A} \label{16.33}
$$

Since both $d\mathbf{F}$ and $d\mathbf{A}$ are vectors, then Equation \ref{16.33} implies that the stress tensor must be a second-rank tensor as described in appendix $19.5$, that is, the stress tensor is analogous to the rotation matrix or the inertia tensor. Note that if $d\mathbf{F}$ and $\mathbf{\hat{n}}d\mathbf{A}$ are colinear, then the stress tensor $\mathbf{T}$ reduces to the conventional pressure $P$. The general stress tensor equals the momentum flux density and has the dimensions of pressure.

### Strain tensor

Forces applied to a solid body can lead to translational, or rotational acceleration, in addition to changing the shape or volume of the body. Elastic forces do not act when an overall displacement $\boldsymbol{\xi}$ of an infinitessimal volume occurs, such as is involved in translational or rotational motion. Elastic forces act to oppose position-dependent differences in the displacement vector $\boldsymbol{\xi}$, that is, the strain depends on the tensor product $\boldsymbol{\nabla} \otimes \boldsymbol{\xi}$. For an elastic medium, the strain depends only on the applied stress and not on the prior loading history.

Consider that the matter at the location $\mathbf{r}$ is subject to an elastic displacement $\boldsymbol{\xi}$, and similarly at a displaced location $\mathbf{r}^{\prime} = \mathbf{r}+ \sum_i \frac{\partial \boldsymbol{\xi}}{\partial x_i} dx_i$ where $x_i$ are cartesian coordinates. The net relative displacement between $\mathbf{r}$ and $\mathbf{r}^{\prime}$ is given by

$$
d\xi^2 = \sum_i (dx_i + d\xi_i)^2 −\sum_i (dx_i)^2 = \sum_{ik} \left[ 2 \left( \frac{d\xi_i}{ dx_k} + \frac{d\xi_k}{ dx_i} \right) + \frac{d\xi_m}{ dx_i} \frac{d\xi_m}{ dx_k} \right] dx_i dx_k \label{16.34}
$$

Ignoring the second order term $\frac{d\xi_m }{dx_i} \frac{d\xi_m }{dx_k}$ equation gives that the $i^{th}$ component of $d\xi_i$ is

$$
d\xi_i = \sum_k \frac{1}{2} \left( \frac{d\xi_i}{ dx_k} + \frac{d\xi_k}{ dx_i} \right) dx_i dx_k \label{16.35}
$$

Define the elements of the strain tensor to be given by

$$
\sigma_{ik} = \frac{1}{2} \left( \frac{d\xi_i }{dx_k} + \frac{d\xi_k }{dx_i} \right) \label{16.36}
$$

then

$$
d\xi_i = \sum_k \sigma_{ik} dx_i dx_k \label{16.37}
$$

Thus the strain tensor $\boldsymbol{\sigma}$ is a rank-2 tensor defined as the ratio of the strain vector $\boldsymbol{\xi}$ and the infinitessimal area vector $d\mathbf{A}$.

$$
d\boldsymbol{\xi} = \boldsymbol{\sigma}\cdot d\mathbf{A} \label{16.38}
$$

where the component form of the rank -2 strain tensor is

$$
\boldsymbol{\sigma} = \frac{1}{ 2 } \begin{vmatrix} \frac{d\xi_1 }{dx_1} & \frac{d\xi_1}{ dx_2} & \frac{d\xi_1 }{dx_3} \\ \frac{d\xi_2}{ dx_1} & \frac{d\xi_2 }{dx_2} & \frac{d\xi_2 }{dx_3} \\ \frac{d\xi_3}{ dx_1} & \frac{d\xi_3}{ dx_2 } & \frac{d\xi_3}{ dx_3} \end{vmatrix} \label{16.39}
$$

The potential-energy density for linear elastic forces is quadratic in the strain components. That is, it is of the form

$$
U = \sum_{ijkl} \frac{1}{2} C_{ijkl}\sigma_{ij}\sigma_{kl} \label{16.40}
$$

where $C_{ijkl}$ is a rank-4 tensor. No preferential directions remain for a homogeneous isotropic elastic body which allows for two contractions, thereby reducing the potential energy density to the inner product

$$
U = \sum_{ik} \frac{1}{2} D_{ik} (\sigma_{ik})^2 \label{16.41}
$$

### Moduli of elasticity

The **modulus of elasticity** of a body is defined to be the slope of the stress-strain curve and thus, in principle, it is a complicated rank-4 tensor that characterizes the elastic properties of a material. Thus the general theory of elasticity is complicated because the elastic properties depend on the orientation of the microscopic composition of the elastic matter. The theory simplifies considerably for homogeneous, isotropic linear materials below the elastic limit, where the strain is proportional to the applied stress. That is, the modulus of elasticity then reduces by contractions to a constant scalar value that depends on the properties of the matter involved.

The potential energy density for homogeneous, isotropic, linear material, Equation \ref{16.41}, can be separated into diagonal and off-diagonal components of the strain tensor. That is,

$$
U = \frac{1}{2} \left[ \lambda \sum_i (\sigma_{ii})^2 + 2\mu \sum_{ik} (\sigma_{ik})^2 \right] \label{16.42}
$$

The diagonal first term is the dilation term which corresponds to changes in the volume with no changes in shape. The off-diagonal second term involves the shear terms that correspond to changes of the shape of the body that also changes the volume. The constants $\lambda$ and $\mu$ are Lamé’s moduli of elasticity which are positive. The various moduli of elasticity, corresponding to different distortions in the shape and volume of any solid body, can be derived from Lamé’s moduli for the material.

The components of the elastic forces can be derived from the gradient of the elastic potential energy, Equation \ref{16.42} by use of Gauss’ law plus vector differential calculus. The components of the elastic force, derived from the strain tensor $\boldsymbol{\sigma}$, can be associated with the corresponding components of the stress tensor $\mathbf{T}$. Thus, for homogeneous isotropic linear materials, the components of the stress tensor are related to the strain tensor by the relation

$$
T_{ij} = \lambda \delta_{ij} \sum_k \frac{\partial\xi_k }{\partial x_k} + \mu \left( \frac{d\xi_i}{ dx_j } + \frac{d\xi_j}{ dx_i} \right) = \lambda \delta_{ij} \sum_k \sigma_{kk} + 2\mu \sigma_{ij} \label{16.43}
$$

where it has been assumed that $\sigma_{ij} = \sigma_{ji}$. The two moduli of elasticity $\lambda$ and $\mu$ are material-dependent constants. Equation \ref{16.43} can be written in tensor notation as

$$
\mathbf{T} = \lambda tr (\boldsymbol{\sigma}) \mathbf{I} + 2\mu \boldsymbol{\sigma} \label{16.44}
$$

where $tr(\sigma )$ is the trace of the strain tensor and $I$ is the identity matrix.

Equation \ref{16.44} can be inverted to give the strain tensor components in terms of the stress tensor components.

$$
\sigma_{ij} = \frac{1}{ 2\mu} \left[ T_{ij} − \frac{\lambda }{(3\lambda + 2\mu )} \sum_k T_{kk} \delta_{ij}\right] \label{16.45}
$$

The various moduli of elasticity relate combinations of different stress and strain tensor components. The following five elastic moduli are used frequently to describe elasticity in homogeneous isotropic media, and all are related to Lamé’s two moduli of elasticity.

1) *Young’s modulus* $E$ describes tensile elasticity which is axial stiffness of the length of a body to deformation along the axis of the applied tensile force.

$$
E \equiv \frac{T_{11}}{ \sigma_{11}} = \frac{\mu (3\lambda + 2\mu )}{ (\lambda + \mu ) } \label{16.46}
$$

2)*Bulk modulus* $B = \frac{\Delta V}{V}$ defines the relative dilation or compression of a bodies volume to pressure applied uniformly in all directions.

$$
B = \lambda + \frac{2}{ 3} \mu \label{16.47}
$$

The bulk modulus is an extension of Young’s modulus to three dimensions and typically is larger than $E$. The inverse of the bulk modulus is called the compressibility of the material.

3) *Shear modulus* $G$ describes the shear stiffness of a body to volume-preserving shear deformations. The shear strain $\sigma$ becomes a deformation angle given by the ratio of the displacement along the axis of the shear force and the perpendicular moment arm. The shear modulus $G$ equals Lamé’s constant $\mu$. That is,

$$
G = \mu \label{16.48}
$$

4) *Poisson’s ratio* $\nu$ is the negative ratio of the transverse to axial strain. It is a measure of the volume conserving tendency of a body to contract in the directions perpendicular to the axis along which it is stretched. In terms of Lamé’s constants, Poisson’s ratio equals

$$
\nu = \frac{\lambda }{2 (\lambda + \mu )} \label{16.49}
$$

Note that for a stable, isotropic elastic material, Poisson’s ratio is bounded between $−1.0 \leq \nu \leq 0.5$ to ensure that the $B$, $\mu$ and $\lambda$ moduli have positive values. At the incompressible limit, $\nu = 0.5$, and the bulk modulus and Lame parameter $\lambda$ are infinite, that is, the compressibility is zero. Typical solids have Poisson’s ratios of $\nu \approx 0.05$ if hard and $\nu = 0.25$ if soft.

The stiffness of elastic solids in terms of the elastic moduli of solids can be complicated due to the geometry and composition of solid bodies. Often it is more convenient to express the stiffness in terms of the **spring constant** $\kappa$ where

$$
\kappa = \frac{dF}{ dx} \label{16.50}
$$

The spring constant is inversely proportional to the length of the spring because the strain of the material is defined to be the *fractional* deformation, not the *absolute* deformation.

### 16.5.4 Equations of motion in a uniform elastic media

The divergence theorem $(H.8)$ relates the volume integral of the divergence of $\mathbf{T}$ to the vector force density $\mathbf{F}$ acting on the closed surface.

$$
\mathbf{F} = \oint \mathbf{T}\cdot d\mathbf{A} = \int \boldsymbol{\nabla} \cdot \mathbf{T}d\tau = \int \mathbf{f}d\tau \label{16.51}
$$

That is, the inner product of the del operator, $\boldsymbol{\nabla}$, and the rank-2 stress tensor $\mathbf{T}$, give the vector force density $\mathbf{f}$. This force acting on the enclosed mass $\oint \rho d\tau$, for the closed volume, leads to an acceleration $\frac{\partial^2 \boldsymbol{\xi}}{ \partial t^2}$. Thus

$$
\mathbf{F} = \oint \mathbf{T}\cdot d\mathbf{A} = \int \boldsymbol{\nabla} \cdot \mathbf{T}d\tau = \oint \rho \frac{ \partial^2\boldsymbol{\xi}}{ \partial t^2} d\tau \label{16.52}
$$

Use Equation \ref{16.44} to relate the stress tensor $\mathbf{T}$ to the moduli of elasticity gives

$$
\rho \frac{ \partial^2\boldsymbol{\xi}_i }{\partial t^2} = \sum_j \left[ (\lambda + \mu ) \frac{\partial^2\boldsymbol{\xi}_j}{ \partial x_i \partial x_j} + \mu \frac{ \partial^2 \boldsymbol{\xi}_i }{\partial x^2_j} \right] \label{16.53}
$$

where $i = 1, 2, 3$. In general this equation is difficult to solve. However, for the simple case of a plane wave in the $i = 1$ direction, the problem reduces to the following three equations

$$
\rho \frac{ \partial^2\boldsymbol{\xi}_1}{ \partial t^2 } = (\lambda + 2\mu ) \frac{\partial^2\boldsymbol{\xi}_1}{ \partial x^2_1} \label{16.54}
$$

$$
\rho \frac{\partial^2\boldsymbol{\xi}_2}{ \partial t^2} = \mu \frac{\partial^2\boldsymbol{\xi}_2}{ \partial x^2_1} \label{16.55}
$$

$$
\rho \frac{\partial^2\boldsymbol{\xi}_3}{ \partial t^2} = \mu \frac{\partial^2\boldsymbol{\xi}_3 }{\partial x^2_1} \label{16.56}
$$

Equation \ref{16.54} corresponds to a longitudinal wave travelling with velocity $v = \sqrt{\frac{(\lambda +2\mu )}{ \rho}}$. Equations \ref{16.55}, \ref{16.56} correspond to two perpendicular transverse waves travelling with velocity $v = \sqrt{\frac{\mu }{\rho }}$. This illustrates the important fact that longitudinal waves travel faster than transverse waves in an elastic solid. Seismic waves in the Earth, generated by earthquakes, exhibit this property. Note that shearing stresses do not exist in ideal liquids and gases since they cannot maintain shear forces and thus $\mu = 0$.

## 16.6: Electromagnetic Field Theory

### Maxwell stress tensor

Analytical formulations for continuous systems, developed for describing elasticity, are generally applicable when applied to other fields, such as the electromagnetic field. The use of the Maxwell’s stress tensor $\mathbf{T}$, to describe momentum in the electromagnetic field, is an important example of the application of continuum mechanics in field theory.

The Lorentz force can be written as

$$
\mathbf{F} = \int \rho (\mathbf{E} + \mathbf{v} \times \mathbf{B}) d\tau = \int (\rho \mathbf{E} + \mathbf{J} \times \mathbf{B}) d\tau = \int \mathbf{f}d\tau \label{16.57}
$$

where the force density $\mathbf{f}$ is defined to be

$$
\mathbf{f} = (\rho \mathbf{E} + \mathbf{J} \times \mathbf{B}) \label{16.58}
$$

Maxwell’s equations

$$
\rho = \epsilon_0\boldsymbol{\nabla} \cdot \mathbf{E} \qquad \mathbf{J} = \frac{1}{ \mu_0} \boldsymbol{\nabla} \times \mathbf{B} − \epsilon_0 \frac{\partial\mathbf{E}}{ \partial t} \label{16.59}
$$

can be used to eliminate the charge and current densities in Equation \ref{16.57}

$$
\mathbf{f} =\epsilon_0 (\boldsymbol{\nabla} \cdot \mathbf{E}) \mathbf{E} + \left( \frac{1 }{\mu_0} \boldsymbol{\nabla} \times \mathbf{B} − \epsilon_0 \frac{\partial\mathbf{E}}{ \partial t } \right) \times \mathbf{B} \label{16.60}
$$

Vector calculus gives that

$$
\frac{\partial}{ \partial t} (\mathbf{E} \times \mathbf{B}) = \frac{\partial\mathbf{E}}{ \partial t} \times \mathbf{B} + \mathbf{E}\times \frac{\partial\mathbf{B}}{ \partial t} \label{16.61}
$$

while Faraday’s law gives

$$
\frac{\partial\mathbf{B}}{ \partial t } = −\boldsymbol{\nabla} \times \mathbf{E} \label{16.62}
$$

Equation \ref{16.62} allows Equation \ref{16.61} to be rewritten as

$$
\frac{\partial\mathbf{E}}{ \partial t} \times \mathbf{B} = + \frac{\partial }{\partial t} (\mathbf{E} \times \mathbf{B}) − \mathbf{E}\times \frac{\partial\mathbf{B}}{ \partial t} = + \frac{\partial }{\partial t } (\mathbf{E} \times \mathbf{B}) + \mathbf{E}\times (\boldsymbol{\nabla} \times \mathbf{E}) \label{16.63}
$$

Equation \ref{16.63} can be inserted into Equation \ref{16.60}. In addition, a term $\frac{1 }{\mu_0} (\boldsymbol{\nabla} \cdot \mathbf{B}) \mathbf{B}$ can be added since $\boldsymbol{\nabla} \cdot \mathbf{B} =0$ which allows equation 16.60 to be written in the symmetric form

$$
\begin{align} \mathbf{f} = \epsilon_0 (\boldsymbol{\nabla} \cdot \mathbf{E}) \mathbf{E} + \frac{1 }{\mu_0} (\boldsymbol{\nabla} \cdot \mathbf{B}) \mathbf{B}+ \frac{1 }{\mu_0} (\boldsymbol{\nabla} \times \mathbf{B}) \times \mathbf{B} − \epsilon_0 \frac{\partial\mathbf{E}}{ \partial t} \times \mathbf{B} \label{16.64} \\ = \epsilon_0 (\boldsymbol{\nabla} \cdot \mathbf{E}) \mathbf{E} + \frac{1 }{\mu_0} (\boldsymbol{\nabla} \cdot \mathbf{B}) \mathbf{B}+ \frac{1 }{\mu_0} (\boldsymbol{\nabla} \times \mathbf{B}) \times \mathbf{B}−\epsilon_0 \frac{\partial}{ \partial t} (\mathbf{E} \times \mathbf{B}) − \epsilon_0 \mathbf{E}\times (\boldsymbol{\nabla} \times \mathbf{E}) \label{16.65} \end{align}
$$

Using the vector identity

$$
\boldsymbol{\nabla}(\mathbf{A} \cdot \mathbf{B}) = \mathbf{A}\times (\boldsymbol{\nabla} \times \mathbf{B}) + \mathbf{B}\times (\boldsymbol{\nabla} \times \mathbf{A})+(\mathbf{A} \cdot \boldsymbol{\nabla}) \mathbf{B}+ (\mathbf{B} \cdot \boldsymbol{\nabla}) \mathbf{A} \label{16.66}
$$

Let $\mathbf{A} = \mathbf{B} = \mathbf{E}$, then

$$
\boldsymbol{\nabla} ( E^2) = 2 \mathbf{E}\times (\boldsymbol{\nabla} \times \mathbf{E})+2(\mathbf{E} \cdot \boldsymbol{\nabla}) \mathbf{E} \label{16.67}
$$

That is

$$
\mathbf{E}\times (\boldsymbol{\nabla} \times \mathbf{E}) = \frac{1}{2} \boldsymbol{\nabla} ( E^2) − (\mathbf{E} \cdot \boldsymbol{\nabla}) \mathbf{E} \label{16.68}
$$

Similarly

$$
\mathbf{B}\times (\boldsymbol{\nabla} \times \mathbf{B}) = \frac{1}{2} \boldsymbol{\nabla} ( B^2) − (\mathbf{B} \cdot \boldsymbol{\nabla}) \mathbf{B} \label{16.69}
$$

Inserting equations \ref{16.68} and \ref{16.69} into Equation \ref{16.65} gives

$$
\mathbf{f}=\epsilon_0 \left[ (\boldsymbol{\nabla} \cdot \mathbf{E}) \mathbf{E}+ (\mathbf{E} \cdot \boldsymbol{\nabla}) \mathbf{E}− \frac{1}{ 2} \boldsymbol{\nabla}E^2 \right] + \frac{1 }{\mu_0} \left[ (\boldsymbol{\nabla} \cdot \mathbf{B}) \mathbf{B}+ (\mathbf{B} \cdot \boldsymbol{\nabla}) \mathbf{B}−\frac{1}{ 2} \boldsymbol{\nabla}B^2 \right] − \epsilon_0 \frac{\partial}{ \partial t} (\mathbf{E} \times \mathbf{B}) \label{16.70}
$$

This complicated formula can be simplified by defining the rank-2 **Maxwell stress tensor** $\mathbf{T}$ which has components

$$
T_{ij} \equiv \epsilon_0 \left( E_iE_j − \frac{1}{2} \delta_{ij}E^2 \right) + \frac{1 }{\mu_0} \left( B_iB_j − \frac{1}{2} \delta_{ij}B^2 \right) \label{16.71}
$$

The inner product of the del operator and the Maxwell stress tensor is a vector with $j$ components of

$$
(\boldsymbol{\nabla} \cdot \mathbf{T})_j = \epsilon_0 \left[ (\boldsymbol{\nabla} \cdot \mathbf{E}) E_j+ (\mathbf{E} \cdot \boldsymbol{\nabla}) E_j − \frac{1}{2} \boldsymbol{\nabla}^2_jE^2 \right] + \frac{1 }{\mu_0} \left[ (\boldsymbol{\nabla} \cdot \mathbf{B}) B_j+ (\mathbf{B} \cdot \boldsymbol{\nabla}) B_j − \frac{1}{2} \boldsymbol{\nabla}^2_jB^2 \right] \label{16.72}
$$

The above definition of the Maxwell stress tensor, plus the Poynting vector $\mathbf{S} = \frac{1 }{\mu_0} (\mathbf{E} \times \mathbf{B})$, allows the force density Equation \ref{16.58} to be written in the form

$$
\mathbf{f} = \boldsymbol{\nabla} \cdot \mathbf{T}−\epsilon_0\mu_0 \frac{\partial \mathbf{S}}{ \partial t} \label{16.73}
$$

The divergence theorem allows the total force, acting of the volume $\tau$, to be written in the form

$$
\begin{align} \mathbf{F} = \int \left( \boldsymbol{\nabla} \cdot \mathbf{T}−\epsilon_0\mu_0 \frac{\partial \mathbf{S}}{ \partial t} \right) d\tau \label{16.74} \\ = \oint \mathbf{T}\cdot d\mathbf{a}−\epsilon_0\mu_0 \frac{d}{dt} \int \mathbf{Sd}\boldsymbol{\tau} \label{16.75}\end{align}
$$

Note that, if the Poynting vector is time independent, then the second term in Equation \ref{16.75} is zero and the Maxwell stress tensor $\mathbf{T}$ is the force per unit area, (stress) acting on the surface. The fact that $\mathbf{T}$ is a rank-2 tensor is apparent since the stress represents the ratio of the force-density vector $d\mathbf{f}$ and the infinitessimal area vector $d\mathbf{a}$, which do not necessarily point in the same directions.

### Momentum in the electromagnetic field

Chapter $7.2$ showed that the electromagnetic field carries a linear momentum $q\mathbf{A}$ where $q$ is the charge on a body and $\mathbf{A}$ is the electromagnetic vector potential. It is useful to use the Maxwell stress tensor to express the momentum density directly in terms of the electric and magnetic fields.

Newton’s law of motion can be used to write Equation \ref{16.75} as

$$
\mathbf{F}= \frac{d\mathbf{p}_{mech}}{ dt} = \oint \mathbf{T}\cdot d\mathbf{a}−\epsilon_0\mu_0 \frac{d}{dt} \int \mathbf{Sd}\boldsymbol{\tau} \label{16.76}
$$

where $\mathbf{p}$ is the total mechanical linear momentum of the volume $\tau$. Equation \ref{16.76} implies that the electromagnetic field carries a linear momentum

$$
\mathbf{p}_{field} = \epsilon_0\mu_0 \int \mathbf{Sd}\boldsymbol{\tau} \label{16.77}
$$

The $\oint \mathbf{T}\cdot d\mathbf{a}$ term in Equation \ref{16.76} is the momentum per unit time flowing into the closed surface. In field theory it can be useful to describe the behavior in terms of the momentum flux density $\boldsymbol{\pi}$. Thus the momentum flux density $\boldsymbol{\pi}_{field}$ in the electromagnetic field is

$$
\boldsymbol{\pi}_{field}=\epsilon_0\mu_0 \mathbf{S} \label{16.78}
$$

Then Equation \ref{16.76} implies that the total momentum flux density $\boldsymbol{\pi} = \boldsymbol{\pi}_{mech}+\boldsymbol{\pi}_{field}$ is related to Maxwell’s stress tensor by

$$
\frac{\partial }{\partial t} (\boldsymbol{\pi}_{mech} + \boldsymbol{\pi}_{field}) = \boldsymbol{\nabla} \cdot \mathbf{T} \label{16.79}
$$

That is, like the elasticity stress tensor, the divergence of Maxwell’s stress tensor $\mathbf{T}$ equals the rate of change of the total momentum density, that is, $-\mathbf{T}$ is the momentum flux density.

This discussion of the Maxwell stress tensor and its relation to momentum in the electromagnetic field illustrates the role that analytical formulations of classical mechanics can play in field theory

## 16.7: Ideal Fluid Dynamics

The distinction between a solid and a fluid is that a fluid flows under shear stress whereas the elasticity of solids oppose distortion and flow. Shear stress in a fluid is opposed by dissipative viscous forces, which depend on velocity, as opposed to elastic solids where the shear stress is opposed by the elastic forces which depend on the displacement. An ideal fluid is one where the viscous forces are negligible, and thus the shear stress **Lamé parameter** $\mu = 0$.

### Continuity Equation

Fluid dynamics requires a different philosophical approach than that used to describe the motion of an ensemble of known solid bodies. The prior discussions of classical mechanics used, as variables, the coordinates of each member of an ensemble of particles with known masses. This approach is not viable for fluids which involve an enormous number of individual atoms as the fundamental bodies of the fluid. The best philosophical approach for describing fluid dynamics is to employ continuum mechanics using definite fixed volume elements $d\tau$ and describe the fluid in terms of macroscopic variables of the fluid such as mass density $\rho$, pressure $P$, and fluid velocity $\mathbf{v}$.

Conservation of fluid mass requires that the rate of change of mass in a fixed volume must equal the net inflow of mass.

$$
\frac{d}{dt}\int_{\tau} \rho d\tau + \oint \rho \mathbf{v} \cdot d\mathbf{a} = \mathbf{0} \label{16.80}
$$

Using the divergence theorem $(H2)$ allows this to be written as

$$
\int_{\tau} \left( \frac{\partial \rho}{ \partial t} + \boldsymbol{\nabla} \cdot (\rho \mathbf{v}) \right) d\tau = 0 \label{16.81}
$$

Mass conservation must hold for any arbitrary volume, therefore the *continuity equation* can be written in the differential form

$$
\frac{\partial \rho}{ \partial t} + \boldsymbol{\nabla} \cdot (\rho \mathbf{v})=0 \label{16.82}
$$

### Euler’s hydrodynamic equation

The fluid surrounding a volume $\tau$ exerts a net force $\mathbf{F}$ that equals the surface integral of the pressure $\mathbf{P}$. This force can be transformed to a volume integral of $\boldsymbol{\nabla}P$. The net force then will lead to an acceleration of the volume element. That is

$$
\mathbf{F} = − \oint P d\mathbf{a} = −\int \boldsymbol{\nabla}P d\tau =\int \rho \frac{d\mathbf{v}}{dt} d\tau \label{16.83}
$$

Thus the force density $\mathbf{f}$ is given by

$$
\mathbf{f} = −\boldsymbol{\nabla}\mathbf{P} =\rho \frac{d\mathbf{v}}{dt} \label{16.84}
$$

Note that the acceleration $\frac{d\mathbf{v}}{dt}$ in Equation \ref{16.83} refers to the rate of change of velocity for *individual atoms in the fluid*, not the rate of change of fluid velocity at a *fixed point in space*. These two accelerations are related by noting that, during the time $dt$, the change in velocity $d\mathbf{v}$ of a given fluid particle is composed of two parts, namely

1. the change during $dt$ in the velocity at a fixed point in space, and
2. the difference between the velocities at that same instant in time at two points displaced a distance $d\mathbf{r}$ apart, where $d\mathbf{r}$ is the distance moved by a given fluid particle during the time $dt$.

The first part is given by $\frac{\partial \mathbf{v}}{ \partial t} dt$ at a given point $(x,y,z)$ in space. The second part equals

$$
dx\frac{\partial \mathbf{v}}{\partial x} + dy \frac{\partial \mathbf{v}}{\partial y} + dz \frac{\partial \mathbf{v}}{\partial z} = (d\mathbf{r} \cdot \boldsymbol{\nabla}) \mathbf{v} \label{16.85}
$$

Thus

$$
d\mathbf{v} = \frac{\partial \mathbf{v}}{\partial t} dt + (d\mathbf{r} \cdot \boldsymbol{\nabla}) \mathbf{v} \label{16.86}
$$

Divide both sides by $dt$ gives that the acceleration of the atoms in the fluid equals

$$
\frac{d\mathbf{v}}{dt} = \frac{\partial \mathbf{v}}{\partial t} + (\mathbf{v} \cdot \boldsymbol{\nabla}) \mathbf{v} \label{16.87}
$$

Substitute Equation \ref{16.87} into \ref{16.84} gives

$$
\frac{\partial \mathbf{v}}{\partial t} + (\mathbf{v} \cdot \boldsymbol{\nabla}) \mathbf{v} = −\frac{1}{ \rho} \boldsymbol{\nabla}P \label{16.88}
$$

This is Euler’s equation for hydrodynamics. The two terms on the left represent the acceleration in the individual fluid components while the right-hand side lists the force density producing the acceleration.

Additional forces can be added to the right-hand side. For example, the gravitational force density $\rho \mathbf{g}$ can be expressed in terms of the gravitational scalar potential $V$ to be

$$
\rho \mathbf{g} = −\boldsymbol{\rho}\boldsymbol{\nabla}V \label{16.89}
$$

Inclusion of the gravitational field force density in Euler’s equation gives

$$
\frac{\partial \mathbf{v}}{\partial t }+ (\mathbf{v} \cdot \boldsymbol{\nabla}) \mathbf{v} = −\frac{1}{ \rho} \boldsymbol{\nabla} (P + \rho V ) \label{16.90}
$$

### Irrotational flow and Bernoulli’s equation

Streamlined flow corresponds to**irrotational flow**, that is, $\boldsymbol{\nabla} \times \mathbf{v} = \mathbf{0}$. Since irrotational flow is curl free, the velocity streamlines can be represented by a scalar potential field $\phi$. That is

$$
\mathbf{v} = −\boldsymbol{\nabla}\phi \label{16.91}
$$

This scalar potential field $\phi$ can be used to derive the vector velocity field for irrotational flow.

Note that the $(\mathbf{v} \cdot \boldsymbol{\nabla}) \mathbf{v}$ term in Euler’s Equation \ref{16.90} can be rewritten using the vector identity

$$
(\mathbf{v} \cdot \boldsymbol{\nabla}) \mathbf{v} = \frac{1}{ 2} \boldsymbol{\nabla} ( v^2) − \mathbf{v} \times \boldsymbol{\nabla} \times \mathbf{v} \label{16.92}
$$

Inserting Equation \ref{16.92} into Euler’s Equation \ref{16.90} then gives.

$$
\frac{\partial \mathbf{v}}{\partial t} = \mathbf{v} \times \boldsymbol{\nabla} \times \mathbf{v}−\frac{1}{ \rho} \boldsymbol{\nabla} \left( \frac{1}{ 2} \rho v^2 + P + \rho V \right) \label{16.93}
$$

Potential flow corresponds to time independent irrotational flow, that is, both $\frac{\partial \mathbf{v}}{\partial t} = 0$ and $\boldsymbol{\nabla} \times \mathbf{v} = 0$. For potential flow Equation \ref{16.93} reduces to

$$
\boldsymbol{\nabla} \left( \frac{1}{ 2} \rho v^2 + P + \rho V \right) = 0 \nonumber
$$

which implies that

$$
\left( \frac{1}{ 2} \rho v^2 + P + \rho V \right) = \text{ constant} \label{16.94}
$$

This is the famous Bernoulli’s equation that relates the interplay of the fluid velocity, pressure and gravitational energy. Bernoulli’s equation plays important roles in both hydrodynamics and aerodynamics.

### Gas flow

Fluid dynamics applied to gases is a straightforward extension of fluid dynamics that employs standard thermodynamical concepts. The following example illustrates the application of fluid mechanics for calculating the velocity of sound in a gas.

Example 16.1: Acoustic Waves in a Gas

Propagation of acoustic waves in a gas provides an example of using the three-dimensional Lagrangian density. Only longitudinal waves occur in a gas and the velocity is given by thermodynamics of the gas. Let the displacement of each gas molecule be designated by the general coordinate $\mathbf{q}$ with corresponding velocity $\mathbf{\dot{q}}$. Let the gas density be $\rho$, then the kinetic energy density $(KED)$ of an infinitessimal volume of gas $\Delta \tau$ is given by

$$
\Delta (KED) = \frac{1}{ 2} \rho_0 \mathbf{\dot{q}}^2 \nonumber
$$

The rapid contractions and expansions of the gas in an acoustic wave occur adiabatically such that the product $P V^{\gamma}$ is a constant, where

$$
\gamma = \frac{\text{specific heat at constant pressure}}{\text{specific heat at constant volume}}. \nonumber
$$

Therefore the change in potential energy density $\Delta (PED)$ is given to second order by

$$
\Delta (PED) = \frac{1}{\tau_0} \int^{ V_0+\Delta V}_{V_0} P d\tau = \frac{P_0}{\tau_0} \Delta \tau + \frac{1}{ 2\tau_0} \left( \frac{\partial P}{ \partial \tau} \right)_0 (\Delta \tau )^2 = \frac{P_0}{\tau_0} \Delta \tau − \frac{1}{ 2\tau_0} \left( \gamma \frac{P_0}{\tau_0} \right) (\Delta \tau )^2 \nonumber
$$

Since the volume and density are related by

$$
\tau_o = \frac{M}{\rho_0} \nonumber
$$

then the fractional change in the density $\sigma$ is related to the density by

$$
\rho = \rho_0(1 + \sigma ) \nonumber
$$

This implies that the potential energy density $(PED)$ is given by

$$
\Delta (PED) = \left[ P_0\sigma + \gamma \frac{P_0}{ 2} \sigma^2 \right] \nonumber
$$

The mass flowing out of the volume $V_0$ must equal the fractional change in density of the volume, that is

$$
\rho_0\int \mathbf{q} \cdot \mathbf{dS} = −\boldsymbol{\rho}_0 \int \sigma d\tau \nonumber
$$

The divergence theorem gives that

$$
\int \mathbf{q} \cdot \mathbf{dS} =\int \nabla \cdot \mathbf{q} d\tau = −\int \sigma d\tau \nonumber
$$

Thus the density $\sigma$ is given by minus the divergence of $\mathbf{q}$

$$
\sigma = −\nabla \cdot \mathbf{q} \nonumber
$$

This allows the potential energy density to be written as

$$
\Delta (PED) = −P_0\nabla \cdot \mathbf{q} + \frac{\gamma P_0}{ 2} (\nabla \cdot \mathbf{q})^2 \nonumber
$$

Combining the kinetic energy density and the potential energy density gives the complete Lagrangian density for an acoustic wave in a gas to be

$$
\mathfrak{L} = \frac{1}{2} \rho_0 \mathbf{\dot{q}}^2 + P_0 \nabla \cdot \mathbf{q} − \frac{\gamma P_0}{ 2} (\nabla \cdot \mathbf{q})^2 \nonumber
$$

Inserting this Lagrangian density in the corresponding equations of motion, equation $(16.3.16)$, gives that

$$
\nabla^2\mathbf{q}− \frac{\rho_0}{ \gamma P_0} \frac{d^2\mathbf{q}}{ dt^2} = 0 \nonumber
$$

where $P_0$ and $\rho_0$ are the ambient pressure and density of the gas. This is the wave equation where the phase velocity of sound is given by

$$
v_{phase} = \sqrt{\frac{\gamma P_0}{ \rho_0}} \nonumber
$$

## 16.8: Viscous Fluid Dynamics

Viscous fluid dynamics is a branch of classical mechanics that plays a pivotal role in a wide range of aspects of life, such as blood flow in human anatomy, weather, hydraulic engineering, and transportation by land, sea, and air. Viscous fluid flow provides natures most common manifestation of nonlinearity and turbulence in classical mechanics, and provides an excellent illustration of possible solutions of non-linear equations of motion introduced in chapter $4$. A detailed description of turbulence remains a challenging problem and this subject has the reputation of being the last great unsolved problem in classical mechanics. There is an apocryphal story that Werner Heisenberg was asked, if given the opportunity, what would he like to ask God. His reply was “When I meet God, I am going to ask him two questions: Why relativity? and why turbulence?, I really believe he will only have an answer to the first”.

In contrast to solids, fluids do not have elastic restoring forces to support shear stress because the fluid flows. Shear stresses in fluids are balance by viscous forces which are velocity dependent. There are two mechanisms that lead to shear stress acting between adjacent fluid layers in relative motion. The first mechanism involves laminar flow where the viscous forces produce shear stress between adjacent layers of the fluid which are moving parallel along adjacent streamlines at differing velocities. Viscous forces typically dominate laminar flow. High viscosity fluids like honey exhibit laminar flow and are more difficult to stir or pour compared with low-viscosity fluids like water. The second mechanism involves turbulent flow where shear stress is due to momentum transfer between adjacent layers when the flow breaks up into large-scale coherent vortex structures which carry most of the kinetic energy. These eddies lead to transverse motion that transfers momentum plus heat between adjacent layers and leads to higher drag. The wing-tip vortex produced by the wing tip of an aircraft is an example of a dynamically-distinct, large-scale, coherent vortex structure which has considerable angular momentum and decays by fragmentation into a cascade of smaller scale structures.

### Navier-Stokes equation

Viscous forces acting on the small-scale coherent structures eventually dissipate the energy in turbulent motion. The viscous drag can be handled in terms of a stress tensor $\mathbf{T}$ analogous to its use when accounting for the elastic restoring forces in elasticity as discussed in chapter $16.5.3$. That is, the viscous force density is related to the deceleration of the volume element by

$$
\frac{\partial}{ \partial t} (\rho \mathbf{v}) = −\boldsymbol{\nabla} \cdot \mathbf{T} \label{16.95}
$$

where the components of the stress tensor are

$$
T_{ki} = T_{ik} = P \delta_{ik} + \rho v_i v_k \label{16.96}
$$

Note that the stress tensor gives the momentum flux density tensor, which involves a diagonal term proportional to pressure $P$, plus a viscous drag term that is proportional to the product of two velocities.

The Navier-Stokes equations are the fundamental equations characterizing fluid flow. They are based on application of Newton’s second law of motion to fluids together with the assumption that the fluid stress is the sum of a diffusing viscous term plus a pressure term. Combining Euler’s equation, $(16.7.11)$, with \ref{16.95} gives the Navier-Stokes equation

$$
\rho \left[ \frac{\partial \mathbf{v}}{ \partial t} + \mathbf{v} \cdot \boldsymbol{\nabla}\mathbf{v} \right] = −\boldsymbol{\nabla}P + \boldsymbol{\nabla} \cdot \mathbf{ }T+\mathbf{f} \label{16.97}
$$

where $\rho$ is the fluid density, $\mathbf{v}$ is the flow velocity vector, $P$ the pressure, $\mathbf{T}$ is the shear stress tensor viscous drag term, and $\mathbf{f}$ represents external body forces per unit volume such as gravity acting on the fluid. For incompressible flow the stress tensor term simplifies to $\boldsymbol{\nabla} \cdot \mathbf{T} =\mu \boldsymbol{\nabla}^2\mathbf{v}$. Then the Navier-Stokes equation simplifies to

$$
\rho \left[ \frac{\partial \mathbf{v}}{ \partial t} + \mathbf{v} \cdot \boldsymbol{\nabla}\mathbf{v} \right] = −\boldsymbol{\nabla}P + \mu \boldsymbol{\nabla}^2\mathbf{v}+\mathbf{f} \label{16.98}
$$

where $\mu \boldsymbol{\nabla}^2\mathbf{v}$ is the viscosity drag term. The left-hand side of Equation \ref{16.98} represents the rate of change of momentum per unit volume while the right-hand side represents the summation of the forces per unit volume that are acting.

The Navier-Stokes equations are nonlinear due to the $(\mathbf{v} \cdot \boldsymbol{\nabla}) \mathbf{v}$ term as well as being a function of velocity. This non-linearity leads to a wide spectrum of dynamic behavior ranging from ordered laminar flow to chaotic turbulence. Numerical solution of the Navier-Stokes equations is extremely difficult because of the wide dynamic range of the dimensions of the coherent structures involved in turbulent motion. For example, simulation calculations require use of a high resolution mesh which is a challenge to the capabilities of current generation computers.

The microscopic boundary condition at the interface of the solid and fluid is that the fluid molecules have zero average tangential velocity relative to the normal to the solid-fluid interface. This implies that there is a boundary layer for which there is a gradient in the tangential velocity of the fluid between the solid-fluid interface and the free-steam velocity. This velocity gradient produces vorticity in the fluid. When the viscous forces are negligible then the angular momentum in any coherent vortex structure is conserved leading to the vortex motion being preserved as it propagates.

### Reynolds number

Fluid flow can be characterized by the Reynolds number Re which is a dimensionless number that is a measure of the ratio of the inertial forces $\rho v^2/L$ to viscous forces $\mu v/L^2$. That is,

$$
\text{Re} \equiv \frac{\text{Inertial forces}}{\text{Viscous forces}} = \frac{\rho vL}{ \mu} = \frac{vL}{ \eta} \label{16.99}
$$

where $v$ is the relative velocity between the free fluid flow and the solid surface, $L$ is a characteristic linear dimension, $\mu$ is the dynamic viscosity of the fluid, $\eta$ is the kinematic viscosity $(\eta = \frac{\mu }{\rho} )$, and $\rho$ is the density of the fluid. The Law of Similarity implies that at a given Reynolds number, for a specific shaped solid body, the fluid flow behaves identically independent of the size of the body. Thus one can use small models in wind tunnels, or water-flow tanks, to accurately model fluid flow that can be scaled up to a full-sized aircraft or boats by scaling $v$ and $L$ to give the same Reynolds number.

### Laminar and turbulent fluid flow

Fluid flow over a cylinder illustrates the general features of fluid flow. The drag force $F_D$ acting on a cylinder of diameter $D$ and length $l$, with the cylindrical axis perpendicular to the fluid flow, is given by

$$
F_D = \frac{1}{ 2} \rho v^2C_D Dl \label{16.100}
$$

where $C_D$ is the coefficient of drag. Figure 16.1 upper shows the dependence of the drag coefficient $C_D$ as a function of the Reynolds number, for fluid flow that is transverse to a smooth circular cylinder. The lower part of Figure 16.1 shows the streamlines for flow around the cylinder at various Reynolds numbers for the points identified by the letters $A$, $B$, $C$, $D$, and $E$ on the plot of the drag coefficient versus Reynolds number for a smooth cylinder.

:::{figure} ../images/lt-21259-15.8.1.png
:alt: 15.8.1.PNG

$1$: Upper: The dependence of the coefficient of drag $C_D$ on Reynolds number Re for fluid flow perpendicular to a smooth circular cylinder of diameter $D$ and length $l$. Lower: Typical flow patterns for flow past a circular cylinder at various Reynolds numbers as indicated in the upper figure.
:::

A) At low velocities, where Re $\leq 1$, the flow is laminar around the cylinder in that the low vorticity is damped by the viscous forces and the $\frac{\partial \mathbf{v}}{ \partial t}$ term in Equation \ref{16.98} can be ignored. The coefficient of drag $C_D$ varies inversely with Re leading to the drag forces that are roughly linear with velocity as described in chapter $2.10.5$. The size and velocities of raindrops in a light rain shower correspond to such Reynolds numbers.

B) For $10 < \text{Re} < 30$ the flow has two turbulent vortices immediately behind the body in the wake of the cylinder, but the flow still is primarily laminar as illustrated.

C) For $40 < \text{Re} < 250$ the pair of vortices peel off alternately producing a regular periodic sequence of vortices although the flow still is laminar. This vortex sheet is called a von Kármán vortex sheet for which the velocity at a given position, relative to the cylinder, is time dependent in contrast to the situation at lower Reynolds numbers.

D) For $10^3 < \text{Re} < 10^5$ viscous forces are negligible relative to the inertial effects of the vortices and boundary-layer vortices have less time to diffuse into the larger region of the fluid, thus the boundary layer is thinner. The boundary-layer flow exhibits a small scale chaotic turbulence in three dimensions superimposed on regular alternating vortex structures. In this range $C_D$ is roughly constant and thus the drag forces are proportional to the square of the velocity. This regime of Reynold numbers corresponds to typical velocities of moving automobiles.

E) For Re $\approx 10^6$, which is typical of a flying aircraft, the inertial effects dominate except in the narrow boundary layer close to the solid-fluid interface. The chaotic region works its way further forward on the cylinder reducing the volume of the chaotic turbulent boundary layer which results in a significant decreases in $C_D$. For a sailplane wing flying at about $50$ $knots$, the boundary layer at the leading edge of the cylinder reduces to the order of a millimeter in thickness at the leading edge and a centimeter at the trailing edge. At these Reynold’s numbers the airflow comprises a thin boundary layer, where viscous effects are important, plus fluid flow in the bulk of the fluid where the vortex inertial terms dominate and viscous forces can be ignored. That is, the viscous stress tensor term $\boldsymbol{\nabla} \cdot \mathbf{T}$, on the right-hand side of Equation \ref{16.97}, can be ignored, and the Navier-Stokes equation reduces to the simpler Euler equation for such inviscid fluid flow.

The importance of the inertia of the vortices is illustrated by the persistence of the vortex structure and turbulence over a wide range of length scales characteristic of turbulent flow. The dynamic range of the dimension of coherent vortex structures is enormous. For example, in the atmosphere the vortex size ranges from $10^5$ $m$ in diameter for hurricanes down to $10^{−3}$ $m$ in thin boundary layers adjacent to an aircraft wing. The transition from laminar to turbulent flow is illustrated by water flow over the hull of a ship which involves laminar flow at the bow followed by turbulent flow behind the bow wave and at the stern of the ship. The broad extent of the white foam of seawater along the side and the stern of a ship illustrates the considerable energy dissipation produced by the turbulence. The boundary layer of a stalled aircraft wing is another example. At a high angle of attack, the airflow on the lower surface of the wing remains laminar, that is, the stream velocity profile, relative to the wing, increases smoothly from zero at the wing surface outwards until it meets the ambient air velocity on the outer surface of the boundary layer which is the order of a millimeter thick. The flow on the top surface of the wing initially is laminar before becoming turbulent at which point the boundary layer rapidly increases in thickness. Further back the airflow detaches from the wing surface and large-scale vortex structures lead to a wide boundary layer comparable in thickness to the chord of the wing with vortex motion that leads to the airflow reversing its direction adjacent to the upper surface of the wing which greatly increases drag. When the vortices begin to shed off the bounded surface they do so at a certain frequency which can cause vibrations that can lead to structural failure if the frequency of the shedding vortices is close to the resonance frequency of the structure.

Considerable time and effort are expended by aerodynamicists and hydrodynamicists designing aircraft wings and ship hulls to maximize the length of laminar region of the boundary layer to minimize drag. When the Reynolds number is large the slightest imperfections in the shape of wing, such as a speck of dust, can trigger the transition from laminar to turbulent flow. The boundaries between adjacent large-scale coherent structures are sensitively identified in computer simulations by large divergence of the streamlines at any separatrix. A large positive, finite-time, Lyapunov exponent identifies divergence of the streamlines which occurs at a separatrix between adjacent large-scale coherent vortex structures, whereas the Lyapunov exponents are negative for converging streamlines within any coherent structure. Computations of turbulent flow often combine the use of finite-time Lyapunov exponents to identify coherent structures, plus Lagrangian mechanics for the equations of motion since the Lagrangian is a scalar function, it is frame independent, and it gives far better results for fluid motion than using Newtonian mechanics. Thus the Lagrangian approach in the continua is used extensively for calculations in aerodynamics, hydrodynamics, and studies of atmospheric phenomena such as convection, hurricanes, tornadoes, etc.

## 16.9: Summary and Implications

The goal of this chapter is to provide a glimpse into the classical mechanics of the continua which introduces the Lagrangian density and Hamiltonian density formulations of classical mechanics.

### Lagrangian density formulation

In three dimensional Lagrangian density $\mathfrak{L}(\mathbf{q}, \frac{d\mathbf{q}}{ dt} ,\boldsymbol{\nabla} \cdot \mathbf{q}, x, y, z, t)$ is related to the Lagrangian $L$ by taking the volume integral of the Lagrangian density.

$$
L = \int \mathfrak{L}(\mathbf{q}, \frac{d\mathbf{q} }{dt }, \boldsymbol{\nabla} \cdot \mathbf{q}, x, y, z, t)d\tau 
$$

Applying Hamilton’s Principle to the three-dimensional Lagrangian density leads to the following set of differential equations of motion

$$
\frac{\partial}{\partial t }\left(\frac{ \partial \mathfrak{L}}{\frac{ \partial \mathbf{q} }{\partial t}} \right) + \frac{\partial}{\partial x} \left(\frac{ \partial \mathfrak{L}}{\frac{ \partial \mathbf{q} }{\partial x}} \right) + \frac{\partial}{\partial y} \left(\frac{ \partial \mathfrak{L}}{\frac{ \partial \mathbf{q} }{\partial y}} \right) + \frac{\partial}{\partial z} \left(\frac{ \partial \mathfrak{L}}{\frac{ \partial \mathbf{q} }{\partial z}} \right) − \frac{\partial \mathfrak{L}} {\partial \mathbf{q}} = 0 
$$

### Hamiltonian density formulation

In the limit that the coordinates $q,p$ are continuous, then the Hamiltonian density can be expressed in terms of a volume integral over the momentum density $\pi$ and the Lagrangian density $\mathfrak{L}$ where

$$
\boldsymbol{\pi} \equiv \frac{\partial \mathfrak{L}}{ \partial \mathbf{\dot{q}}} 
$$

Then the obvious definition of the Hamiltonian density $\mathfrak{H}$ is

$$
H = \int \mathfrak{H} dV = \int (\boldsymbol{\pi} \cdot \mathbf{\dot{q}} - \mathfrak{L}) d\tau 
$$

where the Hamiltonian density is given by

$$
\mathfrak{H} =\boldsymbol{\pi} \cdot \mathbf{\dot{q}} − \mathfrak{L} 
$$

These Lagrangian and Hamiltonian density formulations are of considerable importance to field theory and fluid mechanics.

### Linear elastic solids

The theory of continuous systems was applied to the case of linear elastic solids. The **stress tensor** $\mathbf{T}$ is a rank 2 tensor defined as the ratio of the force vector $d\mathbf{F}$ and the surface element vector $d\mathbf{A}$. That is, the force vector is given by the inner product of the stress tensor $\mathbf{T}$ and the surface element vector $d\mathbf{A}$.

$$
d\mathbf{F} = \mathbf{T}\cdot d\mathbf{A} 
$$

The **strain tensor** $\boldsymbol{\sigma}$ also is a rank 2 tensor defined as the ratio of the strain vector $\boldsymbol{\xi}$ and infinitessimal area $d\mathbf{A}$.

$$
d\boldsymbol{\xi} = \boldsymbol{\sigma}\cdot d\mathbf{A} 
$$

where the component form of the rank 2 strain tensor is

$$
\boldsymbol{\sigma} = \frac{1}{ 2 } \begin{vmatrix} \frac{d\xi_1 }{dx_1} & \frac{d\xi_1}{ dx_2} & \frac{d\xi_1 }{dx_3} \\ \frac{d\xi_2}{ dx_1} & \frac{d\xi_2 }{dx_2} & \frac{d\xi_2 }{dx_3} \\ \frac{d\xi_3}{ dx_1} & \frac{d\xi_3}{ dx_2 } & \frac{d\xi_3}{ dx_3} \end{vmatrix} 
$$

The modulus of elasticity is defined as the slope of the stress-strain curve. For linear, homogeneous, elastic matter, the potential energy density $U$ separates into diagonal and off-diagonal components of the strain tensor

$$
U = \frac{1}{2} \left[ \lambda \sum_i (\sigma_{ii})^2 + 2\mu \sum_{ik} (\sigma_{ik})^2 \right] 
$$

where the constants $\lambda$ and $\mu$ are Lamé’s moduli of elasticity which are positive. The stress tensor is related to the strain tensor by

$$
T_{ij} = \lambda \delta_{ij} \sum_k \frac{\partial\xi_k }{\partial x_k} + \mu \left( \frac{d\xi_i}{ dx_j } + \frac{d\xi_j}{ dx_i} \right) = \lambda \delta_{ij} \sum_k \sigma_{kk} + 2\mu \sigma_{ij} 
$$

### Electromagnetic field theory

The rank 2 Maxwell stress tensor $\mathbf{T}$ has components

$$
T_{ij} \equiv \epsilon_0 \left( E_iE_j − \frac{1}{2} \delta_{ij}E^2 \right) + \frac{1 }{\mu_0} \left( B_iB_j − \frac{1}{2} \delta_{ij}B^2 \right) 
$$

The divergence theorem allows the total electromagnetic force, acting of the volume $\tau$, to be written as

$$
\mathbf{F}= \int \left( \boldsymbol{\nabla} \cdot \mathbf{T} −\epsilon_0\mu_0 \frac{\partial \mathbf{S} }{\partial t} \right) d \tau = \oint \mathbf{T} \cdot d\mathbf{a}−\epsilon_0\mu_0 \frac{d}{dt} \int \mathbf{Sd}\boldsymbol{\tau} 
$$

The total momentum flux density is given by

$$
\frac{\partial}{ \partial t} (\boldsymbol{\pi}_{mech} + \boldsymbol{\pi}_{field}) = \boldsymbol{\nabla} \cdot \mathbf{T} 
$$

where the electromagnetic field momentum density is given by the Poynting vector $\mathbf{S}$ as $\boldsymbol{\pi}_{field}=\epsilon_0 \mu_0 \mathbf{S}$.

### Ideal fluid dynamics

Mass conservation leads to the continuity equation

$$
\frac{\partial \rho }{ \partial t} + \boldsymbol{\nabla}\cdot (\rho \mathbf{v})=0 
$$

Euler’s hydrodynamic equation gives

$$
\frac{\partial \mathbf{v} }{\partial t} + (\mathbf{v} \cdot \boldsymbol{\nabla}) \mathbf{v} = −\frac{1}{ \rho} \boldsymbol{\nabla} (P + \rho V ) 
$$

where $V$ is the scalar gravitational potential. If the flow is irrotational and time independent then

$$
\left(\frac{1}{ 2} \rho v^2 + P + \rho V \right) = \text{ constant} 
$$

### Viscous fluid dynamics

For incompressible flow the stress tensor term simplifies to $\boldsymbol{\nabla} \cdot \mathbf{T} =\mu \boldsymbol{\nabla}^2\mathbf{v}$. Then the Navier-Stokes equation becomes

$$
\rho \left[ \frac{\partial \mathbf{v} }{\partial t} + \mathbf{v} \cdot \boldsymbol{\nabla}\mathbf{v} \right] = −\boldsymbol{\nabla}P + \mu \boldsymbol{\nabla}^2\mathbf{v}+ \mathbf{f} 
$$

where $\mu \boldsymbol{\nabla}^2\mathbf{v}$ is the viscosity drag term. The left-hand side of Equation \ref{16.98} represents the rate of change of momentum per unit volume while the right-hand side represents the summation of the forces per unit volume that are acting.

The Reynolds number is a dimensionless number that characterizes the ratio of inertial forces to viscous forces in a viscous medium. The evolution of flow from laminar flow to turbulent flow, with increase of Reynolds number, was discussed.

The classical mechanics of continuous fields encompasses a remarkably broad range of phenomena with important applications to laminar and turbulent fluid flow, gravitation, electromagnetism, relativity, and quantum fields.
