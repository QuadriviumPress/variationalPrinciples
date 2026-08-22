---
title: "18. The Transition to Quantum Physics"
short_title: "Chapter 18"
label: ch-18-the-transition-to-quantum-physics
---


# 18. The Transition to Quantum Physics

(ch-18)=

## 18.1: Introduction to Quantum Physics

Classical mechanics, including extensions to relativistic velocities, embrace an unusually broad range of topics ranging from astrophysics to nuclear and particle physics, from one-body to many-body statistical mechanics. It is interesting to discuss the role of classical mechanics in the development of quantum mechanics which plays a crucial role in physics. A valid question is “why discuss quantum mechanics in a classical mechanics course?”. The answer is that quantum mechanics supersedes classical mechanics as the fundamental theory of mechanics. Classical mechanics is an approximation applicable for situations where quantization is unimportant. Thus there must be a correspondence principle that relates quantum mechanics to classical mechanics, analogous to the relation between relativistic and non-relativistic mechanics. It is illuminating to study the role played by the Hamiltonian formulation of classical mechanics in the development of quantal theory and statistical mechanics. The Hamiltonian formulation is expressed in terms of the phase-space variables $\mathbf{q}, \mathbf{p}$ for which there are well-established rules for transforming to quantal linear operators.

## 18.2: Brief summary of the origins of quantum theory

The last decade of the $19^{th}$ century saw the culmination of classical physics. By 1900 scientists thought that the basic laws of mechanics, electromagnetism, and statistical mechanics were understood and worried that future physics would be reduced to confirming theories to the fifth decimal place, with few major new discoveries to be made. However, technical developments such as photography, vacuum pumps, induction coil, etc., led to important discoveries that revolutionized physics and toppled classical mechanics from its throne at the beginning of the $20^{th}$ century. Table 18.1 summarizes some of the major milestones leading up to the development of quantum mechanics.

Max Planck searched for an explanation of the spectral shape of the black-body electromagnetic radiation. He found an interpolation between two conflicting theories, one that reproduced the short wavelength behavior, and the other the long wavelength behavior. Planck’s interpolation required assuming that electromagnetic radiation was not emitted with a continuous range of energies, but that electromagnetic radiation is emitted in discrete bundles of energy called quanta. In December 1900 he presented his theory which reproduced precisely the measured black body spectral distribution by assuming that the energy carried by a single quantum must be an integer multiple of $h\nu$:

$$
E = h\nu = \frac{hc}{ \lambda} 
$$

where $\nu$ is the frequency of the electromagnetic radiation and Planck’s constant, $h = 6.62610^{−34}$ $J \cdot s$ was the best fit parameter of the interpolation. That is, Planck assumed that energy comes in discrete bundles of energy equal to $h\nu$ which are called quanta. By making this extreme assumption, in an act of desperation, Planck was able to reproduce the experimental black body radiation spectrum. The assumption that energy was exchanged in bundles hinted that the classical laws of physics were inadequate in the microscopic domain. The older generation physicists initially refused to believe Planck’s hypothesis which underlies quantum theory. It was the new generation physicists, like Einstein, Bohr, Heisenberg, Born, Schrödinger, and Dirac, who developed Planck’s hypothesis leading to the revolutionary quantum theory.

In 1905, Einstein predicted the existence of the photon, derived the theory of specific heat, as well as deriving the Theory of Special Relativity. It is remarkable to realize that he developed these three revolutionary theories in one year, when he was only 26 years old. Einstein uncovered an inconsistency in Planck’s derivation of the black body spectral distribution in that it assumed the statistical part of the energy is quantized, whereas the electromagnetic radiation assumed Maxwell’s equations with oscillator energies being continuous. Planck demanded that light of frequency $\nu$ be packaged in quanta whose energies were multiples of $h\nu$, but Planck never thought that light would have particle-like behavior. Newton believed that light involved corpuscles, and Hamilton developed the Hamilton-Jacobi theory seeking to describe light in terms of the corpuscle theory. However, Maxwell had convinced physicists that light was a wave phenomena; interference plus diffraction effects were convincing manifestations of the wave-like properties of light. In order to reproduce Planck’s prediction, Einstein had to treat black-body radiation as if it consisted of a gas of photons, each photon having energy $E = h\nu$. This was a revolutionary concept that returned to Newton’s corpuscle theory of light. Einstein realized that there were direct tests of his photon hypothesis, one of which is the photo-electric effect. According to Einstein, each photon has an energy $E = h\nu$, in contrast to the classical case where the energy of the photoelectron depends on the intensity of the light. Einstein predicted that the ejected electron will have a kinetic energy

