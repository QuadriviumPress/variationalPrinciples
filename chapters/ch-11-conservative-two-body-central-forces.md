---
title: "11. Conservative two-body Central Forces"
short_title: "Chapter 11"
label: ch-11-conservative-two-body-central-forces
---


(ch-11)=

# 11. Conservative two-body Central Forces

## 11.1: Introduction to Conservative two-body Central Forces

Conservative two-body central forces are important in physics because of the pivotal role that the Coulomb and the gravitational forces play in nature. The Coulomb force plays a role in electrodynamics, molecular, atomic, and nuclear physics, while the gravitational force plays an analogous role in celestial mechanics. Therefore this chapter focusses on the physics of systems involving conservative two-body central forces because of the importance and ubiquity of these conservative two-body central forces in nature.

A conservative two-body central force has the following three important attributes.

1. **Conservative:** A conservative force depends only on the particle position, that is, the force is not time dependent. Moreover the work done by the force moving a body between any two points $1$ and $2$ is path independent. Conservative fields are discussed in chapter $2.10$.

2. **Two-body:** A two-body force between two bodies depends only on the relative locations of the two interacting bodies and is not influenced by the proximity of additional bodies. For two-body forces acting between $n$ bodies, the force on body $1$ is the vector superposition of the two-body forces due to the interactions with each of the other $n-1$ bodies. This differs from three-body forces where the force between any two bodies is influenced by the proximity of a third body.

3. **Central:**A central force field depends on the distance $r_{12}$ from the origin of the force at point $1,$ to the body location at point $2$, and the force is directed along the line joining them, that is, $\mathbf{ \hat{r}}_{12}$.

A conservative, two-body, central force combines the above three attributes and can be expressed as,

$$
\mathbf{F}_{21}\mathbf{=}f(r_{12}\mathbf{) \hat{r}}_{12}\tag{11.1} \label{eq-11-1}
$$

The force field $\mathbf{F}_{21}$ has a magnitude $f(r_{12}\mathbf{)}$ that depends only on the magnitude of the relative separation vector $\mathbf{r} _{12}=\mathbf{r}_{2}-\mathbf{r}_{1}$ between the origin of the force at point $1$ and point $2$ where the force acts, and the force is directed along the line joining them, that is, $\mathbf{\hat{r}}_{12}$.

Chapter $2.10$ showed that if a two-body central force is conservative, then it can be written as the gradient of a scalar potential energy $U(r)$ which is a function of the distance from the center of the force field.

$$
\mathbf{F}_{21}=-\mathbf{\nabla }U(r_{12})\tag{11.2} \label{eq-11-2}
$$
 As discussed in chapter $2$, the ability to represent the conservative central force by a scalar function $U(r)$ greatly simplifies the treatment of central forces.

