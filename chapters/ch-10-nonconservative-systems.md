---
title: "10. Nonconservative Systems"
short_title: "Chapter 10"
label: ch-10-nonconservative-systems
---


(ch-10)=

# 10. Nonconservative Systems

## 10.1: Introduction to Nonconservative Systems

Hamilton’s action principle, Lagrangian mechanics, and Hamiltonian mechanics, all exploit the concept of action which is a single, invariant, quantity. These algebraic formulations of mechanics all are based on energy, which is a scalar quantity, and thus these formulations are easier to handle than the vector concept of force employed in Newtonian mechanics. Algebraic formulations provide a powerful and elegant approach to understand and develop the equations of motion of systems in nature. Chapters $6 − 9$ applied variational principles to Hamilton’s action principle which led to the Lagrangian, and Hamiltonian formulations that simplify determination of the equations of motion for systems in classical mechanics.

A conservative force has the property that the total work done moving between two points is independent of the taken path. That is, a conservative force is time symmetric and can be expressed in terms of the gradient of a scalar potential $V$. *Hamilton’s action principle implicitly assumes that the system is conservative for those degrees of freedom that are built into the definition of the action, and the related Lagrangian, and Hamiltonian.* The focus of this chapter is to discuss the origins of nonconservative motion and how it can be handled in algebraic mechanics.

## 10.2: Origins of Nonconservative Motion

Nonconservative degrees of freedom involve irreversible processes, such as dissipation, damping, and also can result from course-graining, or ignoring coupling to active degrees of freedom. The nonconservative role of ignored active degrees of freedom is illustrated by the weakly-coupled double harmonic oscillator system discussed below. Let the two harmonic oscillators have masses $(m_{1},m_{2}),$ uncoupled angular frequencies $(\omega _{1},\omega _{2})\,$, and oscillation amplitudes $(q_{1},q_{2})$. Assume that the coupling potential energy is $U=\lambda q_{1}q_{2}.$ The Lagrangian for this weakly-coupled double oscillator is

$$
L(q_{1,}q_{2},\dot{q}_{1},\dot{q}_{2},t)=\frac{m_{1}}{2}\left( \dot{q} _{1}^{2}-\omega _{1}^{2}q_{1}^{2}\right) +\lambda q_{1}q_{2}+\frac{m_{2}}{2} \left( \dot{q}_{2}^{2}-\omega _{2}^{2}q_{2}^{2}\right)
$$

Note that the total Lagrangian is conservative since the Lagrangian is explicitly time independent. As shown in chapter $14.2,$ the solution for the amplitudes of the oscillation for the coupled system are given by

$$
\begin{aligned} q_{1}\left( t\right) &=&D\sin \left[ \left( \frac{\omega _{1}+\omega _{2}}{2} \right) t\right] \sin \left[ \left( \frac{\omega _{1}-\omega _{2}}{2}\right) t\right] \\ q_{2}\left( t\right) &=&D\cos \left[ \left( \frac{\omega _{1}+\omega _{2}}{2} \right) t\right] \cos \left[ \left( \frac{\omega _{1}-\omega _{2}}{2}\right) t\right]\end{aligned}
$$

The system exhibits the common "beats" behavior where the coupled harmonic oscillators have an angular frequency that is the average oscillator frequency $\omega _{average}=\left( \frac{\omega _{1}+\omega _{2}}{2}\right) ,$ and the oscillation intensities are modulated at the difference frequency, $\omega _{difference}=\left( \frac{\omega _{1}-\omega _{2}}{2} \right) .$ Although the total energy is conserved for this conservative system, this shared energy flows back and forth between the two coupled harmonic oscillators at the difference frequency. If the equations of motion for oscillator $1$ ignore the coupling to the motion of oscillator $2$, that is, assume a constant average value $q_{2}=\left\langle q_{2}\right\rangle$ is used, then the intensity $\left\vert q_{1}\right\vert ^{2}$ and energy of the first oscillator still is modulated by the $\left\vert \sin \left( \frac{ \omega _{1}-\omega _{2}}{2}\right) t\right\vert ^{2}$ term. Thus the total energy for this truncated coupled-oscillator system is no longer conserved due to neglect of the energy flowing into and out of oscillator $1$ due to its coupling to oscillator $2$. That is, the solution for the truncated system of oscillator $1$ is not conservative since it is exchanging energy with the coupled, but ignored, second oscillator. This elementary example illustrates that ignoring active degrees of freedom can transform a conservative system into a nonconservative system, for which the equations of motion derived using the truncated Lagrangian is incorrect.

The above example illustrates the importance of including all active degrees of freedom when deriving the equations of motion, in order to ensure that the total system is conservative. Unfortunately, nonconservative systems due to viscous or frictional dissipation typically result from weak thermal interactions with an enormous number of nearby atoms, which makes inclusion of all of these degrees of freedom impractical. Even though the detailed behavior of such dissipative degrees of freedom may not be of direct interest, all the active degrees of freedom must be included when applying Lagrangian or Hamiltonian mechanics.

## 10.3: Algebraic Mechanics for Nonconservative Systems

Since Lagrangian and Hamiltonian formulations are invalid for the nonconservative degrees of freedom, the following three approaches are used to include nonconservative degrees of freedom directly in the Lagrangian and Hamiltonian formulations of mechanics.

1. Expand the number of degrees of freedom used to include all active degrees of freedom for the system, so that the expanded system is conservative. This is the preferred approach when it is viable. Hamilton’s action principle based on initial conditions, introduced in chapter $9.2.4$, doubles the number of degrees of freedom, which can be used to account for the dissipative forces providing one approach to solve nonconservative systems. However, this approach typically is impractical for handling dissipated processes because of the large number of degrees of freedom that are involved in thermal dissipation.