$$
KE = h\nu − W 
$$

where $W$ is the work function which is the energy needed to remove an electron from a solid.

Many older scientists, including Planck, accepted Einstein’s theory of relativity but were skeptical of the photon concept, even after Einstein’s photon concept was vindicated in 1915 by Millikan who showed that, as predicted, the energy of the ejected photoelectron depended on the frequency, and not intensity, of the light. In 1923 Compton’s demonstrated that electromagnetic radiation scattered by free electrons obeyed simple two-body scattering laws which finally convinced the many skeptics of the existence of the photon.

| Date | Author | Development |
| --- | --- | --- |
| 1887 | Hertz | Discovered the photo-electric effect |
| 1895 | Röntgen | Discovered x-rays |
| 1896 | Becquerel | Discovered radioactivity |
| 1897 | J.J. Thomson | Discovered the first fundamental particle, the electron |
| 1898 | Pierre & Marie Curie | Showed that thorium is radioactive which founded nuclear physics |
| 1900 | Planck | Quantization $E = h\nu$ explained the black-body spectrum |
| 1905 | Einstein | Theory of special relativity |
| 1905 | Einstein | Predicted the existence of the photon |
| 1906 | Einstein | Used Planck’s constant to explain specific heats of solids |
| 1909 | Millikan | The oil drop experiment measured the charge on the electron |
| 1911 | Rutherford | Discovered the atomic nucleus with radius $10^{−15}$ $m$ |
| 1912 | Bohr | Bohr model of the atom explained the quantized states of hydrogen |
| 1914 | Moseley | X-ray spectra determined the atomic number of the elements. |
| 1915 | Millikan | Used the photo-electric effect to confirm the photon hypothesis. |
| 1915 | Wilson-Sommerfeld | Proposed quantization of the action-angle integral |
| 1921 | Stern-Gerlach | Observed space quantization in non-uniform magnetic field |
| 1923 | Compton | Compton scattering of x-rays confirmed the photon hypothesis |
| 1924 | de Broglie | Postulated wave-particle duality for matter and EM waves |
| 1924 | Bohr | Explicit statement of the correspondence principle |
| 1925 | Pauli | Postulated the exclusion principle |
| 1925 | Goudsmit-Uhlenbeck | Postulated the spin of the electron of $s = \frac{1}{2} \hbar$ |
| 1925 | Heisenberg | Matrix mechanics representation of quantum theory |
| 1925 | Dirac | Related Poisson brackets and commutation relations |
| 1926 | Schrödinger | Wave mechanics |
| 1927 | G.P. Thomson/Davisson | Electron diffraction proved wave nature of electron |
| 1928 | Dirac | Developed the Dirac relativistic wave equation |

### Bohr model of the atom

The Rutherford scattering experiment, performed at Manchester in 1911, discovered that the Au atom comprised a positively charge nucleus of radius $\approx 10^{−14}$ $m$ which is much smaller than the $1.35 \times 10^{−10}$ $m$ radius of the Au atom. Stimulated by this discovery, Niels Bohr joined Rutherford at Manchester in 1912 where he developed the Bohr model of the atom. This theory was remarkably successful in spite of having serious inconsistencies and deficiencies. Bohr’s model assumptions were:

1. Electromagnetic radiation is quantized with $E = h\nu$.
2. Electromagnetic radiation exhibits behavior characteristic of the emission of photons with energy $E = h\nu$ and momentum $p = \frac{h\nu}{c}$. That is, it exhibits both wave-like and particle-like behavior.
3. Electrons are in stationary orbits that do not radiate, which contradicts the predictions of classical electromagnetism.
4. The orbits are quantized such that the electron angular momentum is an integer multiple of $\frac{h}{ 2\pi} = \hbar$.
5. Atomic electromagnetic radiation is emitted with photon energy equal to the difference in binding energy between the two atomic levels involved. $h\nu = E_1 − E_2$

The first two assumptions are due to Planck and Einstein, while the last three were made by Niels Bohr.

The deficiencies of the Bohr model were the philosophical problems of violating the tenets of classical physics in explaining hydrogen-like atoms, that is, the theory was prescriptive, not deductive. The Bohr model was based implicitly on the assumption that quantum theory contains classical mechanics as a limiting case. Bohr explicitly stated this assumption which he called the **correspondence principle**, and which played a pivotal role in the development of the older quantum theory. In 1924 Bohr justified the inconsistencies of the old quantum theory by writing “As frequently emphasized, these principles, although they are formulated by the help of classical conceptions, are to be regarded purely as laws of quantum theory, which give us, not withstanding the formal nature of quantum theory, a hope in the future of a consistent theory, which at the same time reproduces the characteristic features of quantum theory, important for its applicability, and, nevertheless, can be regarded as a rational generalization of classical electrodynamics.”