The Coulomb and gravitational forces both are true conservative, two-body, central forces whereas the nuclear force between nucleons in the nucleus has three-body components. Two bodies interacting via a two-body central force is the simplest possible system to consider, but Equation [11.1](#eq-11-1) is applicable equally for $n$ bodies interacting via two-body central forces because the superposition principle applies for two-body central forces. This chapter will focus first on the motion of two bodies interacting via conservative two-body central forces followed by a brief discussion of the motion for $n>2$ interacting bodies.

## 11.2: Equivalent one-body Representation for two-body motion

The motion of two bodies, $1$ and $2$, interacting via two-body central forces, requires $6$ spatial coordinates, that is, three each for $\mathbf{r}_{1}$ and $\mathbf{r}_{2}$. Since the two-body central force only depends on the relative separation $\mathbf{r=r}_{1}-\mathbf{r}_{2}$ of the two bodies, it is more convenient to separate the $6$ degrees of freedom into $3$ spatial coordinates of relative motion $\mathbf{r,}$ plus $3$ spatial coordinates for the center-of-mass location $\mathbf{R}$ as described in chapter $2.7$. It will be shown here that the equation of motion for relative motion of the two-bodies in the center of mass can be represented by an equivalent one-body problem which simplifies the mathematics.

:::{figure} ../images/lt-21184-9.2.1.png
:label: fig-11-2-1
:enumerator: 11.2.1
:alt: Center of mass cordinates for the two-body system.

Center of mass cordinates for the two-body system.
:::

Consider two bodies acted upon by a conservative two-body central force, where the position vectors $\mathbf{r} _{1}$ and $\mathbf{r}_{2}$ specify the location of each particle as illustrated in [Figure 11.2.1](#fig-11-2-1). An alternate set of six variables would be the three components of the center of mass position vector $\mathbf{R}$ and the three components specifying the difference vector $\mathbf{r}$ defined by [Figure 11.2.1](#fig-11-2-1). Define the vectors $\mathbf{r}_{1}^{\prime }$ and $\mathbf{r} _{2}^{\prime }$ as the position vectors of the masses $m_{1}$ and $m_{2}$ with respect to the center of mass. Then

$$
\begin{align} \tag{11.3} \label{eq-11-3} \mathbf{r}_{1} &=&\mathbf{R}+\mathbf{r}_{1}^{\prime } \\ \mathbf{r}_{2} &=&\mathbf{R}+\mathbf{r}_{2}^{\prime } \notag\end{align}
$$

By the definition of the center of mass

$$
\mathbf{R}= \frac{m_{1}\mathbf{r}_{1}+m_{2}\mathbf{r}_{2}}{m_{1}+m_{2}}
$$

and

$$
m_{1}\mathbf{r}_{1}^{\prime }+m_{2}\mathbf{r}_{2}^{\prime }=0
$$

so that

$$
-\frac{m_{1}}{m_{2}}\mathbf{r}_{1}^{\prime }=\mathbf{r}_{2}^{\prime }
$$

Therefore

$$
\mathbf{r}=\mathbf{r}_{1}^{\prime }-\mathbf{r}_{2}^{\prime }=\frac{ m_{1}+m_{2}}{m_{2}}\mathbf{r}_{1}^{\prime }
$$

that is,

$$
\mathbf{r}_{1}^{\prime }=\frac{m_{2}}{m_{1}+m_{2}}\mathbf{r}
$$

Similarly;

$$
\mathbf{r}_{2}^{\prime }=-\frac{m_{1}}{m_{1}+m_{2}}\mathbf{r}
$$

Substituting these into Equation [11.3](#eq-11-3) gives

$$
\begin{align} \mathbf{r}_{1} &=&\mathbf{R}+\mathbf{r}_{1}^{\prime }=\mathbf{R}+\frac{m_{2} }{m_{1}+m_{2}}\mathbf{r} \notag \\ \mathbf{r}_{2} &=&\mathbf{R}+\mathbf{r}_{2}^{\prime }=\mathbf{R}-\frac{m_{1} }{m_{1}+m_{2}}\mathbf{r} \tag{11.10} \label{eq-11-10} \end{align}
$$

That is, the two vectors $\mathbf{r}_{1},\mathbf{r}_{2}$ are written in terms of the position vector for the center of mass $\mathbf{R}$ and the position vector $\mathbf{r}$ for relative motion in the center of mass frame.

Assuming that the two-body central force is conservative and represented by $U(r)$, then the Lagrangian of the two-body system can be written as

$$
L=\frac{1}{2}m_{1}\left\vert \mathbf{\dot{r}}_{1}\right\vert ^{2}+\frac{1}{2} m_{2}\left\vert \mathbf{\dot{r}}_{2}\right\vert ^{2}-U(r)
$$

Differentiating equations [11.10](#eq-11-10), with respect to time, and inserting them into the Lagrangian, gives

$$
L=\frac{1}{2}M\left\vert \mathbf{\dot{R}}\right\vert ^{2}+\frac{1}{2}\mu \left\vert \mathbf{\dot{r}}\right\vert ^{2}-U(r)
$$

where the total mass $M$ is defined as

$$
M=m_{1}+m_{2}
$$

and the **reduced mass** $\mu$ is defined by

$$
\mu \equiv \frac{m_{1}m_{2}}{m_{1}+m_{2}}
$$

or equivalently 
$$
\frac{1}{\mu }=\frac{1}{m_{1}}+\frac{1}{m_{2}}
$$

The total Lagrangian can be separated into two independent parts

$$
L=\frac{1}{2}M\left\vert \mathbf{\dot{R}}\right\vert ^{2}+L_{cm}
$$

where

$$
L_{cm}=\frac{1}{2}\mu \left\vert \mathbf{\dot{r}}\right\vert ^{2}-U(r)
$$

Assuming that no external forces are acting, then $\frac{\partial L}{ \partial \mathbf{R}}=0$ and the three Lagrange equations for each of the three coordinates of the $\mathbf{R}$ coordinate can be written as

$$
\frac{d}{dt}\frac{\partial L}{\partial \mathbf{\dot{R}}}=\frac{d\mathbf{P} _{cm}}{dt}=0
$$

That is, for a pure central force, the center-of-mass momentum $\mathbf{P} _{cm\text{ }}$is a constant of motion where 
$$
\mathbf{P}_{cm}=\frac{\partial L}{\partial \mathbf{\dot{R}}}=M\mathbf{\dot{R} }
$$

:::{figure} ../images/lt-21185-9.2.2.png
:label: fig-11-2-2
:enumerator: 11.2.2
:alt: Orbits of a two-body system with mass ratio of 2 rotating about the center-of-mass, O. The dashed ellipse is the equivalent one-body orbit with the center of force at the focus O.

Orbits of a two-body system with mass ratio of 2 rotating about the center-of-mass, O. The dashed ellipse is the equivalent one-body orbit with the center of force at the focus O.
:::

It is convenient to work in the center-of-mass frame using the effective Lagrangian $L_{cm}$. In the center-of-mass frame of reference, the translational kinetic energy $\frac{1}{2}M\left\vert \mathbf{\dot{R}}\right\vert ^{2}$ associated with center-of-mass motion is ignored, and only the energy in the center-of-mass is considered. This center-of-mass energy is the energy involved in the interaction between the colliding bodies. *Thus, in the center-of-mass, the problem has been reduced to an equivalent one-body problem of a mass* $\mu$*moving about a fixed force center with a path given by* $\mathbf{r}$*which is the separation vector between the two bodies, as shown in figure* 11.2.2. In reality, both masses revolve around their center of mass, also called the barycenter, in the center-of-mass frame as shown in [Figure 11.2.2](#fig-11-2-2). Knowing $\mathbf{r}$ allows the trajectory of each mass about the center of mass $\mathbf{r}_{1}^{\prime }$ and $\mathbf{r} _{2}^{\prime }$ to be calculated. Of course the true path in the laboratory frame of reference must take into account both the translational motion of the center of mass, in addition to the motion of the equivalent one-body representation relative to the barycenter. Be careful to remember the difference between the actual trajectories of each body, and the effective trajectory assumed when using the reduced mass which only determines the *relative* separation $\mathbf{r}$ of the two bodies. This reduction to an equivalent one-body problem greatly simplifies the solution of the motion, but it misrepresents the actual trajectories and the spatial locations of each mass in space. The equivalent one-body representation will be used extensively throughout this chapter.

## 11.3: Angular Momentum

### Angular momentum $\mathbf{L}$

The notation used for the angular momentum vector is $\mathbf{L}$ where the magnitude is designated by $\left\vert \mathbf{L}\right\vert =$ $l$. Be careful not to confuse the angular momentum vector $\mathbf{L}$ with the Lagrangian $L_{cm}.$ Note that the angular momentum for two-body rotation about the center of mass with angular velocity $\omega$ is identical when evaluated in either the laboratory or equivalent two-body representation. That is, using equations $(11.2.6)$ and $(11.2.7)$ 
$$
\mathbf{L=m}_{1}r_{1}^{\prime 2}\mathbf{\omega +m}_{2}r_{2}^{\prime 2} \mathbf{\omega =}\mu r^{2}\mathbf{\omega }
$$

The center-of-mass Lagrangian leads to the following two general properties regarding the angular momentum vector $\mathbf{L}$.

1) The motion lies entirely in a plane perpendicular to the fixed direction of the total angular momentum vector. This is because

$$
\mathbf{L}\cdot \mathbf{r}=\mathbf{r}\times \mathbf{p}\cdot \mathbf{r}=0
$$

that is, *the radius vector is in the plane perpendicular to the total angular momentum vector*. Thus, it is possible to express the Lagrangian in polar coordinates, $(r,\psi )$ rather than spherical coordinates. In polar coordinates the center-of-mass Lagrangian becomes 
$$
L_{cm}= \frac{1}{2}\mu \left( \dot{r}^{2}+r^{2}\dot{\psi}^{2}\right) -U(r)
$$

2) If the potential is spherically symmetric, then the polar angle $\psi$ is cyclic and therefore Noether’s theorem gives that**the angular momentum $\mathbf{p}_{\psi }\equiv \mathbf{L}=\mathbf{r\times p}$ is a constant of motion. That is, since $\frac{\partial L_{cm}}{\partial \psi } =0,$ then the Lagrange equations imply that

$$
\mathbf{\dot{p}}_{\psi }=\frac{d}{dt}\frac{\partial L_{cm}}{\partial \mathbf{ \dot{\psi}}}=0 \tag{11.23} \label{eq-11-23}
$$

where the vectors $\mathbf{\dot{p}}_{\psi }$ and $\mathbf{\dot{\psi}}$ imply that Equation \text{(11.23)} refers to three independent equations corresponding to the three components of these vectors. *Thus the angular momentum* $\mathbf{p}_{\psi },$*conjugate to* $\mathbf{\psi },$ *is a constant of motion.* The generalized momentum $\mathbf{p} _{\psi }$ is a first integral of the motion which equals

$$
\tag{11.24} \label{eq-11-24}\mathbf{p}_{\psi }=\frac{\partial L_{cm}}{\partial \mathbf{\dot{\psi}}}=\mu r^{2}\mathbf{\dot{\psi}}=\mathbf{\hat{p}}_{\psi }l
$$

where the magnitude of the angular momentum $l$, and the direction $\mathbf{ \hat{p}}_{\psi },$ both are constants of motion.

:::{figure} ../images/lt-21186-9.3.1.png
:label: fig-11-3-1
:enumerator: 11.3.1
:alt: Area swept out by the radius vector in the time dt.

Area swept out by the radius vector in the time dt.
:::

A simple geometric interpretation of Equation \text{(11.24)} is illustrated in Figure 11.3.1. The radius vector sweeps out an area $d\mathbf{A}$ in time $dt$ where

$$
d\mathbf{A}=\frac{1}{2}\mathbf{r\times v}dt
$$

and the vector $\mathbf{A}$ is perpendicular to the $x-y$ plane. The rate of change of area is

$$
\frac{d\mathbf{A}}{dt}=\frac{1}{2}\mathbf{r\times v}
$$

But the angular momentum is

$$
\mathbf{L}=\mathbf{r}\times \mathbf{p}=\mu \mathbf{r\times v}=2\mu \frac{d \mathbf{A}}{dt}
$$

Thus the conservation of angular momentum implies that the areal velocity $\frac{dA}{dt}$ also is a constant of motion. This fact is called Kepler’s second law of planetary motion which he deduced in $1609$ based on Tycho Brahe’s $55$ years of observational records of the motion of Mars. Kepler’s second law implies that a planet moves fastest when closest to the sun and slowest when farthest from the sun. Note that Kepler’s second law is a statement of *the conservation of angular momentum which is independent of the radial form of the central potential.*

## 11.4: Equations of Motion

The equations of motion for two bodies interacting via a conservative two-body central force can be determined using the center of mass Lagrangian, $L_{cm},$ given by equation $(11.3.3)$. For the radial coordinate, the operator equation $\Lambda _{r}L_{cm}=0$ for Lagrangian mechanics leads to

$$
\frac{d}{dt}\left( \mu \dot{r}\right) -\mu r\dot{\psi}^{2}+\frac{\partial U}{ \partial r}=0
$$

But

$$
\dot{\psi}=\frac{l}{\mu r^{2}}
$$

therefore the radial equation of motion is

$$
\mu \ddot{r}=-\frac{\partial U}{\partial r}+\frac{l^{2}}{\mu r^{3}}
$$

Similarly, for the angular coordinate, the operator equation $\Lambda _{\psi }L_{cm}=0$ leads to equation $(11.3.5)$. That is, the angular equation of motion for the magnitude of $p_{\psi }$ is 
$$
p_{\psi }=\frac{\partial L}{\partial \dot{\psi}}=\mu r^{2}\dot{\psi}=l
$$

Lagrange’s equations have given two equations of motion, one dependent on radius $r$ and the other on the polar angle $\psi$. Note that the radial acceleration is just a statement of Newton’s Laws of motion for the radial force $F_{r}$ in the center-of-mass system of 
$$
F_{r}=-\frac{\partial U}{\partial r}+\frac{l^{2}}{\mu r^{3}}
$$

This can be written in terms of an effective potential

$$
U_{eff}(r)\equiv U(r)+\frac{l^{2}}{2\mu r^{2}}\tag{11.33} \label{eq-11-33}
$$

which leads to an equation of motion

$$
F_{r}=\mu \ddot{r}=-\frac{\partial U_{eff}(r)}{\partial r}\tag{11.34} \label{eq-11-34}
$$

Since $\frac{l^{2}}{\mu r^{3}}=\mu r\dot{\psi}^{2}$, the second term in Equation \text{(11.33)} is the usual centrifugal force that originates because the variable $r$ is in a non-inertial, rotating frame of reference. Note that the angular equation of motion is independent of the radial dependence of the conservative two-body central force.

:::{figure} ../images/lt-21187-9.4.1.png
:label: fig-11-4-1
:enumerator: 11.4.1
:alt: The attractive inverse-square law potential (\frac{k}{r}), the centrifugal potential (\frac{l^2}{2\mu r^2}), and the combined effective bound potential.

The attractive inverse-square law potential $(\frac{k}{r})$, the centrifugal potential $(\frac{l^2}{2\mu r^2})$, and the combined effective bound potential.
:::

Figure 11.4.1 shows, by dashed lines, the radial dependence of the potential corresponding to the attractive inverse square law force, that is $U=-\frac{k }{r}$, and the potential corresponding to the centrifugal term $\frac{l^{2}}{ 2\mu r^{2}}$ corresponding to a repulsive centrifugal force. The sum of these two potentials $U_{eff}(r)$, shown by the solid line, has a minimum $U_{\min }$ value at a certain radius similar to that manifest by the diatomic molecule discussed in example $(2.12.1)$.

It is remarkable that the six-dimensional equations of motion, for two bodies interacting via a two-body central force, has been reduced to trivial center-of-mass translational motion, plus a *one-dimensional one-body problem* given by \text{(11.34)} in terms of the relative separation $r$ and an effective potential $U_{eff}(r)$.

## 11.5: Differential Orbit Equation

The differential orbit equation relates the shape of the orbital motion, in plane polar coordinates, to the radial dependence of the two-body central force. A **Binet coordinate transformation**, which depends on the functional form of $\mathbf{F}(\mathbf{r}),$ can simplify the differential orbit equation. For the inverse-square law force, the best Binet transformed variable is $u$ which is defined to be

$$
u\equiv \frac{1}{r}
$$

Inserting the transformed variable $u$ into equation $(11.4.2)$ gives

$$
\dot{\psi}=\frac{lu^{2}}{\mu }
$$

From the definition of the new variable

$$
\frac{dr}{dt}=-u^{-2}\frac{du}{dt}=-u^{-2}\frac{du}{d\psi }\dot{\psi}=-\frac{ l}{\mu }\frac{du}{d\psi }
$$

Differentiating again gives

$$
\frac{d^{2}r}{dt^{2}}=-\frac{l}{\mu }\frac{d}{dt}\left( \frac{du}{d\psi } \right) =-\left( \frac{lu}{\mu }\right) ^{2}\frac{d^{2}u}{d\psi ^{2}}
$$

Substituting these into Lagrange’s radial equation of motion gives

$$
\frac{d^{2}u}{d\psi ^{2}}+u=-\frac{\mu }{l^{2}}\frac{1}{u^{2}}F(\frac{1}{u}) \tag{11.39} \label{eq-11-39}
$$

Binet’s *differential orbit equation* directly relates $\psi$ and $r$ which determines the overall shape of the orbit trajectory. This shape is crucial for understanding the orbital motion of two bodies interacting via a two-body central force. Note that for the special case of an inverse square-law force, that is where $F(\frac{1}{u})=ku^{2}$, then the right-hand side of Equation \text{(11.39)} equals a constant $-\frac{\mu k}{l^{2}}$ since the orbital angular momentum is a conserved quantity.

::::{admonition} Example 11.5.1: Central force leading to a circular orbit $r = 2R\cos \theta$
:class: example

:::{figure} ../images/lt-21188-9.5.1.png
:label: fig-11-5-1
:enumerator: 11.5.1
:alt: Circular trajectory passing through the origin of the central force.

Circular trajectory passing through the origin of the central force.
:::

Binet’s differential orbit equation can be used to derive the central potential that leads to the assumed circular trajectory of $r=2R\cos \theta$ where $R$ is the radius of the circular orbit. Note that this circular orbit passes through the origin of the central force when $r=2R\cos \theta =0$

Inserting this trajectory into Binet’s differential orbit Equation \text{(11.39)} gives

$$
\frac{1}{2R}\frac{d^{2}\left( \cos \theta \right) ^{-1}}{d\theta ^{2}}+\frac{ 1}{2R}\left( \cos \theta \right) ^{-1}=-\frac{\mu }{l^{2}}4R^{2}\left( \cos \theta \right) ^{2}F(\frac{1}{u}) \tag{$\alpha $}
$$

Note that the differential is given by

$$
\frac{d^{2}\left( \cos \theta \right) ^{-1}}{d\theta ^{2}}=\frac{d}{d\theta } \left( \frac{\sin \theta }{\cos ^{3}\theta }\right) =\frac{2\sin ^{2}\theta }{\cos ^{3}\theta }+\frac{1}{\cos \theta }\notag
$$

Inserting this differential into equation $\alpha$ gives 
$$
\frac{2\sin ^{2}\theta }{\cos ^{3}\theta }+\frac{1}{\cos \theta }+\frac{1}{ \cos \theta }=\frac{2}{\cos ^{3}\theta }=-\frac{\mu }{l^{2}}8R^{3}\left( \cos \theta \right) ^{2}F(\frac{1}{u})\notag
$$

Thus the radial dependence of the required central force is

$$
F=-\frac{l^{2}}{8R^{3}\mu }\frac{2}{\cos ^{5}\theta }=-\frac{8R^{2}l^{2}}{ \mu }\frac{1}{r^{5}}=-\frac{k}{r^{5}}\notag
$$

This corresponds to an attractive central force that depends to the fifth power on the inverse radius $\mathit{r}$. Note that this example is unrealistic since the assumed orbit implies that the potential and kinetic energies are infinite when $r\rightarrow 0$ at $\theta \rightarrow \frac{\pi }{2}$.
::::

## 11.6: Hamiltonian

Since the center-of-mass Lagrangian is not an explicit function of time, then

$$
\frac{dH_{cm}}{dt}=\mathcal{-}\frac{\partial L_{cm}}{\partial t}=0
$$

Thus *the center-of mass Hamiltonian* $H_{cm}$*is a constant of motion*. However, since the transformation to center of mass can be time dependent, then $H_{cm}\neq E,$ that is, it does not include the total energy because the kinetic energy of the center-of-mass motion has been omitted from $H_{cm}$. Also, since no transformation is involved, then

$$
H_{cm}=T_{cm}+U=E_{cm}
$$

That is, the center-of-mass Hamiltonian $H_{cm}$ equals the center-of-mass total energy. The center-of-mass Hamiltonian then can be written using the effective potential $(11.4.6)$ in the form 
$$
H_{cm}= \frac{p_{r}^{2}}{2\mu }+\frac{p_{\theta }^{2}}{2\mu r^{2}}+U(r)=\frac{ p_{r}^{2}}{2\mu }+\frac{l^{2}}{2\mu r^{2}}+U(r)=\frac{p_{r}^{2}}{2\mu } +U_{eff}(r)=E_{cm} \tag{11.42} \label{eq-11-42}
$$

It is convenient to express the center-of-mass Hamiltonian $H_{cm}$ in terms of the energy equation for the orbit in a central field using the transformed variable $u=\frac{1}{r}$. Substituting equations $(11.4.6)$ and $(11.5.3)$ into the Hamiltonian Equation \text{(11.42)} gives the*energy equation of the orbit* 
$$
\frac{l^{2}}{2\mu }\left[ \left( \frac{du}{d\psi }\right) ^{2}+u^{2}\right] +U\left( u^{-1}\right) =E_{cm}
$$

Energy conservation allows the Hamiltonian to be used to solve problems directly. That is, since

$$
H_{cm}=\frac{\mu \dot{r}^{2}}{2}+\frac{l^{2}}{2\mu r^{2}}+U(r)=E_{cm}
$$

then

$$
\dot{r}=\frac{dr}{dt}=\pm \sqrt{\frac{2}{\mu }\left( E_{cm}-U-\frac{l^{2}}{ 2\mu r^{2}}\right) }\tag{11.45} \label{eq-11-45}
$$

The time dependence can be obtained by integration

$$
t=\int \frac{\pm dr}{\sqrt{\frac{2}{\mu }\left( E_{cm}-U-\frac{l^{2}}{2\mu r^{2}}\right) }}+\text{ constant}\tag{11.46} \label{eq-11-46}
$$

An inversion of this gives the solution in the standard form $r=r\left( t\right) .$ However, it is more interesting to find the relation between $r$ and $\theta .$ From relation \text{(11.46)} for $\frac{dr}{dt}$ then

$$
dt=\frac{\pm dr}{\sqrt{\frac{2}{\mu }\left( E_{cm}-U-\frac{l^{2}}{2\mu r^{2}} \right) }}
$$

while equation $(11.4.2)$ gives

$$
d\psi =\frac{ldt}{\mu r^{2}}=\frac{\pm ldr}{r^{2}\sqrt{2\mu \left( E_{cm}-U- \frac{l^{2}}{2\mu r^{2}}\right) }}
$$

Therefore

$$
\psi =\int \frac{\pm ldr}{r^{2}\sqrt{2\mu \left( E_{cm}-U-\frac{l^{2}}{2\mu r^{2}}\right) }}+\text{ constant}\tag{11.49} \label{eq-11-49}
$$

which can be used to calculate the angular coordinate. This gives the relation between the radial and angular coordinates which specifies the trajectory.

Although equations \text{(11.45)} and \text{(11.49)} formally give the solution, the actual solution can be derived analytically only for certain specific forms of the force law and these solutions differ for attractive versus repulsive interactions.

## 11.7: General Features of the Orbit Solutions

It is useful to look at the general features of the solutions of the equations of motion given by the equivalent one-body representation of the two-body motion. These orbits depend on the net center of mass energy $E_{cm}.$ There are five possible situations depending on the center-of-mass total energy $E_{cm}$.

1. $\mathbf{E}_{cm}\mathbf{>0}:$ The trajectory is hyperbolic and has a minimum distance, but no maximum. The distance of closest approach is given when $\dot{r}=0.$ At the turning point $E_{cm}=U+$ $\frac{l^{2}}{2\mu r^{2}}$

2. $\mathbf{E}_{cm}\mathbf{=0}:$ It can be shown that the orbit for this case is parabolic.

3. $\mathbf{0>E}_{cm}\mathbf{>U}_{\min }:$ For this case the equivalent orbit has both a maximum and minimum radial distance at which $\dot{r}=0.$ At the turning points the radial kinetic energy term is zero so $E_{cm}=U+$ $\frac{l^{2}}{2\mu r^{2}}.$ For the attractive inverse square law force the path is an ellipse with the focus at the center of attraction (Figure $(11.8.1)$), which is Kepler’s First Law. During the time that the radius ranges from $r_{\min }$ to $r_{\max }$ and back the radius vector turns through an angle $\Delta \psi$ which is given by
    
$$
\Delta \psi =2\int_{r_{\min }}^{r_{\max }}\frac{\pm ldr}{r^{2}\sqrt{2\mu \left( E_{cm}-U-\frac{l^{2}}{2\mu r^{2}}\right) }}
$$

   The general path prescribes a rosette shape which is a closed curve only if $\Delta \psi$ is a rational fraction of $2\pi$.

4. $\mathbf{E}_{cm}\mathbf{=U}_{\min }:$ In this case $r$ is a constant implying that the path is circular since 
$$
\dot{r}=\frac{dr}{dt}=\pm \sqrt{\frac{2}{\mu }\left( E_{cm}-U-\frac{l^{2}}{ 2\mu r^{2}}\right) }=0
$$

5. $\mathbf{E}_{cm}\mathbf{<U}_{\min }:$ For this case the square root is imaginary and there is no real solution.

In general the orbit is not closed, and such open orbits do not repeat. Bertrand’s Theorem states that the inverse-square central force, and the linear harmonic oscillator, are the only radial dependences of the central force that lead to stable closed orbits.

::::{admonition} Example 11.7.1: Orbit equation of motion for a free body
:class: example

It is illustrative to use the differential orbit equation $(11.5.1)$ to show that a body in free motion travels in a straight line. Assume that a line through the origin $O$ intersects perpendicular to the instantaneous trajectory at the point $Q$ which has polar coordinates $(r_{0},\phi )$ relative to the origin. The point $P,$ with polar coordinates $(r,\phi ),$ lies on a straight line through $Q$ that is perpendicular to $OQ$ if, and only if, $r\cos (\phi -\delta )=r_{0}.$ Since the force is zero then the differential orbit equation simplifies to

$$
\frac{d^{2}u(\phi )}{d\phi ^{2}}+u(\phi )=0\notag
$$

A solution of this is

$$
u(\phi )=\frac{1}{r_{0}}\cos (\phi -\delta )\notag
$$

where $r_{0}$ and $\delta$ are arbitrary constants. This can be rewritten as

$$
r(\phi )=\frac{r_{0}}{\cos (\phi -\delta )} \notag
$$

This is the equation of a straight line in polar coordinates as illustrated in the adjacent figure. This shows that a free body moves in a straight line if no forces are acting on the body.

:::{figure} ../images/lt-21189-9.7.1.png
:label: fig-11-7-1
:enumerator: 11.7.1
:alt: Trajectory of a free body

Trajectory of a free body
:::
::::

## 11.8: Inverse-square, two-body, central force

The most important conservative, two-body, central interaction is the attractive inverse-square law force, which is encountered in both gravitational attraction and the Coulomb force. This force $\mathbf{F(r)}$ can be written in the form

$$
\mathbf{F}(r)= \frac{k}{r^{2}}\widehat{\mathbf{r}}\tag{11.52} \label{eq-11-52}
$$

The force constant $k$ is defined to be negative for an attractive force and positive for a repulsive force. In S.I. units the force constant $k=-Gm_{1}m_{2}$ for the gravitational force and $k=+\frac{q_{1}q_{2}}{4\pi \epsilon _{0}}$ for the Coulomb force. Note that this sign convention is the opposite of what is used in many books which use a negative sign in Equation \text{(11.52)} and assume $k$ to be positive for an attractive force and negative for a repulsive force.

The conservative, inverse-square, two-body, central force is unique in that the underlying symmetries lead to four conservation laws, all of which are of pivotal importance in nature.

1. **Conservation of angular momentum:** Like all conservative central forces, the inverse-square central two-body force conserves angular momentum as proven in chapter $11.3$.

2. **Conservation of energy:** This conservative central force can be represented in terms of a scalar potential energy $U(r)$ as given by equation $(11.1.2)$, where for this central force
    
$$
U(r)=\frac{k}{r}\tag{11.53} \label{eq-11-53}
$$

   Moreover, equation $(11.6.3)$ showed that the center-of-mass Hamiltonian is conserved, that is, $H_{cm}=E_{cm}$

3. **Gauss’ Law:** For a conservative, inverse-square, two-body, central force, the flux of the force field out of any closed surface is proportional to the algebraic sum of the sources and sinks of this field that are located inside the closed surface. The net flux is independent of the distribution of the sources and sinks inside the closed surface, as well as the size and shape of the closed surface. Chapter $2.14.5$ proved this for the gravitational force field.

4. **Closed orbits**: Two bodies interacting via the conservative, inverse-square, two-body, central force follow closed (degenerate) orbits as stated by Bertrand’s Theorem. The first consequence of this symmetry is that Kepler’s laws of planetary motion have stable, single-valued orbits. The second consequence of this symmetry is the conservation of the eccentricity vector defined in Equation \text{(11.86)}.

Observables that depend on Gauss’s Law, or on closed planetary orbits, are extremely sensitive to addition of even a miniscule incremental exponent $\xi$ to the radial dependence $r^{-\left( 2\pm \xi \right) }$ of the force. The statement that the inverse-square, two-body, central force leads to closed orbits can be proven by inserting Equation \text{(11.52)} into the orbit differential equation,

$$
\frac{d^{2}u}{d\psi ^{2}}+u=-\frac{\mu }{l^{2}}\frac{1}{u^{2}}ku^{2}=-\frac{ \mu k}{l^{2}}
$$

Using the transformation

$$
y\equiv u+\frac{\mu k}{l^{2}}
$$

the orbit equation becomes

$$
\frac{d^{2}y}{d\psi ^{2}}+y=0
$$

A solution of this equation is

$$
y=B\cos \left( \psi -\psi _{0}\right)
$$

Therefore

$$
u=\frac{1}{r}=-\frac{\mu k}{l^{2}}\left[ 1+\epsilon \cos \left( \psi -\psi _{0}\right) \right]\tag{11.58} \label{eq-11-58}
$$

This is the equation of a conic section. For an attractive, inverse-square, central force, Equation \text{(11.58)} is the equation for an ellipse with the *origin of* $r$*at one of the foci of the ellipse* that has eccentricity $\epsilon ,$ defined as 
$$
\epsilon \equiv B\frac{l^{2}}{\mu k}\tag{11.59} \label{eq-11-59}
$$

Equation \text{(11.58)} is the polar equation of a conic section. Equation \text{(11.58)} also can be derived with the origin at a focus by inserting the inverse square law potential into equation $(11.6.10)$ which gives

$$
\psi =\int \frac{\pm du}{\sqrt{\frac{2\mu E_{cm}}{l^{2}}+\frac{2\mu k}{l^{2}} u-u^{2}}}+\text{ constant}\tag{11.60} \label{eq-11-60}
$$

The solution of this gives

$$
u=\frac{1}{r}=-\frac{\mu k}{l^{2}}\left[ 1+\sqrt{1+\frac{2E_{cm}l^{2}}{\mu k^{2}}}\cos \left( \psi -\psi _{0}\right) \right]\tag{11.61} \label{eq-11-61}
$$

Equations \text{(11.58)} and \text{(11.61)} are identical if the eccentricity $\epsilon$ equals

$$
\epsilon =\sqrt{1+\frac{2E_{cm}l^{2}}{\mu k^{2}}}\tag{11.62} \label{eq-11-62}
$$

The value of $\psi _{0}$ merely determines the orientation of the major axis of the equivalent orbit. Without loss of generality, it is possible to assume that the angle $\psi$ is measured with respect to the major axis of the orbit, that is $\psi _{0}=0$. Then the equation can be written as

$$
u=\frac{1}{r}=-\frac{\mu k}{l^{2}}\left[ 1+\epsilon \cos \left( \psi \right) \right] =-\frac{\mu k}{l^{2}}\left[ 1+\sqrt{1+\frac{2E_{cm}l^{2}}{\mu k^{2}}} \cos \left( \psi \right) \right]\tag{11.63} \label{eq-11-63}
$$

This is the equation of a conic section where $\epsilon$ is the eccentricity of the conic section. The conic section is a hyperbola if $\epsilon >1$, parabola if $\epsilon =1,$ ellipse if $\epsilon <1,$ and a circle if $\epsilon =0.$ All the equivalent one-body orbits for an attractive force have the origin of the force at a focus of the conic section. The orbits depend on whether the force is attractive or repulsive, on the conserved angular momentum $l,$ and on the center-of-mass energy $E_{cm}$.

### Bound orbits

Closed bound orbits occur only if the following requirements are satisfied.

1. The force must be attractive, $(k<0)$ then Equation \text{(11.63)} ensures that $r$ is positive.

2. For a closed elliptical orbit. the eccentricity $\epsilon <1$ of the equivalent one-body representation of the orbit implies that the total center-of-mass energy $E_{cm}<0$, that is, the closed orbit is bound.

Bound elliptical orbits have the center-of-force at one interior focus $F_{1}$ of the elliptical one-body representation of the orbit as shown in Figure 11.8.1.

:::{figure} ../images/lt-21190-9.8.1.png
:label: fig-11-8-1
:enumerator: 11.8.1
:alt: Bound elliptical orbit.

Bound elliptical orbit.
:::

The minimum value of the orbit $r=r_{\min }$ occurs when $\psi =0,$ where

$$
r_{\min }=- \frac{l^{2}}{\mu k\left[ 1+\epsilon \right] }\tag{11.64} \label{eq-11-64}
$$

This minimum distance is called the *periapsis[^11-8-1]*.

The maximum distance, $r=r_{\max },$ which is called the *apoapsis,* occurs when $\psi =180^{o}$

$$
r_{\max }=- \frac{l^{2}}{\mu k\left[ 1-\epsilon \right] }\tag{11.65} \label{eq-11-65}
$$

Remember that since $k<0$ for bound orbits, the negative signs in equations \text{(11.64)} and \text{(11.65)} lead to $r>0$. The most bound orbit is a circle having $\epsilon =0$ which implies that $E_{cm}=-\frac{\mu k^{2}}{l^{2}}$.

The shape of the elliptical orbit also can be described with respect to the center of the elliptical equivalent orbit by deriving the lengths of the semi-major axis $a$ and the semi-minor axis $b$ shown in Figure 11.8.1. 
$$
\begin{align} a &=&\frac{1}{2}\left( r_{\min }+r_{\max }\right) =\frac{1}{2}\left( \frac{ l^{2}}{\mu k\left[ 1+\epsilon \right] }+\frac{l^{2}}{\mu k\left[ 1-\epsilon \right] }\right) =\frac{l^{2}}{\mu k\left[ 1-\epsilon ^{2}\right] }\tag{11.66} \label{eq-11-66} \\ b &=&a\sqrt{1-\epsilon ^{2}}=\frac{l^{2}}{\mu k\sqrt{[1-\epsilon ^{2}]}}\tag{11.67} \end{align}
$$

Remember that the predicted bound elliptical orbit corresponds to the equivalent one-body representation for the two-body motion as illustrated in Figure $(11.2.2)$. This can be transformed to the individual spatial trajectories of the each of the two bodies in an inertial frame.

### Kepler’s laws for bound planetary motion

Kepler’s three laws of motion apply to the motion of two bodies in a bound orbit due to the attractive gravitational force for which $k=-Gm_{1}m_{2}$.

1. Each planet moves in an elliptical orbit with the sun at one focus

2. The radius vector, drawn from the sun to a planet, describes equal areas in equal times

3. The square of the period of revolution about the sun is proportional to the cube of the major axis of the orbit.

Two bodies interacting via the gravitational force, which is a conservative, inverse-square, two-body central force, is best handled using the equivalent orbit representation. The first and second laws were proved in chapters $11.8$ and $11.3$. That is, the second law is equivalent to the statement that the angular momentum is conserved. The third law can be derived using the fact that the area of an ellipse is

$$
A=\pi ab=\pi a^{2} \sqrt{1-\epsilon ^{2}}=\frac{\pi l}{\sqrt{-\mu k}}a^{\frac{3}{2}}
$$

Equations $(11.3.7)$ and $(11.3.8)$ give that the rate of change of area swept out by the radius vector is

$$
\frac{dA}{dt}=\frac{1}{2}r^{2}\dot{\psi}=\frac{l}{2\mu }
$$

Therefore the period for one revolution $\tau$ is given by the time to sweep out one complete ellipse

$$
\tau =\frac{A}{\left( \frac{dA}{dt}\right) }=2\pi \left( \frac{\mu }{-k} \right) ^{\frac{1}{2}}a^{\frac{3}{2}}
$$

This leads to **Kepler’s** $3^{rd}$**law** 
$$
\tau ^{2}=4\pi ^{2}\frac{\mu }{-k}a^{3}\tag{11.71} \label{eq-11-71}
$$

Bound orbits occur only for attractive forces for which the force constant $k$ is negative, and thus cancel the negative sign in Equation \text{(11.71)}. For example, for the gravitational force $k=-Gm_{1}m_{2}$.

Note that the reduced mass $\mu =\frac{m_{1}m_{2}}{m_{1}+m_{2}}$ occurs in Kepler’s $3^{rd}$ law. That is, Kepler’s third law can be written in terms of the actual masses of the bodies to be

$$
\tau ^{2}=\frac{4\pi ^{2}}{G\left( m_{1}+m_{2}\right) }a^{3}\tag{11.72} \label{eq-11-72}
$$

In relating the relative periods of the different planets Kepler made the approximation that the mass of the planet $m_{1}$ is negligible relative to the mass of the sun $m_{2}.$

The eccentricity of the major planets ranges from $\epsilon =0.2056$ for Mercury, to $\epsilon =0.0068$ for Venus. The Earth has an eccentricity of $\epsilon =0.0167$ with $r_{\min }=91\cdot 10^{6\text{ }}$miles and $r_{\max }=95\cdot 10^{6}$ miles. On the other hand, $\epsilon =0.967$ for Halley’s comet, that is, the radius vector ranges from $0.6$ to $18$ times the radius of the orbit of the Earth.

The orbit energy can be derived by substituting the eccentricity, given by Equation \text{(11.62)}, into the semi-major axis length $a,$ given by Equation \text{(11.66)}, which leads to the center-of-mass energy of

$$
E_{cm}=-\frac{k}{2a}
$$

However, the Hamiltonian, given by equation $(11.6.3)$, implies that $E_{cm}$ is

$$
E_{cm}=\frac{1}{2}\mu v^{2}+\left( -\frac{k}{r}\right) =-\frac{k}{2a}
$$

For the simple case of a circular orbit, $a=r$ then the velocity $v$ equals 
$$
v=\sqrt{\frac{k}{\mu r}}
$$

For a circular orbit, the drag on a satellite lowers the total energy resulting in a decrease in the radius of the orbit and a concomitant increase in velocity. That is, when the orbit radius is decreased, part of the gain in potential energy accounts for the work done against the drag, and the remaining part goes towards increase of the kinetic energy. Also note that, as predicted by the Virial Theorem, the kinetic energy always is half the potential energy for the inverse square law force.

### Unbound orbits

Attractive inverse-square central forces lead to hyperbolic orbits for $\epsilon >1$ for which $E_{cm}>0$, that is, the orbit is unbound. In addition, the orbits always are unbound for a repulsive force since $U=\frac{ k}{r}$ is positive as is the kinetic energy $T_{cm}$, thus $E_{cm}=T_{cm}+U_{cm}>0$. The radial orbit equation for either an attractive or a repulsive force is

$$
r=- \frac{l^{2}}{\mu k\left[ 1+\epsilon \cos \psi \right] }
$$

For a repulsive force $k$ is positive and $l^{2}$ always is positive. Therefore to ensure that $r$ remain positive the bracket term must be negative. That is

$$
\left[ 1+\epsilon \cos \psi \right] <0\hspace{1in}k>0
$$

For an attractive force $k$ is negative and since $l^{2}$ is positive then the bracket term must be positive to ensure that $r$ is positive. That is, 
$$
\left[ 1+\epsilon \cos \psi \right] >0\hspace{1in}k<0
$$

:::{figure} ../images/lt-21192-9.8.2.png
:label: fig-11-8-2
:enumerator: 11.8.2
:alt: Hyperbolic two-body orbits for a repulsive (left) and attractive (right) inverse-square, central two-body forces. Both orbits have the angular momentum vector pointing upwards out of the plane of the orbit

Hyperbolic two-body orbits for a repulsive (left) and attractive (right) inverse-square, central two-body forces. Both orbits have the angular momentum vector pointing upwards out of the plane of the orbit
:::

Figure 11.8.2 shows both branches of the hyperbola for a given angle $\psi$ for the equivalent two-body orbits where the center of force is at the origin. For an attractive force, $k<0,$ the center of force is at the interior focus of the hyperbola, whereas for a repulsive force the center of force is at the exterior focus. For a given value of $\left\vert \psi \right\vert$ the asymptotes of the orbits both are displaced by the same **impact parameter** $b$ from parallel lines passing through the center of force. The scattering angle, between the outgoing direction of the scattered body and the incident direction, is designated to be $\theta ,$ which is related to the angle $\psi$ by $\theta =180^{\circ }-2\psi$.

### Eccentricity vector

Two-bodies interacting via a conservative two-body central force have two invariant first-order integrals, namely the conservation of energy and the conservation of angular momentum. For the special case of the inverse-square law, there is a third invariant of the motion, which Hamilton called the **eccentricity vector**[^11-8-2], that unambiguously defines the orientation and direction of the major axis of the elliptical orbit. It will be shown that the angular momentum plus the eccentricity vector completely define the plane and orientation of the orbit for a conservative inverse-square law central force.

Newton’s second law for a central force can be written in the form

$$
\mathbf{ \dot{p}=}f(r)\mathbf{\hat{r}}
$$

Note that the angular moment $\mathbf{L}=\mathbf{r\times p}$ is conserved for a central force, that is $\mathbf{\dot{L}}=0$. Therefore the time derivative of the product $\mathbf{p\times L}$ reduces to

$$
\frac{d}{dt}\left( \mathbf{p\times L}\right) \mathbf{=\dot{p}\times L=}f(r) \mathbf{\hat{r}\times }\left( \mathbf{r\times }\mu \mathbf{\dot{r}}\right) =f(r)\frac{\mu }{r}\left[ \mathbf{r}\left( \mathbf{r\cdot \dot{r}}\right) -r^{2}\mathbf{\dot{r}}\right]\tag{11.80} \label{eq-11-80}
$$

This can be simplified using the fact that

$$
\mathbf{r\cdot \dot{r}=}\frac{1}{2}\frac{d}{dt}\left( \mathbf{r\cdot r} \right) =r\dot{r}
$$

thus

$$
f(r)\frac{\mu }{r}\left[ \mathbf{r}\left( \mathbf{r\cdot \dot{r}}\right) -r^{2}\mathbf{\dot{r}}\right] =-\mu f(r)r^{2}\left[ \frac{\mathbf{\dot{r}}}{r }-\frac{\mathbf{r}\dot{r}}{r^{2}}\right] =-\mu f(r)r^{2}\frac{d}{dt}\left( \frac{\mathbf{r}}{r}\right)
$$

This allows Equation \text{(11.80)} to be reduced to

$$
\frac{d}{dt}\left( \mathbf{p\times L}\right) \mathbf{=}-\mu f(r)r^{2}\frac{d }{dt}\left( \frac{\mathbf{r}}{r}\right)\tag{11.83} \label{eq-11-83}
$$

Assume the special case of the inverse-square law, Equation \text{(11.52)}, then the central force Equation \text{(11.83)} reduces to

$$
\frac{d}{dt}\left( \mathbf{p\times L}\right) \mathbf{=-}\frac{d}{dt}\left( \mu k\mathbf{\hat{r}}\right)\tag{11.84} \label{eq-11-84}
$$

or

$$
\frac{d}{dt}\left[ \left( \mathbf{p\times L}\right) \mathbf{+}\left( \mu k \mathbf{\hat{r}}\right) \right] =0\tag{11.85} \label{eq-11-85}
$$

Define the eccentricity vector $\mathbf{A}$ as

$$
\mathbf{A\equiv }\left( \mathbf{p\times L}\right) \mathbf{+}\left( \mu k \mathbf{\hat{r}}\right)\tag{11.86} \label{eq-11-86}
$$

then Equation \text{(11.85)} corresponds to

$$
\frac{d\mathbf{A}}{dt}=0\tag{11.87} \label{eq-11-87}
$$

This is a statement that *the eccentricity vector* $A$*is a constant of motion for an inverse-square, central force.*

The definition of the eccentricity vector $\mathbf{A}$ and angular momentum vector $\mathbf{L}$ implies a zero scalar product,

$$
\mathbf{A\cdot L=}0\tag{11.88} \label{eq-11-88}
$$

Thus the eccentricity vector $\mathbf{A}$ and angular momentum $\mathbf{L}$ are mutually perpendicular, that is, $\mathbf{A}$ is in the plane of the orbit while $\mathbf{L}$ is perpendicular to the plane of the orbit. The eccentricity vector $\mathbf{A}$, *always points along the major axis of the ellipse from the focus to the periapsis* as illustrated on the left side in Figure 11.8.3. As a consequence, the two orthogonal vectors $\mathbf{ A}$ and $\mathbf{L}$ completely define the plane of the orbit, plus the orientation of the major axis of the Kepler orbit, in this plane. The three vectors $\mathbf{A}$, $\mathbf{p\times L}$, and $\left( \mu k\mathbf{\hat{r}} \right)$ obey the triangle rule as illustrated in the left side of Figure 11.8.3.

:::{figure} ../images/lt-21191-9.8.3.png
:label: fig-11-8-3
:enumerator: 11.8.3
:alt: The elliptical trajectory and eccentricity vector \mathbf{A} for two bodies interacting via the inversesquare, central force for eccentricity \epsilon = 0.75. The left plot shows the elliptical spatial trajectory where the semi-major axis is assumed to be on the x-axis and the angular momentum \m…

The elliptical trajectory and eccentricity vector $\mathbf{A}$ for two bodies interacting via the inversesquare, central force for eccentricity $\epsilon = 0.75$. The left plot shows the elliptical spatial trajectory where the semi-major axis is assumed to be on the $x$-axis and the angular momentum $\mathbf{L} =l \hat{\mathbf{z}}$, is out of the page. The force centre is at one foci of the ellipse. The vector coupling relation $\mathbf{A} \equiv (\mathbf{p} \times \mathbf{L}) + (\mu k \hat{\mathbf{r}})$ is illustrated at four points on the spatial trajectory. The right plot is a hodograph of the linear momentum $\mathbf{p}$ for this trajectory. The periapsis is denoted by the number $\mathbf{1}$ and the apoapsis is marked as $\mathbf{3}$ on both plots. Note that the eccentricity vector $\mathbf{A}$ is a constant that points parallel to the major axis towards the perapsis.
:::

Hamilton noted the direct connection between the eccentricity vector $\mathbf{A}$ and the eccentricity $\epsilon$ of the conic section orbit. This can be shown by considering the scalar product

$$
\mathbf{A\cdot r=}Ar\cos \psi =\mathbf{r\cdot }\left( \mathbf{p\times L} \right) +\mu kr\tag{11.89} \label{eq-11-89}
$$

Note that the triple scalar product can be permuted to give

$$
\mathbf{r\cdot }\left( \mathbf{p\times L}\right) =\left( \mathbf{r}\times \mathbf{p}\right) \mathbf{\cdot L=L\cdot L=}l^{2}\tag{11.90} \label{eq-11-90}
$$

Inserting Equation \text{(11.90)} into \text{(11.89)} gives 
$$
\frac{1}{r}=-\frac{\mu k}{l^{2}}\left( 1-\frac{A}{\mu k}\cos \psi \right)\tag{11.91} \label{eq-11-91}
$$

Note that equations \text{(11.63)} and \text{(11.91)} are identical if $\psi _{0}=0$. This implies that the eccentricity $\epsilon$ and $A$ are related by

$$
\epsilon =-\frac{A}{\mu k}\tag{11.92} \label{eq-11-92}
$$

where $k$ is defined to be negative for an attractive force. The relation between the eccentricity and total center-of-mass energy can be used to rewrite Equation \text{(11.62)} in the form 
$$
A^{2}=\mu ^{2}k^{2}+2\mu E_{cm}l^{2}\tag{11.93} \label{eq-11-93}
$$

The combination of the eccentricity vector $\mathbf{A}$ and the angular momentum vector $\mathbf{L}$ completely specifies the orbit for an inverse square-law central force. The trajectory is in the plane perpendicular to the angular momentum vector $\mathbf{L}$, while the eccentricity, plus the orientation of the orbit, both are defined by the eccentricity vector $\mathbf{A}$. The eccentricity vector and angular momentum vector each have three independent coordinates, that is, these two vector invariants provide six constraints, while the scalar invariant energy $E,$ adds one additional constraint. The exact location of the particle moving along the trajectory is not defined and thus there are only five independent coordinates governed by the above seven constraints. Thus the eccentricity vector, angular momentum, and center-of-mass energy are related by the two equations \text{(11.88)} and \text{(11.93)}.

Noether’s theorem states that each conservation law is a manifestation of an underlying symmetry. Identification of the underlying symmetry responsible for the conservation of the eccentricity vector $\mathbf{A}$ is elucidated using Equation \text{(11.86)} to give

$$
\left( \mu k\mathbf{\hat{r}}\right) =\mathbf{A-}\left( \mathbf{p\times L} \right)
$$
 Take the scalar product

$$
\left( \mu k\mathbf{\hat{r}}\right) \cdot \left( \mu k\mathbf{\hat{r}} \right) =\left( \mu k\right) ^{2}=p^{2}L^{2}+A^{2}-2L\cdot \left( \mathbf{ p\times L}\right)
$$

Choose the angular momentum to be along the $z$-axis, that is, $\mathbf{L=}l \mathbf{\hat{z}}$, and, since $\mathbf{p}$ and $\mathbf{A}$ are perpendicular to $\mathbf{L}$, then $\mathbf{p}$ and $\mathbf{A}$ are in the $\mathbf{\hat{x}-\hat{y}}$ plane. Assume that the semimajor axis of the elliptical orbit is along the $\mathbf{x}$-axis, then the locus of the momentum vector on a momentum hodograph has the equation

$$
p_{x}^{2}+\left( p_{y}-\frac{A}{L}\right) ^{2}=\left( \frac{\mu k}{L}\right) ^{2}\tag{11.96} \label{eq-11-96}
$$

Equation \text{(11.96)} implies that the locus of the momentum vector is a circle of radius $\left\vert \frac{\mu k}{L}\right\vert$ with the center displaced from the origin at coordinates $\left( 0,\frac{A}{L}\right)$ as shown by the momentum hodograph on the right side of an Figure 11.8.3. The angle $\beta$ and eccentricity $\epsilon$ are related by,

$$
\cos \beta =-\frac{A/L}{\mu k/L}=-\frac{A}{\mu k}=\epsilon
$$

The circular orbit is centered at the origin for $\epsilon =-\frac{A}{\mu k} =0$, and thus the magnitude $\left\vert \mathbf{p}\right\vert$ is a constant around the whole trajectory.

The inverse-square, central, two-body, force is unusual in that it leads to stable closed bound orbits because the radial and angular frequencies are degenerate, i.e. $\omega _{r}=\omega _{\psi }.$ In momentum space, the locus of the linear momentum vector $\mathbf{p}$ is a perfect circle which is the underlying symmetry responsible for both the fact that the orbits are closed, and the invariance of the eccentricity vector. Mathematically this symmetry for the Kepler problem corresponds to the body moving freely on the boundary of a four-dimensional sphere in space and momentum. The invariance of the eccentricity vector is a manifestation of the special property of the inverse-square, central force under certain rotations in this four-dimensional space; this $O(4)$ symmetry is an example of a hidden symmetry.

[^11-8-1]: The greek term apsis refers to the points of greatest or least distance of approach for an orbiting body from one of the foci of the elliptical orbit. The term periapsis or pericenter both are used to designate the closest distance of approach, while apoapsis or apocenter are used to designate the farthest distance of approach. Attaching the terms "perí-" and "apo-" to the general term "-apsis" is preferred over having different names for each object in the solar system. For example, frequently used terms are "-helion" for orbits of the sun, "-gee" for orbits around the earth, and "-cynthion" for orbits around the moon.

[^11-8-2]: The symmetry underlying the eccentricity vector is less intuitive than the energy or angular momentum invariants leading to it being discovered independently several times during the past three centuries. Jakob Hermann was the first to indentify this invariant for the special case of the inverse-square central force. Bernoulli generalized his proof in 1710. Laplace derived the invariant at the end of the 18th century using analytical mechanics. Hamilton derived the connection between the invariant and the orbit eccentricity. Gibbs derived the invariant using vector analysis. Runge published the Gibb’s derivation in his textbook which was referenced by Lenz in a 1924 paper on the quantal model of the hydrogen atom. Goldstein named this invariant the "Laplace-Runge-Lenz vector", while others have named it the "Runge-Lenz vector" or the "Lenz vector". This book uses Hamilton’s more intuitive name of "eccentricity vector".

## 11.9: Isotropic, linear, two-body, central force

Closed orbits occur for the two-dimensional linear oscillator when $\frac{\omega _{x}}{\omega _{y}}$ is a rational fraction as discussed in chapter $3.3$. **Bertrand’s Theorem****states that*the linear oscillator, and the inverse-square law (Kepler problem), are the only two-body central forces that have single-valued, stable, closed orbits of the coupled radial and angular motion.* The invariance of the eccentricity vector was the underlying symmetry leading to single-valued, stable, closed orbits for the Kepler problem. It is interesting to explore the symmetry that leads to stable closed orbits for the harmonic oscillator. For simplicity, this discussion will restrict discussion to the isotropic, harmonic, two-body, central force where $\omega _{x}=\omega _{y}=\omega$, for which the two-body, central force is linear

$$
\mathbf{F}(r)=k\mathbf{r}\tag{11.98} \label{eq-11-98}
$$

where $k>0$ corresponds to a repulsive force and $k<0$ to an attractive force. This isotropic harmonic force can be expressed in terms of a spherical potential $U(r)$ where

$$
U(r)=- \frac{1}{2}kr^{2}\tag{11.99} \label{eq-11-99}
$$

Since this is a central two-body force, both the equivalent one-body representation, and the conservation of angular momentum, are equally applicable to the harmonic two-body force. As discussed in section $11.3$, since the two-body force is central, the motion is confined to a plane, and thus the Lagrangian can be expressed in polar coordinates. In addition, since the force is spherically symmetric, then the angular momentum is conserved. The orbit solutions are conic sections as described in chapter $11.7$. The shape of the orbit for the harmonic two-body central force can be derived using either polar or cartesian coordinates as illustrated below.

### Polar coordinates

The origin of the equivalent orbit for the harmonic force will be found to be at the center of an ellipse, rather than the foci of the ellipse as found for the inverse square law. The shape of the orbit can be defined using a Binet differential orbit equation that employs the transformation

$$
u^{\prime }\equiv \frac{1}{r^{2}}\tag{11.100} \label{eq-11-100}
$$

Then

$$
\frac{du^{\prime }}{d\psi }=-\frac{2}{r^{3}}\frac{dr}{d\psi }\tag{11.101} \label{eq-11-101}
$$

The chain rule gives that

$$
\dot{r}=\frac{dr}{d\psi }\dot{\psi}=-\frac{r^{3}}{2}\dot{\psi}\frac{ du^{\prime }}{d\psi }=-\frac{r}{2}\frac{p_{\psi }}{\mu }\frac{du^{\prime }}{ d\psi }\tag{11.102} \label{eq-11-102}
$$

Substitute this into the Hamiltonian $H_{cm},$ equation $(11.6.3)$, gives

$$
\frac{1}{2}\mu \dot{r}^{2}=\frac{1}{8}\frac{p_{\psi }^{2}}{u^{\prime }\mu } \left( \frac{du^{\prime }}{d\psi }\right) ^{2}=E-\frac{p_{\psi }^{2}}{2\mu } u^{\prime }+\frac{k}{2u^{\prime }}\tag{11.103} \label{eq-11-103}
$$

Rearranging this equation gives

$$
\left( \frac{du^{\prime }}{d\psi }\right) ^{2}+4u^{\prime 2}-\frac{8E\mu }{ p_{\psi }^{2}}u^{\prime }=\frac{4k\mu }{p_{\psi }^{2}}\tag{11.104} \label{eq-11-104}
$$

Addition of a constant to both sides of the equation completes the square

$$
\left[ \frac{d}{d\psi }\left( u^{\prime }-\frac{E\mu }{p_{\psi }^{2}}\right) \right] ^{2}+4\left( u^{\prime }-\frac{E\mu }{p_{\psi }^{2}}\right) ^{2}=+ \frac{4k\mu }{p_{\psi }^{2}}+4\left( \frac{E\mu }{p_{\psi }^{2}}\right) ^{2}\tag{11.105} \label{eq-11-105}
$$

The right-hand side of Equation \text{(11.105)} is a constant. The solution of \text{(11.105)} must be a sine or cosine function with polar angle $\psi =\omega t$. That is

$$
\left( u^{\prime }-\frac{E\mu }{p_{\psi }^{2}}\right) =\left[ \left( \frac{ E\mu }{p_{\psi }^{2}}\right) ^{2}+\frac{k\mu }{p_{\psi }^{2}}\right] ^{\frac{ 1}{2}}\cos 2\left( \psi -\psi _{0}\right)\tag{11.106} \label{eq-11-106}
$$

That is,

$$
u^{\prime }=\frac{1}{r^{2}}=\frac{E\mu }{p_{\psi }^{2}}\left( 1+\left( 1+ \frac{kp_{\psi }^{2}}{E^{2}\mu }\right) ^{\frac{1}{2}}\cos 2(\psi -\psi _{0})\right)\tag{11.107} \label{eq-11-107}
$$
 Equation \text{(11.107)} corresponds to a closed orbit centered at the origin of the elliptical orbit as illustrated in Figure 11.9.1. The eccentricity $\epsilon$ of this closed orbit is given by

$$
\left( 1+\frac{kp_{\psi }^{2}}{E^{2}\mu }\right) ^{\frac{1}{2}}=\frac{ \epsilon ^{2}}{2-\epsilon ^{2}}\tag{11.108} \label{eq-11-108}
$$

Equations $(11.8.15)$, $(11.8.16)$ give that the eccentricity is related to the semi-major $a$ and semi-minor $b$ axes by

$$
\epsilon ^{2}=1-\left( \frac{b}{a}\right) ^{2}\tag{11.109} \label{eq-11-109}
$$

Note that for a repulsive force $k>0$, then $\epsilon \geq 1$ leading to unbound hyperbolic or parabolic orbits centered on the origin. An attractive force, $k<0,$ allows for bound elliptical, as well as unbound parabolic and hyperbolic orbits.

:::{figure} ../images/lt-21193-9.9.1.png
:label: fig-11-9-1
:enumerator: 11.9.1
:alt: The elliptical equivalent trajectory for two bodies interacting via the linear, central force for eccentricity \epsilon = 0.75. The left plot shows the elliptical spatial trajectory where the semi-major axis is assumed to be on the x-axis and the angular momentum \mathbf{L} =l\hat{\mathbf{z}}, is…

The elliptical equivalent trajectory for two bodies interacting via the linear, central force for eccentricity $\epsilon = 0.75$. The left plot shows the elliptical spatial trajectory where the semi-major axis is assumed to be on the $x$-axis and the angular momentum $\mathbf{L} =l\hat{\mathbf{z}}$, is out of the page. The force center is at the center of the ellipse. The right plot is a hodograph of the linear momentum $\mathbf{p}$ for this trajectory.
:::

### Cartesian coordinates

The isotropic harmonic oscillator, expressed in terms of cartesian coordinates in the $(x,y)$ plane of the orbit, is separable because there is no direct coupling term between the $x$ and $y$ motion. That is. the center-of-mass Lagrangian in the $(x,y)$ plane separates into independent motion for $x$ and $y$.

$$
L=\frac{1}{2}\mu \mathbf{\dot{r}\cdot \dot{r}}+\frac{1}{2}k\mathbf{r\cdot r}= \left[ \frac{1}{2}\mu \dot{x}^{2}+\frac{1}{2}kx^{2}\right] +\left[ \frac{1}{2 }\mu \dot{y}^{2}+\frac{1}{2}ky^{2}\right]\tag{11.110} \label{eq-11-110}
$$

Solutions for the independent coordinates, and their corresponding momenta, are

$$
\begin{align} \tag{11.111} \label{eq-11-111}\mathbf{r} &=&\mathbf{\hat{\imath}}A\cos \left( \omega t+\alpha \right) + \mathbf{\hat{\jmath}}B\cos \left( \omega t+\beta \right) \\ \tag{11.112}\mathbf{p} &\mathbf{=}&\mathbf{-\hat{\imath}}A\mu \omega \sin \left( \omega t+\alpha \right) -\mathbf{\hat{\jmath}}B\mu \omega \sin \left( \omega t+\beta \right)\end{align}
$$

where $\omega =\sqrt{\frac{k}{\mu }}$. Therefore

$$
\begin{align}\tag{11.113} \label{eq-11-113} r^{2} &=&x^{2}+y^{2}=\left[ A\cos \left( \omega t+\alpha \right) \right] ^{2}+\left[ B\cos \left( \omega t+\beta \right) \right] ^{2} \\ &=&\frac{A^{2}+B^{2}}{2}+\frac{\sqrt{A^{4}+B^{4}+2AB^{2}\cos \left( \alpha -\beta \right) }}{2}\cos \left( 2\omega t+\psi _{0}\right) \tag{11.114}\end{align}
$$

where

$$
\cos \psi _{0}=\frac{A^{2}\cos \alpha +B^{2}\cos \beta }{\sqrt{ A^{4}+B^{4}+2AB^{2}\cos \left( \alpha -\beta \right) }}\tag{11.115} \label{eq-11-115}
$$

For a phase difference $\alpha -\beta =\pm \frac{\pi }{2},$ this equation describes an ellipse centered at the origin which agrees with Equation \text{(11.107)} that was derived using polar coordinates.

The two normal modes of the isotropic harmonic oscillator are degenerate, therefore $x,y$ are equally good normal modes with two corresponding total energies, $E_{1},E_{2}$, while the corresponding angular momentum $J$ points in the $z$ direction. 
$$
\begin{align} E_{1} &=&\frac{p_{x}^{2}}{2\mu }+\frac{1}{2}kx^{2} \tag{11.116} \label{eq-11-116}\\ E_{2} &=&\frac{p_{y}^{2}}{2\mu }+\frac{1}{2}ky^{2} \\ J &=&\mu \left( xp_{y}-yp_{x}\right)\tag{11.117}\end{align}
$$

Figure 11.9.1 shows the closed elliptical equivalent orbit plus the corresponding momentum hodograph for the isotropic harmonic two-body central force. Figures $(11.8.3)$ and 11.9.1 contrast the differences between the elliptical orbits for the inverse-square force, and those for the harmonic two-body central force. Although the orbits for bound systems with the harmonic two-body force, and the inverse-square force, both lead to elliptical bound orbits, there are important differences. Both the radial motion and momentum are two valued per cycle for the reflection-symmetric harmonic oscillator, whereas the radius and momentum have only one maximum and one minimum per revolution for the inverse-square law. Although the inverse-square, and the isotropic, harmonic, two-body central forces both lead to closed bound elliptical orbits for which the angular momentum is conserved and the orbits are planar, there is another important difference between the orbits for these two interactions. The orbit equation for the Kepler problem is *expressed with respect to a foci of the elliptical equivalent orbit,* as illustrated in Figure $(11.8.3)$, whereas the orbit equation for the isotropic harmonic oscillator orbit is*expressed with respect to the center of the ellipse* as illustrated in Figure 11.9.1.

### Symmetry tensor $\mathbf{A}^{\prime }$

The invariant vectors $\mathbf{L}$ and $\mathbf{A}$ provide a complete specification of the geometry of the bound orbits for the inverse square-law Kepler system. It is interesting to search for a similar invariant that fully specifies the orbits for the isotropic harmonic central force. In contrast to the Kepler problem, the harmonic force center is at the center of the elliptical orbit, and the orbit is reflection symmetric with the radial and angular frequencies related by $\omega _{r}=2\omega _{\psi }$. Since the orbit is reflection-symmetric, the orientation of the major axis of the orbit cannot be uniquely specified by a vector. Therefore, for the harmonic interaction it is necessary to specify the orientation of the principal axis by the **symmetry tensor**. The symmetry of the isotropic harmonic, two-body, central force leads to the symmetry tensor $\mathbf{A}^{\prime },$ which is an invariant of the motion analogous to the eccentricity vector $\mathbf{A}$. Like a rotation matrix, the symmetry tensor defines the orientation, but not direction, of the major principal axis of the elliptical orbit. In the plane of the polar orbit the $3\times 3$ symmetry tensor $\mathbf{A}^{\prime }$ reduces to a $2\times 2$ matrix having matrix elements defined to be,

$$
A_{ij}^{\prime }= \frac{p_{i}p_{j}}{2\mu }+\frac{1}{2}kx_{i}x_{j}\tag{11.118} \label{eq-11-118}
$$

The diagonal matrix elements $A_{11}^{\prime }=E_{1}$, and $A_{22}^{\prime }=E_{2}$ are constants of motion. The off-diagonal term is given by

$$
A_{12}^{\prime 2}\equiv \left( \frac{p_{x}p_{y}}{2\mu }+\frac{1}{2} kxy\right) ^{2}=\left( \frac{p_{x}^{2}}{2\mu }+\frac{1}{2}kx^{2}\right) \left( \frac{p_{y}^{2}}{2\mu }+\frac{1}{2}ky^{2}\right) -4\mu \left( xp_{y}-yp_{x}\right) ^{2}=E_{1}E_{2}-\frac{kJ^{2}}{4\mu ^{3}}\tag{11.119} \label{eq-11-119}
$$

The terms on the right-hand side of Equation \text{(11.119)} all are constants of motion, therefore $A_{12\text{ }}^{\prime 2}$ also is a constant of motion. Thus the $3\times 3$ symmetry tensor $\mathbf{A}^{\prime }$ can be reduced to a $2\times 2$ symmetry tensor for which all the matrix elements are constants of motion, and the trace of the symmetry tensor is equal to the total energy.

In summary, the inverse-square, and harmonic oscillator two-body central interactions both lead to closed, elliptical equivalent orbits, the plane of which is perpendicular to the conserved angular momentum vector. However, for the inverse-square force, the origin of the equivalent orbit is at the focus of the ellipse and $\omega _{r}=\omega _{\phi }$, whereas the origin is at the center of the ellipse and $\omega _{r}=2\omega _{\phi }$ for the harmonic force. As a consequence, the elliptical orbit is reflection symmetric for the harmonic force but not for the inverse square force. The eccentricity vector and symmetry tensor both specify the major axes of these elliptical orbits, the plane of which are perpendicular to the angular momentum vector. The eccentricity vector, and the symmetry tensor, both are directly related to the eccentricity of the orbit and the total energy of the two-body system. Noether’s theorem states that the invariance of the eccentricity vector and symmetry tensor, plus the corresponding closed orbits, are manifestations of underlying symmetries. The dynamical $SU3$ symmetry underlies the invariance of the symmetry tensor, whereas the dynamical $O4$ symmetry underlies the invariance of the eccentricity vector. These symmetries lead to stable closed elliptical bound orbits only for these two specific two-body central forces, and not for other two-body central forces.

## 11.10: Closed-orbit Stability

Bertrand’s theorem states that the linear oscillator and the inverse-square law are the only two-body, central forces for which all bound orbits are single-valued, and stable closed orbits. The stability of closed orbits can be illustrated by studying their response to perturbations. For simplicity, the following discussion of stability will focus on circular orbits, but the general principles are the same for elliptical orbits.

A circular orbit occurs whenever the attractive force just balances the effective ”centrifugal force” in the rotating frame. This can occur for any radial functional form for the central force. The effective potential, equation $(11.4.6)$ will have a stationary point when

$$
\left( \frac{\partial U_{eff}}{\partial r}\right) _{r=r_{0}}=0\tag{11.120} \label{eq-11-120}
$$

that is, when

$$
\left( \frac{\partial U}{\partial r}\right) _{r=r_{0}}-\frac{l^{2}}{\mu r_{0}^{3}}=0\tag{11.121} \label{eq-11-121}
$$

This is equivalent to the statement that the net force is zero. Since the central attractive force is given by

$$
F(r)=-\frac{\partial U_{eff}}{\partial r}\tag{11.122} \label{eq-11-122}
$$

then the stationary point occurs when

$$
F(r_{0})=-\frac{l^{2}}{\mu r_{0}^{3}}=-\mu r_{0}\dot{\psi}^{2}\tag{11.123} \label{eq-11-123}
$$

This is the so-called centrifugal force in the rotating frame. The Hamiltonian, equation $(11.6.5)$, gives that

$$
\dot{r}=\pm \sqrt{\frac{2}{\mu }\left( E_{cm}-U-\frac{l^{2}}{2\mu r^{2}} \right) }\tag{11.124} \label{eq-11-124}
$$

For a circular orbit $\dot{r}=0$ that is

$$
E_{cm}=U-\frac{l^{2}}{2\mu r^{2}}\tag{11.125} \label{eq-11-125}
$$

A stable circular orbit is possible if both equations \text{(11.121)} and \text{(11.125)} are satisfied. Such a circular orbit will be a **stable orbit** at the minimum when

$$
\left( \frac{d^{2}U_{eff}}{dr^{2}}\right) _{r=r_{0}}>0\tag{11.126} \label{eq-11-126}
$$

Examples of stable and unstable orbits are shown in Figure 11.10.1.

:::{figure} ../images/lt-21196-9.10.1.png
:label: fig-11-10-1
:enumerator: 11.10.1
:alt: Stable and unstable effective central potentials. The repulsive centrifugal and the attractive potentials (k<0) are shown dashed. The solid curve is the effective potential.

Stable and unstable effective central potentials. The repulsive centrifugal and the attractive potentials $(k<0)$ are shown dashed. The solid curve is the effective potential.
:::

Stability of a circular orbit requires that

$$
\left( \frac{\partial ^{2}U}{\partial r^{2}}\right) _{r=r_{0}}+\frac{3l^{2}}{ \mu r_{0}^{4}}>0\tag{11.127} \label{eq-11-127}
$$

which can be written in terms of the central force for a **stable orbit** as

$$
-\left( \frac{\partial F}{\partial r}\right) _{r_{0}}+\frac{3F\left( r_{0}\right) }{r_{0}}>0\tag{11.128} \label{eq-11-128}
$$

If the attractive central force can be expressed as a power law

$$
F(r)=-kr^{n}\tag{11.129} \label{eq-11-129}
$$

then stability requires

$$
kr_{0}^{n-1}\left( 3+n\right) >0
$$

or 
$$
n>-3
$$

Stable equivalent orbits will undergo oscillations about the stable orbit if perturbed. To first order, the restoring force on a bound reduced mass $\mu$ is given by

$$
F_{restore}=-\left( \frac{d^{2}U_{eff}}{dr^{2}}\right) _{r=r_{0}}\left( r-r_{0}\right) =\mu \ddot{r}
$$

To the extent that this linear restoring force dominates over higher-order terms, then a perturbation of the stable orbit will undergo simple harmonic oscillations about the stable orbit with angular frequency

$$
\omega =\sqrt{\frac{\left( \frac{d^{2}U_{eff}}{dr^{2}}\right) _{r=r_{0}}}{ \mu }}
$$

The above discussion shows that a small amplitude radial oscillation about the stable orbit with amplitude $\xi$ will be of the form

$$
\xi =A\sin (2\pi \omega t+\delta )
$$

The orbit will be closed if the product of the oscillation frequency $\omega ,$ and the orbit period $\tau$ is an integer value.

The fact that planetary orbits in the gravitational field are observed to be closed is strong evidence that the gravitational force field must obey the inverse square law. Actually there are small precessions of planetary orbits due to perturbations of the gravitational field by bodies other than the sun, and due to relativistic effects. Also the gravitational field near the earth departs slightly from the inverse square law because the earth is not a perfect sphere, and the field does not have perfect spherical symmetry. The study of the precession of satellites around the earth has been used to determine the oblate quadrupole and slight octupole (pear shape) distortion of the shape of the earth.

The most famous test of the inverse square law for gravitation is the precession of the perihelion of Mercury. If the attractive force experienced by Mercury is of the form

$$
\mathbf{F(}r\mathbf{)}=-G\frac{m_{s}m_{m}}{r^{2+\alpha }}\mathbf{\hat{r}}\notag
$$

where $\left\vert \alpha \right\vert$ is small, then it can be shown that, for approximate circular orbitals, the perihelion will advance by a small angle $\pi \alpha$ per orbit period. That is, the precession is zero if $\alpha =0$, corresponding to an inverse square law dependence which agrees with Bertrand’s theorem. The position of the perihelion of Mercury has been measured with great accuracy showing that, after correcting for all known perturbations, the perihelion advances by $43(\pm 5)$ seconds of arc per century, that is $5\times 10^{-7}$ radians per revolution. This corresponds to $\alpha =1.6\times 10^{-7}$ which is small but still significant. This precession remained a puzzle for many years until $1915$ when Einstein predicted that one consequence of his general theory of relativity is that the planetary orbit of Mercury should precess at $43$ seconds of arc per century, which is in remarkable agreement with observations.

::::{admonition} Example 11.10.1: Linear two-body restoring force
:class: example

The effective potential for a linear two-body restoring force $F=-kr$ is

$$
U_{eff}= \frac{1}{2}kr^{2}+\frac{l^{2}}{2\mu r^{2}}\notag
$$

At the minimum

$$
\left( \frac{\partial U_{eff}}{\partial r}\right) _{r=r_{0}}=kr-\frac{l^{2}}{ \mu r^{3}}=0\notag
$$

Thus

$$
r_{0}=\left( \frac{l^{2}}{\mu k}\right) ^{\frac{1}{4}}\notag
$$

and

$$
\left( \frac{d^{2}U_{eff}}{dr^{2}}\right) _{r=r_{0}}=\frac{3l^{2}}{\mu r_{0}^{4}}+k=4k>0\notag
$$

which is a stable orbit. Small perturbations of such a stable circular orbit will have an angular frequency

$$
\omega =\sqrt{\frac{\left( \frac{d^{2}U_{eff}}{dr^{2}}\right) _{r=r_{0}}}{ \mu }}=2\sqrt{\frac{k}{\mu }} \notag
$$

Note that this is twice the frequency for the planar harmonic oscillator with the same restoring coefficient. This is due to the central repulsion, the effective potential well for this rotating oscillator example has about half the width for the corresponding planar harmonic oscillator. Note that the kinetic energy for the rotational motion, which is $\frac{ l^{2}}{2\mu r^{2}},$ equals the potential energy $\frac{1}{2} kr^{2}$ at the minimum as predicted by the Virial Theorem for a linear two-body restoring force.
::::

::::{admonition} Example 11.10.2: Inverse square law attractive force
:class: example

The effective potential for an inverse square law restoring force $F=-\frac{k}{r^{2}}\hat{r},$ where $k$ is assumed to be positive,

$$
U_{eff}=- \frac{k}{r}+\frac{l^{2}}{2\mu r^{2}}\notag
$$

At the minimum

$$
\left( \frac{\partial U_{eff}}{\partial r}\right) _{r=r_{0}}=\frac{k}{r^{2}}- \frac{l^{2}}{\mu r^{3}}=0\notag
$$

Thus

$$
r_{0}=\frac{l^{2}}{\mu k}\notag
$$

and

$$
\left( \frac{d^{2}U_{eff}}{dr^{2}}\right) _{r=r_{0}}=\frac{3l^{2}}{\mu r_{0}^{4}}-\frac{2k}{r_{0}^{3}}=\frac{k}{r_{0}^{3}}>0\notag
$$

which is a stable orbit. Small perturbations about such a stable circular orbit will have an angular frequency 
$$
\omega =\sqrt{\frac{\left( \frac{d^{2}U_{eff}}{dr^{2}}\right) _{r=r_{0}}}{ \mu }}=\frac{\mu k^{2}}{l^{3}} \notag
$$

The kinetic energy for oscillations about this stable circular orbit, which is $\frac{l^{2}}{2\mu r^{2}},$ equals half the magnitude of the potential energy $-\frac{k}{r}$ at the minimum as predicted by the Virial Theorem.
::::

::::{admonition} Example 11.10.3: Attractive inverse cubic central force
:class: example

The inverse cubic force is an interesting example to investigate the stability of the orbit equations. One solution of the inverse cubic central force, for a reduced mass $\mu ,$ is a spiral orbit

$$
r=r_{0}e^{\alpha \psi }\notag
$$

That this is true can be shown by inserting this orbit into the differential orbit equation.

Using a Binet transformation of the variable $r$ to $u$ gives

$$
u = \frac{1}{r}=\frac{1}{r_{0}}e^{-\alpha \psi } \nonumber
$$

$$
\frac{du}{d\psi } = -\frac{\alpha }{r_{0}}e^{-\alpha \psi } \nonumber
$$

$$
\frac{d^{2}u}{d\psi ^{2}} = \frac{\alpha ^{2}}{r_{0}}e^{-\alpha \psi } \nonumber
$$

Substituting these into the differential equation of the orbit

$$
\frac{d^{2}u}{d\psi ^{2}}+u=-\frac{\mu }{l^{2}}\frac{1}{u^{2}}F(\frac{1}{u})\notag
$$

gives

$$
\frac{\alpha ^{2}}{r_{0}}e^{-\alpha \psi }+\frac{1}{r_{0}}e^{-\alpha \psi }=- \frac{\mu }{l^{2}}r_{0}^{2}e^{2\alpha \psi }F\left( \frac{1}{u}\right)\notag
$$

That is

$$
F\left( \frac{1}{u}\right) =-\frac{\left( \alpha ^{2}+1\right) l^{2}}{\mu } r_{0}^{-3}e^{-3\alpha \psi }=-\frac{\left( \alpha ^{2}+1\right) l^{2}}{\mu r^{3}}\notag
$$

which is a central attractive inverse cubic force.

The time dependence of the spiral orbit can be derived since the angular momentum gives

$$
\dot{\psi}=\frac{l}{\mu r^{2}}=\frac{l}{\mu r_{0}^{2}e^{2\alpha \psi }}\notag
$$

This can be written as

$$
e^{2\alpha \psi }d\psi =\frac{l}{\mu r_{0}^{2}}dt\notag
$$

Integrating gives

$$
\frac{e^{2\alpha \psi }}{2\alpha }=\frac{lt}{\mu r_{0}^{2}}+\beta\notag
$$

where $\beta$ is a constant. But the orbit gives

$$
r^{2}=r_{0}^{2}e^{2\alpha \psi }=\frac{2\alpha lt}{\mu }+2\alpha \beta \notag
$$

Thus the radius increases or decreases as the square root of the time. That is, an attractive cubic central force does not have a stable orbit which is what is expected since there is no minimum in the effective potential energy. Note that it is obvious that there will be no minimum or maximum for the summation of effective potential energy since, if the force is $F=-\frac{k}{r^{3}},$ then the effective potential energy is

$$
U_{eff}=-\frac{k}{2r^{2}}+\frac{l^{2}}{2\mu r^{2}}=\left( \frac{l^{2}}{\mu } -k\right) \frac{1}{2r^{2}} \notag
$$

which has no stable minimum or maximum.
::::

::::{admonition} Example 11.10.4: Spiralling mass attached by a string to a hanging mass
:class: example

An example of an application of orbit stability is the case shown in the adjacent figure. A particle of mass $m$ moves on a horizontal frictionless table. This mass is attached by a light string of fixed length $b$ and rotates about a hole in the table. The string is attached to a second equal mass $m$ that is hanging vertically downwards with no angular motion.

:::{figure} ../images/lt-21195-9.10.2.png
:label: fig-11-10-2
:enumerator: 11.10.2
:alt: Rotating mass m on a frictionless horizontal table connected to a suspended mass m.

Rotating mass $m$ on a frictionless horizontal table connected to a suspended mass $m$.
:::

The equations are most conveniently expressed in cylindrical coordinates ($r,\theta ,z)$ with the origin at the hole in the table, and $z$ vertically upward. The fixed length of the string requires $z=r-b$. The potential energy is 
$$
U=mgz=mg(r-b)\notag
$$

The system is central and conservative, thus the Hamiltonian can be written as

$$
H=\frac{m}{2}\left( \dot{r}^{2}+r^{2}\dot{\theta}^{2}\right) +\frac{m}{2} \overset{.}{r}^{2}+mg(r-b)=E\notag
$$

The Lagrangian is independent of $\theta$, that is, $\theta$ is cyclic, thus the angular momentum $mr^{2}\dot{\theta} =l$ is a constant of motion. Substituting this into the Hamiltonian equation gives

$$
m\dot{r}^{2}+\frac{l^{2}}{2mr^{2}}+mg(r-b)=E\notag
$$

The effective potential is

$$
U_{eff}=\frac{l^{2}}{2mr^{2}}+mg(r-b)\notag
$$

which is shown in the adjacent figure. The stationary value occurs when

$$
\left( \frac{\partial U_{eff}}{\partial r}\right) _{r_{0}}=-\frac{l^{2}}{ mr_{0}^{3}}+mg=0\notag
$$

That is, when the angular momentum is related to the radius by

$$
l^{2}=m^{2}gr_{0}^{3}\notag
$$

Note that $r_{0}=0$ if $l=0$.

:::{figure} ../images/lt-21194-9.10.3.png
:label: fig-11-10-3
:enumerator: 11.10.3
:alt: Effective potential for two connected masses.

Effective potential for two connected masses.
:::

The stability of the solution is given by the second derivative

$$
\left( \frac{\partial ^{2}U_{eff}}{\partial r^{2}}\right) _{r_{0}}=\frac{ 3l^{2}}{mr_{0}^{4}}=\frac{3mg}{r_{0}}>0\notag
$$

Therefore the stationary point is stable.

Note that the equation of motion for the minimum can be expressed in terms of the restoring force on the two masses

$$
2m\ddot{r}=-\left( \frac{\partial ^{2}U_{eff}}{\partial r^{2}}\right) _{r_{0}}\left( r-r_{0}\right)\notag
$$

Thus the system undergoes harmonic oscillation with frequency

$$
\omega =\sqrt{\frac{\frac{3mg}{r_{0}}}{2m}}=\sqrt{\frac{3g}{2r_{0}}}\notag
$$

The solution of this system is stable and undergoes simple harmonic motion.
::::

## 11.11: The Three-Body Problem

Two bodies interacting via conservative central forces can be solved analytically for the inverse square law and the Hooke’s law radial dependences as already discussed. Central forces that have other radial dependences for the equations of motion may not be expressible in terms of simple functions, nevertheless the motion always can be given in terms of an integral. For a gravitational system comprising $n\geq 3$ bodies that are interacting via the two-body central gravitational force, then the equations of motion can be written as

$$
m_{j}\mathbf{ \ddot{q}=G}\sum_{\substack{ k \\ k\neq j}}^{n}m_{j}m_{k}\frac{\left( \mathbf{q}_{k}-\mathbf{q}_{j}\right) }{\left\vert \mathbf{q}_{k}-\mathbf{q} _{j}\right\vert ^{3}} \tag{$j=1,2,..,n$}
$$

Even when all the $n$ bodies are interacting via two-body central forces, the problem usually is insoluble in terms of known analytic integrals. Newton first posed the difficulty of the three-body Kepler problem which has been studied extensively by mathematicians and physicists. No known general analytic integral solution has been found. Each body for the $n$-body system has $6$ degrees of freedom, that is, $3$ for position and $3$ for momentum. The center-of-mass motion can be factored out, therefore the center-of-mass system for the $n$-body system has $6n-10$ degrees of freedom after subtraction of $3$ degrees for location of the center of mass, $3$ for the linear momentum of the center of mass, $3$ for rotation of the center of mass, and $1$ for the total energy of the system. Thus for $n=2$ there are $12-10=2$ degrees of freedom for the two-body system for which the Kepler approach takes to be $\mathbf{r}$ and $\theta .$ For $n=3$ there are $8$ degrees of freedom in the center of mass system that have to be determined.

:::{figure} ../images/lt-23553-11.11_new.png
:label: fig-11-11-1
:enumerator: 11.11.1
:alt: A contour plot of the effective potential for the Sun-Earth gravitational system in the rotating frame where the Sun and Earth are stationary. The 5 Lagrange points L_i are saddle points where the net force is zero. (Figure created by NASA)

A contour plot of the effective potential for the Sun-Earth gravitational system in the rotating frame where the Sun and Earth are stationary. The 5 Lagrange points $L_i$ are saddle points where the net force is zero. (Figure created by NASA)
:::

Numerical solutions to the three-body problem can be obtained using successive approximation or perturbation methods in computer calculations. The problem can be simplified by restricting the motion to either of following two approximations:

### 1) Planar approximation

This approximation assumes that the three masses move in the same plane, that is, the number of degrees of freedom are reduced from $8$ to $6$ which simplifies the numerical solution.

### 2) Restricted three-body approximation

The restricted three-body approximation assumes that two of the masses are large and bound while the third mass is negligible such that the perturbation of the motion of the larger two by the third body is negligible. This approximation essentially reduces the system to a two body problem in order to calculate the gravitational fields that act on the third much lighter mass.

Euler and Lagrange showed that the restricted three-body system has five points at which the combined gravitational attraction plus centripetal force of the two large bodies cancel. These are called the Lagrange points and are used for parking satellites in stable orbits with respect to the Earth-Moon system, or with respect to the Sun-Earth system. Figure 11.11.1 illustrates the five Lagrange points for the Earth-Sun system. Only two of the Lagrange points, $L_{4}$ and $L_{5}$ lead to stable orbits. Note that these Lagrange points are fixed with respect to the Earth-Sun system which rotates with respect to inertial coordinate frames. The $1900$’s discovery of the Trojan asteroids at the $L_{4}$ and $L_{5}$ Lagrange points of the Sun-Jupiter system confirmed the Lagrange predictions.

Poincaré showed that the motion of a light mass bound to two heavy bodies can exhibit extreme sensitivity to initial conditions as well as characteristics of chaos. Solution of the three-body problem has remained a largely unsolved problem since Newton identified the difficulties involved.

## 11.12: Two-body Scattering

Two moving bodies, that are interacting via a central force, scatter when the force is repulsive, or when an attractive system is unbound. Two-body scattering of bodies is encountered extensively in the fields of astronomy, atomic, nuclear, and particle physics. The probability of such scattering is most conveniently expressed in terms of scattering cross sections defined below.

### Total two-body scattering cross section

:::{figure} ../images/lt-21198-9.12.1.png
:label: fig-11-12-1
:enumerator: 11.12.1
:alt: Scattering probability for an incident beam of cross sectional area A by a target body of cross sectional area \sigma.

Scattering probability for an incident beam of cross sectional area A by a target body of cross sectional area $\sigma$.
:::

The concept of scattering cross section for two-body scattering is most easily described for the total two-body cross section. The probability $P$ that a beam of $n_{B}$ incident point particles/second, distributed over a cross sectional area $A_{B},$ will hit a single solid object, having a cross sectional area $\sigma ,$ is given by the ratio of the areas as illustrated in Figure 11.12.1. That is,

$$
P=\frac{\sigma }{A_{B}}\tag{11.134} \label{eq-11-134}
$$

where it is assumed that $A_{B}>>\sigma .$ For a spherical target body of radius $r$, the cross section $\sigma =\pi r^{2}.$ The scattering probability $P$ is proportional to the cross section $\sigma$ which is the cross section of the target body perpendicular to the beam; thus $\sigma$ has the units of area.

Since the incident beam of $n_{B}$ incident point particles/second, has a cross sectional area $A_{B}$, then it will have an areal density $I$ given by

$$
I=\frac{n_{B}}{A_{B}}\text{ beam particles}/m^{2}/s \tag{11.135} \label{eq-11-135}
$$

The number of beam particles scattered per second $N_{S}$ by this single target scatterer equals

$$
N_{S}=Pn_{B}=\frac{\sigma }{A_{B}}IA_{B}=\sigma I\tag{11.136} \label{eq-11-136}
$$

Thus the cross section for scattering by this single target body is

$$
\sigma =\frac{N_{S}}{I}=\frac{\text{Scattered particles}/s}{\text{incident beam/m}^{2}/s}\tag{11.137} \label{eq-11-137}
$$

Realistically one will have many target scatterers in the target and the total scattering probability increases proportionally to the number of target scatterers. That is, for a target comprising an areal density of $\eta _{T}$ target bodies per unit area of the incident beam, then the number scattered will increase proportional to the target areal density $\eta _{T}.$ That is, there will be $\eta _{T}A_{B}$ scattering bodies that interact with the beam assuming that the target has a larger area than the beam. Thus the total number scattered per second $N_{S}$ by a target that comprises multiple scatterers is

$$
N_{S}=\sigma \frac{n_{B}}{A_{B}}\eta _{T}A_{B}=\sigma n_{B}\eta _{T}\tag{11.138} \label{eq-11-138}
$$

Note that this is independent of the cross sectional area of the beam assuming that the target area is larger than that of the beam. That is, the number scattered per second is proportional to the cross section $\sigma$ times the product of the number of incident particles per second, $n_{B},$ and the areal density of target scatterers, $\eta _{T}$. Typical cross sections encountered in astrophysics are $\sigma \approx 10^{14}m^{2}$, in atomic physics: $\sigma \approx 10^{-20}m^{2}$, and in nuclear physics; $\sigma \approx 10^{-28}m^{2}=barns.$[^11-12-3]

N. B., the above proof assumed that the target size is larger than the cross sectional area of the incident beam. If the size of the target is smaller than the beam, then $n_{B}$ is replaced by the areal density/s of the beam $\eta _{B}$ and $\eta _{T}$ is replaced by the number of target particles $n_{T}$ and the cross-sectional size of the target cancels.

### Differential two-body scattering cross section

:::{figure} ../images/lt-21199-9.12.2.png
:label: fig-11-12-2
:enumerator: 11.12.2
:alt: The equivalent one-body problem for scattering of a reduced mass \mu by a force centre in the centre of mass system.

The equivalent one-body problem for scattering of a reduced mass $\mu$ by a force centre in the centre of mass system.
:::

The differential two-body scattering cross section gives much more detailed information of the scattering force than does the total cross section because of the correlation between the impact parameter and the scattering angle. That is, a measurement of the number of beam particles scattered into a given solid angle as a function of scattering angles $\theta ,\phi$ probes the radial form of the scattering force.

The differential cross section for scattering of an incident beam by a single target body into a solid angle $d\Omega$ at scattering angles $\theta ,\phi$ is defined to be

$$
\frac{d\sigma }{d\Omega }\left( \theta \phi \right) \equiv \frac{1}{I}\frac{ dN_{S}\left( \theta ,\phi \right) }{d\Omega }\tag{11.139} \label{eq-11-139}
$$

where the right-hand side is the ratio of the number scattered per target nucleus into solid angle $d\Omega (\theta ,\phi ),$ to the incident beam intensity $I$ $particles/m^{2}/s$.

Similar reasoning used to derive Equation \text{(11.137)} leads to the number of beam particles scattered into a solid angle $d\Omega$ for $n_{B}$ beam particles incident upon a target with areal density $\eta _{T}$ is 
$$
\frac{dN_{S}\left( \theta ,\phi \right) }{d\Omega }=n_{B}\eta _{T}\frac{ d\sigma }{d\Omega }\left( \theta \phi \right)\tag{11.140} \label{eq-11-140}
$$

Consider the equivalent one-body system for scattering of one body by a scattering force center in the center of mass. As shown in figures $(11.8.2)$ and 11.12.2, the perpendicular distance between the center of force of the two body system and trajectory of the incoming body at infinite distance is called the *impact parameter* $b$. For a central force the scattering system has cylindrical symmetry, therefore the solid angle $d\Omega (\theta \phi )=\sin \theta d\theta d\phi$ can be integrated over the azimuthal angle $\phi$ to give $d\Omega (\theta )=2\pi \sin \theta d\theta .$

For the inverse-square, two-body, central force there is a one-to-one correspondence between impact parameter $b$ and scattering angle $\theta$ for a given bombarding energy. In this case, assuming conservation of flux means that the incident beam particles passing through the impact-parameter annulus between $b$ and $b+db$ must equal the number passing between the corresponding angles $\theta$ and $\theta +d\theta .$ That is, for an incident beam flux of $I$ $particles/m^{2}/s$ the number of particles per second passing through the annulus is

$$
I2\pi b\left\vert db\right\vert =2\pi \frac{d\sigma }{d\Omega }I\sin \theta \left\vert d\theta \right\vert\tag{11.141} \label{eq-11-141}
$$

The modulus is used to ensure that the number of particles is always positive. Thus 
$$
\frac{d\sigma }{d\Omega }=\frac{b}{\sin \theta }\left\vert \frac{db}{d\theta }\right\vert\tag{11.142} \label{eq-11-142}
$$

### Impact parameter dependence on scattering angle

If the function $b=f(\theta ,E_{cm})$ is known, then it is possible to evaluate $\left\vert \frac{db}{d\theta }\right\vert$ which can be used in Equation \text{(11.141)} to calculate the differential cross section. A simple and important case to consider is two-body elastic scattering for the inverse-square law force such as the Coulomb or gravitational forces. To avoid confusion in the following discussion, the center-of-mass scattering angle will be called $\theta ,$ while the angle used to define the hyperbolic orbits in the discussion of trajectories for the inverse square law, will be called $\psi$.

In chapter $11.8$ the equivalent one-body representation gave that the radial distance for a trajectory for the inverse square law is given by

$$
\frac{1}{r}=-\frac{\mu k}{l^{2}}\left[ 1+\epsilon \cos \psi \right]\tag{11.143} \label{eq-11-143}
$$

Note that closest approach occurs when $\psi =0$ while for $r\rightarrow \infty$ the bracket must equal zero, that is

$$
\cos \psi _{\infty }=\pm \left\vert \frac{1}{\epsilon }\right\vert\tag{11.144} \label{eq-11-144}
$$

The polar angle $\psi$ is measured with respect to the symmetry axis of the two-body system which is along the line of distance of closest approach as shown in Figure $(11.8.2)$. The geometry and symmetry show that the scattering angle $\theta$ is related to the trajectory angle $\psi _{\infty }$ by

$$
\theta =\pi -2\psi _{\infty }\tag{11.145} \label{eq-11-145}
$$

Equation $(11.7.1)$ gives that

$$
\psi _{\infty }=\int_{r_{\min }}^{\infty }\frac{\pm ldr}{r^{2}\sqrt{2\mu \left( E_{cm}-U-\frac{l^{2}}{2\mu r^{2}}\right) }}\tag{11.146} \label{eq-11-146}
$$

Since

$$
l^{2}=b^{2}p^{2}=b^{2}2\mu E_{cm}
$$

then the scattering angle can be written as.

$$
\psi _{\infty }=\frac{\pi -\theta }{2}=\int_{r_{\min }}^{\infty }\frac{bdr}{ r^{2}\sqrt{\left( 1-\frac{U}{E_{cm}}-\frac{b^{2}}{r^{2}}\right) }}\tag{11.147} \label{eq-11-147}
$$

Let $u=\frac{1}{r}$, then 
$$
\psi _{\infty }=\frac{\pi -\theta }{2}=\int_{r_{\min }}^{\infty }\frac{bdu}{ \sqrt{\left( 1-\frac{U}{E_{cm}}-b^{2}u^{2}\right) }}\tag{11.148} \label{eq-11-148}
$$

For the repulsive inverse square law

$$
U=-\frac{k}{r}=-ku\tag{11.149} \label{eq-11-149}
$$

where $k$ is taken to be positive for a repulsive force. Thus the scattering angle relation becomes 
$$
\psi _{\infty }=\frac{\pi -\theta }{2}=\int_{r_{\min }}^{\infty }\frac{bdu}{ \sqrt{\left( 1+\frac{ku}{E_{cm}}-b^{2}u^{2}\right) }}\tag{11.150} \label{eq-11-150}
$$

:::{figure} ../images/lt-21200-9.12.3.png
:label: fig-11-12-3
:enumerator: 11.12.3
:alt: Impact parameter dependence on scattering angle for Rutherford scattering.

Impact parameter dependence on scattering angle for Rutherford scattering.
:::

The solution of this equation is given by equation $(11.8.12)$ to be

$$
u=\frac{1}{r}=-\frac{\mu k}{l^{2}}\left[ 1+\epsilon \cos \psi \right]\tag{11.151} \label{eq-11-151}
$$

where the eccentricity

$$
\epsilon =\sqrt{1+\frac{2E_{cm}l^{2}}{\mu k^{2}}}\tag{11.152} \label{eq-11-152}
$$

For $r\rightarrow \infty ,$ $u=0$ then, as shown previously,

$$
\left\vert \frac{1}{\epsilon }\right\vert =\cos \psi _{\infty }=\cos \frac{ \pi -\theta }{2}=\sin \frac{\theta }{2}\tag{11.153} \label{eq-11-153}
$$

Therefore

$$
\frac{2E_{cm}b}{k}=\sqrt{\epsilon ^{2}-1}=\cot \frac{\theta }{2}\tag{11.154} \label{eq-11-154}
$$

that is, the impact parameter $b$ is given by the relation

$$
b=\frac{k}{2E_{cm}}\cot \frac{\theta }{2}\tag{11.155} \label{eq-11-155}
$$

Thus, for an inverse-square law force, the two-body scattering has a one-to-one correspondence between impact parameter $b$ and scattering angle $\theta$ as shown schematically in Figure 11.12.3.

:::{figure} ../images/lt-21201-9.12.4.png
:label: fig-11-12-4
:enumerator: 11.12.4
:alt: Classical trajectories for scattering to a given angle by the repulsive Coulomb field plus the attractive nuclear field for three different impact parameters. Path 1 is pure Coulomb. Paths 2 and 3 include Coulomb plus nuclear interactions. The dashed parts of trajectories 2 and 3 correspond to on…

Classical trajectories for scattering to a given angle by the repulsive Coulomb field plus the attractive nuclear field for three different impact parameters. Path 1 is pure Coulomb. Paths 2 and 3 include Coulomb plus nuclear interactions. The dashed parts of trajectories 2 and 3 correspond to only the Coulomb force acting, i.e. zero nuclear force
:::

If $k$ is negative, which corresponds to an attractive inverse square law, then one gets the same relation between impact parameter and scattering angle except that the sign of the impact parameter $b$ is opposite. This means that the hyperbolic trajectory has an interior rather than exterior focus. That is, the trajectory partially orbits around the center of force rather than being repelled away.

$$
r_{\min }=\frac{k}{2E_{cm}}\left( 1+\frac{1}{\sin \frac{\theta }{2}}\right)\tag{11.157} \label{eq-11-157}
$$

Note that for $\theta =180^{o}$ then

$$
E_{cm}=\frac{k}{r_{\min }}=U(r_{\min )}\tag{11.158} \label{eq-11-158}
$$

which is what you would expect from equating the incident kinetic energy to the potential energy at the distance of closest approach.

For scattering of two nuclei by the repulsive Coulomb force, if the impact parameter becomes small enough, the attractive nuclear force also acts leading to impact-parameter dependent effective potentials illustrated in Figure 11.12.4. Trajectory $1$ does not overlap the nuclear force and thus is pure Coulomb. Trajectory $2$ interacts at the periphery of the nuclear potential and the trajectory deviates from pure Coulomb shown dashed. Trajectory $3$ passes through the interior of the nuclear potential. These three trajectories all can lead to the same scattering angle and thus there no longer is a one-to-one correspondence between scattering angle and impact parameter.

### Rutherford scattering

Two models of the nucleus evolved in the $1900$’s, the Rutherford model assumed electrons orbiting around a small nucleus like planets around the sun, while J.J. Thomson’s ”plum-pudding” model assumed the electrons were embedded in a uniform sphere of positive charge the size of the atom. When Rutherford derived his classical formula in $1911$ he realized that it can be used to determine the size of the nucleus since the electric field obeys the inverse square law only when outside of the charged spherical nucleus. Inside a uniform sphere of charge the electric field is $\mathbf{E}\varpropto \mathbf{r}$ and thus the scattering cross section will not obey the Rutherford relation for distances of closest approach that are less than the radius of the sphere of negative charge. Observation of the angle beyond which the Rutherford formula breaks down immediately determines the radius of the nucleus.

$$
\frac{d\sigma }{d\Omega }=\frac{1}{4}\left( \frac{k}{2E_{cm}}\right) ^{2} \frac{1}{\sin ^{4}\frac{\theta }{2}}\tag{11.159} \label{eq-11-159}
$$

This cross section assumes elastic scattering by a repulsive two-body inverse-square central force. For scattering of nuclei in the Coulomb potential, the constant $k$ is given to be 
$$
k=\frac{Z_{p}Z_{T}e^{2}}{4\pi \varepsilon _{o}}\tag{11.160} \label{eq-11-160}
$$

The cross section, scattering angle and $E_{cm}$ of Equation \text{(11.159)} are evaluated in the center-of-mass coordinate system, whereas usually two-body elastic scattering data involve scattering of the projectiles by a stationary target as discussed in chapter $11.13.$

Gieger and Marsden performed scattering of $7.7$ MeV $\alpha$ particles from a thin gold foil and proved that the differential scattering cross section obeyed the Rutherford formula back to angles corresponding to a distance of closest approach of $10^{-14}m$ which is much smaller that the $10^{-10}m$ size of the atom. This validated the Rutherford model of the atom and immediately led to the Bohr model of the atom which played such a crucial role in the development of quantum mechanics. Bohr showed that the agreement with the Rutherford formula implies the Coulomb field obeys the inverse square law to small distances. This work was performed at Manchester University, England between $1908$ and $1913$. It is fortunate that the classical result is identical to the quantal cross section for scattering, otherwise the development of modern physics could have been delayed for many years.

Scattering of very heavy ions, such as $^{208}$Pb, can electromagnetically excite target nuclei. For the Coulomb force the impact parameter $b$ and the distance of closest approach, $r_{\min }$ are directly related to the scattering angle $\theta$ by Equation \text{(11.155)}. Thus observing the angle of the scattered projectile unambiguously determines the hyperbolic trajectory and thus the electromagnetic impulse given to the colliding nuclei. This process, called Coulomb excitation, uses the measured angular distribution of the scattered ions for inelastic excitation of the nuclei to precisely and unambiguously determine the Coulomb excitation cross section as a function of impact parameter. This unambiguously determines the shape of the nuclear charge distribution.

::::{admonition} Example 11.12.1: Two-body scattering by an inverse cubic force
:class: example

Assume two-body scattering by a potential $U= \frac{k}{r^{2}}$ where $k>0$. This corresponds to a repulsive two-body force $\mathbf{F=}\frac{2k}{r^{3}}\mathbf{\hat{r}}$. Insert this force into Binet’s differential orbit, equation $(11.5.5)$, gives

$$
\frac{d^{2}u}{d\phi ^{2}}+u\left( 1+\frac{2k\mu }{l^{2}}\right) =0 \notag
$$

The solution is of the form $u=A\sin (\omega \psi +\beta )$ where $A$ and $\beta$ are constants of integration, $l=\mu r^{2}\dot{\psi},$ and

$$
\omega ^{2}=\left( 1+\frac{2k\mu }{l^{2}}\right)\notag
$$

Initially $r=\infty$, $u=0,$ and therefore $\beta =0$. Also at $r=\infty$, $E=\frac{1}{2}\mu \dot{r}_{\infty }^{2}$, that is $\left\vert \dot{r}_{\infty } \right\vert =\sqrt{\frac{2E}{\mu } }$. Then

$$
\dot{r}=\frac{dr}{d\psi }\dot{\psi}=\frac{dr}{d\psi }\frac{l}{\mu r^{2}}=- \frac{l}{\mu }\frac{du}{d\psi }=-A\frac{l}{\mu }\omega \cos \left( \omega \psi \right)\notag
$$

The initial energy gives that $A=\frac{1}{l\omega }\sqrt{2\mu E}.$ Hence the orbit equation is

$$
u=\frac{1}{r}=\frac{\sqrt{2\mu E}}{l\omega }\sin \left( \omega \psi \right)\notag
$$

The above trajectory has a distance of closest approach, $r_{\min }$, when $\psi _{\min }=\frac{\pi }{2\omega }$. Moreover, due to the symmetry of the orbit, the scattering angle $\theta$ is given by

$$
\theta =\pi -2\psi _{0}=\pi \left( 1-\frac{1}{\omega }\right)\notag
$$

Since $l^{2}=\mu ^{2}b^{2}\dot{r}_{\infty }^{2}=2b^{2}\mu E$ then

$$
1-\frac{\theta }{\pi }=\left( 1+\frac{2k\mu }{l^{2}}\right) ^{-\frac{1}{2} }=\left( 1+\frac{k}{b^{2}E}\right) ^{-\frac{1}{2}}\notag
$$

This gives that the impact parameter $b$ is related to scattering angle by

$$
b^{2}=\frac{k}{E}\frac{\left( \pi -\theta \right) ^{2}}{\left( 2\pi -\theta \right) \theta } \notag
$$

This impact parameter relation can be used in Equation \text{(11.141)} to give the differential cross section

$$
\frac{d\sigma }{d\Omega }=\frac{b}{\sin \theta }\left\vert \frac{db}{d\theta }\right\vert =\frac{k}{Esin\theta }\frac{\pi ^{2}\left( \pi -\theta \right) }{\left( 2\pi -\theta \right) ^{2}\theta ^{2}} \notag
$$

These orbits are called Cotes spirals.
::::

[^11-12-3]: The term "barn" was chosen because nuclear physicists joked that the cross sections for neutron scattering by nuclei were as large as a barn door.

## 11.13: Two-body kinematics

So far the discussion has been restricted to the center-of-momentum system. Actual scattering measurements are performed in the laboratory frame, and thus it is necessary to transform the scattering angle, energies and cross sections between the laboratory and center-of-momentum coordinate frame. In principle the transformation between the center-of-momentum and laboratory frames is straightforward, using the vector addition of the center-of-mass velocity vector and the center-of-momentum velocity vectors of the two bodies. The following discussion assumes non-relativistic kinematics apply.

In chapter $2.8$ it was shown that, for Newtonian mechanics, the center-of-mass and center-of-momentum frames of reference are identical. By definition, in the center-of-momentum frame the vector sum of the linear momentum of the incoming projectile, $p_{P}^{Initial}$ and target, $p_{T}^{Initial}$ are equal and opposite. That is

$$
\mathbf{p}_{P}^{Initial}+\mathbf{p}_{T}^{Initial}=0\tag{11.161} \label{eq-11-161}
$$

Using the center-of-momentum frame, coupled with the conservation of linear momentum, implies that the vector sum of the final momenta of the $N$ reaction products, $p_{i}^{Final},$ also is zero. That is

$$
\sum_{i=1}^{N}\mathbf{p}_{i}^{Final}=0\tag{11.162} \label{eq-11-162}
$$

An additional constraint is that energy conservation relates the initial and final kinetic energies by

$$
\frac{\left( p_{P}^{Initial}\right) ^{2}}{2m_{P}}+\frac{\left( p_{T}^{Initial}\right) ^{2}}{2m_{T}}+Q=\frac{\left( p_{P}^{Final}\right) ^{2} }{2m_{P}}+\frac{\left( p_{T}^{Final}\right) ^{2}}{2m_{T}}\tag{11.163} \label{eq-11-163}
$$

where the $Q$ value is the energy contributed to the final total kinetic energy by the reaction between the incoming projectile and target. For exothermic reactions, $Q>0,$ the summed kinetic of the reaction products exceeds the sum of the incoming kinetic energies, while for endothermic reactions, $Q<0,$ the summed kinetic energy of the reaction products is less than that of the incoming channel.

For two-body kinematics, the following are three advantages to working in the center-of-momentum frame of reference.

1. The two incident colliding bodies are colinear as are the two final bodies.

2. The linear momenta for the two colliding bodies are identical in both the incident channel and the outgoing channel.

3. The total energy in the center-of-momentum coordinate frame is the energy available to the reaction during the collision. The trivial kinetic energy of the center-of-momentum frame relative to the laboratory frame is handled separately.

The kinematics for two-body reactions is easily determined using the conservation of linear momentum along and perpendicular to the beam direction plus the conservation of energy, \text{(11.161)}-\text{(11.163)}. Note that it is common practice to use the term "center-of-mass" rather than "center-of-momentum" in spite of the fact that, for relativistic mechanics, only the center-of-momentum is a meaningful concept.

General features of the transformation between the center-of-momentum and laboratory frames of reference are best illustrated by elastic or inelastic scattering of nuclei where the two reaction products in the final channel are identical to the incident bodies. Inelastic excitation of an excited state energy of $\Delta E_{ex}$ in either reaction product corresponds to $Q=-\Delta E_{exc},$ while elastic scattering corresponds to $Q=-\Delta E_{exc}=0$.

For inelastic scattering, the conservation of linear momenta for the outgoing channel in the center-of-momentum simplifies to

$$
\mathbf{p}_{P}^{Final}+\mathbf{p}_{T}^{Final}=0
$$

that is, the linear momenta of the two reaction products are equal and opposite.

Assume that the center-of-momentum direction of the scattered projectile is at an angle $\vartheta _{cm}^{P}=\vartheta$ relative to the direction of the incoming projectile and that the scattered target nucleus is scattered at a center-of-momentum direction $\vartheta _{cm}^{T}=\pi -\vartheta$. Elastic scattering corresponds to simple scattering for which the magnitudes of the incoming and outgoing projectile momenta are equal, that is, $\left\vert p_{P}^{Final}\right\vert =\left\vert p_{P}^{Initial}\right\vert$.

:::{figure} ../images/lt-21202-9.13.1.png
:label: fig-11-13-1
:enumerator: 11.13.1
:alt: Vector hodograph of the scattered projectile and target velocities for a projectile, with incident velocity v_i, that is elastically scattered by a stationary target body. The circles show the magnitude of the projectile and target body final velocities in the center of mass. The center-of-mass v…

Vector hodograph of the scattered projectile and target velocities for a projectile, with incident velocity $v_i$, that is elastically scattered by a stationary target body. The circles show the magnitude of the projectile and target body final velocities in the center of mass. The center-of-mass velocity vectors are shown as dashed lines while the laboratory vectors are shown as solid lines. The left hodograph shows normal kinematics where the projectile mass is less than the target mass. The right hodograph shows inverse kinematics where the projectile mass is greater than the target mass. For elastic scattering $u_T = u^{\prime}_T$.
:::

### Velocities

The transformation between the center-of-momentum and laboratory frames requires knowledge of the particle velocities which can be derived from the linear momenta since the particle masses are known. Assume that a projectile, mass $m_{P}$, with incident energy $E_{P}$ in the laboratory frame bombards a stationary target with mass $m_{T}.$ The incident projectile velocity $v_{i}$ is given by

$$
v_{i}=\sqrt{\frac{2E_{P}}{m_{P}}}
$$

The initial velocities in the laboratory frame are taken to be

$$
\begin{align} w_{P} &=&v_{i} \tag{Initial Lab velocities} \\ w_{T} &=&0 \notag\end{align}
$$

The final velocities in the laboratory frame after the inelastic collision are 
$$
\begin{align} &&w_{P}^{\prime } \tag{Final Lab velocities} \\ &&w_{T}^{\prime } \notag\end{align}
$$

In the center-of-momentum coordinate system, equation $(11.2.8)$ implies that the initial center-of-momentum velocities are 
$$
\begin{align} u_{P} &=&v_{i}\frac{m_{T}}{m_{P}+m_{T}} \notag \\ u_{T} &=&v_{i}\frac{m_{P}}{m_{P}+m_{T}}\end{align}
$$

It is simple to derive that the final center-of-momentum velocities after the inelastic collision are given by

$$
\begin{align} u_{P}^{\prime } &=&\frac{m_{T}}{m_{P}+m_{T}}\sqrt{\frac{2}{m_{P}}\tilde{E}} \notag \\ u_{T}^{\prime } &=&\frac{m_{P}}{m_{P}+m_{T}}\sqrt{\frac{2}{m_{P}}\tilde{E}}\end{align}
$$

The energy $\tilde{E}$ is defined to be given by

$$
\tilde{E}=E_{P}+Q(1+\frac{m_{P}}{m_{T}})
$$

where $Q=-\Delta E$ which is the excitation energy of the final excited states in the outgoing channel.

### Angles

The angles of the scattered recoils are written as

$$
\begin{align} &&\theta _{lab}^{P} \tag{Final laboratory angles} \\ &&\theta _{lab}^{T} \notag\end{align}
$$

and

$$
\begin{align} \vartheta _{cm}^{P} &=&\vartheta \tag{Final CM angles} \\ \vartheta _{cm}^{T} &=&\pi -\vartheta \notag\end{align}
$$

where $\vartheta$ is the center-of-mass (center-of-momentum) scattering angle.

Figure 11.13.1 shows that the angle relations between the laboratory and center of momentum frames for the *scattered projectile* are connected by

$$
\frac{\sin (\vartheta _{cm}^{P}-\theta _{lab}^{P})}{\sin \theta _{lab}^{P}}= \frac{m_{P}}{m_{T}}\sqrt{\frac{E_{P}}{\tilde{E}}}\equiv \tau \tag{11.169} \label{eq-11-169}
$$

where

$$
\tau =\frac{m_{P}}{m_{T}}\frac{1}{\sqrt{1+\frac{Q}{E_{P}}(1+\frac{m_{P}}{ m_{T}})}}=\frac{m_{P}}{m_{T}}\frac{1}{\sqrt{1+\frac{Q}{E_{P}/m_{P}}(\frac{ m_{P}+m_{T}}{m_{P}m_{T}})}}
$$

and $\frac{E_{P}}{m_{P}}$ is the energy per nucleon on the incident projectile.

Equation \text{(11.169)} can be rewritten as 
$$
\tan \theta _{lab}^{P}=\frac{\sin \vartheta _{cm}^{P}}{\cos \vartheta _{cm}^{P}+\tau }
$$

Another useful relation from Equation \text{(11.169)} gives the center-of-momentum scattering angle in terms of the laboratory scattering angle.

$$
\vartheta _{cm}^{P}=\sin ^{-1}(\tau \sin \theta _{lab}^{P})+\theta _{lab}^{P}
$$

This gives the difference in angle between the lab scattering angle and the center-of-momentum scattering angle. Be careful with this relation since $\vartheta _{lab}^{P}$ is two-valued for inverse kinematics corresponding to the two possible signs for the solution.

The angle relations between the lab and center-of-momentum for the *recoiling target nucleus* are connected by

$$
\frac{\sin (\vartheta _{cm}^{T}-\theta _{lab}^{T})}{\sin \theta _{lab}^{T}}= \sqrt{\frac{E_{P}}{\tilde{E}}}\equiv \tilde{\tau}\tag{11.173} \label{eq-11-173}
$$

That is

$$
\vartheta _{cm}^{T}=\sin ^{-1}(\tilde{\tau}\sin \theta _{lab}^{T})+\theta _{lab}^{T}
$$

where 
$$
\tilde{\tau}=\frac{1}{\sqrt{1+\frac{Q}{E_{P}}(1+\frac{m_{P}}{m_{T}})}}=\frac{ 1}{\sqrt{1+\frac{Q}{E_{P}/m_{P}}(\frac{m_{P}+m_{T}}{m_{P}m_{T}})}}
$$

Note that $\tilde{\tau}$ is the same under interchange of the two nuclei at the same incident energy/nucleon, and that $\tilde{\tau}$ is always larger than or equal to unity since $Q$ is negative. For elastic scattering $\tilde{ \tau}=1$ which gives 
$$
\theta _{lab}^{T}=\frac{1}{2}(\pi -\vartheta ) \tag{Recoil lab angle for elastic scattering}
$$

For the target recoil Equation \text{(11.173)} can be rewritten as 
$$
\tan \theta _{lab}^{T}=\frac{\sin \vartheta _{cm}^{T}}{\cos \vartheta _{cm}^{T}+\tilde{\tau}} \tag{Target lab to CM angle conversion}
$$

:::{figure} ../images/lt-21204-9.13.2.png
:label: fig-11-13-2
:enumerator: 11.13.2
:alt: The kinematic correlation of the laboratory and center-of-mass scattering angles of the recoiling projectile and target nuclei for scattering for 4.3 MeV/nucleon ^{104}Pd on ^{208}Pb (left) and for the inverse 4.3 MeV/nucleon ^{208}Pb on ^{104}Pd (right). The projectile scattering angles are show…

The kinematic correlation of the laboratory and center-of-mass scattering angles of the recoiling projectile and target nuclei for scattering for $4.3$ $MeV$/nucleon $^{104}$Pd on $^{208}$Pb (left) and for the inverse $4.3$ $MeV$/nucleon $^{208}$Pb on $^{104}$Pd (right). The projectile scattering angles are shown by solid lines while the recoiling target angles are shown by dashed lines. The blue curves correspond to elastic scattering, that is $Q=0$ while the red curves correspond to inelastic scattering with $Q = −5$ $MeV$.
:::

Velocity vector hodographs provide useful insight into the behavior of the kinematic solutions. As shown in Figure 11.13.1, in the center-of-momentum frame the scattered projectile has a fixed final velocity $u_{P}^{\prime }$, that is, the velocity vector describes a circle as a function of $\vartheta$. The vector addition of this vector and the velocity of the center-of-mass vector $-u_{T}$ gives the laboratory frame velocity $w_{P}^{\prime }$. Note that for normal kinematics, where $m_{P}<m_{T},$ then $\left\vert u_{T}\right\vert <\left\vert u_{P}^{\prime }\right\vert$ leading to a monotonic one-to-one mapping of the center-of-momentum angle $\vartheta _{P}$ and $\theta _{lab}^{P}$. However, for inverse kinematics, where $m_{P}>m_{T},$ then $\left\vert u_{T}\right\vert >\left\vert u_{P}^{\prime }\right\vert$ leading to two valued $\vartheta$ solutions at any fixed laboratory scattering angle $\theta$.

Billiard ball collisions are an especially simple example where the two masses are identical and the collision is essentially elastic. Then essentially $\tau =\tilde{\tau}=1$, $\theta _{lab}^{P}=\frac{\vartheta _{cm}^{P}}{2},$ and $\theta _{lab}^{T}=\frac{1}{2}\left( \pi -\vartheta _{cm}^{P}\right)$, that is, the angle between the scattered billiard balls is $\frac{\pi }{2}$.

Both normal and inverse kinematics are illustrated in Figure 11.13.2 which shows the dependence of the projectile and target scattering angles in the laboratory frame as a function of center-of-momentum scattering angle for the Coulomb scattering of $^{104}$Pd by $^{208}$Pb, that is, for a mass ratio of $2:1$. Both normal and inverse kinematics are shown for the same bombarding energy of $4.3$ $MeV/nucleon$ for elastic scattering and for inelastic scattering with a $Q$-value of $-5MeV$.

:::{figure} ../images/lt-21203-9.13.3.png
:label: fig-11-13-3
:enumerator: 11.13.3
:alt: Recoil energies, in MeV, versus laboratory scattering angle, shown on the left for scattering of 447 MeV ^{104}Pd by ^{208}Pb with Q = −5.0 MeV, and shown on the right for scattering of 894 MeV ^{208}Pb on ^{104}Pd with Q = −5.0 MeV.

Recoil energies, in $MeV$, versus laboratory scattering angle, shown on the left for scattering of $447$ $MeV$ $^{104}$Pd by $^{208}$Pb with $Q = −5.0$ $MeV$, and shown on the right for scattering of $894$ $MeV$ $^{208}$Pb on $^{104}$Pd with $Q = −5.0$ $MeV$.
:::

Since $\sin (\vartheta _{cm}^{T}-\theta _{lab}^{T})\leq 1$ then Equation \text{(11.173)} implies that $\tilde{\tau}\sin \theta _{lab}^{T}\leq 1.$ Since $\tilde{\tau}$ is always larger than or equal to unity there is a maximum scattering angle in the laboratory frame for the recoiling target nucleus given by

$$
\sin \theta _{\max }^{T}=\frac{1}{\tilde{\tau}}
$$

For elastic scattering $\theta _{lab}^{T}=\sin ^{-1}(\frac{1}{\tilde{\tau}} )=90^{\circ }$ since $\tilde{\tau}=1$ for both $894$ $MeV$ $^{208}$Pb bombarding $^{104}$Pd, and the inverse reaction using a $447$ $MeV$ $^{104}$Pd beam scattered by a $^{208}$Pb target. A $Q$-value of $-5$ $MeV$ gives$\ \tilde{\tau}=1.002808$ which implies a maximum scattering angle of $\theta _{lab}^{T}=85.71^{\circ }$ for both $894$ $MeV$ $^{208}$Pb bombarding $^{104}$ Pd, and the inverse reaction of a $447$ $MeV$ $^{104}$Pd beam scattered by a $^{208}$Pb target. As a consequence there are two solutions for $\vartheta _{cm}^{T}$ for any allowed value of $\theta _{lab}^{T}$ as illustrated in Figure $11.13.3$.

Since $\sin (\vartheta _{cm}^{P}-\theta _{lab}^{P})\leq 1$ then equation $(11.12.18)$ implies that $\tau \sin \theta _{lab}^{P}\leq 1.$ For a $447$ $MeV$ $^{104}$Pd beam scattered by a $^{208}$Pb target $\frac{m_{P}}{m_{T}}=0.50$, thus $\tau =0.5$ for elastic scattering which implies that there is no upper bound to $\theta _{lab}^{P}$. This leads to a one-to-one correspondence between $\theta _{lab}^{P}$ and $\vartheta _{cm}^{P}$ for normal kinematics. In contrast, the projectile has a maximum scattering angle in the laboratory frame for inverse kinematics since $\frac{m_{P}}{m_{T}}=2.0$ leading to an upper bound to $\theta _{lab}^{P}$ given by

$$
\sin \theta _{\max }^{P}=\frac{1}{\tau }
$$

For elastic scattering $\tau =2$ implying $\theta _{\max }^{P}=30^{\circ }$. In addition to having a maximum value for $\theta _{lab}^{P}$, when $\tau >1,$ also there are two solutions for $\vartheta _{cm}^{P}$ for any allowed value of $\theta _{lab}^{P}$. For the example of $894$ $MeV$ $^{208}$Pb bombarding $^{178}$Hf leads to a maximum projectile scattering angle of $\theta _{lab}^{P}=30.0^{\circ }$ for elastic scattering and $\theta _{lab}^{P}=29.907^{\circ }$ for $Q=-5$ $MeV.$

### Kinetic energies

The initial total kinetic energy in the center-of-momentum frame is

$$
E_{cm}^{Initial}=E_{P} \frac{m_{T}}{m_{P}+m_{T}}
$$

The final total kinetic energy in the center-of-momentum frame is 
$$
E_{cm}^{Final}=E_{cm}^{Initial}+Q=\tilde{E}\frac{m_{T}}{m_{P}+m_{T}}
$$

In the laboratory frame the kinetic energies of the scattered projectile and recoiling target nucleus are given by

$$
\begin{align} E_{P}^{Lab} &=&\left( \frac{m_{T}}{m_{P}+m_{T}}\right) ^{2}\left( 1+\tau ^{2}+2\tau \cos \vartheta _{cm}^{P}\right) \tilde{E} \\ E_{T}^{Lab} &=&\frac{m_{P}m_{T}}{\left( m_{P}+m_{T}\right) ^{2}}\left( 1+ \tilde{\tau}^{2}+2\tilde{\tau}\cos \vartheta _{cm}^{T}\right) \tilde{E}\end{align}
$$

where $\vartheta _{cm}^{P}$ and $\vartheta _{cm}^{T}$ are the center-of-mass scattering angles respectively for the scattered projectile and target nuclei.

For the chosen incident energies the normal and inverse reactions give the same center-of-momentum energy of $298$ $MeV$ which is the energy available to the interaction between the colliding nuclei. However, the kinetic energy of the center-of-momentum is $447-298=149$ $MeV$ for normal kinematics and $894-298=596$ $MeV$ for inverse kinematics. This trivial center-of-momentum kinetic energy does not contribute to the reaction. Note that inverse kinematics focusses all the scattered nuclei into the forward hemisphere which reduces the required solid angle for recoil-particle detection.

### Solid angles

The laboratory-frame solid angles for the scattered projectile and target are taken to be $d\omega _{P}$ and $d\omega _{T}$ respectively, while the center-of-momentum solid angles are $d\Omega _{P}$ and $d\Omega _{T}$ respectively. The Jacobian relating the solid angles is 
$$
\frac{d\omega _{P}}{d\Omega _{P}}=\left( \frac{\sin \theta _{lab}^{P}}{\sin \vartheta _{cm}^{P}}\right) ^{2}\left\vert \cos (\vartheta _{cm}^{P}-\theta _{lab}^{P})\right\vert
$$

$$
\frac{d\omega _{T}}{d\Omega _{T}}=\left( \frac{\sin \theta _{lab}^{T}}{\sin \vartheta _{cm}^{T}}\right) ^{2}\left\vert \cos (\vartheta _{cm}^{T}-\theta _{lab}^{T})\right\vert
$$

These can be used to transform the calculated center-of-momentum differential cross sections to the laboratory frame for comparison with measured values. Note that relative to the center-of-momentum frame, the forward focussing increases the observed differential cross sections in the forward laboratory frame and decreases them in the backward hemisphere.

### Exploitation of two-body kinematics

Computing the above non-trivial transform relations between the center-of-mass and laboratory coordinate frames for two-body scattering is used extensively in many fields of physics. This discussion has assumed non-relativistic two-body kinematics. Relativistic two-body kinematics encompasses non-relativistic kinematics as discussed in chapter $17.4$. Many computer codes are available that can be used for making either non-relativistic or relativistic transformations.

It is stressed that the underlying physics for two interacting bodies is identical irrespective of whether the reaction is observed in the center-of-mass or the laboratory coordinate frames. That is, no new physics is involved in the kinematic transformation. However, the transformation between these frames can dramatically alter the angles and velocities of the observed scattered bodies which can be beneficial for experimental detection. For example, in heavy-ion nuclear physics the projectile and target nuclei can be interchanged leading to very different velocities and scattering angles in the laboratory frame of reference. This can greatly facilitate identification and observation of the velocities vectors of the scattered nuclei. In high-energy physics it is advantageous to collide beams having identical, but opposite, linear momentum vectors, since then the laboratory frame is the center-of-mass frame, and the energy required to accelerate the colliding bodies is minimized.

## 11.E: Conservative two-body Central Forces (Exercises)

1. Listed below are several statements concerning central force motion. For each statement, give the reason for why the statement is true. If a statement is only true in certain situations, then explain when it holds and when it doesn’t. The system referred to below consists of mass

   $m_{1}$

   located at

   $r_{1}$

   and mass

   $m_{2}$

   located at

   $r_{2}$

   .

   1. The potential energy of the system depends only on the difference $r_{1}-r_{2}$, not on $r_{1}$ and $r_{2}$ separately.

   2. The potential energy of the system depends only on the magnitude of $r_{1}-r_{2}$, not the direction.

   3. It is possible to choose an inertial reference frame in which the center of mass of the system is at rest.

   4. The total energy of the system is conserved.

   5. The total angular momentum of the system is conserved.

2. A particle of mass $m$ moves in a potential $U(r) = -U_0 e^{-\lambda^2r^2}$.

   1. Given the constant $l$, find an implicit equation for the radius of the circular orbit. A circular orbit at $r = \rho$ is possible if 
$$
\left. \left( \frac{\partial V}{\partial r} \right) \right\vert_{r = \rho} = 0 \notag
$$
 where $V$ is the effective potential.

   2. What is the largest value of $l$ for which a circular orbit exists? What is the value of the effective potential at this critical orbit?

3. A particle of mass $m$ is observed to move in a spiral orbit given by the equation $r = k\theta$, where $k$ is a constant. Is it possible to have such an orbit in a central force field? If so, determine the form of the force function.

4. The interaction energy between two atoms of mass $m$ is given by the Lennard-Jones potential, $U(r) = \epsilon [(r_0/r)^{12} - 2(r_0/r)^{6}]$

   1. Determine the Lagrangian of the system where $r_1$ and $r_2$ are the positions of the first and second mass, respectively.

   2. Rewrite the Lagrangian as a one-body problem in which the center-of-mass is stationary.

   3. Determine the equilibrium point and show that it is stable.

   4. Determine the frequency of small oscillations about the stable point.

5. Consider two bodies of mass $m$ in circular orbit of radius $r_0/2$, attracted to each other by a force $F(r)$, where $r$ is the distance between the masses.

   1. Determine the Lagrangian of the system in the center-of-mass frame (Hint: a one-body problem subject to a central force).

   2. Determine the angular momentum. Is it conserved?

   3. Determine the equation of motion in $r$ in terms of the angular momentum and $|\mathbf{F}(r)|$.

   4. Expand your result in (c) about an equilibrium radius $r_0$ and show that the condition for stability is, $\frac{F^{\prime}(r_0)}{F(r_0)} + \frac{3}{r_0} > 0$

6. Consider two charges of equal magnitude $q$ connected by a spring of spring constant $k^{\prime}$ in circular orbit. Can the charges oscillate about some equilibrium? If so, what condition must be satisfied?

7. Consider a mass $m$ in orbit around a mass $M$, which is subject to a force $F = -\frac{k}{r^2} \hat{r}$, where $r$ is the distance between the masses. Show that the eccentricity vector $A = p \times L - \mu k \hat{r}$ is conserved.

8. Show that the areal velocity is constant for a particle moving under the influence of an attractive force given by $F(r) = -kr$. Calculate the time averages of the kinetic and potential energies and compare with the results of the virial theorem.

9. Assume that the Earth’s orbit is circular and that the Sun’s mass suddenly decreases by a factor of two.

   1. What orbit will the earth then have?

   2. Will the Earth escape the solar system?

10. Discuss the motion of a particle in a central inverse-square-law force field for a superimposed force whose magnitude is inversely proportional to the cube of the distance from the particle to force center; that is 
$$
F(r) = - \frac{k}{r^2} - \frac{\lambda}{r^3} \tag{$k, \lambda > 0$}
$$
 Show that the motion is described by a precessing ellipse. Consider the cases a) $\lambda < \frac{l^2}{\mu}$, b) $\lambda = \frac{l^2}{\mu}$, c) $\lambda > \frac{l^2}{\mu}$ where $l$ is the angular momentum and $\mu$ the reduced mass.

