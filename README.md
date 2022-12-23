[![INFORMS Journal on Computing Logo](https://INFORMSJoC.github.io/logos/INFORMS_Journal_on_Computing_Header.jpg)](https://pubsonline.informs.org/journal/ijoc)

# CacheTest

This archive is distributed in association with the [INFORMS Journal on
Computing](https://pubsonline.informs.org/journal/ijoc) under the [MIT License](LICENSE).

The software and data in this repository are a snapshot of the software and data
that were used in the research reported on in the paper 

The snapshot is based on 
[this SHA](https://github.com/tkralphs/JoCTemplate/commit/f7f30c63adbcb0811e5a133e1def696b74f3ba15) 
in the development repository. 

## Cite

To cite this software, please cite the [paper](https://doi.org/10.1287/ijoc.2019.0934) using its DOI and the software itself, using the following DOI.

[![DOI](https://zenodo.org/badge/285853815.svg)](https://zenodo.org/badge/latestdoi/285853815)

Below is the BibTex for citing this version of the code.

```
@article{CacheTest,
  author =        {Jingxu Xu and Zeyu Zheng},
  publisher =     {INFORMS Journal on Computing},
  title =         {{CacheTest} Version v1.0},
  year =          {2022},
  doi =           {10.5281/zenodo.3977566},
  url =           {https://github.com/INFORMSJoC/JoCTemplate},
}  
```

## Description

The goal of the software is to implement the two algorithms constructed in Section 3 (with FD gradient estimators) and Section 4 (with multilevel FD gradient estimators) on the simulation-optimization problem of portfolio selection, where the underlying prices of assets are driven by stochastic differential equations. We implement the two algorithms and numerically demonstrate the convergence rates and the central limit theorem. The experiment also shows that the additional use of multilevel gradient estimators can reduce the order of computation cost required to achieve a certain level of precision.

## Building

In this optimization problem, the decision variable is to select the portfolio weights for the assets at the beginning. We set the parameters of this problem setting such that this optimization problem has an exact closed-form solution. In src/generate_optimal.py we calculate the closed-form optimal solution under generated parameters of problem setting. 

In src/FD estimator.py, we implement the simulation-optimization algorithm based on regular FD estimator (Algorithm 1 in the paper).

In src/Multilevel FD estimator.py, we implement the simulation optimization algorithm based on multilevel FD estimator (Algorithm 2 in the paper).

## Results

We present all the experimental results in the folder results, as well as figures in the paper. Specifically, we provide:

the mean square error of $\theta_t$ when dimension is 2,5 and 20 and when the simulation-optimization algorithm is based on FD estimator and multilevel FD estimator respectively.


## Replicating

## 