The old quantum theory was remarkably successful in reproducing the black-body spectrum, specific heats of solids, the hydrogen atom, and the periodic table of the elements. Unfortunately, from a methodological point of view, the theory was a hodgepodge of hypotheses, principles, theorems, and computational recipes, rather than a logical consistent theory. Every problem was first solved in terms of classical mechanics, and then would pass through a mysterious quantization procedure involving the correspondence principle. Although built on the foundation of classical mechanics, it required Bohr’s hypotheses which violated the laws of classical mechanics and predictions of Maxwell’s equations.

### Quantization

By 1912 Planck, and others, had abandoned the concept that quantum theory was a branch of classical mechanics, and were searching to see if classical mechanics was a special case of a more general quantum physics, or quantum physics was a science altogether outside of classical mechanics. Also they were trying to find a consistent and rational reason for quantization to replace the ad hoc assumption of Bohr.

In 1912 Sommerfeld proposed that, in every elementary process, the atom gains or loses a definite amount of action between times $t_0$ and $t$ of

$$
S = \int^t_{t_0} L(t^{\prime} )dt^{\prime} 
$$

where $S$ is the quantal analogue of the classical action function. It has been shown that the classical principle of least action states that the action function is stationary for small variations of the trajectory. In 1915 Wilson and Sommerfeld recognized that the quantization of angular momentum could be expressed in terms of the action-angle integral, that is equation $(15.5.1)$. They postulated that, for every coordinate, the action-angle variable is quantized

$$
\oint p_k dq_k = nh 
$$

where the action-angle variable integral is over one complete period of the motion. That is, they postulated that Hamilton’s phase space is quantized, but the microscopic granularity is such that the quantization is only manifest for atomic-sized domains. That is, $n$ is a small integer for atomic systems in contrast to $n \approx 10^{64}$ for the Earth-Sun two-body system.

Sommerfeld recognized that quantization of more than one degree of freedom is needed to obtain a more accurate description of the hydrogen atom. Sommerfeld reproduced the experimental data by assuming quantization of the three degrees of freedom,

$$
\oint p_r dr = n_1h \quad \oint p_{\theta} d\theta = n_2h \quad \oint p_{\phi} d\phi = n_3h 
$$

and solving Hamilton-Jacobi theory by separation of variables. In 1916 the Bohr-Sommerfeld model solved the classical orbits for the hydrogen atom, including relativistic corrections as described in example $17.7.1$. This reproduced fine structure observed in the optical spectra of hydrogen. The use of the canonical transformation to action-angle variables proved to be the ideal approach for solving many such problems in quantum mechanics. In 1921, Stern and Gerlach demonstrated space quantization by observing the splitting of atomic beams deflected by non-uniform magnetic fields. This result was a major triumph for quantum theory. Sommerfeld declared that “With their bold experimental method, Stern and Gerlach demonstrated not only the existence of space quantization, they also proved the atomic nature of the magnetic moment, its quantum-theoretic origin, and its relation to the atomic structure of electricity.”

In 1925, Pauli’s Exclusion Principle proposed that no more than one electron can have identical quantum numbers and that the atomic electronic state is specified by four quantum numbers. Two students, Goudsmit and Uhlenbeck suggested that a fourth two-valued quantum number was the electron spin of $\pm \frac{\hbar}{2}$. This provided a plausible explanation for the structure of multi-electron atoms.

### Wave-particle duality

In his 1924 doctoral thesis, Prince Louis de Broglie proposed the hypothesis of wave-particle duality which was a pivotal development in quantum theory. de Broglie used the classical concept of a matter wavepacket, analogous to classical wave packets discussed in chapter $3.11$. He assumed that both the group and signal velocities of a matter wave packet must equal the velocity of the corresponding particle. By analogy with Einstein’s relation for the photon, and using the Theory of Special Relativity, de Broglie assumed that

$$
\hbar \omega = E = \frac{mc^2}{\sqrt{\left(1 - \frac{v^2}{c^2}\right)}} 
$$

The group velocity is required to equal the velocity of the mass

$$
v_{group} = \left(\frac{d\omega}{ dk} \right) = \left(\frac{d\omega}{ dv } \right) \left(\frac{dv }{dk} \right) = v 
$$

This gives

$$
\frac{dk }{dv} = \frac{1}{ v} \left(\frac{d\omega}{ dv} \right) = \left( \frac{m}{\hbar} \right) \left( 1 − \frac{v^2}{ c^2} \right)^{− \frac{3}{ 2}} 
$$