11. A communications satellite is in a circular orbit around the earth at a radius $R$ and velocity $v$. A rocket accidentally fires quite suddenly, giving the rocket an outward velocity $v$ in addition to its original tangential velocity $v$.

    1. Calculate the ratio of the new energy and angular momentum to the old.

    2. Describe the subsequent motion of the satellite and plot $T(R)$, $U(r)$, the net effective potential, and $E(r)$ after the rocket fires.

12. Two identical point objects, each of mass $m$ are bound by a linear two-body force $F = -kr$ where $r$ is the vector distance between the two point objects. The two point objects each slide on a horizontal frictionless plane subject to a vertical gravitational field $g$. The two-body system is free to translate, rotate and oscillate on the surface of the frictionless plane.

    1. Derive the Lagrangian for the complete system including translation and relative motion.

    2. Use Noether’s theorem to identify all constants of motion.

    3. Use the Lagrangian to derive the equations of motion for the system.

    4. Derive the generalized momenta and the corresponding Hamiltonian.

    5. Derive the period for small amplitude oscillations of the relative motion of the two masses.

13. A bound binary star system comprises two spherical stars of mass $m_1$ and $m_2$ bound by their mutual gravitational attraction. Assume that the only force acting on the stars is their mutual gravitation attraction and let $r$ be the instantaneous separation distance between the centers of the two stars where $r$ is much larger than the sum of the radii of the stars.

    1. Show that the two-body motion of the binary star system can be represented by an equivalent one-body system and derive the Lagrangian for this system.

    2. Show that the motion for the equivalent one-body system in the center of mass frame lies entirely in a plane and derive the angle between the normal to the plane and the angular momentum vector.

    3. Show whether $H_{cm}$ is a constant of motion and whether it equals the total energy.

    4. It is known that a solution to the equation of motion for the equivalent one-body orbit for this gravitational force has the form 