2. Nonconservative forces can be introduced directly at the equations of motion stage as generalized forces $Q_{j}^{EXC}$. This approach is used extensively. For the case of linear velocity dependence, the Rayleigh’s dissipation function provides an elegant and powerful way to express the generalized forces in terms of scalar potential energies.

3. New degrees of freedom or effective forces can be postulated that are then incorporated into the Lagrangian or the Hamiltonian in order to mimic the effects of the nonconservative forces.

Examples that exploit the above three ways to introduce nonconservative dissipative forces in algebraic formulations are given below.

## 10.4: Rayleigh’s Dissipation Function

As mentioned above, nonconservative systems involving viscous or frictional dissipation, typically result from weak thermal interactions with many nearby atoms, making it impractical to include a complete set of active degrees of freedom. In addition, dissipative systems usually involve complicated dependences on the velocity and surface properties that are best handled by including the dissipative drag force explicitly as a generalized drag force in the Euler-Lagrange equations. The drag force can have any functional dependence on velocity, position, or time.

$$
\mathbf{F}^{drag}=-f(\mathbf{\dot{q}},\mathbf{q},t)\mathbf{\hat{v}}
$$

Note that since the drag force is dissipative the dominant component of the drag force must point in the opposite direction to the velocity vector.

In $1881$ Lord Rayleigh showed that if a dissipative force $\mathbf{F}$ depends linearly on velocity, it can be expressed in terms of a scalar potential functional of the generalized coordinates called the *Rayleigh dissipation function* $\mathcal{R(}\mathbf{\dot{q})}$. **The Rayleigh dissipation function is an elegant way to include linear velocity-dependent dissipative forces in both Lagrangian and Hamiltonian mechanics, as is illustrated below for both Lagrangian and Hamiltonian mechanics.

### Generalized dissipative forces for linear velocity dependence

Consider $n$ equations of motion for the $n$ degrees of freedom, and assume that the dissipation depends linearly on velocity. Then, allowing all possible cross coupling of the equations of motion for $q_{j},$ the equations of motion can be written in the form

$$
\sum_{i=1}^{n}\left[ m_{ij} \ddot{q}_{j}+b_{ij}\dot{q}_{j}+c_{ij}q_{j}-Q_{i}(t)\right] =0 \tag{10.5} \label{eq-10-5}
$$