Integration of this equation assuming that $k = 0$ when $v = 0$, then gives

$$
\hbar \mathbf{k} = \frac{m\mathbf{v}}{\sqrt{\left(1-\frac{\mathbf{v}\cdot\mathbf{v}}{c^2}\right)}} = \mathbf{p} 
$$

This relation, derived by de Broglie, is required to ensure that the particle travels at the group velocity of the wave packet characterizing the particle. Note that although the relations used to characterize the matter waves are purely classical, the physical content of such waves is beyond classical physics. In 1927 C. Davisson and G.P. Thomson independently observed electron diffraction confirming wave/particle duality for the electron. Ironically, J.J. Thomson discovered that the electron was a particle, whereas his son attributed it to an electron wave.

Heisenberg developed the modern matrix formulation of quantum theory in 1925; he was 24 years old at the time. A few months later Schrödinger’s developed wave mechanics based on de Broglie’s concept of wave-particle duality. The matrix mechanics, and wave mechanics, quantum theories are radically different. Heisenberg’s algebraic approach employs non-commuting quantities and unfamiliar mathematical techniques that emphasized the discreteness characteristic of the corpuscle aspect. In contrast, Schrödinger used the familiar analytical approach that is an extension of classical laws of motion and waves which stressed the element of continuity.

## 18.3: Hamiltonian in Quantum Theory

### Heisenberg’s Matrix-Mechanics Representation

The algebraic Heisenberg representation of quantum theory is analogous to the algebraic Hamiltonian representation of classical mechanics, and shows best how quantum theory evolved from, and is related to, classical mechanics. Heisenberg decided to ignore the prevailing conceptual theories, such as classical mechanics, and based his quantum theory on observables. This approach was influenced by the success of Bohr’s older quantum theory and Einstein’s theory of relativity. He abandoned the classical notions that the canonical variables $p_k, q_k$ can be measured directly and simultaneously. Secondly he wished to absorb the correspondence principle directly into the theory instead of it being an ad hoc procedure tailored to each application. Heisenberg considered the Fourier decomposition of transition amplitudes between discrete states and found that the product of the conjugate variables do not commute. Heisenberg derived, for the first time, the correct energy levels of the one-dimensional harmonic oscillator as $E_n = \hbar \omega (n + \frac{1}{2})$ which was a significant achievement. Born recognized that Heisenberg’s strange multiplication and commutation rules for two variables, corresponded to matrix algebra. Prior to 1925, matrix algebra was an obscure branch of pure mathematics not known or used by the physics community. Heisenberg, Born, and the young mathematician Jordan, developed the commutation rules of matrix mechanics. Heisenberg’s approach represents the classical position and momentum coordinates $q, p$ by matrices $\mathbf{q}$ and $\mathbf{p}$, with corresponding matrix elements $q_{mn}e^{i\omega_{mn}t}$ and $p_{mn}e^{i\omega_{mn}t}$. Born showed that the trace of the matrix

$$
H(\mathbf{pq}) = \mathbf{p}\mathbf{\dot{q}}−L \label{18.10}
$$

gives the Hamiltonian function $H(\mathbf{p}, \mathbf{q})$ of the matrices $\mathbf{q}$ and $\mathbf{p}$ which leads to Hamilton’s canonical equations

$$
\mathbf{\dot{q}}= \frac{\partial H }{\partial \mathbf{p}} \quad \mathbf{\dot{p}} =−\frac{\partial H }{\partial \mathbf{q}} \label{18.11}
$$

Heisenberg and Born also showed that the commutator of $\mathbf{q}, \mathbf{p}$ equals

$$
q_kp_l − p_lq_k = i\hbar \delta_{kl} \label{18.12} \\ q_kq_l − q_lq_k = 0 \\ p_kp_l − p_lp_k = 0
$$

Born realized that Equation \ref{18.12} is the only fundamental equation for introducing $\hbar$ into the theory in a logical and consistent way.

Chapter $15.2.4$ discussed the formal correspondence between the Poisson bracket, defined in chapter $15.3$, and the commutator in classical mechanics. It was shown that the commutator of two functions equals a constant multiplicative factor $\lambda$ times the corresponding Poisson Bracket. That is

$$
(F_jG_k − G_kF_j ) = \lambda \{F_j , G_k\} \label{18.13}
$$

where the multiplicative factor $\lambda$ is a number independent of $F_j , G_k$, and the commutator.