$$
\frac{1}{r} = -\frac{\mu k}{l^2} [1+\epsilon \cos \theta]\notag
$$
 and that the angular momentum is a constant of motion $L = l$. Use these to prove that the attractive force leading to this bound orbit is 
$$
\mathbf{F} = \frac{k}{r^2} \hat{\mathbf{r}}\notag
$$
 where $k$ must be negative.

14. When performing the Rutherford experiment, Gieger and Marsden scattered $7.7$ $MeV$ $^4$He particles (alpha particles) from $^{238}$U at a scattering angle in the laboratory frame of $\theta = 90^{\circ}$. Derive the following observables as measured in the laboratory frame.

    1. The recoil scattering angle of the $^{238}$U in the laboratory frame.

    2. The scattering angles of the $^4$He and $^{238}$U in the center-of-mass frame

    3. The kinetic energies of the $^4$He and $^{238}$U in the laboratory frame

    4. The impact parameter

    5. The distance of closest approach $r_{\text{min}}$

## 11.S: Conservative two-body Central Forces (Summary)

This chapter has focussed on the classical mechanics of bodies interacting via conservative, two-body, central interactions. The following are the main topics presented in this chapter.

### Equivalent one-body representation for two bodies interacting via a central interaction

The equivalent one-body representation of the motion of two bodies interacting via a two-body central interaction greatly simplifies solution of the equations of motion. The position vectors $\mathbf{r}_{1}$ and $\mathbf{r}_{2}$ are expressed in terms of the center-of-mass vector $\mathbf{ R}$ plus total mass $M=m_{1}+m_{2}$ while the position vector $\mathbf{r}$, plus associated reduced mass $\mu =\frac{m_{1}m_{2}}{m_{1}+m_{2}},$ describe the relative motion of the two bodies in the center of mass. The total Lagrangian then separates into two independent parts

