[![INFORMS Journal on Computing Logo](https://INFORMSJoC.github.io/logos/INFORMS_Journal_on_Computing_Header.jpg)](https://pubsonline.informs.org/journal/ijoc)

# CacheTest

This archive is distributed in association with the [INFORMS Journal on
Computing](https://pubsonline.informs.org/journal/ijoc) under the [MIT License](LICENSE).

The software and data in this repository are a snapshot of the software and data
that were used in the research reported on in the paper [Gradient-based Simulation Optimization Algorithms via Multi-Resolution System Approximations](https://pubsonline.informs.org/journal/ijoc).

## Cite

To cite this software, please cite the paper [Gradient-based Simulation Optimization Algorithms via Multi-Resolution System Approximations](https://pubsonline.informs.org/journal/ijoc) using its DOI and the software itself, using the following DOI. (DOI TBA)

[![DOI](https://zenodo.org/badge/285853815.svg)](https://zenodo.org/badge/latestdoi/285853815)

Below is the BibTex for citing this version of the code.

```
@article{multiapproximationopt,
  author =        {Jingxu Xu and Zeyu Zheng},
  publisher =     {INFORMS Journal on Computing},
  title =         {Gradient-based Simulation Optimization Algorithms via Multi-Resolution System Approximations, v2021.0289},
  year =          {2022},
  doi =           {TBA},
  note =          {[https://github.com/INFORMSJoC/2021.0289](https://github.com/INFORMSJoC/2021.0289)},
}  
```

## Description

The goal of the software is to implement the two algorithms constructed in Section 3 (with FD gradient estimators) and Section 4 (with multilevel FD gradient estimators) on the simulation-optimization problem of portfolio selection, where the underlying prices of assets are driven by stochastic differential equations. We implement the two algorithms and numerically demonstrate the convergence rates and the central limit theorem. The experiment also shows that the additional use of multilevel gradient estimators can reduce the order of computation cost required to achieve a certain level of precision.

## Building

In this optimization problem, the decision variable is to select the portfolio weights for the assets at the beginning. We set the parameters of this problem setting such that this optimization problem has an exact closed-form solution. In src/generate_optimal.py we calculate the closed-form optimal solution under generated parameters of problem setting. 

In src/FD estimator.py, we implement the simulation-optimization algorithm based on regular FD estimator (Algorithm 1 in the paper).

In src/Multilevel FD estimator.py, we implement the simulation optimization algorithm based on multilevel FD estimator (Algorithm 2 in the paper).

## Results

We present all the experimental results in the folder results. Specifically, we provide:

for Algorithm 1 and Algorithm 2, the mean square error of $\theta_t$ for $t=1,2,...200$ when dimension is 2; for Algorithm 1, we provide the value of $\theta_t$ for 200 independent solving process to demonstrate central limit theorem;

for Algorithm 2, the mean square error of $\theta_t$ and cumulative computational cost for $t=1,2,...200$ when dimension is 5;

for Algorithm 1 and Algorithm 2, the mean square error of $\theta_t$ and cumulative computational cost for $t=1,2,...200$ when dimension is 20.

We provide original figures in the paper. 

## Replicating

In scripts, we provide the code for replicating Figure 2 (estimated density function by using kernel density estimation). Other figures in the paper can be replicated by using numerical results we provide.

## Additional Document

In docs/appendix_joc_multi.pdf, we present the appendix of the paper.The appendix provides additional lemmas, proofs of results in the main body, and additional results that are complementary to the main body.