Multiplying Equation [10.5](#eq-10-5) by $\dot{q}_{i}$, take the time integral, and sum over $i,j$, gives the following energy equation 
$$
\sum_{i=1}^{n}\sum_{j=1}^{n}\int_{0}^{t}m_{ij}\ddot{q}_{j}\dot{q} _{i}dt+\sum_{i=1}^{n}\sum_{j=1}^{n}\int_{0}^{t}b_{ij}\dot{q}_{j}\dot{q} _{i}dt+\sum_{i=1}^{n}\sum_{j=1}^{n}\int_{0}^{t}c_{ij}q_{j}\dot{q} _{i}dt=\sum_{i}^{n}\int_{0}^{t}Q_{i}(t)\dot{q}_{i}dt
$$

The right-hand term is the total energy supplied to the system by the external generalized forces $Q_{i}(t)$ at the time $t$. The first time-integral term on the left-hand side is the total kinetic energy, while the third time-integral term equals the potential energy. The second integral term on the left is defined to equal $2\mathcal{R}(\mathbf{\dot{q}} )$ where Rayeigh’s dissipation function $\mathcal{R}(\mathbf{\dot{q}})$ is defined as

$$
\mathcal{R}(\mathbf{ \dot{q}})\mathcal{\equiv }\frac{1}{2}\sum_{i=1}^{n}\sum_{j=1}^{n}b_{ij}\dot{q }_{i}\dot{q}_{j}
$$

and the summations are over all $n$ particles of the system. This definition allows for complicated cross-coupling effects between the $n$ particles.

The particle-particle coupling effects usually can be neglected allowing use of the simpler definition that includes only the diagonal terms. Then the diagonal form of the Rayleigh dissipation function simplifies to

$$
\mathcal{R}(\mathbf{\dot{q}})\mathcal{\equiv }\frac{1}{2}\sum_{i=1}^{n}b_{i} \dot{q}_{i}^{2}
$$

Therefore the frictional force in the $q_{i}$ direction depends linearly on velocity $\dot{q}_{i}$, that is

$$
F_{q_{i}}^{f}=-\frac{\partial \mathcal{R}(\mathbf{\dot{q}})}{\partial \dot{q} _{i}}=-b_{i}\dot{q}_{i}
$$

In general, the dissipative force is the velocity gradient of the Rayleigh dissipation function, 
$$
\mathbf{F}^{f}=-\nabla _{\mathbf{\dot{q}}}\mathcal{R}(\mathbf{\dot{q}})
$$

The physical significance of the Rayleigh dissipation function is illustrated by calculating the work done by one particle $i$ *against* friction, which is

$$
dW_{i}^{f}=-\mathbf{F}_{i}^{f}\cdot d\mathbf{r=-F}_{i}^{f}\cdot \mathbf{\dot{ q}}_{i}dt=b_{i}\dot{q}_{i}^{2}dt
$$
 Therefore

$$
2\mathcal{R}(\mathbf{\dot{q}})\mathcal{=}\frac{dW^{f}}{dt}
$$

which is the rate of energy (power) loss due to the dissipative forces involved. The same relation is obtained after summing over all the particles involved.

Transforming the frictional force into generalized coordinates requires equation $(6.3.10)$

$$
\mathbf{\dot{r}}_{i}\mathbf{=}\sum_{k}\frac{\partial \mathbf{r}_{i}}{ \partial q_{k}}\dot{q}_{k}+\frac{\partial \mathbf{r}_{i}}{\partial t}
$$

Note that the derivative with respect to $\dot{q}_{k}$ equals

$$
\frac{\partial \mathbf{\dot{r}}_{i}}{\partial \dot{q}_{j}}=\frac{\partial \mathbf{r}_{i}}{\partial q_{j}}
$$

Using equations $(6.3.11)$ and $7.3.12$, the $j$ component of the generalized frictional force $Q_{j}^{f}$ is given by 
$$
Q_{j}^{f}=\sum_{i=1}^{n}\mathbf{F}_{i}^{f}\cdot \frac{\partial \mathbf{r}_{i} }{\partial q_{j}}=\sum_{i=1}^{n}\mathbf{F}_{i}^{f}\cdot \frac{\partial \mathbf{\dot{r}}_{i}}{\partial \dot{q}_{j}}=-\sum_{i=1}^{n}\nabla _{v_{i}} \mathcal{R}(\mathbf{\dot{q}})\cdot \frac{\partial \mathbf{\dot{r}}_{i}}{ \partial \dot{q}_{j}}=-\frac{\partial \mathcal{R}(\mathbf{\dot{q}})}{ \partial \dot{q}_{j}}\tag{10.15} \label{eq-10-15}
$$

Equation [10.15](#eq-10-15) provides an elegant expression for the generalized dissipative force $Q_{j}^{f}$ in terms of the Rayleigh’s scalar dissipation potential $\mathcal{R}$.

### Generalized dissipative forces for nonlinear velocity dependence

The above discussion of the Rayleigh dissipation function was restricted to the special case of linear velocity-dependent dissipation. Virga[Vir15] proposed that the scope of the classical Rayleigh-Lagrange formalism can be extended to include nonlinear velocity dependent dissipation by assuming that the nonconservative dissipative forces are defined by

$$
\mathbf{F}_{i}^{f}=-\frac{\partial R(\mathbf{q},\mathbf{\dot{q}})}{\partial \mathbf{\dot{q}}}
$$

where the generalized Rayleigh dissipation function $\mathcal{R(}\mathbf{q}, \mathbf{\dot{q}})$ satisfies the general Lagrange mechanics relation

$$
\frac{\delta L}{\delta q}-\frac{\partial R}{\partial \dot{q}}=0
$$

This generalized Rayleigh’s dissipation function eliminates the prior restriction to linear dissipation processes, which greatly expands the range of validity for using Rayleigh’s dissipation function.

### Lagrange equations of motion

Linear dissipative forces can be directly, and elegantly, included in Lagrangian mechanics by using Rayleigh’s dissipation function as a generalized force $Q_{j}^{f}$. Inserting Rayleigh dissipation function [10.15](#eq-10-15) in the generalized Lagrange equations of motion $(6.5.12)$ gives

$$
\left\{ \frac{d}{dt}\left( \frac{\partial L}{\partial \dot{q}_{j}}\right) - \frac{\partial L}{\partial q_{j}}\right\} =\left[ \sum_{k=1}^{m}\lambda _{k} \frac{\partial g_{k}}{\partial q_{j}}(\mathbf{q},t)+Q_{j}^{EXC}\right] - \frac{\partial \mathcal{R(}\mathbf{q},\mathbf{\dot{q}})}{\partial \dot{q}_{j} }\tag{10.18} \label{eq-10-18}
$$

where $Q_{j}^{EXC}$ corresponds to the generalized forces remaining after removal of the generalized linear, velocity-dependent, frictional force $Q_{j}^{f}$.

The holonomic forces of constraint are absorbed into the Lagrange multiplier term.

### Hamiltonian mechanics

If the nonconservative forces depend linearly on velocity, and are derivable from Rayleigh’s dissipation function according to Equation [10.15](#eq-10-15), then using the definition of generalized momentum gives

$$
\begin{align} \dot{p}_{i} &=&\frac{d}{dt}\frac{\partial L}{\partial \dot{q}_{j}}=\frac{ \partial L}{\partial q_{i}}+\left[ \sum_{k=1}^{m}\lambda _{k}\frac{\partial g_{k}}{\partial q_{j}}(\mathbf{q},t)+Q_{j}^{EXC}\right] -\frac{\partial \mathcal{R(}\mathbf{q},\mathbf{\dot{q}})}{\partial \dot{q}_{j}} \\ \dot{p}_{i} &=&-\frac{\partial H(\mathbf{p,q},t\mathbf{)}}{\partial q_{i}}+ \left[ \sum_{k=1}^{m}\lambda _{k}\frac{\partial g_{k}}{\partial q_{j}}( \mathbf{q},t)+Q_{j}^{EXC}\right] -\frac{\partial \mathcal{R(}\mathbf{q}, \mathbf{\dot{q}})}{\partial \dot{q}_{j}}\end{align}
$$

Thus Hamilton’s equations become

$$
\begin{align} \dot{q}_{i} &=&\frac{\partial H}{\partial p_{i}} \\ \dot{p}_{i} &=&-\frac{\partial H}{\partial q_{i}}+\left[ \sum_{k=1}^{m} \lambda _{k}\frac{\partial g_{k}}{\partial q_{j}}(\mathbf{q},t)+Q_{j}^{EXC} \right] -\frac{\partial \mathcal{R(}\mathbf{q},\mathbf{\dot{q}})}{\partial \dot{q}_{j}}\end{align}
$$

The Rayleigh dissipation function $\mathcal{R(}\mathbf{q},\mathbf{\dot{q}})$ provides an elegant and convenient way to account for dissipative forces in both Lagrangian and Hamiltonian mechanics.

::::{admonition} Example 10.4.1: Driven, Linearly-Damped, Coupled Linear Oscillators
:class: example

Consider the two identical, linearly damped, coupled oscillators (damping constant $\beta$) shown in the figure.

:::{figure} ../images/lt-21615-imageedit_1_4324574508.png
:label: fig-10-4-1
:enumerator: 10.4.1
:alt: Harmonically-driven, linearly-damped, coupled linear oscillators.

Harmonically-driven, linearly-damped, coupled linear oscillators.
:::

A periodic force $F=F_{0}\cos (\omega t)$ is applied to the left-hand mass $m$. The kinetic energy of the system is

$$
T=\frac{1}{2}m(\dot{x}_{1}^{2}+\dot{x}_{2}^{2})\nonumber
$$
 The potential energy is

$$
U=\frac{1}{2}\kappa x_{1}^{2}+\frac{1}{2}\kappa x_{2}^{2}+\frac{1}{2}\kappa ^{\prime }\left( x_{2}-x_{1}\right) ^{2}=\frac{1}{2}\left( \kappa +\kappa ^{\prime }\right) x_{1}^{2}+\frac{1}{2}\left( \kappa +\kappa ^{\prime }\right) x_{2}^{2}-\kappa ^{\prime }x_{1}x_{2} \notag
$$

Thus the Lagrangian equals 
$$
L=\frac{1}{2}m(\dot{x}_{1}^{2}+\dot{x}_2^{2})-\left[ \frac{1}{2} ( \kappa +\kappa^{\prime } ) x_{1}^{2}+\frac{1}{2} ( \kappa +\kappa^{\prime } ) x_{2}^{2}-\kappa^{\prime }x_{1}x_{2}\right]\nonumber
$$

Since the damping is linear, it is possible to use the Rayleigh dissipation function

$$
\mathcal{R=}\frac{1}{2}\beta (\dot{x}_{1}^{2}+\dot{x}_{2}^{2})\nonumber
$$

The applied generalized forces are

$$
Q_{1}^{\prime }=F_{o}\cos \left( \omega t\right) \hspace{1in}Q_{2}^{\prime }=0\nonumber
$$

Use the Euler-Lagrange equations [10.18](#eq-10-18) to derive the equations of motion

$$
\left\{ \frac{d}{dt}\left( \frac{\partial L}{\partial \dot{q}_{j}}\right) - \frac{\partial L}{\partial q_{j}}\right\} +\frac{\partial \mathcal{F}}{ \partial \dot{q}_{j}}=Q_{j}^{\prime }+\sum_{k=1}^{m}\lambda _{k}\frac{ \partial g_{k}}{\partial q_{j}}(\mathbf{q},t)\nonumber
$$
 gives 
$$
\begin{aligned} m\ddot{x}_{1}+\beta \dot{x}_{1}+(\kappa +\kappa ^{\prime })x_{1}-\kappa ^{\prime }x_{2} &=&F_{0}\cos \left( \omega t\right) \\ m\ddot{x}_{2}+\beta \dot{x}_{2}+(\kappa +\kappa ^{\prime })x_{2}-\kappa ^{\prime }x_{1} &=&0\end{aligned}
$$

These two coupled equations can be decoupled and simplified by making a transformation to normal coordinates, $\eta _{1},\eta _{2}$ where

$$
\eta _{1}=x_{1}-x_{2}\hspace{1in}\eta _{2}=x_{1}+x_{2}\nonumber
$$

Thus 
$$
x_{1}=\frac{1}{2}(\eta _{1}+\eta _{2})\hspace{1in}x_{2}=\frac{1}{2}(\eta _{2}-\eta _{1})\nonumber
$$

Insert these into the equations of motion gives

$$
\begin{aligned} m(\ddot{\eta}_{1}+\ddot{\eta}_{2})+\beta (\dot{\eta}_{1}+\dot{\eta} _{2})+(\kappa +\kappa ^{\prime })(\eta _{1}+\eta _{2})-\kappa ^{\prime }(\eta _{2}-\eta _{1}) &=&2F_{0}\cos \left( \omega t\right) \\ m(\eta _{2}-\eta _{1})+\beta (\eta _{2}-\eta _{1})+(\kappa +\kappa ^{\prime })(\eta _{2}-\eta _{1})-\kappa ^{\prime }(\eta _{1}+\eta _{2}) &=&0\end{aligned}
$$

Add and subtract these two equations gives the following two decoupled equations

$$
\begin{aligned} \ddot{\eta}_{1}+\frac{\beta }{m}\dot{\eta}_{1}+\frac{\left( \kappa +2\kappa ^{\prime }\right) }{m}\eta _{1} &=&\frac{F_{0}}{m}\cos \left( \omega t\right) \\ \ddot{\eta}_{2}+\frac{\beta }{m}\dot{\eta}_{2}+\frac{\kappa }{m}\eta _{2} &=& \frac{F_{0}}{m}\cos \left( \omega t\right)\end{aligned}
$$

Define $\Gamma =\frac{\beta }{m},\omega _{1}=\sqrt{\frac{\left( \kappa +2\kappa ^{\prime }\right) }{m}},\omega _{2}=\sqrt{\frac{\kappa }{m}} ,A=\frac{F_{0}}{m}$. Then the two independent equations of motion become

$$
\ddot{\eta}_{1}+\Gamma \dot{\eta}_{1}+\omega _{1}^{2}\eta _{1}=A\cos \left( \omega t\right) \hspace{1in}\ddot{\eta}_{2}+\Gamma \dot{\eta}_{2}+\omega _{2}^{2}\eta _{2}=A\cos \left( \omega t\right)\nonumber
$$

This solution is a superposition of two independent, linearly-damped, driven normal modes $\eta _{1}$ and $\eta _{2}$ that have different natural frequencies $\omega _{1}$ and $\omega _{2}$. For weak damping these two driven normal modes each undergo damped oscillatory motion with the $\eta _{1}$ and $\eta _{2}$ normal modes exhibiting resonances at $\omega _{1}^{\prime }=\sqrt{\omega _{1}^{2}-2\left( \frac{\Gamma }{2}\right) ^{2}}$ and $\omega _{2}^{\prime }=\sqrt{\omega _{2}^{2}-2\left( \frac{ \Gamma }{2}\right) ^{2}}$
::::

::::{admonition} Example 10.4.2: Kirchhoff’s Rules for Electrical Circuits
:class: example

The mathematical equations governing the behavior of mechanical systems and $LRC$ electrical circuits have a close similarity. Thus variational methods can be used to derive the analogous behavior for electrical circuits. For example, for a system of $n$ separate circuits, the magnetic flux $\Phi _{ik \text{ }}$through circuit $i,$ due to electrical current $I_{k}=\dot{q}_{k}$ flowing in circuit $k,$ is given by

$$
\Phi _{ik}=M_{ik}\dot{q}_{k}\nonumber
$$

where $M_{ik}$ is the mutual inductance. The diagonal term $M_{ii}=L_{i}$ corresponds to the self inductance of circuit $i$. The net magnetic flux $\Phi _{i}$ through circuit $i,$ due to all $n$ circuits, is the sum

$$
\Phi _{i}=\sum_{k=1}^{n}M_{ik}\dot{q}_{k}\nonumber
$$

Thus the total magnetic energy $W_{mag},$which is analogous to kinetic energy $T,$ is given by summing over all $n$ circuits to be 
$$
W_{mag}=T=\frac{1}{2}\sum_{i=1}^{n}\sum_{k=1}^{n}M_{ik}\dot{q}_{i}\dot{q}_{k}\nonumber
$$

Similarly the electrical energy $W_{elect}$ stored in the mutual capacitance $C_{ik}$ between the $n$ circuits, which is analogous to potential energy, $U,$ is given by

$$
W_{elect}=U=\frac{1}{2}\sum_{i=1}^{n}\sum_{k=1}^{n}\frac{q_{i}q_{k}}{C_{ik}}\nonumber
$$

Thus the standard Lagrangian for this electric system is given by

$$
L=T-U=\frac{1}{2}\sum_{i=1}^{n}\sum_{k=1}^{n}\left[ M_{ik}\dot{q}_{i}\dot{q} _{k}-\frac{q_{i}q_{k}}{C_{ik}}\right] \tag{$\alpha $} \label{eq-10-alpha}
$$

Assuming that Ohm’s Law is obeyed, that is, the dissipation force depends linearly on velocity, then the Rayleigh dissipation function can be written in the form

$$
\mathcal{R\equiv }\frac{1}{2}\sum_{i=1}^{n}\sum_{k=1}^{n}R_{ik}\dot{q}_{i} \dot{q}_{k} \tag{$\beta $} \label{eq-10-beta}
$$

where $R_{ik}$ is the resistance matrix. Thus the dissipation force, expressed in volts, is given by

$$
F_{i}=-\frac{\partial \mathcal{R}}{\partial \dot{q}_{j}}=\frac{1}{2} \sum_{k=1}^{n}R_{ik}\dot{q}_{k} \label{eq-10-gamma} \tag{$\gamma $}
$$

Inserting equations [alpha](#eq-10-alpha), [beta](#eq-10-beta), and [gamma](#eq-10-gamma) into Equation [10.18](#eq-10-18), plus making the assumption that an additional generalized electrical force $Q_{i}=\xi _{i}(t)$ volts is acting on circuit $i,$ then the Euler-Lagrange equations give the following equations of motion.

$$
\sum_{k=1}^{n}\left[ M_{ik}\ddot{q}_{k}+R_{ik}\dot{q}_{k}+\frac{q_{k}}{C_{ik} }\right] =\xi _{i}(t)\nonumber
$$

This is a generalized version of Kirchhoff’s loop rule which can be seen by considering the case where the diagonal term $i=k$ is the only non-zero term. Then

$$
\left[ M_{ii}\ddot{q}_{i}+R_{ii}\dot{q}_{i}+\frac{q_{i}}{C_{ii}}\right] =\xi _{i}(t)\nonumber
$$

This sum of the voltages is identical to the usual expression for Kirchhoff’s loop rule. This example illustrates the power of variational methods when applied to fields beyond classical mechanics.
::::

## 10.5: Dissipative Lagrangians

The prior discussion of nonconservative systems mentioned the following three ways to incorporate dissipative processes into Lagrangian or Hamiltonian mechanics.

1. Expand the number of degrees of freedom to include all the active dissipative active degrees of freedom as well as the conservative ones.

2. Use generalized forces to incorporate dissipative processes.

3. Add dissipative terms to the Lagrangian or Hamiltonian to mimic dissipation.

The following illustrates the use of dissipative Lagrangians.

Bateman pointed out that an isolated dissipative system is physically incomplete, that is, a complete system must comprise at least two coupled subsystems where energy is transferred from a dissipating subsystem to an absorbing subsystem. A complete system should comprise both the dissipating and absorbing systems to ensure that the total system Lagrangian and Hamiltonian are conserved, as is assumed in conventional Lagrangian and Hamiltonian mechanics. Both Bateman and Dekker have illustrated that the equations of motion for a linearly-damped, free, one-dimensional harmonic oscillator are derivable using the Hamilton variational principle via introduction of a fictitious complementary subsystem that mimics dissipative processes. The following example illustrate that deriving the equations of motion for the linearly-damped, linear oscillator may be handled by three alternative equivalent non-standard Lagrangians that assume either: (1) a multidimensional system, (2) explicit time dependent Lagrangians and Hamiltonians, or (3) complex non-standard Lagrangians.

::::{admonition} Example 10.5.1: The linearly-damped, linear oscillator
:class: example

Three toy dynamical models have been used to describe the linearly-damped, linear oscillator employing very different non-standard Lagrangians to generate the required Hamiltonians, and to derive the correct equations of motion.

### 1: Dual-component Lagrangian: $L_{Dual}$

Bateman proposed a dual system comprising a mass $m$ subject to two coupled one-dimensional variables $(x,y)$ where $x$ is the observed variable and $y$ is the mirror variable for the subsystem that absorbs the energy dissipated by the subsystem $x$.

Assume a non-standard Lagrangian of the form

$$
L_{Dual}=\frac{m}{2}\left[ \dot{x}\dot{y}-\frac{\Gamma }{2}\left[ y\dot{x}-x \dot{y}\right] -\omega _{0}^{2}xy\right] \tag{$a$}
$$

where $\Gamma =\frac{\lambda }{m}$ is the damping coefficient. Minimizing by variation of the auxiliary variable $y$, that is, $\Lambda _{y}L=0$, leads to the uncoupled equation of motion for $x$

$$
\frac{m}{2}\left[ \ddot{x}+\Gamma \dot{x}+\omega _{0}^{2}x\right] =0 \tag{$b$}\label{eq-10-b1}
$$

Similarly minimizing by variation of the primary variable $x,$ that is $\Lambda _{x}L=0,$ leads to the uncoupled equation of motion for $y\qquad$

$$
\frac{m}{2}\left[ \ddot{y}-\Gamma \dot{y}+\omega _{0}^{2}y\right] =0 \tag{$c$}\label{eq-10-c1}
$$

Note that equation of motion [b1](#eq-10-b1), which was obtained by variation of the auxiliary variable $y,$ corresponds to that for the usual free, linearly-damped, one-dimensional harmonic oscillator for the $x$ variable which dissipates energy as is discussed in chapter $3.5$. The equation of motion [c1](#eq-10-c1) is obtained by variation of the primary variable $x$ and corresponds to a free linear, one-dimensional, oscillator for the $y$ variable that is absorbing the energy dissipated by the dissipating $x$ system.

The generalized momenta,

$$
p_{i}\equiv \frac{\partial L}{\partial \dot{q}_{i}}\nonumber
$$

can be used to derive the corresponding Hamiltonian

$$
\begin{align} H_{Dual}(x,p_{x},y,p_{y}) &=\left[ p_{x}\dot{x}+p_{y}\dot{y}-L\right] \nonumber\\[4pt] &=\frac{ p_{x}p_{y}}{2m}-\frac{\Gamma }{2}\left[ xp_{x}-yp_{y}\right] +\frac{m}{2} \left( \omega _{0}^{2}-\left( \frac{\Gamma }{2}\right) ^{2}\right) xy \tag{$d$} \end{align}
$$

Note that this Hamiltonian is time independent, and thus is conserved for this complete dual-variable system. Using Hamilton’s equations of motion gives the same two uncoupled equations of motion as obtained using the Lagrangian, i.e. [b1](#eq-10-b1) and [c1](#eq-10-c1).

### 2: Time-dependent Lagrangian: $L_{Damped}$

The complementary subsystem of the above dual-component Lagrangian, that is added to the primary dissipative subsystem, is the adjoint to the equations for the primary subsystem of interest. In some cases, a set of the solutions of the complementary equations can be expressed in terms of the solutions of the primary subsystem allowing the equations of motion to be expressed solely in terms of the variables of the primary subsystem. Inspection of the solutions of the damped harmonic oscillator, presented in chapter $3.5$, implies that $x$ and $y$ must be related by the function

$$
y=xe^{\Gamma t} \tag{$e$}
$$

Therefore Bateman proposed a time-dependent, non-standard Lagrangian $L_{Damped}$ of the form

$$
L_{Damped}=\frac{m}{2}e^{\Gamma t}\left[ \dot{x}^{2}-\omega _{0}^{2}x^{2} \right] \tag{$f$}
$$
 This Lagrangian $L_{Dampes}$ corresponds to a harmonic oscillator for which the mass $m=m_{0}e^{\Gamma t}\$is accreting exponentially with time in order to mimic the exponential energy dissipation. Use of this Lagrangian in the Euler-Lagrange equations gives the solution

$$
me^{\Gamma t}\left[ \ddot{x}+\Gamma \dot{x}+\omega _{0}^{2}x\right] =0 \tag{$g$}
$$

If the factor outside of the bracket is non-zero, then the equation in the bracket must be zero. The expression in the bracket is the required equation of motion for the linearly-damped linear oscillator. This Lagrangian generates a generalized momentum of

$$
p_{x}=me^{\Gamma t}\dot{x}\notag
$$

and the Hamiltonian is

$$
H_{Damped}=p_{x}\dot{x}-L_{2}=\frac{p_{x}^{2}}{2m}e^{-\Gamma t}+\frac{m}{2} \omega _{0}^{2}e^{\Gamma t}x^{2} \tag{$h$}
$$

The Hamiltonian is time dependent as expected. This leads to Hamilton’s equations of motion

$$
\begin{align} \dot{x} &=\frac{\partial H_{Damped}}{\partial p_{x}}=\frac{p_{x}}{m} e^{-\Gamma t} \tag{$i$} \\[4pt] -\dot{p}_{x} &= \frac{\partial H_{Damped}}{\partial x}=m\omega _{0}^{2}e^{\Gamma t}x \tag{$j$}\end{align}
$$

Take the total time derivative of equation $h$ and use equation $i$ to substitute for $\dot{p}_{x}$ gives

$$
me^{\Gamma t}\left[ \ddot{x}+\Gamma \dot{x}+\omega _{0}^{2}x\right] =0 \tag{$k$}
$$

If the term $me^{\Gamma t}$ is non-zero, then the term in brackets is zero. The term in the bracket is the usual equation of motion for the linearly-damped harmonic oscillator.

### 3: Complex Lagrangian: $L_{Complex}$

Dekker proposed use of complex dynamical variables for solving the linearly-damped harmonic oscillator. It exploits the fact that, in principle, each second order differential equation can be expressed in terms of a set of first-order differential equations. This feature is the essential difference between Lagrangian and Hamiltonian mechanics. Let $q$ be complex and assume it can be expressed in the form of a real variable $x$ as

$$
q=\dot{x}-\left( i\omega +\frac{\Gamma }{2}\right) x \tag{$l$}
$$

Substituting this complex variable into the relation

$$
\dot{q}+\left[ i\omega +\frac{\Gamma }{2}\right] q=0 \tag{$m$}\label{eq-10-m}
$$

leads to the second-order equation for the real variable $x$ of

$$
\ddot{x}+\Gamma \dot{x}+\omega _{0}^{2}=0 \tag{$n$}\label{eq-10-n}
$$

This is the desired equation of motion for the linearly-damped harmonic oscillator. This result also can be shown by taking the time derivative of Equation \text{(m)} and taking only the real part, i.e.

$$
\ddot{q}+i\omega \dot{q}+\frac{\Gamma }{2}\dot{q}=\ddot{q}+\left( i\omega - \frac{\Gamma }{2}\right) \dot{q}+\Gamma \dot{q}=\ddot{q}+\Gamma \dot{q} +\omega _{0}^{2}x=0 \tag{$o$}
$$

This feature is exploited using the following Lagrangian

$$
L_{Complex}=\frac{i}{2}\left( q^{\ast }\dot{q}-q\dot{q}^{\ast }\right) - \left[ \omega -i\frac{\Gamma }{2}\right] q^{\ast }q \tag{$p$}
$$

where $\omega ^{2}\equiv \omega _{0}^{2}-\left( \frac{\Gamma }{2} \right) ^{2}$. The Lagrangian $L_{Complex}$ is real for a conservative system and complex for a dissipative system. Using the Lagrange-Euler equation for variation of $q^{\ast }$, that is, $\Lambda _{q^{\ast }}L_{Complex}=0$, gives Equation \text{(m)} which leads to the required equation of motion \text{(n)}.

The canonical conjugate momenta are given by

$$
p=\frac{\partial L_{Complex}}{\partial \dot{q}} \tilde{p}= \frac{\partial L_{Complex}}{\partial \dot{q}^{\ast }} \tag{$q$}
$$

The above Lagrangian plus canonically conjugate momenta lead to the complimentary Hamiltonians

$$
\begin{align} H_{Complex}(p,q,\tilde{p},q^{\ast }) &=\left( i\omega +\frac{\Gamma }{2} \right) \left( \tilde{p}_{^{\ast }}q^{\ast }-pq\right) \tag{$s$} \\[4pt] \tilde{H}_{Complex}(p,q,\tilde{p},q^{\ast }) &=\left( i\omega -\frac{\Gamma }{2}\right) \left( \tilde{p}_{^{\ast }}q^{\ast }-pq\right) \tag{$r$}\end{align}
$$

These Hamiltonians give Hamilton equations of motion that lead to the correct equations of motion for $q$ and $q^{\ast }$
::::

The above examples have shown that three very different, non-standard, Lagrangians, plus their corresponding Hamiltonians, all lead to the correct equation of motion for the linearly-damped harmonic oscillator. This illustrates the power of using non-standard Lagrangians to describe dissipative motion in classical mechanics. However, postulating non-standard Lagrangians to produce the required equations of motion appears to be of questionable usefulness. A fundamental approach is needed to build a firm foundation upon which non-standard Lagrangian mechanics can be based. Non-standard Lagrangian mechanics remains an active, albeit narrow, frontier of classical mechanics

## 10.S: Nonconservative systems (Summary)

Dissipative drag forces are non-conservative and usually are velocity dependent. Chapter $4$ showed that the motion of non-linear dissipative dynamical systems can be highly sensitive to the initial conditions and can lead to chaotic motion.

### Algebraic mechanics for nonconservative systems

Since Lagrangian and Hamiltonian formulations are invalid for the nonconservative degrees of freedom, the following three approaches are used to include nonconservative degrees of freedom directly in the Lagrangian and Hamiltonian formulations of mechanics.

1. Expand the number of degrees of freedom used to include all active degrees of freedom for the system, so that the expanded system is conservative. This is the preferred approach when it is viable. Unfortunately this approach typically is impractical for handling dissipated processes because of the large number of degrees of freedom that are involved in thermal dissipation.

2. Nonconservative forces can be introduced directly at the equations of motion stage as generalized forces $Q_{j}^{EXC}$. This approach is used extensively. For the case of linear velocity dependence, the Rayleigh’s dissipation function provides an elegant and powerful way to express the generalized forces in terms of scalar potential energies.

3. New degrees of freedom or effective forces can be postulated that are then incorporated into the Lagrangian or the Hamiltonian in order to mimic the effects of the nonconservative forces.

### Rayleigh’s Dissipation Function

Generalized dissipative forces that have a linear velocity dependence can be easily handled in Lagrangian or Hamiltonian mechanics by introducing the powerful Rayleigh’s dissipation function $\mathcal{R}(\mathbf{ \dot{q}})$ where

$$
\mathcal{R}(\mathbf{\dot{q}})\mathcal{\equiv }\frac{1}{2}\sum_{i=1}^{n} \sum_{j=1}^{n}b_{ij}\dot{q}_{i}\dot{q}_{j} \tag{10.7} \label{eq-10-7}
$$

This approach is used extensively in physics. This approach has been generalized by defining a linear velocity dependent Rayleigh dissipation function

$$
\mathbf{F}_{i}^{f}=-\frac{\partial R(\mathbf{q},\mathbf{\dot{q}})}{\partial \mathbf{\dot{q}}} \tag{10.16} \label{eq-10-16}
$$

where the generalized Rayleigh dissipation function $\mathcal{R(}\mathbf{q}, \mathbf{\dot{q}})$ satisfies the general Lagrange mechanics relation

$$
\frac{\delta L}{\delta q}-\frac{\partial R}{\partial \dot{q}}=0 \tag{10.17} \label{eq-10-17}
$$

This generalized Rayleigh’s dissipation function eliminates the prior restriction to linear dissipation processes, which greatly expands the range of validity for using Rayleigh’s dissipation function.

### Rayleigh dissipation in Lagrange equations of motion

Linear dissipative forces can be directly, and elegantly, included in Lagrangian mechanics by using Rayleigh’s dissipation function as a generalized force $Q_{j}^{f}$. Inserting Rayleigh dissipation function $(10.4.12)$ in the generalized Lagrange equations of motion $(6.5.12)$ gives

$$
\left\{ \frac{d}{dt}\left( \frac{\partial L}{\partial \dot{q}_{j}}\right) - \frac{\partial L}{\partial q_{j}}\right\} =\left[ \sum_{k=1}^{m}\lambda _{k} \frac{\partial g_{k}}{\partial q_{j}}(\mathbf{q},t)+Q_{j}^{EXC}\right] - \frac{\partial \mathcal{R(}\mathbf{q},\mathbf{\dot{q}})}{\partial \dot{q}_{j} } \tag{10.18}
$$

Where $Q_{j}^{EXC}$ corresponds to the generalized forces remaining after removal of the generalized linear, velocity-dependent, frictional force $Q_{j}^{f}$. The holonomic forces of constraint are absorbed into the Lagrange multiplier term.

### Rayleigh dissipation in Hamiltonian mechanics

If the nonconservative forces depend linearly on velocity, and are derivable from Rayleigh’s dissipation function according to equation $(10.4.12)$, then using the definition of generalized momentum gives

$$
\begin{align} \dot{p}_{i} &=&\frac{d}{dt}\frac{\partial L}{\partial \dot{q}_{j}}=\frac{ \partial L}{\partial q_{i}}+\left[ \sum_{k=1}^{m}\lambda _{k}\frac{\partial g_{k}}{\partial q_{j}}(\mathbf{q},t)+Q_{j}^{EXC}\right] -\frac{\partial \mathcal{R(}\mathbf{q},\mathbf{\dot{q}})}{\partial \dot{q}_{j}} \tag{10.19} \label{eq-10-19} \\ \dot{p}_{i} &=&-\frac{\partial H(\mathbf{p,q},t\mathbf{)}}{\partial q_{i}}+ \left[ \sum_{k=1}^{m}\lambda _{k}\frac{\partial g_{k}}{\partial q_{j}}( \mathbf{q},t)+Q_{j}^{EXC}\right] -\frac{\partial \mathcal{R(}\mathbf{q}, \mathbf{\dot{q}})}{\partial \dot{q}_{j}} \tag{10.20}\end{align}
$$

Thus Hamilton’s equations become

$$
\dot{q}_{i} = \frac{\partial H}{\partial p_{i}} \tag{10.21} \label{eq-10-21}
$$

$$
\begin{align}\dot{p}_{i} &=&-\frac{\partial H}{\partial q_{i}}+\left[ \sum_{k=1}^{m} \lambda _{k}\frac{\partial g_{k}}{\partial q_{j}}(\mathbf{q},t)+Q_{j}^{EXC} \right] -\frac{\partial \mathcal{R(}\mathbf{q},\mathbf{\dot{q}})}{\partial \dot{q}_{j}} \tag{10.22} \label{eq-10-22}\end{align}
$$

The Rayleigh dissipation function $\mathcal{R(}\mathbf{q},\mathbf{\dot{q}})$ provides an elegant and convenient way to account for dissipative forces in both Lagrangian and Hamiltonian mechanics.

### Dissipative Lagrangians or Hamiltonians

New degrees of freedom or effective forces can be postulated that are then incorporated into the Lagrangian or the Hamiltonian in order to mimic the effects of the nonconservative forces. This approach has been used for special cases.