$$
L=\frac{1}{2}M\left\vert \mathbf{\dot{R}}\right\vert ^{2}+L_{cm} \tag{11.16} \label{eq-11-16}
$$

where the center-of-mass Lagrangian is

$$
L_{cm}=\frac{1}{2}\mu \left\vert \mathbf{\dot{r}}\right\vert ^{2}-U(r) \tag{11.17} \label{eq-11-17}
$$

Equations $(11.2.8)$, and $(11.2.9)$ can be used to derive the actual spatial trajectories of the two bodies expressed in terms of $\mathbf{r}_{1}$ and $\mathbf{r}_{2}$, from the relative equations of motion, written in terms of $\mathbf{R}$ and $\mathbf{r}$, for the equivalent one-body solution..

### Angular momentum

Noether’s theorem shows that the angular momentum is conserved if only a spherically-symmetric two-body central force acts between the interacting two bodies. The plane of motion is perpendicular to the angular momentum vector and thus the Lagrangian can be expressed in polar coordinates as 
$$
L_{cm}=\frac{1}{2}\mu \left( \dot{r}^{2}+r^{2}\dot{\psi}^{2}\right) -U(r) \tag{11.22} \label{eq-11-22}
$$

### Differential orbit equation of motion

The Binet transformation $u=\frac{1}{r}$ allows the center-of-mass Lagrangian $L_{cm}$ for a central force $\mathbf{F=}f(r)\mathbf{\hat{r}}$ to be used to express the differential orbit equation for the radial motion as