In 1925, Paul Dirac, a 23-year old graduate student at Bristol, recognized the crucial importance of the above correspondence between the commutator and the Poisson Bracket of two functions, to relating classical mechanics and quantum mechanics. Dirac noted that if the constant $\lambda$ is assigned the value $\lambda = i\hbar$, then Equation \ref{18.13} directly relates Heisenberg’s commutation relations between the fundamental canonical variables $(q_j , p_k)$ to the corresponding classical Poisson Bracket $\{q_j , p_k\}$. That is,

$$
q_kp_l − p_lq_k = i\hbar \{q_k, p_l\} = i\hbar \delta_{kl} \label{18.14}
$$

$$
q_kq_l − q_lq_k = i\hbar \{q_k, q_l\}=0 \label{18.15}
$$

$$
p_kp_l − p_lp_k = i\hbar \{p_k, p_l\}=0 \label{18.16}
$$

Dirac recognized that the correspondence between the classical Poisson bracket, and quantum commutator, given by Equation \ref{18.13}, provides a logical and consistent way that builds quantization directly into the theory, rather than using an ad-hoc, case-dependent, hypothesis as used by the older quantum theory of Bohr. The basis of Dirac’s quantization principle, involves replacing the classical Poisson Bracket, $\{F_j , G_k\}$ by the commutator, $\frac{1}{ i\hbar } (F_j, G_k − G_kF_j )$. That is,

$$
\{F_j , G_k\} \Longrightarrow \frac{1}{i\hbar} (F_jG_k − G_kF_j ) \label{18.17}
$$

Hamilton’s canonical equations, as introduced in chapter $15$, are only applicable to classical mechanics since they assume that the exact position and conjugate momentum can be specified both exactly and simultaneously which contradicts the Heisenberg’s Uncertainty Principle. In contrast, the Poisson bracket generalization of Hamilton’s equations allows for non-commuting variables plus the corresponding uncertainty principle. That is, the transformation from classical mechanics to quantum mechanics can be accomplished simply by replacing the classical Poisson Bracket by the quantum commutator, as proposed by Dirac. The formal analogy between classical Hamiltonian mechanics, and the Heisenberg representation of quantum mechanics is strikingly apparent using the correspondence between the Poisson Bracket representation of Hamiltonian mechanics and Heisenberg’s matrix mechanics.

The direct relation between the quantum commutator, and the corresponding classical Poisson Bracket, applies to many observables. For example, the quantum analogs of Hamilton’s equations of motion are given by use of Hamilton’s equations of motion, $(15.2.42)$, $(15.2.45)$, and replacing each Poisson Bracket by the corresponding commutator. That is

$$
\frac{dq_k}{ dt} = \frac{\partial H }{\partial p_k} = \{q_k, H\} = \frac{1}{i\hbar} (q_kH − Hq_k) \label{18.18}
$$

$$
\frac{dp_k }{dt} = −\frac{\partial H }{\partial q_k } = \{p_k, H\} = \frac{1}{i\hbar} (p_kH − Hp_k) \label{18.19}
$$

Chapter $15.2.5$ discussed the time dependence of observables in Hamiltonian mechanics. Equation $(15.2.34)$ gave the total time derivative of any observable $G$ to be

$$
\frac{dG}{dt} = \frac{\partial G}{\partial t} + \{G, H\} \label{18.20}
$$

Equation \ref{18.17} can be used to replace the Poisson Bracket by the quantum commutator, which gives the corresponding time dependence of observables in quantum physics.

$$
\frac{dG}{dt} = \frac{\partial G}{\partial t} + \frac{1}{i\hbar} (GH − HG) \label{18.21}
$$

In quantum mechanics, Equation \ref{18.21} is called the *Heisenberg equation*. Note that if the observable $G$ is chosen to be a fundamental canonical variable, then $\frac{\partial q_k}{ \partial t} =0= \frac{\partial p_k}{ \partial t}$ and equation $(15.2.9)$ reduces to Hamilton’s equations \ref{18.18} and \ref{18.19}.

The analogies between classical mechanics and quantum mechanics extend further. For example, if $G$ is a constant of motion, that is $\frac{dG}{dt} = 0$, then Heisenberg’s equation of motion gives

$$
\frac{\partial G}{\partial t} + \frac{1}{i\hbar} (GH − HG)=0 \label{18.22}
$$

Moreover, if $G$ is not an explicit function of time, then

$$
0 = \frac{1}{i\hbar} (GH − HG) \label{18.23}
$$

That is, the transition to quantum physics shows that, if $G$ is a constant of motion, and is not explicitly time dependent, then $G$ commutes with the Hamiltonian $H$.