$$
\frac{d^{2}u}{d\psi ^{2}}+u=-\frac{\mu }{l^{2}}\frac{1}{u^{2}}F(\frac{1}{u}) \tag{11.39}
$$

The Lagrangian, and the Hamiltonian all were used to derive the equations of motion for two bodies interacting via a two-body, conservative, central interaction. The general features of the conservation of angular momentum and conservation of energy for a two-body, central potential were presented.

### Inverse-square, two-body, central force

The inverse-square, two-body, central force is of pivotal importance in nature since it is applies to both the gravitational force and the Coulomb force. The underlying symmetries of the inverse-square, two-body, central interaction, lead to conservation of angular momentum, conservation of energy, Gauss’s law, and that the two-body orbits follow closed, degenerate, orbits that are conic sections, for which the eccentricity vector is conserved. The radial dependence, relative to the force center lying at one focus of the conic section, is given by

$$
\frac{1}{r}=-\frac{\mu k}{l^{2}}\left[ 1+\epsilon \cos \left( \psi -\psi _{0}\right) \right] \tag{11.58}
$$

where the orbit eccentricity $\epsilon$ equals

$$
\epsilon =\sqrt{1+\frac{2E_{cm}l^{2}}{\mu k^{2}}} \tag{11.62}
$$

These lead to Kepler’s three laws of motion for two bodies in a bound orbit due to the attractive gravitational force for which $k=-Gm_{1}m_{2}$. The inverse-square law is special in that the eccentricity vector $\mathbf{A}$ is a third invariant of the motion, where