The above discussion has illustrated the close and beautiful correspondence between the Poisson Bracket representation of classical Hamiltonian mechanics, and the Heisenberg representation of quantum mechanics. Dirac provided the elegant and simple correspondence principle connecting the Poisson bracket representation of classical Hamiltonian mechanics, to the Heisenberg representation of quantum mechanics.

### Schrödinger’s Wave-Mechanics Representation

The wave mechanics formulation of quantum mechanics, by the Austrian theorist Schrödinger, was built on the wave-particle duality concept that was proposed in 1924 by Louis de Broglie. Schrödinger developed his wave mechanics representation of quantum physics a year after the development of matrix mechanics by Heisenberg and Born. The Schrödinger wave equation is based on the non-relativistic Hamilton-Jacobi representation of a wave equation, melded with the operator formalism of Born and Wiener. The 39-year old Schrödinger was an expert in classical mechanics and wave theory, which was invaluable when he developed the important Schrödinger equation. As mentioned in chapter $15.4.4$, the Hamilton-Jacobi theory is a formalism of classical mechanics that allows the motion of a particle to be represented by a wave. That is, the wavefronts are surfaces of constant action $S$, and the particle momenta are normal to these constant-action surfaces, that is, $\mathbf{p} = \boldsymbol{\nabla}S$. The wave-particle duality of Hamilton-Jacobi theory is a natural way to handle the wave-particle duality proposed by de Broglie.

Consider the classical Hamilton-Jacobi equation for one body, given by \ref{18.20}.

$$
\frac{\partial S}{\partial t} + H(\mathbf{q},\boldsymbol{\nabla}S,t)=0 \label{18.24}
$$

If the Hamiltonian is time independent, then equation $(15.4.2)$ gives that

$$
\frac{\partial S}{\partial t} = −H(\mathbf{q}, \mathbf{p}, t) = −E (\boldsymbol{\alpha}) \label{18.25}
$$

The integration of the time dependence is trivial, and thus the action integral for a time-independent Hamiltonian is

$$
S(\mathbf{q}, \boldsymbol{\alpha},t) = W (\mathbf{q}, \boldsymbol{\alpha}) − E (\boldsymbol{\alpha})t \label{18.26}
$$

A formal transformation gives

$$
E = −\frac{\partial S}{\partial t} \qquad \mathbf{p} = \boldsymbol{\nabla}S \label{18.27}
$$

Consider that the classical time-independent Hamiltonian, for motion of a single particle, is represented by the Hamilton-Jacobi equation.

$$
H = \frac{\mathbf{p}^2}{ 2\mu } + U(q) = −\frac{\partial S}{\partial t} \label{18.28}
$$

Substitute for $\mathbf{p}$ leads to the classical Hamilton-Jacobi relation in terms of the action $S$

$$
\frac{1}{ 2\mu } (\boldsymbol{\nabla}S \cdot \boldsymbol{\nabla}S) + U(q) = −\frac{\partial S}{\partial t} \label{18.29}
$$

By analogy with the Hamilton-Jacobi equation, Schrödinger proposed the quantum operator equation

$$
i\hbar \frac{ \partial \psi}{ \partial t} = \hat{H}\psi \label{18.30}
$$

where $\hat{H}$ is an operator given by

$$
\hat{H} = − \frac{\hbar^2 }{2\mu} \nabla^2 + U(r) \label{18.31}
$$

In 1926, Max Born and Norbert Wiener introduced the operator formalism into matrix mechanics for prediction of observables and this has become an integral part of quantum theory. In the operator formalism, the observables are represented by operators that project the corresponding observable from the wavefunction. That is, the quantum operator formalism for the assumed momentum and energy operators, that operate on the wavefunction $\psi$, are

$$
p_j = \frac{\hbar}{ i} \frac{\partial}{ \partial q_j} \quad E = −\frac{\hbar}{ i} \frac{\partial}{ \partial t} \label{18.32}
$$

Formal transformations of $\mathbf{p}$ and $E$ in the Hamiltonian \ref{18.26} leads to the time-independent Schrödinger equation

$$
− \frac{\hbar^2}{ 2\mu} \frac{ \partial^2\psi}{ \partial q^2} + U(q)\psi = E\psi \label{18.33}
$$

Assume that the wavefunction is of the form

$$
\psi = Ae^{\frac{ iS}{ \hbar}} \label{18.34}
$$

where the action $S$ gives the phase of the wavefront, and $A$ the amplitude of the wave, as described in chapter $15.4.4$. The time dependence, that characterizes the motion of the wavefront, is contained in the time dependence of $S$. This form for the wavefunction has the advantage that the wavefunction frequently factors into a product of terms, e.g. $\psi = R(r)\Theta (\theta ) \Phi (\phi )$ which corresponds to a summation of the exponents $S = W_r + W_{\theta} + W_{\phi} − Et$. This summation form is exploited by separation of the variables, as discussed in chapter $15.4.3$.