$$
\mathbf{A\equiv }\left( \mathbf{p\times L}\right) \mathbf{+}\left( \mu k \mathbf{ \hat{r}}\right) \tag{11.86}
$$

The eccentricity vector unambiguously defines the orientation and direction of the major axis of the elliptical orbit. The invariance of the eccentricity vector, and the existence of stable closed orbits, are manifestations of the dynamical $04$ symmetry.

### Isotropic, harmonic, two-body, central force

The isotropic, harmonic, two-body, central interaction is of interest since, like the inverse-square law force, it leads to closed elliptical orbits described by

$$
\frac{1}{r^{2}}=\frac{E\mu }{p_{\psi }^{2}}\left( 1+\left( 1+\frac{kp_{\psi }^{2}}{E^{2}\mu }\right) ^{\frac{1}{2}}\cos 2(\psi -\psi _{0})\right) \tag{11.107}
$$

where the eccentricity $\epsilon$ is given by

$$
\left( 1+\frac{kp_{\psi }^{2}}{E^{2}\mu }\right) ^{\frac{1}{2}}=\frac{ \epsilon ^{2}}{2-\epsilon ^{2}} \tag{11.108}
$$

The harmonic force orbits are distinctly different from those for the inverse-square law in that the force center is at the center of the ellipse, rather than at the focus for the inverse-square law force. This elliptical orbit is reflection symmetric for the harmonic force, but not for the inverse square force. The isotropic harmonic two-body force leads to invariance of the symmetry tensor, $\mathbf{A}^{\prime }$ which is an invariant of the motion analogous to the eccentricity vector $\mathbf{A}$. This leads to stable closed orbits, which are manifestations of the dynamical $SU3$ symmetry.