Insert $\psi$ defined by \ref{18.34} into Equation \ref{18.33}, plus using the fact that

$$
\frac{\partial^2\psi}{ \partial q^2} = \frac{\partial}{ \partial q} \left( \frac{\partial \psi}{ \partial S} \frac{\partial S}{ \partial q} \right) = \frac{\partial}{ \partial q} \left( \frac{i}{ \hbar} \psi \frac{ \partial S }{\partial q} \right) = − \frac{1}{ \hbar^2} \psi \left( \frac{\partial S}{ \partial q } \right)^2 + \frac{i}{ \hbar} \psi \frac{ \partial^2S}{ \partial q^2} \label{18.35}
$$

leads to

$$
−\frac{\partial S}{\partial t} = \frac{1}{ 2\mu} (\boldsymbol{\nabla}S \cdot \boldsymbol{\nabla}S) + U(q) − \frac{i\hbar}{ 2\mu} \nabla^2S = E \label{18.36}
$$

Note that if Planck’s constant $\hbar = 0$, then the imaginary term in Equation \ref{18.36} is zero, leading to \ref{18.36} being real, and identical to the Hamilton-Jacobi result, Equation \ref{18.29}. The fact that Equation \ref{18.35} equals the Hamilton-Jacobi equation in the limit $\hbar \rightarrow 0$, illustrates the close analogy between the waveparticle duality of the classical Hamilton-Jacobi theory, and de Broglie’s wave-particle duality in Schrödinger’s quantum wave-mechanics representation.

The Schrödinger approach was accepted in 1925 and exploited extensively with tremendous success, since it is much easier to grasp conceptually than is the algebraic approach of Heisenberg. Initially there was much conflict between the proponents of these two contradictory approaches, but this was resolved by Schrödinger who showed in 1926 that there is a formal mathematical identity between wave mechanics and matrix mechanics. That is, these two quantal representations of Hamiltonian mechanics are equivalent, even though they are built on either the Poisson bracket representation, or the Hamilton-Jacobi representation. Wave mechanics is based intimately on the quantization rule of the action variable. Heisenberg’s Uncertainty Principle is automatically satisfied by Schrödinger’s wave mechanics since the uncertainty principle is a feature of all wave motion, as described in chapter $3$.