### Orbit stability

Bertrand’s theorem states that only the inverse square law and the linear radial dependences of the central forces lead to stable closed bound orbits that do not precess. These are manifestation of the dynamical symmetries that occur for these two specific radial forms of two-body forces.

### The three-body problem

The difficulties encountered in solving the equations of motion for three bodies, that are interacting via two-body central forces, was discussed. The three-body motion can include the existence of chaotic motion. It was shown that solution of the three-body problem is simplified if either the planar approximation, or the restricted three-body approximation, are applicable.

### Two-body scattering

The total and differential two-body scattering cross sections were introduced. It was shown that for the inverse-square law force there is a simple relation between the impact parameter $b$ and scattering angle $\theta$ given by

$$
b=\frac{k}{2E_{cm}}\cot \frac{\theta }{2} \tag{11.155}
$$

This led to the solution for the differential scattering cross-section for Rutherford scattering due to the Coulomb interaction.

$$
\frac{d\sigma }{d\Omega }=\frac{1}{4}\left( \frac{k}{2E_{cm}}\right) ^{2} \frac{1}{\sin ^{4}\frac{\theta }{2}} \tag{11.159}
$$

This cross section assumes elastic scattering by a repulsive two-body inverse-square central force. For scattering of nuclei in the Coulomb potential the constant $k$ is given to be 
$$
k=\frac{Z_{p}Z_{T}e^{2}}{4\pi \varepsilon _{o}} \tag{11.160}
$$

### Two-body kinematics

The transformation from the center-of-momentum frame to laboratory frames of reference was introduced. Such transformations are used extensively in many fields of physics for theoretical modelling of scattering, and for analysis of experiment data.