In 1928 Dirac developed a relativistic wave equation which includes spin as an integral part. This[Dirac equation](https://phys.libretexts.org/Under_Construction/Purgatory/Book%3A_Quantum_Mechanics_(Fitzpatrick)/11%3A_Relativistic_Electron_Theory/11.2%3A_The_Dirac_Equation) remains the fundamental wave equation of quantum mechanics. Unfortunately it is difficult to apply.

Today the powerful and efficient Heisenberg representation is the dominant approach used in the field of physics, whereas chemists tend to prefer the more intuitive Schrödinger wave mechanics approach. In either case, the important role of Hamiltonian mechanics in quantum theory is undeniable.

## 18.4: Lagrangian Representation in Quantum Theory

The classical notion of canonical coordinates and momenta, has a simple quantum analog which has allowed the Hamiltonian theory of classical mechanics, that is based on canonical coordinates, to serve as the foundation for the development of quantum mechanics. The alternative Lagrangian formulation for classical dynamics is described in terms of coordinates and velocities, instead of coordinates and momenta. The Lagrangian and Hamiltonian formulations are closely related, and it may appear that the Lagrangian approach is more fundamental. The Lagrangian method allows collecting together all the equations of motion and expressing them as stationary properties of the action integral, and thus it may appear desirable to base quantum mechanics on the Lagrangian theory of classical mechanics. Unfortunately, the Lagrangian equations of motion involve partial derivatives with respect to coordinates, and their velocities, and the meaning ascribed to such derivatives is difficult in quantum mechanics. The close correspondence between Poisson brackets and the commutation rules leads naturally to Hamiltonian mechanics. However, Dirac showed that Lagrangian mechanics can be carried over to quantum mechanics using canonical transformations such that the classical Lagrangian is considered to be a function of coordinates at time $t$ and $t + dt$ rather than of coordinates and velocities.

The motivation for Feynman’s 1942 Ph.D thesis, entitled “*The Principle of Least Action in Quantum Mechanics*”, was to quantize the classical action at a distance in electrodynamics. This theory adopted an overall space-time viewpoint for which the classical Hamiltonian approach, as used in conventional formulations of quantum mechanics, is inapplicable. Feynman used the Lagrangian, plus the principle of least action, to underlie his development of quantum field theory. To paraphrase Feynman’s Nobel Lecture, he used a physical approach that is quite different from the customary Hamiltonian point of view for which the system is discussed in great detail as a function of time. That is, you have the field at this moment, then a differential equation gives you the field at a later moment and so on; that is, the Hamiltonian approach is a time differential method. In Feynman’s least-action approach the action describes the character of the path throughout all of space and time. The behavior of nature is determined by saying that the whole space-time path has a certain character. The use of action involves both advanced and retarded terms that make it difficult to transform back to the Hamiltonian form. The Feynman space-time approach is far beyond the scope of this course. This topic will be developed in advanced graduate courses on quantum field theory

## 18.5: Correspondence Principle

The Correspondence Principle implies that any new theory in physics must reduce to preceding theories that have been proven to be valid. For example, Einstein’s Special Theory of Relativity satisfies the Correspondence Principle since it reduces to classical mechanics for velocities small compared with the velocity of light. Similarly, the General Theory of Relativity reduces to Newton’s Law of Gravitation in the limit of weak gravitational fields. Bohr’s Correspondence Principle requires that the predictions of quantum mechanics must reproduce the predictions of classical physics in the limit of large quantum numbers. Bohr’s Correspondence Principle played a pivotal role in the development of the old quantum theory, from it’s inception in 1912, until 1925 when the old quantum theory was superseded by the current matrix and wave mechanics representations of quantum mechanics.

Quantum theory now is a well-established field of physics that is equally as fundamental as is classical mechanics. The Correspondence Principle now is used to project out the analogous classical-mechanics phenomena that underlie the observed properties of quantal systems. For example, this book has studied the classical-mechanics analogs of the observed behavior for typical quantal systems, such as the vibrational and rotational modes of the molecule, and the vibrational modes of the crystalline lattice. The nucleus is the epitome of a many-body, strongly-interacting, quantal system. Example $14.12.1$ showed that there is a close correspondence between classical-mechanics predictions, and quantal predictions, for both the rotational and vibrational collective modes of the nucleus, as well as for the single-particle motion of the nucleons in the nuclear mean field, such as the onset of Coriolis-induced alignment. This use of the Correspondence Principle can provide considerable insight into the underlying classical physics embedded in quantal systems.

## 18.S: The Transition to Quantum Physics (Summary)

The important point of this discussion is that variational formulations of classical mechanics provide a rational, and direct basis, for the development of quantum mechanics. It has been shown that the final form of quantum mechanics is closely related to the Hamiltonian formulation of classical mechanics. Quantum mechanics supersedes classical mechanics as the fundamental theory of mechanics in that classical mechanics only applies for situations where quantization is unimportant, and is the limiting case of quantum mechanics when $\hbar \rightarrow 0$ which is in agreement with the Bohr’s Correspondence Principle. The Dirac relativistic theory of quantum mechanics is the ultimate quantal theory for the relativistic regime.

This discussion has barely scratched the surface of the correspondence between classical and quantal mechanics, which goes far beyond the scope of this course. The goal of this chapter is to illustrate that classical mechanics, in particular, Hamiltonian mechanics, underlies much of what you will learn in your quantum physics courses. An interesting similarity between quantum mechanics and classical mechanics is that physicists usually use the more visual Schrödinger wave representation in order to describe quantum physics to the non-expert, which is analogous to the similar use of Newtonian physics in classical mechanics. However, practicing physicists invariably use the more abstract Heisenberg matrix mechanics to solve problems in quantum mechanics, analogous to widespread use of the variational approach in classical mechanics, because the analytical approaches are more powerful and have fundamental advantages. Quantal problems in molecular, atomic, nuclear, and subnuclear systems, usually involve finding the normal modes of a quantal system, that is, finding the eigen-energies, eigen-functions, spin, parity, and other observables for the discrete quantized levels. Solving the equations of motion for the modes of quantal systems is similar to solving the many-body coupled-oscillator problem in classical mechanics, where it was shown that use of matrix mechanics is the most powerful representation. It is ironic that the introduction of matrix methods to classical mechanics is a by-product of the development of matrix mechanics by Heisenberg, Born and Jordan. This illustrates that classical mechanics not only played a pivotal role in the development of quantum mechanics, but it also has benefitted considerably from the development of quantum mechanics; that is, the synergistic relation between these two complementary branches of physics has been beneficial to both classical and quantum mechanics.

### Recommended reading

“Quantum Mechanics” by P.A.M. Dirac, Oxford Press, 1947,

“Conceptual Development of Quantum Mechanics” by Max Jammer, Mc Graw Hill 1966.
